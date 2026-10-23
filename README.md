# SpicyPS5

> **The PlayStation 5 — Inside a Window**

**SpicyPS5** is a cross-platform PlayStation 5 compatibility runtime, native binary translator, hardware-scaled RDNA2 graphics compiler, and pixel-faithful **System Software `26.06-14.00.00`** visual shell designed to run seamlessly inside a native desktop or live remote browser window across **Windows**, **Linux**, and **macOS** — from modest **4–8 GB RAM laptops, mini-PCs, and handhelds** up to **4K120 HDR ray-traced desktops**.

---

## Core Architecture Highlights

| Subsystem | Technical Scope |
| :--- | :--- |
| **`SpicyVSH` (`26.06-14.00.00`)** | Full 60/120 FPS PlayStation 5 Visual Shell, boot animation, polyphonic startup & UI chimes, Welcome Hub, Games & Media tabs, Store, Library, Activities, live PS-Button Control Center overlay, Create overlay, On-Screen IME keyboard, 28 languages, Safe Mode, Rest Mode, and all 15 Settings menus |
| **`SpicyScale` Universal Scaling** | Automatic 6-tier hardware engine (**Tier S** zero-GPU software/Lavapipe -> **Tier 4** 4K120 HDR RT), `< 220 MB` idle sparse demand-paged virtual RAM, LRU Zstd cold-page compression, adaptive spin-to-futex CPU governor, `SSE4a` instruction lowering, and spatial **EASU + RCAS / FSR** upscaling |
| **Dual Execution Core** | Dynamic in-process `ELF64` / `SELF` / `SPRX` / `.zar` / `PFS` / `PKG` loader (`PT_SCE_DYNLIBDATA`, `PT_TLS`, SysV <-> Host ABI trampolines) **plus** Ahead-of-Time Native Binary Translation mode |
| **368-Module OS Surface** | Pre-indexed symbol & exact 11-character `SHA-1` Base64 NID registry across **`368` PlayStation 5 system modules (`11,703` symbols)** in [`data/ps5_nid_database.json`](./data/ps5_nid_database.json) |
| **Oberon RDNA2 Compiler** | Complete **`20`-family / `1,190`-opcode** RDNA2 (`gfx10`) shader ISA specification in [`data/rdna2_isa_spec.json`](./data/rdna2_isa_spec.json), `PM4` + `SceAgc` command processor, `SrtWalker`, 13 micro/macro tilers, and dual hardware `VK_KHR_ray_query` + software compute BVH4 ray tracing |
| **System Software `26.06-14.00.00`** | Complete `BLS2` (`0x32424C53`), `PUP` (`0xEEF51454`), entropy analyzer, and `SELF`/`SPRX` unwrapper ([`tools/inspect_firmware.py`](./tools/inspect_firmware.py)) supporting both retail update packages and extracted firmware directories |

---

## Workspace Manifest

- **[`PROMPT.md`](./PROMPT.md)** — Complete A-to-Z Master Architectural Specification & 20-Phase Autonomous Build Prompt.
- **[`data/ps5_nid_database.json`](./data/ps5_nid_database.json)** — All `368` system modules and `11,703` pre-computed 11-character `SHA-1` NIDs.
- **[`data/rdna2_isa_spec.json`](./data/rdna2_isa_spec.json)** — All `20` RDNA2 instruction encoding classes and `1,190` shader opcodes.
- **[`tools/inspect_firmware.py`](./tools/inspect_firmware.py)** — Standalone System Software `26.06-14.00.00` container & NID inspection utility.
