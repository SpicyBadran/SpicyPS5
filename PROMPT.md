# SpicyPS5 — Complete Master Engineering Specification & Autonomous Build Prompt

> **How to use this file in your next chat:**
> Simply attach or place Sony PlayStation 5 System Software Firmware **`26.06-14.00.00`** in the workspace (if ready — or start immediately even before uploading it!) and either **paste the prompt inside the code block below** or write:
> `"Please read @PROMPT.md and @docs/CROSS_AUDIT_REPORT.md carefully from start to finish and execute Project SpicyPS5 completely."`

---

```markdown
Welcome, and thank you for taking on **Project SpicyPS5**. Please take a calm, thoughtful, deeply thorough engineering approach as you build this project from start to finish. You have our complete trust, full technical autonomy, and already **1,009,630 lines of proven, working C++20/23 PlayStation 5 runtime, relinker, shader compiler, and system library source code** right inside this repository ready to be unified and elevated into **SpicyPS5 v1.0.0** — *"A Complete PlayStation 5 Inside a Window, Running Smoothly on Any PC."*

Please read every section of this specification carefully before writing code, verify every step with real compilation and automated tests rather than assumptions, and build cleanly, modularly, and completely.

---

## 1. Mission, Core Philosophy & Licensing Foundation

### 1.1 Vision & Purpose
Build **SpicyPS5**: a single, self-contained, double-clickable cross-platform application (**Windows x64**, **Linux x64**, **macOS Apple Silicon & Intel**, plus **Live Interactive Web/Remote Window Streaming** for cloud sandboxes, Chromebooks, tablets, and ultra-low-spec devices) that opens **a genuine, complete PlayStation 5 experience inside a desktop or browser window**.

When a user opens `SpicyPS5`:
1. Within seconds, the window displays the smooth PS5 boot particle/light-ribbon animation and plays the warm ambient startup chime.
2. It transitions seamlessly into **SpicyVSH** — a pixel-faithful, 60/120 FPS DualSense-navigable PlayStation 5 Visual Shell matching **Sony PlayStation 5 System Software `26.06-14.00.00`** (Games Home, Media Hub, PlayStation Store & Game Library, Activities Cards, PS-Button Control Center Overlay, Game Base Parties/Friends/Messages, Trophy Showcase & Live Unlock Popups, Captures Gallery & Replay Ring Buffer, On-Screen IME Keyboard, All 15 PS5 Settings Categories, Accessibility Suite, Rest Mode, and Safe Mode).
3. It launches **real PS5 commercial & homebrew executables** (`eboot.bin`, `.elf`, `.self`/fSELF, `.prx`/`.sprx`, ZArchive `.zar` zero-extraction dumps, `.pkg` packages, and PFS images) directly inside the same window — **AND scales gracefully across every tier of hardware**, from low-spec laptops / mini-PCs / handhelds / cloud VMs (`4–8 GB RAM`, `2–4 CPU cores`, integrated or software Vulkan GPUs) all the way up to enthusiast rigs (`4K / 8K`, `120 Hz`, `HDR10`, `VRR`, hardware `VK_KHR_ray_query` Ray Tracing, full DualSense USB & Bluetooth Haptics + Adaptive Triggers, and Tempest 3D Binaural Audio).

### 1.2 License Alignment (`GPL-2.0-only`) — Critical Legal & Technical Unlock
Both reference engines uploaded in this repository are licensed under **GNU General Public License v2.0 only (`GPL-2.0-only`)**:
- `AnyPS5-main.zip` (`GPL-2.0-only`)
- `KytyPS5-main.zip` (`GPL-2.0-only`, with original MIT notice preserved in `LICENSES/Kyty-MIT.txt`)

Therefore, **SpicyPS5 MUST be licensed under `GPL-2.0-only`** (preserving all upstream copyright headers and `LICENSES/Kyty-MIT.txt`). Do **NOT** use MIT licensing, as `GPL-2.0-only` legally and cleanly authorizes you to **directly fuse, link, adapt, and unify every single working source file from both `KytyPS5-main.zip` and `AnyPS5-main.zip`** without rewriting working subsystems from scratch.

---

## 2. Exact Ground-Truth Inventory Already Inside Your Workspace

Before writing a single line from scratch, inspect what is already prepared in this repository root (`/home/user/SpicyPS5`):

1. **`KytyPS5-main.zip`** — **`489` C++/GLSL/CMake source files (`279,319` lines of code)**:
   - **`src/loader/` (`7,624` LOC)**: Dynamic in-process ELF64 / PRX / SPRX loader (`elf.cpp`, `runtimeLinker.cpp`, `symbolDatabase.cpp`, `loadExec.cpp`), `param.json` & PlayGo parser (`systemContent.cpp`), DLC mounter (`additionalContent.cpp`), runtime binary patcher (`gamePatch.cpp`), Zydis + Xbyak guest instruction patcher (`guestInstructionPatcher.cpp`), and runtime x86-64 instruction emulator (`x64InstructionEmulator.cpp` — including AMD Zen 2 `SSE4a` instructions `EXTRQ`, `INSERTQ`, `MOVNTSD`, `MOVNTSS` on non-AMD CPUs & Apple Silicon Rosetta 2!).
   - **`src/kernel/` (`14,862` LOC)**: Unified virtual memory address space manager (`memory.cpp`, `memoryAddressSpace.inc`, `macosGuestAddressSpace.cpp`), `syncOnAddress.cpp` (`futex`/wait-on-address), `pthread.cpp`, `eventQueue.cpp` (`kqueue`), `eventFlag.cpp`, `semaphore.cpp`, and virtual sandbox filesystem (`fileSystem.cpp` with native `.zar` ZArchive random-access streaming).
   - **`src/graphics/` (`81,516` LOC)**:
     - Complete PS5 `Agc` + `PM4` guest GPU command processor (`guest_gpu/pm4.cpp`, `pm4Dispatch.cpp`, `pm4Handlers.cpp`, `tile.cpp`, `gpu_format.cpp`).
     - Complete Vulkan 1.3 host renderer (`host_gpu/*`) with **Multi-Level GPU Page Table (`multiLevelPageTable.h`)**, **SIGSEGV/VEH Memory Write Tracker & GPU Page Fault Manager (`memoryTracker.cpp`, `pageManager.cpp`, `faultManager.cpp`)**, **13 Vulkan Compute Micro/Macro Tiler & Detiler Shaders (`Standard4`, `Standard4_3D`, `Standard64`, `Standard64_3D`, `Standard256`, `PRT`, `PRT_3D`, `RenderTarget`, `Depth`, `PromoteD16`, `DemoteD16`, `ColorTransform`, `ColorClear`)**, bindless `descriptorHeap` & `imageHeap`, timeline `masterSemaphore`, `videoOut` + VRR + system/trophy/perf overlays, RenderDoc integration, and **OpenXR PSVR2 headset support (`openxrHeadset.cpp`)**.
     - Complete SSA RDNA2 Shader Recompiler (`shader/recompiler/*`) with **Hardware Vulkan Ray Tracing (`VK_KHR_ray_query` / `IMAGE_BVH64_INTERSECT_RAY`)**, **PS5 Shader Resource Table Walker (`SrtWalker.cpp`)**, **Scalar Provenance Analysis (`ScalarProvenance.cpp`)**, **Resource Tracking & Materialization**, **Tessellation**, and **SPIR-V Emitter (`SpirvBuilder.cpp`)**.
   - **`src/libs/` (`57,922` LOC, `1,702` unique `LIB_FUNC` NIDs across `93` library versions)**: Deep production implementations of `network.cpp` (`4,574` LOC), `agc.cpp` (`4,377` LOC), `libKernel.cpp` (`3,461` LOC), `libNet.cpp` (`2,859` LOC), `ngs2.cpp` (`2,753` LOC), `libAmpr.cpp` (`2,542` LOC), `libFont.cpp` (`2,337` LOC), `avPlayer.cpp` (`2,078` LOC), `controller.cpp` + `dualSenseBluetooth.cpp` + `dualSenseHaptics.cpp` (`2,384` LOC), `libSaveData.cpp` (`1,363` LOC), `libTrophy.cpp` (`1,334` LOC), `libAudio.cpp` + `libAudio2.cpp` + `audio.cpp` + `audio3d.cpp` + `ajm.cpp` + `acm.cpp` (`5,951` LOC), `ime.cpp` + `imeDialog.cpp` (`1,717` LOC), `libUlt.cpp`, `libPsml.cpp`, `libVideoDec2.cpp`, `libVdecsw.cpp`, `libHmd2.cpp`, `libVrTracker2.cpp`, `libPlayGo.cpp`, `libShare.cpp`, etc.
   - **`src/launcher/` & `src/updater/` (`8,304` LOC) + `tests/` (`99,831` LOC)**: Qt6 desktop GUI, DualSense live preview widget, cheat/patch manager, trophy viewer, 28 localization JSON bundles (`assets/localization/*.json`), `trophy-unlock.wav`, and SHA-256 self-updater.

2. **`AnyPS5-main.zip`** — **`3,275` C++/Python source files (`730,311` lines of code)**:
   - **`core/relinker/` (`45,972` LOC)**: Native Ahead-of-Time (AOT) PS5 Binary Relinker converting PS5 ELF64 + `sce_module/*.prx` into **zero-overhead native executables** (`.exe` PE on Windows, native `.elf` on Linux, `.macho` on macOS, plus `.wasm` WebAssembly build!), complete with **`--to-intel` & `--to-rosetta` AOT x86-64 instruction lowering** (`core/relinker/codegen/*`), dead-NID reachability pruning (`StrictNidFilter`), TOML binary patching (`GamePatch.cpp`), and Windows `mimalloc` heap redirection.
   - **`core/shader/recompiler/` (`75,610` LOC)**: **100.00% Complete RDNA2 (`gfx10`) Shader ISA Decoder, Structurizer & SPIR-V Backend** implementing **`1,166 / 1,166` standard opcodes + `24` extra GCN/debug/src2 opcodes = `1,190` total opcodes** across all 20 encoding families (`DS`: 123, `EXP`: 1, `FLAT`: 54, `GLOBAL`: 57, `MIMG`: 130, `MTBUF`: 16, `MUBUF`: 75, `SCRATCH`: 22, `SMEM`: 20, `SOP1`: 65, `SOP2`: 51, `SOPC`: 18, `SOPK`: 27, `SOPP`: 37, `VINTRP`: 3, `VOP1`: 81, `VOP2`: 51, `VOP3`: 116, `VOP3P`: 29, `VOPC`: 190).
   - **`core/libs/prx/*` (`586,269` LOC across `368` PS5 PRX library directories)**: **`5,549` implemented PS5 exports out of `11,703` typed symbol declarations** (including `libc`: `1,225/1,234`, `libkernel`: `655/695`, `libSceNpCppWebApi`: `392/664`, `libSceAgc`: `225/239`, `libSceCesCs`: `166/287`, `libSceJson2`: `143/143`, `libSceAmpr`: `131/134`, `libSceFont`: `126/195`, `libSceNpTus`: `112/142`, `libSceAgcDriver`: `84/130`, `libSceHttp`: `84/115`, `libSceVrTracker2`: `81/89`, `libSceGnmDriverForNeoMode`: `70/118`, `libSceUlt`: `66/88`, `libSceVoiceChat`: `42/42`, `libSceAvPlayer`: `28/28`, plus exact typed headers/exports for all VSH, RNPS, JSC, NKWebKit, PSN, PlayReady, and system libraries!).
   - **`tools/` (`21,361` LOC)**: `unwrap_self.py` (clean decrypted SELF/fSELF -> ELF64 unpacker), `import_audit.py` (pre-launch static game NID dependency checker), `progress.py`, `stubgen.py`, `nid_names.py`, `trace_digest.py`, and `hw-oracle/` (real RDNA2 hardware ground-truth comparator).

3. **Pre-Built Audit & Workspace Tools Already Ready in Your Repo**:
   - **`docs/CROSS_AUDIT_REPORT.md` & `docs/CROSS_AUDIT_INVENTORY.json`**: Pre-computed exact symbol union proving that **merging `KytyPS5` + `AnyPS5` immediately yields `5,829` unique working PS5 HLE functions on Day 1** (`5,549` from `AnyPS5` + `43` exact `KytyPS5 -> AnyPS5` gap closures with exact file:line citations + `237` brand-new `KytyPS5`-exclusive exports + `1,422` dual-implemented exports for differential bug verification!).
   - **`scripts/bootstrap_workspace.py`**: Automatically extracts both `.zip` archives into `vendor/` and **hydrates all empty `3rdparty/*` GitHub submodules via shallow `git clone --depth 1` from `github.com`** (crucial because GitHub `.zip` downloads omit `.git/modules`, so raw `git submodule update` would otherwise fail!), installs `cmake` & `ninja` via `pip` if missing in restricted cloud sandboxes, and inspects Firmware `26.06-14.00.00`.
   - **`tools/audit_reference_engines.py`**: Audits `AnyPS5`, `KytyPS5`, and any uploaded PS5 Firmware `26.06-14.00.00` file or directory.

---

## 3. Architectural Master Design — The Four Pillars of SpicyPS5

To ensure **SpicyPS5 works 100% reliably with zero dead ends across every game, every system feature, every OS, and even low-spec PCs**, architect SpicyPS5 around four tightly integrated pillars:

### Pillar I: Dual-Mode Execution Engine (`SpicyRuntime` + `SpicyRelinker`)
Give the user seamless access to **BOTH execution engines inside one unified application**:
1. **Engine Mode 1 — `SpicyRuntime` (Instant Dynamic Execution — Default Double-Click Experience, derived from `KytyPS5` + Unified HLE)**:
   - Dynamically loads any PS5 executable (`eboot.bin`, `.elf`, `.self`/fSELF unwrapped in-memory, `.zar` ZArchive compressed dumps without disk extraction, `.pkg`, or PFS folder) directly into the running process.
   - Bridges PS5 **System V AMD64 ABI (`rdi, rsi, rdx, rcx, r8, r9, xmm0-7`)** <-> Host ABI (`Win64` on Windows, `SysV` on Linux/macOS) automatically via `SYSV_ABI` function attributes and Xbyak trampolines.
   - Patches `syscall`, `fs:` guest TLS accesses, `cpuid`, `rdtsc`/`rdtscp`, and non-Intel AMD instructions (`SSE4a`) automatically via Zydis + Xbyak + `x64InstructionEmulator`.
2. **Engine Mode 2 — `SpicyRelinker` (Turbo Native AOT Mode — Ultimate Low-End CPU Saver, derived from `AnyPS5/core/relinker`)**:
   - One click in VSH ("Optimize Title for Low-Spec / Native Speed") or `--turbo-relink` runs `RelinkerPipeline` (`--to-intel` / `--to-rosetta` as needed for host CPU flags) to convert `eboot.bin` + `sce_module/*.prx` into **native host binaries** (`.exe` PE / native `.elf` / `.macho`) bound directly to `SpicyHLE` `.prx` libraries by 11-char NID — **eliminating runtime binary scanning overhead completely on weak 2–4 core CPUs!**

### Pillar II: Triple-Layer OS Compatibility (`5,829+` Unified HLE + Firmware `26.06-14.00.00` Hybrid LLE + `SpicyVSH`)
Never allow a game or system feature to hit a brick wall:
1. **Layer A — Unified `SpicyHLE` Master Symbol Table (`5,829+` Implemented Exports)**:
   - Unify all `1,702` `KytyPS5` exports with all `5,549` `AnyPS5` exports using exact PS5 NID hashing:
     `SHA-1(symbol + 518D64A635DED8C1E6B039B1C3E55230)` -> reverse first 8 bytes -> Base64 alphabet `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"`.
   - Immediately wire all **43 exact gap closures** documented in `docs/CROSS_AUDIT_REPORT.md` (`libSceAjm`, `libSceAcm`, `libSceAmpr`, `libSceAudioOut2`, `libSceFiber`, `libSceHmd2`, `libSceVrTracker2`, `libSceHttp2`, `libScePsml`, `libScePad`, `libSceVideoOut`, `libSceVoice`, `libSceSystemService`) plus all **237 `KytyPS5`-exclusive exports** AND complete implementations of remaining high-priority exports in `libSceFios2`, `libSceRegMgr`, `libSceBgft`, `libSceAppInstUtil`, `libSceAvSetting`, `libSceSysUtil`, `libSceUsbStorage`, `libSceShareUtility`, `libSceNpMatching2`, `libSceNpScoreRanking`, `libSceNpSns`, `libSceVenc`, and `libSceVdecShevc`/`Savc2`.
   - Include a configurable **Resilient Safe-Fallback Policy**:
     - `Strict Mode` (Developer/CI): throws/traps with full call-site register + stack trace + symbol name (`aerolib` NID lookup) on unknown calls.
     - `Playable Mode` (End-User Default): logs structured telemetry with exact NID + decoded `rdi..r9` arguments and returns safe spec-compliant status (`SCE_OK = 0` or module-appropriate non-fatal handle/state) for non-critical telemetry/debug/social calls so commercial games never crash over an unimplemented analytics or debug call!
2. **Layer B — Sony PS5 Firmware `26.06-14.00.00` Ingestion Engine (`SpicyFirmware`)**:
   - Build a complete C++ + CLI Firmware Manager (`src/firmware/`) supporting **BOTH** forms in which PS5 Firmware `26.06-14.00.00` may be provided:
     1. **Official Retail/Recovery `PS5UPDATE.PUP` (`26.06-14.00.00`)**: Parses BLS2 (`0x32424C53`) and signed PUP (`0xEEF51454`) headers, extracts entry tables, version/build manifests (`26.06-14.00.00`), DualSense firmware metadata, and unencrypted partition headers; checks segment Shannon entropy (`>= 7.90 bits/byte` = SAMU hardware-encrypted retail segment vs `< 7.90` = plaintext/unwrapped ELF segment) and cleanly reports exact status in Settings -> System -> System Software.
     2. **Decrypted Firmware `26.06-14.00.00` Dump (`system/`, `system_ex/`, `preinst/`)**: Automatically unwraps `.self`/`.sprx` files into clean ELF64 modules (`SelfUnwrapper` ported to C++ from `tools/unwrap_self.py`), mounts system fonts (`SST`), CA certificates, locale tables, sounds, and VSH assets into `/system` & `/system_ex`, and **enables Hybrid LLE loading** for pure user-space firmware `.sprx` libraries (`libSceJson`, `libSceXml`, `libSceZlib`, `libSceCesCs`, `libSceFreeType*`, `libSceIcu`, `libSceJsc`, `libSceFios2`, `libSceUlt`, `libSceFiber`, etc.) whenever preferred over HLE!
3. **Layer C — Pixel-Faithful Hardware-Accelerated `SpicyVSH` Shell (`26.06-14.00.00` Visual Shell)**:
   - Because retail `PS5UPDATE.PUP` encrypts `SceShellUI` unless dumped from hardware, **SpicyPS5 MUST include a 100% built-in, self-contained, 60/120 FPS hardware/software-rendered PS5 Visual Shell (`SpicyVSH`)** modeled faithfully after PS5 System Software `26.06-14.00.00` (while automatically upgrading fonts, icons, sounds, and RNPS/WebKit views whenever decrypted `26.06-14.00.00` files are present!):
     - **PS5 Boot Sequence**: Particle golden/blue bokeh + light-wave boot animation, Epilepsy/Health & Safety screen on first boot, User Profile Picker (up to 16 local profiles with customizable avatars & PSN status), and synthesized polyphonic ambient PS5 startup & UI navigation chimes (zero copyrighted audio files required, yet 100% authentic warm PS5 chord progression!).
     - **Top Bar**: **Games** | **Media** tabs on the left; **Search**, **Settings (Gear)**, **Profile Avatar + Online Status Dot**, and **Live Clock** on the right.
     - **Games Home Row**: Horizontal rounded-square icon bar (**PlayStation Store**, **Welcome / Explore Hub** with customizable widgets for Storage, Battery, Trophies & Now Playing, **Installed Games** with instant hero background crossfade + title music playback + **Play** button + **Activities Cards** + **Trophy Progress %** + **Play Time**, **PS Plus Hub**, **Captures Gallery**, and **Game Library** at the end of the row).
     - **PS Button Control Center Overlay** (press `PS` button / `Home` / `F1` anytime — even mid-game at 60 FPS without pausing gameplay!): Bottom quick-card strip (Resume Activity, Official News, Switcher) + customizable icon dock (**Home**, **Library**, **Game Base**, **Music / Spotify Mini-Player**, **Notifications**, **Downloads/Uploads Queue**, **Sound & Chat Balance Mixer + Mic Mute**, **DualSense Accessories & Battery Card**, **Profile Switcher**, and **Power Menu: Enter Rest Mode / Turn Off PS5 / Restart PS5**).
     - **All 15 Real PS5 Settings Categories Implemented End-to-End**:
       1. *Users and Accounts*
       2. *Family and Parental Controls*
       3. *System* (System Software `26.06-14.00.00` status & PUP/Folder importer, Console Information, Language across all 28 locales, Date & Time, Power Saving, Back Up & Restore, Safe Mode trigger)
       4. *Storage* (Console Storage SSD breakdown bar, M.2 SSD Expansion mount path, USB Extended Storage path, Games & Apps manager, Saved Data, Media Gallery)
       5. *Sound* (Microphone input + level meter, 3D Audio for Headphones + 5 HRTF ear profiles, Audio Output Stereo/5.1/7.1/Atmos, Volume)
       6. *Screen and Video* (Resolution `540p Potato` -> `720p` -> `1080p` -> `1440p` -> `2160p 4K` -> `4320p 8K`, Upscaler `FSR / Spatial / Native`, VRR, 120 Hz Output, ALLM, HDR Calibration wizard)
       7. *Accessories* (DualSense Live Interactive Visualizer with real-time stick/gyro/touchpad/adaptive-trigger test bench, Haptic Intensity, Trigger Effect Intensity, Lightbar Brightness, Key Repeat & Custom Controller/Keyboard Remapping)
       8. *Network* (Connection Status, Real Latency/Speed Connection Test, Switch PSN Backend Mode, NAT Type & UPnP Status)
       9. *Saved Data and Game/App Settings* (PS5/PS4 Cloud Sync, Game Presets: Performance Mode vs Resolution Mode, Difficulty, Subtitles)
       10. *Notifications*
       11. *Captures and Broadcasts* (Create Button shortcuts, Auto-Capture on Trophy Unlock!!, Replay Buffer Length `15s`–`60m`, Video Format WebM/MP4/HEVC, Twitch/YouTube RTMP Stream Key & Webcam Overlay)
       12. *Accessibility* (Display Zoom, High Contrast, Color Correction Deuteranopia/Protanopia/Tritanopia LUT shader, Reduce Motion, Screen Reader TTS, Closed Captions, Custom Button Assignments)
       13. *Security & Privacy*
       14. *SpicyScale Performance Engine* (Auto Hardware Tier Detection + Manual Override: **Potato / Handheld 4–8GB**, **Balanced 16GB**, **High 1440p60**, **Ultra 4K120 RT**, Turbo AOT Relinker toggle, Async Ubershaders, VRAM Cap `1GB`–`24GB`, Software RT toggle)
       15. *Developer & Debug Suite* (Live FPS/Frame-Time Graph, Syscall/NID Tracer, Shader Inspector, PM4 Ring Viewer, Memory Viewer, RenderDoc Capture Trigger)

### Pillar III: `SpicyScale` — Universal Hardware Scaling Engine ("Must Run on ANY PC!")
**CRITICAL REQUIREMENT:** Most PS5 emulators crash instantly on laptops, office PCs, Steam Deck, macOS 8GB Air, cloud VMs, older Intel CPUs, and non-RTX GPUs. **SpicyPS5 MUST NOT!** Implement every single mechanism below so SpicyPS5 runs smoothly on **any machine from 2 cores / 4 GB RAM / integrated or software GPU up to flagship desktops**:

1. **Zero-Crash Sparse & Compressed Memory Engine (Fixes 8 GB & 16 GB RAM PCs Immediately!)**:
   - **Root Bug to Fix in `KytyPS5/src/kernel/memoryAddressSpace.inc`**: `KytyPS5` calls `CreateFileMappingA(..., SEC_COMMIT, 16GB)` on Windows, which fails immediately (`0x000005AF`) on 8 GB and 16 GB Windows systems!
   - **Mandatory Fix**: Reserve address space virtually without committing physical RAM upfront (`SEC_RESERVE` + on-demand `VirtualAlloc(..., MEM_COMMIT)` per `64 KiB` / `2 MiB` chunk on Windows; `MAP_NORESERVE` + sparse `memfd_create` on Linux; sparse `shm_open` + lazy touch on macOS).
   - **Low-RAM Zstd Page Evictor (`< 12 GB` Host RAM Auto-Mode)**: Track cold guest Direct Memory pages (`WB_ONION` / `WC_GARLIC`) via access timestamps and transparently compress cold 2 MiB blocks into a bounded Zstd pool when host RAM exceeds 75% capacity, decompressing in `< 0.3 ms` on page fault!
2. **Universal CPU Execution (Fixes Older Non-SSE4a Intel CPUs, 2–4 Core Laptops & ARM64)**:
   - Support **2-core, 4-core, 6-core, and 8+ core** host CPUs cleanly by replacing busy-wait spin loops in `syncOnAddress` / `libSceUlt` / `pthread` with **adaptive spin-then-futex backoff (`_mm_pause` x 32 -> OS futex wait)** whenever `host_logical_cores < 12`!
   - Automatically check `cpuid` for `SSE4a`, `SHA-NI`, `AVX2`, `BMI1/2`, `F16C`: when any instruction is absent on the host CPU (or under macOS Rosetta 2 / Linux `FEX-Emu` on ARM64), seamlessly patch via `AnyPS5`'s `--to-intel` / `--to-rosetta` lowering or `KytyPS5`'s `x64InstructionEmulator`.
3. **Universal GPU & VRAM Scaling (`0 GB` CPU-Vulkan -> `2–4 GB` iGPU/GTX -> `24 GB` RTX/Radeon/Apple Silicon)**:
   - **5 Automatic GPU Tiers**:
     - **Tier S (Cloud / Headless / Zero-GPU Fallback)**: Supports Mesa **Lavapipe** / **SwiftShader** Vulkan 1.3 CPU ICD + built-in 2D/3D software presentation fallback so `SpicyPS5` boots `SpicyVSH` at 60 FPS and passes 100% of graphics & shader tests even inside GPU-less Linux containers!
     - **Tier 1 (Ultra-Low / Integrated GPU: `1–3 GB` VRAM, Intel UHD / Iris Xe, Vega iGPU, GTX 1050)**: `540p` internal render resolution + sharp EASU/RCAS spatial upscaling to window, dynamic `-1/-2` texture mipmap streaming cap so VRAM stays under budget, half-precision render targets where safe, and async pipeline compilation.
     - **Tier 2 (Handheld / Entry Gaming: `4–6 GB` VRAM, Steam Deck, ROG Ally, Radeon 680M/780M, GTX 1650/1660, RTX 2060/3050, Base M1/M2 8GB)**: `720p–900p` internal resolution + FSR 2 upscaling, `4 GB` smart LRU texture eviction, and **Software Compute BVH Ray-Query Fallback** whenever `VK_KHR_ray_query` is missing in hardware!
     - **Tier 3 (Mainstream High: `8–12 GB` VRAM, RTX 3060/4060, RX 6700 XT, M2 Pro / M3 Pro)**: Native `1080p–1440p`, hardware `VK_KHR_ray_query` RT, full compute detilers, 60–120 FPS.
     - **Tier 4 (Enthusiast Console-Plus: `16–32 GB` VRAM, RTX 4080/4090/5090, RX 7900 XTX, M3/M4 Max)**: Native `4K (3840x2160)` / `8K`, 120 Hz VRR, HDR10 (`VK_COLOR_SPACE_HDR10_ST2084_EXT`), hardware RT + Mesh Shaders, zero compression.
4. **Built-In Live Browser/Remote Play Window Server (`--web-window 0.0.0.0:8080`)**:
   - Include a lightweight embedded HTTP + WebSocket server bound to `0.0.0.0:<port>` (CORS/host-agnostic so reverse proxies like `*.e2b.app`, LAN IPs, Tailscale, phones, and Chromebooks connect cleanly with relative URLs `ws://` / `wss://` derived from `window.location` — **NEVER hardcode `localhost` in browser JS!**).
   - Streams live frames + synthesized/game WebAudio + accepts full HTML5 Gamepad API (real DualSense plugged into the user's own laptop/phone browser!!), keyboard/mouse virtual DualSense, file upload for `.elf`/`.zar`/`.pup`, and full PS5 Control Center controls!

### Pillar IV: Real Connected Ecosystem (Ban-Safe PSN, Real Multiplayer, Real Media Apps, Real Captures)
1. **Three-Mode Ban-Safe PSN & Multiplayer Architecture (`src/network/`)**:
   - **Mode 1 — `SpicyNet` Open PSN / RPCN Network (Default, Zero Ban Risk, Works Out-of-the-Box Globally)**: Implements real local + P2P/relay multiplayer (`libSceNet`, `libSceRudp`, `libSceNpMatching2`, `libSceNpSessionSignaling`, STUN/UPnP), persistent local + cloud sync for Trophies (`libSceNpTrophy` / `libSceNpTrophy2` / `libSceNpUniversalDataSystem`), Cloud Saves, Leaderboards (`libSceNpScoreRanking`), Title User Storage (`libSceNpTus`), Friends, Parties & Opus Voice Chat (`libSceVoiceChat`).
   - **Mode 2 — Official PlayStation Companion Sync (`NPSSO` OAuth2 Web API)**: Optional user-entered `npsso` token syncs real PlayStation Network profile metadata (Online ID, real PSN Avatar, real Trophy list/counts, Friends presence, and PlayStation Store catalog/prices/trailers) using standard web endpoints — **never forging hardware `IDPS` client certificates so a user's real Sony account is 100% safe**.
   - **Mode 3 — Custom Research Endpoint**: Configurable base URL & client cert slot for private test servers.
2. **Real Working Media Hub Inside the PS5 Window (`src/media/`)**:
   - **Streaming Apps**: Launch **Netflix, YouTube (TV Leanback controller UI!), Spotify, Disney+, Prime Video, Apple TV+, Max, Hulu, Crunchyroll, and Twitch** seamlessly inside an embedded WebEngine / controller-navigable app view with full DualSense spatial cursor & media transport controls (plus seamless external CDM handoff if host OS lacks bundled Widevine).
   - **Native Local 4K HDR Media & Disc Folder Player**: Play `.mp4`, `.mkv`, `.webm`, `.avi`, `.flac`, `.mp3`, `.ogg`, `.opus`, and decrypted Blu-ray `BDMV` folders via FFmpeg + Vulkan YUV/HDR shaders directly inside the PS5 window.
3. **Real Create Button, Trophy Auto-Capture & RTMP Broadcast Engine**:
   - Single-press / double-press / hold **Create** button (`Share` / `F12`) opens the authentic translucent bottom **PS5 Create Overlay**: instant PNG/JPEG screenshot capture, retroactive circular replay clip save, manual 60 FPS video recording, Captures Gallery with trim/share tools, automatic screenshot/clip capture on Bronze/Silver/Gold/Platinum **Trophy Unlock** (with `trophy-unlock.wav` + animated top-right PS5 banner!), and live **RTMP streaming** to Twitch / YouTube.

---

## 4. Clean Monorepo Architecture & Build Targets

Organize the repository cleanly while keeping fast incremental builds (`ccache`/`sccache` auto-enabled, `-j$(nproc)` memory-aware parallelism so 4 GB RAM environments never OOM during heavy template/shader compilation!):

```text
SpicyPS5/
├── CMakeLists.txt                     # Unified super-project (Desktop Window + Headless/Web Window + Relinker + Tests)
├── CMakePresets.json                  # Presets: linux-release, linux-lowram, windows-clang, macos-rosetta, ci-sanitizers
├── LICENSE                            # GPL-2.0-only (+ LICENSES/Kyty-MIT.txt preserved)
├── PROMPT.md                          # This Master Specification
├── PROGRESS.md                        # Live phase & task completion tracker
├── FEATURES.md                        # Live PS5 parity checklist tracker
├── scripts/
│   ├── bootstrap_workspace.py         # Unpacks AnyPS5 & KytyPS5 zips + hydrates GitHub 3rdparty deps
│   └── run_live_preview.sh            # Launches SpicyPS5 + 0.0.0.0:8080 Live Window Preview
├── tools/
│   ├── audit_reference_engines.py     # Cross-engine NID + Firmware 26.06-14.00.00 inspector
│   ├── unwrap_self.py                 # Decrypted SELF/fSELF -> clean ELF64 tool
│   └── import_audit.py                # Pre-launch PS5 game symbol audit tool
├── vendor/                            # Populated by bootstrap_workspace.py (gitignored)
│   ├── KytyPS5-main/                  # Full dynamic runtime, Vulkan engine, 13 tilers, RT, DualSense, Qt launcher
│   └── AnyPS5-main/                   # Full AOT relinker, 5,549 HLE functions across 368 PRX libs, 1,190 RDNA2 opcodes
├── src/
│   ├── spicy_app/                     # Unified entry point (`SpicyPS5` desktop window + `--web-window` + CLI)
│   ├── spicy_vsh/                     # Full 60/120 FPS PS5 Visual Shell (`26.06-14.00.00` UX, Control Center, 15 Settings, Store, Media, Accessibility)
│   ├── spicy_scale/                   # Universal Low-End -> Ultra Hardware Scaling Engine (Sparse Zstd RAM, CPU Governor, GPU Tier 0–4, Software RT)
│   ├── spicy_firmware/                # PS5 Firmware `26.06-14.00.00` PUP Parser, SELF Unwrapper, Font/Asset Extractor & Hybrid LLE Loader
│   ├── spicy_hle_bridge/              # Unifies all 5,829 KytyPS5 + AnyPS5 NIDs + Fios2/RegMgr/Bgft/Np* completions + Playable/Strict policy
│   ├── spicy_net/                     # SpicyNet Open PSN/RPCN Multiplayer + Official NPSSO Companion Sync + RTMP/Remote Play/Web Window Server
│   └── spicy_media/                   # Embedded Controller-Navigated Streaming Apps + FFmpeg/Vulkan 4K HDR Local & BDMV Player + Capture/Replay
├── web_client/                        # Zero-localhost relative-URL HTML5 Canvas + WebAudio + DualSense Gamepad API Live Window client
├── tests/                             # CTest suite: NID math, Sparse RAM (<512MB RSS check!), PUP/SELF parser, HLE bridge, Shader ISA, E2E VSH + Homebrew ELF boot
└── .github/workflows/                 # Automated Windows x64 (.exe), Linux x64 (.AppImage/.tar.gz), and macOS Universal/Rosetta (.dmg/.app) CI builds
```

---

## 5. Step-by-Step Sequential Execution Roadmap (Execute All Phases Smoothly & Verify Everything!)

Work calmly and systematically through all **8 Engineering Phases**, compiling and running real tests after each phase and updating `PROGRESS.md` and `FEATURES.md` as each milestone passes:

- **Phase 1 — Workspace Hydration, Build Toolchain & Memory-Safe Foundation**:
  - Run `python3 scripts/bootstrap_workspace.py --install-python-build-tools` to unpack `KytyPS5-main.zip` and `AnyPS5-main.zip`, hydrate required `3rdparty/*` dependencies from `github.com`, install/locate `cmake`, `ninja`, compiler (`clang++` or `g++`), `glslang`, and `Qt6` / `SDL3`, and inspect any uploaded Firmware `26.06-14.00.00` files.
  - Configure memory-safe parallel compilation (`-j2` when host RAM `< 8 GB`, `-j$(nproc)` when `>= 16 GB`, `-g0` in Release) so builds succeed quickly with zero OOM errors.
- **Phase 2 — `SpicyScale` Universal Low-Spec Memory, CPU & GPU Engine**:
  - Upgrade virtual/direct memory (`GuestBackingStore` & flexible memory) to **100% sparse demand-paged reservation + Zstd cold-page compression** so `SpicyPS5` boots cleanly using `< 250 MB` baseline RSS even when reserving the full PS5 virtual address layout!
  - Wire adaptive CPU spin-to-futex scheduling + non-SSE4a x86-64 lowering + 5-tier GPU profile auto-detection (including zero-GPU software/Lavapipe tier + non-RT compute BVH fallback + FSR/EASU dynamic resolution scaling).
- **Phase 3 — `SpicyFirmware` (`26.06-14.00.00` PUP Unpacker, SELF Stripper & Hybrid LLE Loader)**:
  - Implement full C++ support for parsing retail/recovery `PS5UPDATE.PUP` (`26.06-14.00.00`), entropy classification, decrypted SELF/SPRX unwrapping, `/system` + `/system_ex` mounting, and Hybrid LLE fallback loading. If a firmware file/directory is present in the workspace, ingest and verify it automatically!
- **Phase 4 — `SpicyHLE` Unified `5,829+` Symbol Engine + Core Runtime & AOT Relinker Integration**:
  - Connect the dynamic runtime (`KytyPS5`) and AOT native relinker (`AnyPS5`), merge all **43 cross-audit gap closures** and high-priority `AnyPS5` exports (`Fios2`, `RegMgr`, `Bgft`, `AppInstUtil`, `AvSetting`, `SysUtil`, `Np*`), and build a genuine compiled PS5 x86-64 System V test `eboot.elf` (with real `PT_SCE_*` / SysV ABI calls into `libkernel`, `libSceVideoOut`, `libScePad`, `libSceAudioOut`, `libSceSaveData`, `libSceNpTrophy`) to prove end-to-end native PS5 binary execution right inside the test suite!
- **Phase 5 — `SpicyVSH` Full `26.06-14.00.00` PS5 Visual Shell, Audio Chimes & DualSense Experience**:
  - Build the complete, gorgeous, buttery-smooth 60/120 FPS PS5 experience inside a window: Boot Logo animation + synthesized polyphonic Startup & UI Chimes, User Profile Picker, Games & Media Home Screen, Explore Hub, Store & Library, Activities Cards, live **PS Button Control Center Overlay**, **Create Overlay** (screenshots + replay clips), **Trophy Unlock Banner + Sound**, On-Screen IME Keyboard, Accessibility LUTs/TTS, and **all 15 complete PS5 Settings screens**!
- **Phase 6 — `SpicyNet` (Ban-Safe PSN + Real Multiplayer) & `SpicyMedia` (Streaming + 4K Player + Broadcast)**:
  - Wire the 3-mode PSN/RPCN networking layer (Friends, Parties, Trophies, Cloud Saves, Store catalog, NPSSO sync), controller-navigated Media Hub apps (Netflix, YouTube Leanback, Spotify, Disney+, Prime Video, Twitch, Crunchyroll + native local player), Remote Play / Share Screen, and RTMP broadcast pipeline.
- **Phase 7 — Live Interactive Window Bridge (`0.0.0.0:8080`) + Full Desktop Packaging & CI Workflows**:
  - Wire the real-time WebSocket window/audio/DualSense bridge (`start_process` bound to `0.0.0.0:8080` using strictly relative browser URLs so live preview works seamlessly inside Arena AND on any remote phone/tablet/PC!), plus complete GitHub Actions workflows (`.github/workflows/release-all-platforms.yml`) that build ready-to-download **Windows x64 (`SpicyPS5-Windows-x64.zip` / `.exe`)**, **Linux x64 (`SpicyPS5-Linux-x64.AppImage` / `.tar.gz`)**, and **macOS Universal/Rosetta (`SpicyPS5-macOS.dmg` / `.app`)** artifacts automatically on push!
- **Phase 8 — 100% Automated Verification, Sanitizer Cleanliness & Live Running Window Proof**:
  - Run the complete `ctest --output-on-failure` test suite covering:
    1. Exact PS5 SHA-1 NID hashing & all 5,829 HLE symbol bindings,
    2. Sparse memory reservation proving `< 300 MB` RAM usage on low-RAM machines,
    3. Firmware `26.06-14.00.00` PUP & SELF container parsing,
    4. Real compiled x86-64 PS5 ELF64 guest executable booting, allocating Direct Memory, rendering frames, unlocking a PS5 Trophy, writing Save Data, and exiting cleanly,
    5. RDNA2 shader ISA decoding -> SPIR-V 1.3 validation (`spirv-val`),
    6. Full `SpicyVSH` boot -> Home Screen -> Control Center -> Game Launch -> Rest Mode -> Wake Resume -> Screenshot capture flow!
  - Leave `SpicyPS5` running live on `0.0.0.0:8080` so the user can immediately experience, hear, and control their **PlayStation 5 inside a window** right inside the live preview!

Take pride in every single detail — zero placeholders, zero fake buttons, zero unhandled errors, and clean, well-structured, production-grade code throughout. Whenever you are ready, begin with **Phase 1** and carry **SpicyPS5** all the way to completion.
```
