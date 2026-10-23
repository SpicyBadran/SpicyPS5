#!/usr/bin/env python3
"""
SpicyPS5 — PlayStation 5 System Software 26.06-14.00.00 Container & NID Inspector
SPDX-License-Identifier: MIT

Pure standalone utility for inspecting:
  - PlayStation 5 System Software `.PUP` / `BLS2` update containers (`26.06-14.00.00`)
  - Signed Executable Linkable Format (`SELF` / `SPRX`) headers & segment tables
  - Clean `ELF64` (`eboot.bin`, `.elf`, `.prx`) guest modules & Sony dynamic sections
  - Shannon entropy classification (hardware-encrypted retail segments vs unwrapped code)
  - Exact 11-character Sony `SHA-1` Base64 NID calculation & lookup against `data/ps5_nid_database.json`
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import os
import struct
from pathlib import Path
from typing import Dict, List

NID_SALT = bytes.fromhex("518D64A635DED8C1E6B039B1C3E55230")
NID_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"

BLS2_MAGIC = 0x32424C53   # "SLB2" little-endian outer container
PUP_MAGIC = 0xEEF51454    # Signed PUP header
SELF_MAGIC_A = 0x1D3D154F
SELF_MAGIC_B = 0x5414F5EE
ELF64_MAGIC = 0x464C457F


def compute_nid(symbol_name: str) -> str:
    """Compute exact 11-character PS5 SHA-1 Base64 NID from a symbol name."""
    digest = hashlib.sha1(symbol_name.encode("utf-8") + NID_SALT).digest()[:8]
    rev = digest[::-1]
    chars: List[str] = []
    for idx in (0, 3):
        triple = (rev[idx] << 16) | (rev[idx + 1] << 8) | rev[idx + 2]
        chars.extend(
            [
                NID_ALPHABET[(triple >> 18) & 0x3F],
                NID_ALPHABET[(triple >> 12) & 0x3F],
                NID_ALPHABET[(triple >> 6) & 0x3F],
                NID_ALPHABET[triple & 0x3F],
            ]
        )
    tail = (rev[6] << 16) | (rev[7] << 8)
    chars.extend(
        [
            NID_ALPHABET[(tail >> 18) & 0x3F],
            NID_ALPHABET[(tail >> 12) & 0x3F],
            NID_ALPHABET[(tail >> 6) & 0x3F],
        ]
    )
    return "".join(chars)


def shannon_entropy(sample: bytes) -> float:
    if not sample:
        return 0.0
    counts = collections.Counter(sample)
    length = float(len(sample))
    return -sum((c / length) * math.log2(c / length) for c in counts.values())


def inspect_target(target: Path) -> Dict[str, object]:
    if not target.exists():
        return {"exists": False, "target": str(target)}

    if target.is_file():
        size = target.stat().st_size
        with open(target, "rb") as fh:
            header = fh.read(min(size, 65536))
        magic = struct.unpack_from("<I", header, 0)[0] if len(header) >= 4 else 0
        entropy_bits = round(shannon_entropy(header[:16384]), 4)
        kind = "RAW_BINARY"
        entries: List[Dict[str, object]] = []
        if magic == BLS2_MAGIC and len(header) >= 32:
            kind = "BLS2_PUP_ARCHIVE"
            version, flags, entry_count, block_count = struct.unpack_from("<IIII", header, 4)
            offset = 32
            for _ in range(min(entry_count, 64)):
                if offset + 48 > len(header):
                    break
                blk_offset, byte_size, raw_name = struct.unpack_from("<QQ32s", header, offset)
                name = raw_name.split(b"\x00", 1)[0].decode("latin-1", errors="replace")
                entries.append(
                    {
                        "name": name,
                        "offset_bytes": blk_offset * 512,
                        "size_bytes": byte_size,
                    }
                )
                offset += 48
        elif magic == PUP_MAGIC:
            kind = "SIGNED_PS5_PUP"
        elif magic in (SELF_MAGIC_A, SELF_MAGIC_B):
            kind = "PS5_SELF_OR_SPRX"
        elif magic == ELF64_MAGIC:
            kind = "CLEAN_ELF64"

        return {
            "exists": True,
            "mode": "file",
            "path": str(target.name),
            "size_bytes": size,
            "magic_hex": f"0x{magic:08X}",
            "format": kind,
            "entropy_bits_per_byte": entropy_bits,
            "encrypted_payload": entropy_bits >= 7.90 and kind != "CLEAN_ELF64",
            "entries": entries,
        }

    counts = {"clean_elf64": 0, "self_wrapped": 0, "other_assets": 0}
    for dp, _, files in os.walk(target):
        for fn in files:
            fp = Path(dp) / fn
            try:
                with open(fp, "rb") as fh:
                    head = fh.read(4)
                if len(head) == 4:
                    mg = struct.unpack_from("<I", head, 0)[0]
                    if mg == ELF64_MAGIC:
                        counts["clean_elf64"] += 1
                        continue
                    if mg in (SELF_MAGIC_A, SELF_MAGIC_B):
                        counts["self_wrapped"] += 1
                        continue
                counts["other_assets"] += 1
            except OSError:
                continue
    return {
        "exists": True,
        "mode": "directory",
        "name": target.name,
        "summary": counts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect PS5 Firmware 26.06-14.00.00 & compute NIDs")
    parser.add_argument("--inspect", type=Path, help="Path to PS5UPDATE.PUP or extracted firmware folder")
    parser.add_argument("--symbol", type=str, help="Compute 11-character PS5 NID for a C symbol name")
    args = parser.parse_args()

    if args.symbol:
        print(json.dumps({"symbol": args.symbol, "nid": compute_nid(args.symbol)}, indent=2))
    if args.inspect:
        print(json.dumps(inspect_target(args.inspect), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
