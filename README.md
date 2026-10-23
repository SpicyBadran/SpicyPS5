# SpicyPS5

> **"A Complete PlayStation 5 Inside a Window — Built to Run Smoothly on Any PC."**

`SpicyPS5` unifies two complementary open-source PlayStation 5 engines under **`GPL-2.0-only`** together with **Sony PlayStation 5 System Software `26.06-14.00.00`** ingestion, **`SpicyVSH`** (a pixel-faithful 60/120 FPS PS5 Visual Shell & Control Center), and **`SpicyScale`** (universal low-spec hardware scaling from 4–8 GB RAM laptops & handhelds up to 4K120 HDR ray-traced desktops):

| Repository Asset | Files | Lines of Code | Core Engineering Role |
| :--- | ---: | ---: | :--- |
| **`KytyPS5-main.zip`** | `489` | `279,319` | Dynamic in-process ELF/SPRX/ZArchive (`.zar`) runtime, `1,702` unique `LIB_FUNC` HLE exports, Vulkan 1.3 renderer, Multi-Level GPU Page Table + SIGSEGV/VEH fault manager, `13` compute micro/macro tilers, SSA RDNA2 recompiler with hardware `VK_KHR_ray_query` Ray Tracing, DualSense USB/Bluetooth + Haptics + Adaptive Triggers, Qt6 launcher & updater |
| **`AnyPS5-main.zip`** | `3,275` | `730,311` | Native AOT binary relinker (`ELF` -> native Windows `PE`, Linux `ELF`, macOS `Mach-O`, and `WASM`) with `--to-intel` / `--to-rosetta` lowering, **`5,549` implemented PS5 HLE exports across `368` PRX libraries**, **`1,190` RDNA2 (`gfx10`) shader ISA opcodes (`100.00%`)**, `unwrap_self.py`, `import_audit.py`, and `hw-oracle` |
| **Unified `SpicyPS5` Foundation** | **`3,764`** | **`1,009,630`** | **`5,829` Day-1 unique working HLE functions** (`43` immediate cross-engine gap closures + `237` `KytyPS5`-exclusive exports + `1,422` 1:1 cross-validated exports), Firmware `26.06-14.00.00` PUP/SELF hybrid engine, `SpicyVSH`, `SpicyScale`, and Live Desktop + Web Window (`0.0.0.0:8080`) |

---

## Ready-to-Use Files in This Repository

- **[`PROMPT.md`](./PROMPT.md)** — **The Complete Master Engineering Specification & Single Autonomous Build Prompt** for the next chat session.
- **[`docs/CROSS_AUDIT_REPORT.md`](./docs/CROSS_AUDIT_REPORT.md)** — Exact programmatic cross-audit of `AnyPS5-main.zip` + `KytyPS5-main.zip`, including all **43 immediate file-and-line gap closures** and full **RDNA2 ISA coverage**.
- **[`docs/CROSS_AUDIT_INVENTORY.json`](./docs/CROSS_AUDIT_INVENTORY.json)** — Machine-readable symbol, NID, and shader inventory across all `368` PS5 PRX modules.
- **[`scripts/bootstrap_workspace.py`](./scripts/bootstrap_workspace.py)** — Turnkey workspace bootstrapper that unpacks both `.zip` archives into `vendor/` and hydrates all required `3rdparty/*` GitHub submodules cleanly.
- **[`tools/audit_reference_engines.py`](./tools/audit_reference_engines.py)** — Zero-dependency Python 3 audit & Firmware `26.06-14.00.00` inspector (`python3 tools/audit_reference_engines.py --firmware <PUP-or-folder>`).

## Quick Launch in Next Chat

1. Optionally drop your PS5 Firmware **`26.06-14.00.00`** (`PS5UPDATE.PUP` and/or decrypted `firmware/` dump) into the repository root or `firmware/`.
2. Paste the prompt inside **[`PROMPT.md`](./PROMPT.md)** (or reference `@PROMPT.md` and `@docs/CROSS_AUDIT_REPORT.md`).
