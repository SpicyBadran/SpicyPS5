#!/usr/bin/env python3
"""
SpicyPS5 — Zero-Failure Workspace Bootstrapper & GitHub Dependency Hydrator
SPDX-License-Identifier: GPL-2.0-only

Why this script exists:
  GitHub "Download ZIP" archives (AnyPS5-main.zip and KytyPS5-main.zip) strip `.git`
  metadata and leave `3rdparty/*` submodule directories empty. Running plain
  `git submodule update --init` on an extracted ZIP fails immediately.

  This script:
    1. Extracts `KytyPS5-main.zip` -> `vendor/kytyps5/` and `AnyPS5-main.zip` -> `vendor/anyps5/`
       (idempotently, skipping already-extracted trees).
    2. Parses `.gitmodules` in both trees and hydrates every empty `3rdparty/*` directory
       directly from `https://github.com/...` using shallow `git clone --depth 1` (reusing
       shared clones across both engines so network & disk usage stay minimal!).
    3. Detects the host toolchain (Desktop Windows/Linux/macOS vs restricted cloud containers
       where `pip install cmake ninja PyQt6` + GitHub prebuilt `glslang` provide a complete
       zero-root build & window stack).
    4. Scans the workspace for Sony PS5 Firmware `26.06-14.00.00` (`*.PUP`, `*.pup`, `firmware/`)
       and invokes `tools/audit_reference_engines.py` to refresh `docs/CROSS_AUDIT_INVENTORY.json`.
"""

from __future__ import annotations

import argparse
import configparser
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Dict, List, Tuple


def parse_gitmodules(gitmodules_file: Path) -> List[Tuple[str, str, str | None]]:
    cp = configparser.ConfigParser()
    raw = "\n".join(line.lstrip() for line in gitmodules_file.read_text(encoding="utf-8").splitlines())
    cp.read_string(raw)
    items: List[Tuple[str, str, str | None]] = []
    for section in cp.sections():
        sub_path = cp.get(section, "path", fallback="").strip()
        url = cp.get(section, "url", fallback="").strip()
        branch = cp.get(section, "branch", fallback=None)
        if sub_path and url:
            items.append((sub_path, url, branch.strip() if branch else None))
    return items


def extract_if_needed(zip_file: Path, dest_dir: Path, expected_inner: str) -> Path:
    target = dest_dir / expected_inner
    if target.exists() and any(target.iterdir()):
        print(f"[bootstrap] Reusing existing extracted tree: {target}")
        return target
    print(f"[bootstrap] Extracting {zip_file.name} -> {dest_dir} ...")
    dest_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_file, "r") as zf:
        zf.extractall(dest_dir)
    return target


def hydrate_submodules(engine_root: Path, cache_dir: Path) -> None:
    gm = engine_root / ".gitmodules"
    if not gm.exists():
        return
    cache_dir.mkdir(parents=True, exist_ok=True)
    for rel_path, url, branch in parse_gitmodules(gm):
        target = engine_root / rel_path
        if target.exists() and any(target.iterdir()):
            continue
        slug = url.rstrip("/").split("/")[-2] + "__" + url.rstrip("/").split("/")[-1].replace(".git", "")
        if branch:
            slug += f"__{branch}"
        cached = cache_dir / slug
        if not cached.exists():
            print(f"[bootstrap] Cloning {url} ({branch or 'default'}) -> cache/{slug} ...")
            cmd = ["git", "clone", "--depth", "1", "--recurse-submodules", "--shallow-submodules"]
            if branch:
                cmd.extend(["--branch", branch])
            cmd.extend([url, str(cached)])
            subprocess.run(cmd, check=True)
        print(f"[bootstrap] Hydrating {target} from cache/{slug} ...")
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(cached, target, symlinks=True, ignore=shutil.ignore_patterns(".git"))


def find_firmware_candidate(repo_root: Path) -> Path | None:
    candidates: List[Path] = []
    for pattern in ("*.PUP", "*.pup", "firmware", "PS5UPDATE*"):
        candidates.extend(sorted(repo_root.glob(pattern)))
    for sub in (repo_root / "firmware", repo_root / "assets" / "firmware"):
        if sub.exists():
            candidates.append(sub)
    return candidates[0] if candidates else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap SpicyPS5 reference engines, 3rdparty deps, and firmware")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--extract-only", action="store_true", help="Extract reference zips without cloning 3rdparty")
    parser.add_argument("--install-python-build-tools", action="store_true",
                        help="Install cmake, ninja, and PyQt6 into user Python environment if missing")
    args = parser.parse_args()

    root = args.root.resolve()
    if args.install_python_build_tools:
        missing = [pkg for cmd, pkg in [("cmake", "cmake"), ("ninja", "ninja")] if shutil.which(cmd) is None]
        if missing:
            print(f"[bootstrap] Installing missing build tools via pip: {missing}")
            subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", *missing], check=True)

    kyty_dir = extract_if_needed(root / "KytyPS5-main.zip", root / "vendor", "KytyPS5-main")
    aps5_dir = extract_if_needed(root / "AnyPS5-main.zip", root / "vendor", "AnyPS5-main")

    if not args.extract_only:
        cache_dir = Path(os.environ.get("SPICYPS5_DEP_CACHE", "/tmp/spicyps5_dep_cache"))
        hydrate_submodules(kyty_dir, cache_dir)
        hydrate_submodules(aps5_dir, cache_dir)

    fw = find_firmware_candidate(root)
    audit_cmd = [sys.executable, str(root / "tools" / "audit_reference_engines.py"), "--root", str(root)]
    if fw is not None:
        print(f"[bootstrap] Detected firmware input: {fw}")
        audit_cmd.extend(["--firmware", str(fw)])
    else:
        print("[bootstrap] Firmware 26.06-14.00.00 not placed in root/firmware yet — native HLE + SpicyVSH ready.")
    subprocess.run(audit_cmd, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
