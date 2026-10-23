# SpicyPS5 — Complete Master Engineering Specification & Autonomous Build Prompt

> **Single Copy-Paste Master Prompt (Also Ready in Workspace as `@PROMPT.md`):**
> Everything between the opening and closing prompt borders below is a **single, self-contained, exhaustive A-to-Z specification** covering every hardware register, binary container layout, ABI convention, system call, `368`-module `libSce*` library surface (`data/ps5_nid_database.json`), `1,190`-opcode RDNA2 shader ISA (`data/rdna2_isa_spec.json`), PlayStation 5 System Software **`26.06-14.00.00`** ingestion pipeline, universal low-spec PC scaling engine (**`SpicyScale`**), visual shell (**`SpicyVSH`**), networking stack, audio DSP engine, DualSense protocol, desktop window, live web/remote window server, automated test suite, and cross-platform installer pipeline.

---

```markdown
⟪══════════════════════════════════════════════════════════════════════════════════════════⟫
⟪                                                                                          ⟫
⟪    ███████╗██████╗ ██╗ ██████╗██╗   ██╗██████╗ ███████╗███████╗                          ⟫
⟪    ██╔════╝██╔══██╗██║██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝                          ⟫
⟪    ███████╗██████╔╝██║██║      ╚████╔╝ ██████╔╝███████╗███████╗                          ⟫
⟪    ╚════██║██╔═══╝ ██║██║       ╚██╔╝  ██╔═══╝ ╚════██║╚════██║                          ⟫
⟪    ███████║██║     ██║╚██████╗   ██║   ██║     ███████║███████║                          ⟫
⟪    ╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝                          ⟫
⟪                                                                                          ⟫
⟪               PROJECT SPICYPS5 — THE COMPLETE MASTER ARCHITECTURAL SPECIFICATION         ⟫
⟪             A COMPLETE PLAYSTATION 5 INSIDE A WINDOW — RUNNING SMOOTHLY ON ANY PC        ⟫
⟪                  TARGET SYSTEM SOFTWARE: 26.06-14.00.00  |  VERSION 1.0.0                ⟫
⟪                                                                                          ⟫
⟪══════════════════════════════════════════════════════════════════════════════════════════⟫

Welcome, and thank you wholeheartedly for taking on **Project SpicyPS5**.

Please approach this project with calm focus, deep engineering pride, crystal-clear architectural thinking, and unwavering thoroughness. You have full technical autonomy and complete trust to design, implement, compile, test, refine, and verify every layer of **SpicyPS5** until a user opening the application experiences a complete, responsive, unmistakable **PlayStation 5 inside a window** — running smoothly not only on flagship gaming rigs, **but equally cleanly, reliably, and gracefully on everyday laptops, mini-PCs, handhelds, macOS notebooks, and modest or low-spec machines**.

Take your time to read every part of this specification before writing code. Also inspect the pre-populated machine-readable hardware and operating-system specifications already prepared inside this workspace:
  - `data/ps5_nid_database.json` — All **368 PlayStation 5 system modules** and **11,703 exact symbol names + pre-computed 11-character SHA-1 Base64 NID hashes**.
  - `data/rdna2_isa_spec.json` — All **20 AMD RDNA2 (`gfx10` / Oberon) shader instruction encoding classes** and **1,190 exact shader instruction mnemonics**.
  - `tools/inspect_firmware.py` — Standalone PlayStation 5 System Software **`26.06-14.00.00`** container, entropy, ELF/SELF, and SHA-1 NID inspection utility.
  - Any PlayStation 5 System Software **`26.06-14.00.00`** file (`PS5UPDATE.PUP`) or extracted firmware directory (`firmware/`) placed in the workspace now or loaded later at runtime.

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                 PART I: ARCHITECTURAL MINDSET & ENGINEERING COMMITMENT                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 1.1 — YOUR ENGINEERING DISCIPLINE & TECHNICAL MASTERY                                    │
└──────────────────────────────────────────────────────────────────────────────────────────┘

You bring calm, methodical, world-class mastery across every systems engineering discipline
required to make **SpicyPS5** work for real in production:

  ▪ Operating Systems & Kernel Architecture:
      FreeBSD 11/12 & Prospero/Orbis kernel design (`vm_map`, sparse virtual memory, demand
      paging, `kqueue`/`kevent`, futex/wait-on-address synchronization, user-level threading
      `ULT`, fibers, sandboxes, POSIX pthreads, and zero-overhead syscall trampolines).
  ▪ Binary Formats, ABI Translation & Ahead-of-Time / Dynamic Compilation:
      x86-64 System V AMD64 ABI (`rdi, rsi, rdx, rcx, r8, r9`, `xmm0–xmm7`, 128-byte red zone)
      to host Microsoft x64 ABI (`rcx, rdx, r8, r9`, 32-byte shadow space, `xmm6–xmm15` callee-
      saved), POSIX `x86-64`, and `ARM64` (`AArch64` / Apple Silicon) bridging; guest `fs:`
      Thread-Local Storage (`PT_TLS`, TCB, dynamic TLS); `ELF64`, `SELF`, `SPRX`, `PE32+`,
      `Mach-O`, `WebAssembly`, `BLS2`/`PUP`, `PFS`, `PKG`, and `ZArchive` (`.zar`).
  ▪ GPU Architecture, Shader Compilers & Real-Time Rendering:
      Custom AMD RDNA2 (`gfx10` / "Oberon") command processors (`PM4` Type-3 packets + `Agc`
      high-level draw/compute/async command buffers + `Gnm` backward-compatibility paths),
      Shader Resource Tables (`SRT`), scalar provenance tracking, complete 20-family / 1,190-
      opcode RDNA2 ISA decoding, control-flow structurization, SSA optimization, SPIR-V 1.6 /
      MSL / HLSL emission, Multi-Level GPU Page Tables with write-watch fault recovery,
      compute-shader micro/macro texture tilers & detilers, Vulkan 1.3 dynamic rendering,
      Metal 3, DirectX 12 Ultimate, hardware `VK_KHR_ray_query` AND software compute BVH
      ray tracing fallback for non-RT GPUs, plus CPU software Vulkan (`Lavapipe`/`SwiftShader`)
      fallback for zero-GPU machines.
  ▪ Digital Signal Processing & Spatial Audio:
      48 kHz 32-bit float mixing, partitioned FFT overlap-save HRTF binaural convolution
      (Tempest 3D Audio engine), multi-bus DSP rack processing (`Ngs2`), batch hardware codec
      processing (`Ajm`: ATRAC9, AAC, MP3, Opus, PCM), convolution reverb (`Acm`), and low-
      latency cross-platform audio output (`WASAPI`/`XAudio2`, `PipeWire`/`PulseAudio`/`ALSA`,
      `CoreAudio`, and WebAudio).
  ▪ Human Interface Devices & Haptic Mechatronics:
      Full USB HID & Bluetooth L2CAP HID stacks, byte-exact DualSense (`0x054C:0x0CE6`) &
      DualSense Edge (`0x054C:0x0DF2`) input/output reports, Bluetooth seed CRC-32 signing,
      10+ programmable adaptive trigger motor resistance curves, 48 kHz dual-LRA haptic
      waveforms, Opus speaker audio, 6-axis IMU sensor fusion, dual-touch capacitive touchpad,
      and full keyboard/mouse virtual DualSense mapping.
  ▪ Low-Spec Performance Engineering (`SpicyScale`):
      Designing every memory pool, thread scheduler, shader pipeline, texture cache, and render
      pass so that machines with **only 4–8 GB RAM, 2–4 CPU cores, older non-SSE4a Intel CPUs,
      or integrated / non-ray-tracing GPUs** run smoothly without out-of-memory crashes, CPU
      spinlock starvation, missing-instruction faults, or shader compilation freezes.

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 1.2 — GUIDING PRINCIPLES FOR EVERY FILE YOU WRITE                                        │
└──────────────────────────────────────────────────────────────────────────────────────────┘

  1. Build Real, Working Subsystems — Never Hollow Shells:
     Every button in the UI performs a real action; every parser reads real bytes; every
     allocator manages real pages; every HLE module executes real state transitions; every
     shader stage emits valid SPIR-V verified by automated tests.
  2. Always Verify With Real Compilation & Execution:
     Never stop at "mental compilation" when a real compiler, Python interpreter, test runner,
     and live preview server are right at your fingertips. Compile after every milestone, run
     tests continuously, fix every warning immediately, and keep the build green at all times.
  3. Universal Hardware Inclusivity ("Run on Anything"):
     Treat a modest laptop, mini-PC, handheld, MacBook Air, or cloud VM with the same care and
     first-class engineering respect as a 24 GB enthusiast desktop GPU. Never hard-commit
     16 GB of physical RAM upfront and never crash simply because an optional GPU extension
     is absent on the host machine.
  4. Zero Blocker Resilience on Firmware `26.06-14.00.00`:
     Whether the user launches SpicyPS5 before importing firmware, imports an official retail
     `PS5UPDATE.PUP` (`26.06-14.00.00`), or imports a decrypted `/system` + `/system_ex`
     firmware directory, **SpicyPS5 MUST boot cleanly into a full 60/120 FPS PlayStation 5
     experience inside a window with zero errors**.

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║            PART II: PROJECT CONSTITUTION, SCALING TIERS & PARITY CHECKLIST               ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 2.1 — PROJECT CONSTITUTION & TECHNOLOGY STACK                                            │
└──────────────────────────────────────────────────────────────────────────────────────────┘

  PROJECT NAME:           SpicyPS5
  VERSION:                1.0.0
  TARGET SYSTEM SOFTWARE: PlayStation 5 System Software 26.06-14.00.00
  TAGLINE:                "The PlayStation 5 — Inside a Window — Smooth on Every Machine"
  LICENSE:                MIT / Permissive Clean-Room Original Architecture
  LANGUAGE STACK:
    ▪ C++23 ( with clean C++20 compiler compatibility where needed )
    ▪ C11 ( low-level ABI trampolines, signal/exception glue, atomic primitives )
    ▪ Objective-C++ ( macOS Cocoa + Metal 3 + CoreAudio native integration )
    ▪ GLSL 4.60 / Vulkan SPIR-V 1.6 / MSL 3.0 / HLSL SM 6.6 ( GPU shaders & compute tilers )
    ▪ HTML5 Canvas / WebGL2 + WebAudio + Gamepad API ( built-in Live Remote Window client )
    ▪ Python 3.10+ ( firmware inspector, NID database codegen, build & test automation )
  UI & WINDOWING STACK:
    ▪ Desktop Native Window: Qt 6 Widgets/Quick + SDL3 Vulkan/Metal/D3D12 Presentation Surface
    ▪ Embedded Live Window Server: Zero-dependency HTTP + WebSocket real-time window, audio &
      DualSense controller bridge (`0.0.0.0:8080`) so headless hosts, Chromebooks, tablets,
      phones, and low-end devices stream & control the full PS5 window seamlessly at 60 FPS!
  BUILD & QUALITY SYSTEM:
    ▪ CMake 3.24+ with `CMakePresets.json` + Ninja + automatic `ccache`/`sccache` detection
    ▪ Automated Test Suite via CTest + Catch2 / standalone C++23 unit & end-to-end binaries
    ▪ GitHub Actions CI/CD producing ready-to-run artifacts for Windows x64, Linux x64, and
      macOS (Apple Silicon + Intel)

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 2.2 — SPICYSCALE HARDWARE MATRIX ("RUNS ON ANYTHING" — TIER S THROUGH TIER 4)            │
└──────────────────────────────────────────────────────────────────────────────────────────┘

  Unlike traditional console runtimes that demand 32 GB RAM and a flagship GPU just to open
  a window, **SpicyPS5 automatically detects host CPU, RAM, and GPU capabilities at startup**
  and scales smoothly across **all six real-world hardware profiles**:

  ▪ TIER S — Cloud VM / Office PC / Zero-GPU Software Mode:
      • Hardware: 2+ cores, 3.5–4 GB RAM, NO discrete or hardware Vulkan GPU required
      • Strategy: Demand-paged sparse memory (`< 220 MB` idle RSS) + CPU Vulkan (`Lavapipe` /
        `SwiftShader`) or built-in SIMD software rasterizer + 540p/720p fast presentation +
        optional Live Web Window (`0.0.0.0:8080`).
  ▪ TIER 0 — Ultra-Light Entry Laptop / Mini-PC:
      • Hardware: 4-core Intel Core i3/i5 or Ryzen 3, **8 GB RAM**, Intel UHD / Vega iGPU (1–2 GB)
      • Strategy: Sparse virtual memory + **LRU Zstd Cold-Page RAM Compressor** + **Native AOT
        Binary Translator (`--lower-cpu`)** + `540p` internal render -> sharp **EASU + RCAS**
        spatial upscale + `-2` mipmap streaming budget cap + async ubershaders.
  ▪ TIER 1 — Everyday Laptop / Budget Desktop:
      • Hardware: 4–6 cores, **8–16 GB RAM**, Intel Iris Xe / Arc / GTX 1050 Ti / GTX 1650 / RX 580
      • Strategy: `720p` internal render -> **AMD FSR 2** upscaling to 1080p window + **Compute-
        Shader Software BVH Ray Tracing Fallback** (so ray-traced PS5 titles never crash!) +
        adaptive spin-to-futex CPU thread governor.
  ▪ TIER 2 — Handheld Gaming PCs & Base Apple Silicon Macs:
      • Hardware: Steam Deck (Van Gogh 16 GB unified), ROG Ally / Legion Go (Radeon 780M),
        Apple MacBook Air / Mac mini M1/M2/M3 (8 GB or 16 GB unified RAM)
      • Strategy: Unified memory fast-path (`VK_EXT_external_memory_host` / Metal shared heaps),
        `720p–900p` FSR / MetalFX upscaling, battery-aware frame pacing (40 Hz / 60 Hz lock),
        and full Rosetta 2 / ARM64 + `SSE4a` instruction translation.
  ▪ TIER 3 — Mainstream Gaming Desktop:
      • Hardware: 8-core CPU (Ryzen 7 / Core i7), 16–32 GB RAM, RTX 3060/4060 / RX 6700 XT / M3 Pro
      • Strategy: Native `1080p–1440p`, hardware `VK_KHR_ray_query` ray tracing, full 13 Vulkan
        compute detilers, 60–120 FPS, full DualSense haptics & Tempest 3D HRTF audio.
  ▪ TIER 4 — Enthusiast Console-Plus Workstation:
      • Hardware: 12–24+ cores, 32–64+ GB RAM, RTX 4080/4090/5090 / RX 7900 XTX / M3-M4 Max
      • Strategy: Native `4K (3840×2160)` & `8K (7680×4320)` supersampling, `120 Hz` VRR,
        `HDR10` (`ST.2084 PQ`) / `Dolby Vision` metadata, full hardware ray tracing, mesh
        shaders, variable rate shading (`VRS`), and lossless uncompressed memory pools.

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 2.3 — COMPLETE FEATURE PARITY CHECKLIST (100% REQUIRED — ZERO DEAD BUTTONS OR STUBS)     │
└──────────────────────────────────────────────────────────────────────────────────────────┘

BOOT, SYSTEM & FIRMWARE 26.06-14.00.00:
  ✅ Authentic PS5 golden/blue particle & light-ribbon boot animation (smooth 60/120 FPS)
  ✅ Synthesized polyphonic ambient startup chime & authentic PS5 UI navigation sound effects
  ✅ First-time console setup wizard (language, display area, HDR calibration, power profile,
     hardware scaling tier preview, user profile creation, optional firmware `26.06-14.00.00` import)
  ✅ PlayStation 5 System Software `26.06-14.00.00` inspector, `BLS2`/`PUP` unpacker, entropy
     verifier, decrypted `SELF`/`SPRX` unwrapper, & hot-reloadable system module mounter
  ✅ Rest Mode / Standby (suspends guest execution, snapshots state, minimizes window/power while
     continuing background downloads & updates, and resumes instantly to exact frame!)
  ✅ Complete 8-Option PS5 Safe Mode Recovery Menu (`--safe-mode` or holding power in UI:
     1. Restart PS5, 2. Change Video Output, 3. Update System Software, 4. Restore Default
     Settings, 5. Clear Cache and Rebuild Database, 6. Reset PS5, 7. Reset PS5 [Reinstall
     System Software `26.06-14.00.00`], 8. Set HDCP / Performance Mode)
  ✅ Up to 4 simultaneous local controllers + pairing & user-assignment screen at boot

VISUAL SHELL (SPICYVSH — SYSTEM SOFTWARE 26.06-14.00.00 UX):
  ✅ Top navigation bar: **Games** tab | **Media** tab on left; **Search**, **Settings**, **User
     Profile Avatar + Online Presence Dot**, and **Real-Time Clock** on right
  ✅ Welcome / Explore Hub (26.06-14.00.00 bento widget board: Console Storage gauge, DualSense
     Battery widget, Recent Trophies card, Friends Online card, Now Playing & Activity Resume,
     and customizable dynamic PS5 background themes!)
  ✅ Horizontal rounded-square Home Tile Bar with smooth scaling focus ring, full-bleed hero key-
     art crossfade, per-title ambient background music (`snd0.at9` / `.ogg` / `.wav`), play-time
     counter, Trophy progress bar, and **Activities Cards** (instant deep-link launch / resume)
  ✅ **PS Button Control Center Overlay** (press `PS` / `Home` / `F1` anytime — seamlessly layered
     at 60/120 FPS directly over VSH OR over a live running PS5 game!):
       - Activity & Switcher Quick Cards across top row
       - Customizable Bottom Icon Dock: **Home**, **Game Library**, **Game Base**, **Music**,
         **Notifications**, **Downloads/Uploads**, **Sound & Voice Balance**, **Mic Mute**,
         **Accessories / Battery**, **User Profile Switcher**, **SpicyScale Quick Tuner**, and
         **Power (Enter Rest Mode / Turn Off PS5 / Restart PS5)**
  ✅ Instant Multi-App / Multi-Game **Switcher**
  ✅ **Game Base** panel (Friends list, Parties, 16-user voice chat channels, persistent text/voice
     message groups, game invites, and one-click session join)
  ✅ **Notifications** toast overlay (top-right genuine PS5 slide-in card with chime for Trophy
     Unlocks, Downloads Complete, Friend Online, Party Invites, and Screenshots Saved!)
  ✅ **On-Screen DualSense Keyboard (`SceIme` / `SceImeDialog`)** supporting D-pad typing, R3/L3
     shortcuts, touchpad cursor swipe, predictive suggestions, and physical host keyboard typing
  ✅ Built-in Web Browser (`SceWebBrowserDialog` + hidden VSH browser)

USER ACCOUNTS, TROPHIES & SOCIAL ECOSYSTEM:
  ✅ Up to 16 local user profiles with custom avatars, cover banners, bio, language, & PIN lock
  ✅ Family Management & Parental Controls (playtime limits, age ratings, spending/chat gates)
  ✅ **3-Mode Ban-Safe Network & PSN Architecture**:
       1. `SpicyNet` Open PSN / RPCN Cloud & LAN Network (Default — 100% ban-safe real friends,
          real multiplayer matchmaking, real parties, cloud saves, leaderboards & trophy sync)
       2. Official PlayStation Web Companion Sync (`NPSSO` OAuth2 read/sync — imports real Online
          ID, real PSN Avatar, real Trophy list/progress, Friends presence & Store catalog safely
          without ever forging hardware `IDPS` client certificates!)
       3. Custom Research Server Mode (configurable endpoint & certificate slot)
  ✅ Complete Trophy System (`libSceNpTrophy` + `libSceNpTrophy2` + `UDS`): Bronze, Silver, Gold,
     and Platinum unlocks, real-time top-right popup banner + unlock sound, automatic screenshot /
     video clip capture at the exact moment a trophy unlocks, Trophy Showcase & Friend Comparison!

STORE, GAME LIBRARY & UNIVERSAL FORMAT SUPPORT:
  ✅ Built-in PlayStation Store & Homebrew/Demo Hub (browse categories, deals, search, trailers,
     PS Plus catalog view, wishlist, wallet simulation, and one-click install of free/homebrew
     PS5 test titles so users can launch real compiled PS5 x86-64 binaries IMMEDIATELY out of the box!)
  ✅ Complete Game Library (Installed, All Collection, ZArchive `.zar`, PS4 Backward-Compat,
     Hidden Titles; filter by platform/genre/players; sort by Recent, A–Z, Size, Play Time)
  ✅ Zero-Extraction mounting for **`.zar` (ZArchive)** compressed game images, **`.elf` / `eboot.bin`**,
     unwrapped **`.self` / `.sprx`**, **`.pkg`** packages, **PFS** images, **Game Patches**, & **DLC (`addcont`)**
  ✅ Per-user local & cloud-synced **Save Data Manager** (`libSceSaveData` + `SaveDataDialog` +
     automatic backup snapshots & import/export)

GRAPHICS, DISPLAY & GAMEPLAY EXCELLENCE:
  ✅ Internal render scaling from **`360p` / `540p` (Potato Mode)** -> `720p` -> `1080p` ->
     `1440p` -> **`4K (3840×2160)`** -> **`8K (7680×4320)`**
  ✅ Sharp **AMD FSR 2 / Spatial EASU+RCAS / MetalFX** upscaling inside any window or fullscreen size
  ✅ **30 / 40 / 60 / 120 FPS** + uncapped mode + microsecond-accurate **Frame Pacer**, **VRR**, & **ALLM**
  ✅ **HDR10 (`ST.2084 PQ`)**, **HDR Calibration Wizard**, **Auto-HDR** inverse tone-mapping, and
     **Dolby Vision** metadata passthrough
  ✅ **Hardware Ray Tracing (`VK_KHR_ray_query` / Metal RT / DXR)** + **Automatic Compute-Shader
     Software BVH Ray Tracing Fallback** on non-RT GPUs!
  ✅ Mesh Shaders, Tessellation, Geometry Shaders, Compute Detilers, & Variable Rate Shading (`VRS`)
  ✅ Instant **One-Click Native Binary Optimization (`NativeTranslator`)** for weak CPUs

CREATE, CAPTURE, SHARE FACTORY & LIVE BROADCASTING:
  ✅ **Create Button Overlay** (`Create` button / `F12`): Take 4K PNG/JPEG Screenshot, Save Last
     `15s / 30s / 1m / 5m / 15m / 60m` Circular Replay Video Clip, or Start/Stop Recording
  ✅ **Media Gallery & Built-In Share Studio Editor** (view, trim clips, add captions/overlays,
     export MP4/WebM/PNG, one-click share/export for X, YouTube, Discord, Reddit)
  ✅ **Live RTMP Broadcast Engine** (Twitch & YouTube streaming with live viewer/chat HUD overlay,
     picture-in-picture webcam composite, and commentary microphone audio ducking)
  ✅ **Remote Play Host & Client + Share Screen / Share Play** (play your SpicyPS5 window remotely
     from any browser, phone, tablet, or second PC at 60 FPS with full controller support!)

CONTROLLERS, TEMPEST 3D AUDIO, MEDIA APPS, ACCESSIBILITY & SETTINGS:
  ✅ Complete **DualSense**, **DualSense Edge**, **DualShock 4**, **Access Controller**, **PSVR2
     Sense (via OpenXR)**, and **Virtual Keyboard + Mouse DualSense** support (full dual-LRA
     haptics, all 10+ adaptive trigger profiles, 6-axis gyro/accel, dual-touch touchpad, speaker,
     mic + mute button LED, RGB light bar, player LEDs, and battery level telemetry)
  ✅ Complete **Tempest 3D Audio Engine** (256+ 3D-positioned sources, 5 personalized HRTF ear
     profiles via FFT overlap-save binaural convolution, Stereo / 5.1 / 7.1 / Atmos output, Pulse
     3D EQ presets, voice-chat mix balance, and acoustic echo cancellation)
  ✅ Working **Media Tab Apps** right inside the PS5 window (**Netflix, YouTube TV Leanback,
     Spotify, Disney+, Apple TV+, Prime Video, Hulu, Max, Crunchyroll, Twitch**, plus a built-in
     **4K HDR Local Media & Decrypted Blu-ray `BDMV` Player** supporting `.mp4`, `.mkv`, `.webm`,
     `.flac`, `.mp3`, `.ogg`, `.opus`)
  ✅ Full **Accessibility Suite** (Screen Reader TTS, Display Zoom, High Contrast, Colorblind
     Protanopia/Deuteranopia/Tritanopia GPU LUT filters, Reduce Motion, Closed Captions, Chat
     Transcription, Mono Audio, and Per-Game Custom Button Remapping)
  ✅ **All 15 Official PS5 Settings Pages + SpicyScale Tuner + Built-In Developer Debugger**
     (Memory Hex Viewer, Live Syscall/NID Tracer, RDNA2 Shader Disassembler/SPIR-V Inspector,
     PM4 Packet Ring Inspector, Frame Debugger, and Live Performance Telemetry HUD!)

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║       PART III: COMPLETE HARDWARE, ABI, FIRMWARE 26.06-14.00.00 & KERNEL SPEC            ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Implement every binary parser, ABI bridge, memory manager, GPU command processor, shader
recompiler, firmware loader, audio DSP, and HID driver strictly according to these exact
byte-level hardware and operating-system specifications.

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.1 — CPU ("OBERON" ZEN 2), ABI BRIDGING, TLS, SYSCALLS & NON-AMD INSTRUCTION LOWERING   │
└──────────────────────────────────────────────────────────────────────────────────────────┘

1. Hardware & ISA Baseline:
   - Architecture: 8-core / 16-thread custom AMD Zen 2 (`x86-64`), variable clock up to `3.50 GHz`
     (`TSC` frequency = `3,500,000,000 Hz`).
   - Instruction Extensions Expected by Guest Code: `SSE`..`SSE4.2`, **`SSE4a` (`EXTRQ`, `INSERTQ`,
     `MOVNTSD`, `MOVNTSS` — AMD-specific! ABSENT on ALL Intel CPUs & Apple Silicon Rosetta 2!)**,
     `AVX`, `AVX2`, `FMA3`, `BMI1`, `BMI2`, `F16C`, `AES-NI`, `PCLMULQDQ`, `SHA-NI`, `MOVBE`,
     `POPCNT`, `LZCNT` (`ABM`), `RDRAND`, `RDSEED`, `CLFLUSHOPT`, `FSGSBASE`.

2. Critical Calling Convention Bridge (Guest System V AMD64 <-> Host ABI):
   - **EVERY PlayStation 5 function (`eboot.bin`, `.prx`/`.sprx`, callbacks, `pthread` entry
     points, module `_init`/`module_start`) uses the System V AMD64 ABI (`__attribute__((sysv_abi))`)**:
       • Integer/pointer arguments 1–6: `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`
       • Floating-point/vector arguments 1–8: `xmm0` – `xmm7`
       • Return values: `rax`, `rdx` (int128/struct) and `xmm0`, `xmm1`
       • Callee-saved registers: `rbx`, `rbp`, `r12`, `r13`, `r14`, `r15` (`xmm6–xmm15` are
         CALLER-saved in guest SysV, whereas on Windows `ms_abi` `xmm6–xmm15`, `rdi`, and `rsi`
         are CALLEE-saved and require a 32-byte shadow home space!)
   - **Mandatory Rule**: Mark EVERY HLE export entry point with `SPICY_SYSV_ABI`
     (`__attribute__((sysv_abi))` on Clang/GCC; custom register-saving assembly trampoline when
     calling back from host into guest function pointers or when executing on ARM64!).

3. Guest Thread-Local Storage (`fs:` Segment Override `0x64`) & Syscall (`0F 05`) Interception:
   - PlayStation 5 userland reads thread-local data via `mov rax, fs:[0x00]` (Thread Control
     Block pointer where `*(tcb + 0x00) == tcb`, DTV at `*(tcb + 0x08)`, static module `PT_TLS`
     image placed at negative offset `tcb - align_up(memsz, align)`).
   - Because Windows reserves `gs:`/`fs:` TEB slots and macOS/Linux own `fs_base` unless `ARCH_SET_FS`
     / `wrfsbase` is isolated:
       • On Linux `x86_64` with `FSGSBASE` (or dedicated guest thread `arch_prctl(ARCH_SET_FS)`
         with host-call thunk switching `fs_base` across host boundaries) OR via Zydis/AOT binary
         code patching: rewrite every `fs:`-prefixed memory operand into an explicit call/thunk to
         `spicy_tls_get_base()` cached in a dedicated register/slot!
       • Rewrite or trap every raw `0F 05` (`syscall`) and `CD 80` instruction (`rax` = Prospero /
         FreeBSD syscall number, args in `rdi, rsi, rdx, r10, r8, r9`, return in `rax` with `CF=0`
         on success or `CF=1` and positive `errno` in `rax` on error!) straight into
         `SyscallDispatcher::Dispatch(GuestCpuContext&)`.

4. Universal CPU Lowering Engine (Guarantees Intel CPUs, Budget PCs & Apple Silicon Never Fault):
   - Probe host CPU capabilities at startup via `cpuid` (or `sysctl` on macOS).
   - Support BOTH **Ahead-of-Time binary lowering** (during loading/relinking) AND **SIGILL /
     Vectored Exception Handler (`VEH`) JIT fallback emulation** for every non-universal instruction:
       • `EXTRQ xmm1, ib, ib` (`66 0F 78 /0 ib ib`) & `EXTRQ xmm1, xmm2` (`66 0F 79 /r`):
         Extract bitfield `(index = imm8_2 & 63, length = imm8_1 & 63)` from lower 64 bits of `xmm1`
         (`length == 0` means `64` bits!).
       • `INSERTQ xmm1, xmm2, ib, ib` (`F2 0F 78 /r ib ib`) & `INSERTQ xmm1, xmm2` (`F2 0F 79 /r`):
         Insert `length` low bits from `xmm2[63:0]` into `xmm1[63:0]` starting at bit `index`.
       • `MOVNTSD m64, xmm1` (`F2 0F 2B /r`) -> lower directly to standard `MOVSD m64, xmm1`!
       • `MOVNTSS m32, xmm1` (`F3 0F 2B /r`) -> lower directly to standard `MOVSS m32, xmm1`!
       • `SHA-NI` (`SHA1RNDS4`, `SHA1NEXTE`, `SHA1MSG1`, `SHA1MSG2`, `SHA256RNDS2`, `SHA256MSG1`,
         `SHA256MSG2`) -> emulate in fast C++ SIMD handler if older CPU lacks `SHA-NI`!

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.2 — DUAL EXECUTION ENGINE, ELF64/SPRX DYNAMIC LINKER & EXACT SHA-1 NID ALGORITHM       │
└──────────────────────────────────────────────────────────────────────────────────────────┘

1. Sony PlayStation 5 Custom ELF64 Types, Program Headers & Dynamic Tags:
```cpp
namespace spicyps5::loader {

inline constexpr uint16_t ET_SCE_EXEC        = 0xFE00;
inline constexpr uint16_t ET_SCE_REPLAY_EXEC = 0xFE01;
inline constexpr uint16_t ET_SCE_DYNEXEC     = 0xFE10; // Main eboot.bin position-independent/fixed exec
inline constexpr uint16_t ET_SCE_DYNAMIC     = 0xFE18; // .prx / .sprx dynamic shared module

inline constexpr uint32_t PT_SCE_RELA        = 0x60000000;
inline constexpr uint32_t PT_SCE_DYNLIBDATA  = 0x61000000; // Separate dynamic symbol/string/reloc blob!
inline constexpr uint32_t PT_SCE_PROCPARAM   = 0x61000001; // Guest process parameters (malloc/free/sceLibc)
inline constexpr uint32_t PT_SCE_MODULE_PARAM= 0x61000002; // Module param table
inline constexpr uint32_t PT_SCE_RELRO       = 0x61000010; // Read-only after relocation
inline constexpr uint32_t PT_SCE_COMMENT     = 0x6FFFFF00;
inline constexpr uint32_t PT_SCE_VERSION     = 0x6FFFFF01;

inline constexpr uint64_t DT_SCE_IDTABENTSZ      = 0x61000005;
inline constexpr uint64_t DT_SCE_FINGERPRINT     = 0x61000007;
inline constexpr uint64_t DT_SCE_ORIGINAL_FILENAME = 0x61000009;
inline constexpr uint64_t DT_SCE_MODULE_INFO     = 0x6100000D;
inline constexpr uint64_t DT_SCE_NEEDED_MODULE   = 0x6100000F;
inline constexpr uint64_t DT_SCE_MODULE_ATTR     = 0x61000011;
inline constexpr uint64_t DT_SCE_EXPORT_LIB      = 0x61000013;
inline constexpr uint64_t DT_SCE_IMPORT_LIB      = 0x61000015;
inline constexpr uint64_t DT_SCE_EXPORT_LIB_ATTR = 0x61000017;
inline constexpr uint64_t DT_SCE_IMPORT_LIB_ATTR = 0x61000019;
inline constexpr uint64_t DT_SCE_HASH            = 0x61000025;
inline constexpr uint64_t DT_SCE_PLTGOT          = 0x61000027;
inline constexpr uint64_t DT_SCE_JMPREL          = 0x61000029;
inline constexpr uint64_t DT_SCE_PLTREL          = 0x6100002B;
inline constexpr uint64_t DT_SCE_PLTRELSZ        = 0x6100002D;
inline constexpr uint64_t DT_SCE_RELA            = 0x6100002F;
inline constexpr uint64_t DT_SCE_RELASZ          = 0x61000031;
inline constexpr uint64_t DT_SCE_RELAENT         = 0x61000033;
inline constexpr uint64_t DT_SCE_STRTAB          = 0x61000035;
inline constexpr uint64_t DT_SCE_STRSZ           = 0x61000037;
inline constexpr uint64_t DT_SCE_SYMTAB          = 0x61000039;
inline constexpr uint64_t DT_SCE_SYMENT          = 0x6100003B;
inline constexpr uint64_t DT_SCE_HASHSZ          = 0x6100003D;
inline constexpr uint64_t DT_SCE_SYMTABSZ        = 0x6100003F;

} // namespace spicyps5::loader
```
   - **CRITICAL DETAIL (`PT_SCE_DYNLIBDATA`)**: In PlayStation 5 `ET_SCE_DYNEXEC` and `ET_SCE_DYNAMIC`
     binaries, `DT_SCE_STRTAB`, `DT_SCE_SYMTAB`, `DT_SCE_RELA`, `DT_SCE_JMPREL`, and `DT_SCE_HASH`
     store **byte offsets relative to the beginning of the `PT_SCE_DYNLIBDATA` segment** (NOT virtual
     memory addresses!), whereas in standard relinked ELF64 files `DT_STRTAB`/`DT_SYMTAB`/`DT_RELA`
     store virtual addresses. Your loader MUST support **both** `ET_SCE_*` (`PT_SCE_DYNLIBDATA`
     offsets) AND standard `ET_EXEC` / `ET_DYN` (`PT_DYNAMIC` virtual addresses) seamlessly!
   - **Encoded Symbol Format in `DT_SCE_STRTAB`**: Each imported/exported symbol string has the
     format `<11-char-NID>#<lib_id_base64>#<mod_id_base64>` (for example: `rTXw65xmLIA#B#C`), or a
     plain C symbol name such as `strcmp`. Strip everything from `#` onward to obtain the exact
     11-character NID, and decode the library/module indices using Sony's Base64 table.

2. Exact Bit-for-Bit PlayStation 5 SHA-1 NID Hashing Algorithm (Mandatory Implementation):
```cpp
// Exact Sony 16-byte SHA-1 suffix & custom Base64 alphabet ('+' and '-', NO '=' padding):
inline constexpr std::array<uint8_t, 16> kSceNidSalt = {
    0x51, 0x8D, 0x64, 0xA6, 0x35, 0xDE, 0xD8, 0xC1,
    0xE6, 0xB0, 0x39, 0xB1, 0xC3, 0xE5, 0x52, 0x30
};
inline constexpr std::string_view kSceNidAlphabet =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-";

// Steps:
// 1. Concatenate ASCII bytes of `symbol_name` + `kSceNidSalt` (16 bytes).
// 2. Compute 20-byte SHA-1 digest.
// 3. Reverse the first 8 bytes: `rev[i] = digest[7 - i]` for `i = 0..7` (little-endian uint64 read).
// 4. Base64-encode those 8 reversed bytes (64 bits -> 11 6-bit groups, trailing 2 bits zero-padded):
//      group 0 (bytes 0,1,2) -> 4 chars; group 1 (bytes 3,4,5) -> 4 chars;
//      tail (bytes 6,7 << 8) -> 3 chars = 11 characters total!
// Verification test vector: ComputeNid("sceKernelAllocateDirectMemory") == "rTXw65xmLIA".
```

3. Dual Execution Modes Inside SpicyPS5:
   - **Mode A — `RuntimeEngine` (Instant Dynamic Execution — Default)**: Maps segments directly into
     sparse virtual memory, resolves all `R_X86_64_64`, `R_X86_64_GLOB_DAT`, `R_X86_64_JUMP_SLOT`,
     `R_X86_64_RELATIVE`, `R_X86_64_DTPMOD64`, `R_X86_64_DTPOFF64`, `R_X86_64_TPOFF64`, and
     `R_X86_64_PC32` relocations in-process, wires every imported 11-char NID to `SpicyHLE` (or
     loaded guest/firmware `.prx`/`.sprx`), executes `.preinit_array` -> `.init` -> `.init_array`,
     and jumps cleanly to `e_entry` with a valid SysV stack `{argc, argv[0], nullptr, envp...}` in `rdi`.
   - **Mode B — `NativeTranslator` (Ahead-of-Time Native Binary Compiler — Low-Spec CPU Turbo)**:
     Provides one-click & CLI static translation of PS5 ELF64 + `sce_module/*.prx` into native
     host binaries (`.exe` PE32+ on Windows, native `ET_DYN` ELF64 on Linux, `MH_EXECUTE` Mach-O
     on macOS, plus WebAssembly module export) with dead-NID reachability pruning, TOML binary
     patch application, and static `SSE4a` -> `SSE2/SSE4.1` instruction lowering for maximum FPS
     on weak 2–4 core CPUs!

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.3 — PLAYSTATION 5 SYSTEM SOFTWARE 26.06-14.00.00 COMPLETE CONTAINER & HYBRID LLE SPEC  │
└──────────────────────────────────────────────────────────────────────────────────────────┘

Implement full support in `src/firmware/` for **PlayStation 5 System Software `26.06-14.00.00`**
across all container formats so that ANY valid firmware artifact works cleanly with zero confusion:

1. Outer `BLS2` (`SLB2`) Container Header (`PS5UPDATE.PUP` Outer Wrapper):
```cpp
#pragma pack(push, 1)
struct Bls2Header {
    uint32_t magic;        // 0x32424C53 ("SLB2" in little-endian)
    uint32_t version;      // Container version (typically 1)
    uint32_t flags;        // Bit flags
    uint32_t file_count;   // Number of embedded update sub-files
    uint32_t block_count;  // Total 512-byte blocks in archive
    uint8_t  reserved[12]; // Padding to 32 bytes
};
static_assert(sizeof(Bls2Header) == 32);

struct Bls2Entry {
    uint64_t block_offset; // Multiply by 512 for byte offset from archive start
    uint64_t file_size;    // Exact byte size of inner sub-archive / XML / image
    char     name[32];     // Null-terminated ASCII entry name (e.g. "PS5UPDATE1.PUP", "version.xml")
};
static_assert(sizeof(Bls2Entry) == 48);
#pragma pack(pop)
```

2. Signed `PUP` & `SELF` / `SPRX` Container Structures:
```cpp
#pragma pack(push, 1)
struct SelfHeader {
    uint32_t magic;          // 0x1D3D154F (userland/game SELF/SPRX) or 0x5414F5EE (signed PUP/kernel)
    uint8_t  version;        // 0x00
    uint8_t  mode;           // 0x01
    uint8_t  endian;         // 0x01 (little-endian)
    uint8_t  attributes;     // 0x12
    uint32_t key_type;       // Key category identifier
    uint16_t header_size;    // Size of outer SELF metadata header
    uint16_t meta_size;      // Signature + per-segment digest metadata size
    uint64_t file_size;      // Original signed file length
    uint16_t num_entries;    // Count of SelfEntry records starting at byte offset 0x20
    uint16_t flags;          // Container flags
    uint32_t reserved;       // Padding to 32 bytes
};
static_assert(sizeof(SelfHeader) == 32);

struct SelfEntry {
    uint64_t props;          // [1:1]=encrypted, [3:3]=compressed, [11:11]=blocked, [31:20]=phdr index!
    uint64_t file_offset;    // Offset of segment bytes inside SELF file
    uint64_t encrypted_size; // Stored size in container
    uint64_t decrypted_size; // Uncompressed/unwrapped segment size
};
static_assert(sizeof(SelfEntry) == 32);
#pragma pack(pop)
```
   - **SelfUnwrapper Algorithm**:
     1. Read `SelfHeader` at `0x00` and `num_entries` × `SelfEntry` records starting at `0x20`.
     2. Immediately following the `SelfEntry` table (aligned to `0x10`) lies the embedded `Elf64_Ehdr`
        (`magic == 0x464C457F`) followed by `e_phnum` × `Elf64_Phdr` (`56` bytes each).
     3. Map each `SelfEntry` with `props & (1ULL << 11)` (`BLOCKED`) to target program header
        `phdr_idx = (props >> 20) & 0xFFF`. Decompress Zlib/Zstd if `props & (1ULL << 3)` is set.
     4. Measure Shannon entropy across `PT_LOAD` code segments:
        - If `< 7.90 bits/byte`: segment contains valid decrypted x86-64 machine code! Reconstruct
          a clean, standard `ELF64` image in memory or cache and load seamlessly.
        - If `>= 7.90 bits/byte`: segment is still hardware-SAMU AES-encrypted (such as inside an
          unmodified retail download `PS5UPDATE.PUP`). Record clean metadata (`26.06-14.00.00`
          version manifest, partition inventory, checksums) in System Software Settings **and
          automatically serve clean native C++ HLE + `SpicyVSH` without error or interruption!**

3. Hybrid HLE + Firmware `26.06-14.00.00` LLE Execution:
   - Mount `/app0`, `/hostapp`, `/system`, `/system_ex`, `/preinst`, `/data`, `/temp0`, `/download0`,
     `/savedata0`, and `/usb0` inside a deterministic virtual sandbox VFS.
   - Maintain a per-module policy switch (`HLE_NATIVE` | `FIRMWARE_LLE_IF_PRESENT` | `AUTO`):
     - Hardware-facing & OS-boundary modules (`libkernel`, `libSceAgcDriver`, `libSceGnmDriver`,
       `libSceVideoOut`, `libSceAudioOut`, `libScePad`, `libSceAmpr`, `libSceNet`, `libSceSsl`,
       `libSceSaveData`, `libSceNp*`, `libSceSystemService`, `libSceUserService`) **ALWAYS run native
       hardware-accelerated `SpicyHLE`** for maximum speed and host hardware integration.
     - Pure user-space helper modules (`libSceJson`, `libSceJson2`, `libSceXml`, `libSceZlib`,
       `libSceCesCs`, `libSceFreeType*`, `libSceFont*`, `libSceIcu`, `libSceJsc`, `libSceUlt`,
       `libSceFiber`, `libSceNgs2`) have **BOTH complete native C++ `SpicyHLE` implementations
       AND optional transparent loading of unwrapped Firmware `26.06-14.00.00` `.sprx` binaries**
       whenever present in `firmware/26.06-14.00.00/system/common/lib/`!

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.4 — GPU ("OBERON" RDNA2), PM4/AGC, SRT, 1,190-OPCODE ISA, 13 TILERS & RAY TRACING      │
└──────────────────────────────────────────────────────────────────────────────────────────┘

1. Command Stream Architecture (`PM4` Type-3 Packets + `SceAgc` Command Buffers):
   - Every `PM4` Type-3 packet header dword is `((type & 0x3) << 30) | (((dword_count - 1) & 0x3FFF) << 16) | ((opcode & 0xFF) << 8) | (predicate & 0x1)` where `type == 3`:
       • `0x10` `IT_NOP` (also carries debug markers, `SceAgc` inline metadata, & flip tags!)
       • `0x11` `IT_SET_BASE`
       • `0x15` `IT_DISPATCH_DIRECT` (`dim_x, dim_y, dim_z, dispatch_initiator`)
       • `0x16` `IT_DISPATCH_INDIRECT`
       • `0x1D` `IT_ATOMIC_GDS` / `0x1E` `IT_ATOMIC_MEM`
       • `0x22` `IT_COND_EXEC` / `0x27` `IT_DRAW_INDEX_2` (`max_size, index_lo, index_hi, count, draw_initiator`)
       • `0x2A` `IT_INDEX_TYPE` (`16-bit`, `32-bit`, `8-bit`)
       • `0x2D` `IT_DRAW_INDEX_AUTO` (`index_count, draw_initiator`)
       • `0x37` `IT_WRITE_DATA` (CPU/CP inline write to guest memory or MMIO register)
       • `0x3C` `IT_WAIT_REG_MEM` (`<, <=, ==, !=, >=, >` masked poll — integrate with host timeline semaphore!)
       • `0x3F` `IT_INDIRECT_BUFFER` (chained/nested sub-command buffer `DCB`/`CCB`/`ACB` jump!)
       • `0x46` `IT_EVENT_WRITE` / `0x47` `IT_EVENT_WRITE_EOP` / `0x48` `IT_EVENT_WRITE_EOS`
       • `0x49` `IT_RELEASE_MEM` (writes end-of-pipe fence label / triggers flip interrupt!)
       • `0x4D` `IT_DISPATCH_MESH_INDIRECT_MULTI` (PS5 Mesh/Task shader dispatch!)
       • `0x50` `IT_DMA_DATA` (CP DMA copy/fill between `ONION`/`GARLIC`/GDS)
       • `0x58` `IT_ACQUIRE_MEM` (GPU cache invalidation / barrier -> emits Vulkan memory barrier!)
       • `0x68` `IT_SET_CONFIG_REG` (base `0x02000`)
       • `0x69` `IT_SET_CONTEXT_REG` (base `0x0A000` — blend, depth/stencil, raster, viewport, MRTs!)
       • `0x76` `IT_SET_SH_REG` (base `0x02C00` — shader stage `PGM_LO/HI`, `RSRC1/2`, `USER_DATA_0..15`!)
       • `0x79` `IT_SET_UCONFIG_REG` (base `0x0C000` — `GE_CNTL`, primitive type, VRS state!)

2. Hardware Resource Descriptors (`V#` Buffer, `T#` Image/BVH, `S#` Sampler) & `SRT` Walker:
   - **Buffer Sharp `V#` (4 dwords / 128 bits)**: `base_address[47:0]`, `stride[13:0]`, `cache_swizzle`,
     `swizzle_enable`, `num_records` (32-bit element/byte count), `dst_sel_x/y/z/w`, `nfmt`, `dfmt`,
     `oob_select`.
   - **Image Sharp `T#` (8 dwords / 256 bits)**: `base_address_256B[39:0]`, `data_format`, `num_format`,
     `width`, `height`, `perf_mod`, `interlaced`, `dst_sel_x/y/z/w`, `base_level`, `last_level`,
     `tiling_idx` (`Linear`, `Standard4`, `Standard64`, `Standard256`, `PRT`, `RenderTarget`, `Depth`),
     `type` (`1D`, `2D`, `3D`, `Cube`, `1DArray`, `2DArray`, `2DMsaa`, **`BVH` node pointer**),
     `depth`/`array_pitch`, `meta_data_address` (DCC / HTILE / CMASK fast-clear metadata!).
   - **Sampler Sharp `S#` (4 dwords / 128 bits)**: `clamp_x/y/z`, `max_aniso_ratio`, `depth_compare_func`,
     `force_unnormalized`, `lod_bias`, `xy_mag_filter`, `xy_min_filter`, `z_filter`, `mip_filter`,
     `min_lod`, `max_lod`, `border_color_type`.
   - **Shader Resource Table (`SRT`) Walker & Scalar Provenance Pass**:
     PS5 `Agc` shaders pass pointers to nested tables of `T#`/`V#`/`S#` descriptors in `SGPR` user-data
     registers (`SPI_SHADER_USER_DATA_*`) and dereference them via `S_LOAD_DWORDX2` / `S_LOAD_DWORDX4` /
     `S_LOAD_DWORDX8`. Implement **Scalar Provenance Analysis + `SrtWalker`** so nested `SRT` descriptor
     loads resolve seamlessly into Vulkan bindless descriptor heaps (`VK_EXT_descriptor_indexing` /
     `VK_EXT_descriptor_buffer`) or standard descriptor sets on older GPUs!

3. Complete 20-Family / 1,190-Opcode RDNA2 (`gfx10`) Shader Recompiler (`data/rdna2_isa_spec.json`):
   - Support **Wave32 and Wave64**, all stages (`VS`, `PS`, `CS`, `GS`/`NGG`, `HS`/`DS` Tessellation,
     and `MS`/`TS` Mesh/Task shaders), and **all 20 encoding families** listed in `data/rdna2_isa_spec.json`:
       `SOP2` (51), `SOPK` (27), `SOP1` (65), `SOPC` (18), `SOPP` (37), `SMEM` (20),
       `VOP2` (51), `VOP1` (81), `VOPC` (190), `VOP3` (116), `VOP3P` (29), `VINTRP` (3),
       `DS` (123), `MUBUF` (75), `MTBUF` (16), `MIMG` (130), `EXP` (1), `FLAT` (54),
       `GLOBAL` (57), `SCRATCH` (22), plus the 24 extended opcodes = **1,190 opcodes**.
   - Structurize arbitrary `S_CBRANCH_*` / `EXEC`-masked control flow (`If`, `Loop`, `Break`, `Continue`),
     run SSA passes (`SsaRewrite`, `ConstantPropagation`, `DeadCodeElimination`, `ReadLaneElimination`,
     `ScalarProvenance`, `ResourceMaterialization`), emit valid **SPIR-V** (plus cross-compiled
     **MSL** / **HLSL** when needed), and persist compiled pipelines to an on-disk xxHash64 cache!

4. Dual Hardware + Software Ray Tracing & 13 Micro/Macro Compute Tilers:
   - Lower `IMAGE_BVH_INTERSECT_RAY` / `IMAGE_BVH64_INTERSECT_RAY` to **`VK_KHR_ray_query`** on RT-capable
     GPUs **AND** automatically emit a **Pure Compute-Shader Software BVH4 Box/Triangle Intersection
     Function** whenever `VK_KHR_ray_query` is unsupported on the host GPU (GTX 10/16 series, entry
     iGPUs, CPU Vulkan `Lavapipe`) so **ray-traced PS5 titles NEVER crash on non-RT hardware!**
   - Provide compute shaders (with SIMD CPU fallback for ultra-minimal devices) for all **13 RDNA2
     tiling modes**: `Standard4`, `Standard4_3D`, `Standard64`, `Standard64_3D`, `Standard256`,
     `PRT`, `PRT_3D`, `RenderTarget`, `Depth`, `PromoteD16`, `DemoteD16`, `ColorTransform`, `ColorClear`.

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.5 — UNIFIED 16 GB SPARSE MEMORY ENGINE & SPICYSCALE LOW-SPEC OPTIMIZATIONS             │
└──────────────────────────────────────────────────────────────────────────────────────────┘

1. Guest Virtual Address Space Layout (`src/core/memory_manager.{h,cpp}`):
   - System Managed Reservation: `0x0000'0004'0000` – `0x0007'FFFF'BFFF`
   - User / Direct & Flexible Memory Aperture: `0x0010'0000'0000` – `0x00FB'FFFF'FFFF`
     (automatically shifted above `0x0070'0000'0000` on macOS when Rosetta/CommPage occupies low ranges)
   - Physical Direct Memory Pool (`sceKernelAllocateDirectMemory`, `sceKernelMapDirectMemory`,
     `sceKernelCheckedReleaseDirectMemory`): reports full PS5 `13.5 GB` physical capacity to games
     across memory types `WB_ONION` (`0`), `WC_GARLIC` (`3`), and `UC` (`4`), plus full `Flexible`
     memory (`sceKernelMapFlexibleMemory`, `sceKernelMapNamedFlexibleMemory`).

2. MANDATORY LOW-RAM BREAKTHROUGH — Sparse Virtual Reservation + LRU Zstd Cold-Page Eviction:
   - **NEVER call `VirtualAlloc(..., MEM_COMMIT)` or `CreateFileMapping(..., SEC_COMMIT)` on a 16 GB
     backing store at startup!** That immediately fails on 4 GB, 8 GB, and 16 GB PCs!
   - Instead:
       • **Windows**: Reserve virtual address ranges using `VirtualAlloc2` `MEM_RESERVE | MEM_RESERVE_PLACEHOLDER`
         (or `VirtualAlloc(..., MEM_RESERVE)` + sparse `SEC_RESERVE` file-mapping views committed in
         `64 KiB` / `2 MiB` chunks ONLY when mapped or first touched!).
       • **Linux**: Reserve address space with `PROT_NONE | MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE`
         and back aliasable Direct Memory offsets using sparse `memfd_create` (`fallocate` punches
         holes via `FALLOC_FL_PUNCH_HOLE | FALLOC_FL_KEEP_SIZE` immediately upon unmap/release!).
       • **macOS**: Use sparse `shm_open` + `mach_vm_remap` without upfront page dirtying.
       • **LRU Zstd Cold-Page Compressor**: When `host_total_ram < 12 GB` and process RSS approaches
         `65%` of host RAM, compress cold 2 MiB guest pages with fast `ZSTD_compress(..., level=1)`
         (typically `3:1`–`6:1` compression ratio on game heaps/assets!) and transparently restore
         on access via page-fault handler in `< 250 µs`!
   - **Result**: `SpicyPS5` boots the entire VSH + OS runtime in **`< 220 MB` physical RAM**, allowing
     even **4 GB and 8 GB RAM laptops and cloud VMs** to run smoothly!

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.6 — ALL 368 SYSTEM MODULES (`libSce*`) & PROSPERO OS HLE ARCHITECTURE                  │
└──────────────────────────────────────────────────────────────────────────────────────────┘

Use `data/ps5_nid_database.json` (**368 modules / 11,703 symbol & NID entries**) to generate complete
registration tables and implement modular, well-tested HLE subsystems across all 12 domain groups:

  1. **Core Kernel, Threading & C Runtime** (`libkernel`, `libkernel_sys`, `libc`, `libSceLibcInternal`,
     `libSceUlt` [User-Level Threading queue/runtime/semaphore/mutex], `libSceFiber`, `libSceAmpr`
     [Asynchronous Memory Page & DMA file/page engine], `libSceFios2` [async I/O scheduler, overlays,
     decompressor filters], `libSceRtc`, `libSceRegMgr`, `libSceRandom`, `ulobjmgr`).
  2. **System Lifecycle, Users & Security Spoof** (`libSceSysmodule`, `libSceSystemService`,
     `libSceUserService`, `libSceLoginService`, `libSceLoginDialog`, `libSceSigninDialog`,
     `libSceDipsw`, `libSceSpSysCallWrapper`, `libSceTEEClient` — cleanly returning valid tokens/OK).
  3. **Graphics, Display & VRR** (`libSceAgc`, `libSceAgcDriver`, `libSceAgcResourceRegistration`,
     `libSceAgcVsh`, `libSceGnmDriverForNeoMode`, `libSceGnmDriverCompat1`, `libSceVideoOut`,
     `libSceVideoOutSecondary`, `libSceHdrScopes`, `libSceDolbyVision`, `libScePsml` [PlayStation ML
     / PSSR upscaling & dispatch API]).
  4. **Tempest 3D Audio, Codec Batch Engine & Voice** (`libSceAudioOut` [including `sceAudioOut2*`!],
     `libSceAudioIn`, `libSceAudio3d`, `libSceAudioPropagation`, `libSceS3da`, `libSceNgs2` /
     `libSceNgs2.native`, `libSceAjm` / `libSceAjm.native` [ATRAC9, AAC, MP3, Opus batch jobs],
     `libSceAcm` [FFT, IFFT, convolution reverb], `libSceAudiodec*`, `libSceOpus*`, `libSceVorbisDec`,
     `libSceVoice`, `libSceVoiceChat`, `libSceVoiceQoS`, `libSceTextToSpeech2`, `libSceSystemTts`).
  5. **Input, Haptics, Camera & PSVR2** (`libScePad`, `libScePadTracker`, `libSceHidControl`,
     `libSceBluetoothHid`, `libSceUsbd`, `libSceMouse`, `libSceKeyboard`, `libSceConvertKeycode`,
     `libSceMove`, `libSceSystemGesture`, `libSceCamera`, `libSceHmd`, `libSceHmd2`, `libSceVrTracker`,
     `libSceVrTracker2`, `libSceHandTracker`).
  6. **Save Data, Packaging, DLC & Background Install** (`libSceSaveData` / `.native`,
     `libSceSaveDataDialog` / `.native`, `libSceAppContent`, `libSceAppInstUtil`, `libScePlayGo`,
     `libScePlayGoDialog`, `libSceBgft`, `libSceUsbStorage`, `libSceContentSearch`, `libSceContentExport`,
     `libSceContentDelete`, `libSceGameUpdate`).
  7. **Networking, TLS, HTTP/2 & PlayStation Network** (`libSceNet`, `libSceNetCtl`, `libSceNetCtlAp`,
     `libSceRudp`, `libSceSsl`, `libSceLibreSsl`, `libSceLibreSsl3`, `libSceHttp`, `libSceHttp2`,
     `libSceHttpCache`, `libSceNpCommon`, `libSceNpManager`, `libSceNpAuth`, `libSceNpWebApi`,
     `libSceNpWebApi2`, `libSceNpCppWebApi`, `libSceNpTrophy`, `libSceNpTrophy2`,
     `libSceNpUniversalDataSystem`, `libSceNpTus`, `libSceNpScoreRanking`, `libSceNpMatching2`,
     `libSceNpSessionSignaling`, `libSceNpSignaling`, `libSceNpParty`, `libSceNpCommerce`,
     `libSceNpEntitlementAccess`, `libSceNpGameIntent`, `libSceNpSns`, `libSceNpUtility`).
  8. **Media Playback, Image Codecs, Streaming & DRM Containers** (`libSceAvPlayer`,
     `libSceAvPlayerStreaming`, `libSceVideodec`, `libSceVideodec2`, `libSceVdecCore`, `libSceVdecsw`,
     `libSceVdecSavc2`, `libSceVdecShevc`, `libSceVenc`, `libSceJpegDec`, `libSceJpegEnc`,
     `libScePngDec`, `libScePngEnc`, `libSceJxr`, `libSceImageUtil`, `libSceZlib`, `libSceJson2`,
     `libSceXml`, `libSceCesCs`, `libSceFont`, `libSceFontFt`, `libSceFreeType*`, `libScePlayReady*`).
  9. **Dialogs, Share, Broadcast, Remote Play & VSH Shell Bridges** (`libSceCommonDialog`,
     `libSceMsgDialog`, `libSceErrorDialog`, `libSceIme`, `libSceImeDialog`, `libSceWebBrowserDialog`,
     `libSceNpProfileDialog`, `libSceNpFriendListDialog`, `libScePlayerInvitationDialog`,
     `libSceScreenShot`, `libSceVideoRecording`, `libSceShare`, `libSceShareUtility`,
     `libSceShareFactoryUtil`, `libSceSharePlay`, `libSceGameLiveStreaming`, `libSceRemoteplay`,
     `libSceSocialScreen`, `libSceCompanionHttpd`, `libSceCompanionUtil`, `libSceShellUIUtil`,
     `libSceRnpsAppMgr`, `libSceJsc`, `libSceNKWebKit`, `libSceComposite`).

  **Resilient Unimplemented Export Policy**:
  Provide two selectable modes:
    • `Playable Mode` (Default for users): Any call to an unimplemented minor NID logs a structured
      one-time warning (`[HLE:UNIMPL] module::symbol (NID) rdi=... rsi=...`), records the hit in live
      telemetry, and returns `SCE_OK (0)` (or valid dummy handle) so games keep running smoothly!
    • `Strict Verification Mode` (`--strict-hle`): Traps immediately with full register + stack dump
      for debugging and automated test validation.

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.7 — BYTE-EXACT DUALSENSE USB & BLUETOOTH PROTOCOL (HAPTICS + 10 TRIGGER MODES + CRC32) │
└──────────────────────────────────────────────────────────────────────────────────────────┘

Implement full native HID communication for **DualSense (`0x054C:0x0CE6`)** and **DualSense Edge
(`0x054C:0x0DF2`)** over BOTH **USB** and **Bluetooth**, plus **DualShock 4 (`0x054C:0x05C4` /
`0x09CC`)**, generic XInput/SDL gamepads, and **Keyboard + Mouse Virtual DualSense**:

  1. **USB Input Report (`Report ID 0x01`, `64` bytes)** vs **Bluetooth Full Input Report (`Report ID 0x31`, `78` bytes)**:
     - Note the critical `1`-byte shift in Bluetooth `0x31` reports (byte `0` = `0x31`, byte `1` =
       BT header seq/tag, so sticks start at byte `2` on Bluetooth vs byte `1` on USB!):
         • Sticks: `lx, ly, rx, ry` (`uint8`, `0x80` neutral)
         • Analog Triggers: `l2_analog, r2_analog` (`uint8`, `0..255`)
         • Sequence Counter (`uint8`)
         • Buttons `[0]`: low nibble = D-Pad hat (`0=N, 1=NE, 2=E, 3=SE, 4=S, 5=SW, 6=W, 7=NW, 8=Released`),
           bit4=`Square`, bit5=`Cross`, bit6=`Circle`, bit7=`Triangle`
         • Buttons `[1]`: bit0=`L1`, bit1=`R1`, bit2=`L2`, bit3=`R2`, bit4=`Create`, bit5=`Options`,
           bit6=`L3`, bit7=`R3`
         • Buttons `[2]`: bit0=`PS`, bit1=`TouchpadClick`, bit2=`Mute`
         • 6-Axis IMU (`int16_t` LE × 6): `gyro_pitch, gyro_yaw, gyro_roll, accel_x, accel_y, accel_z`
           + `uint32_t sensor_timestamp` + `uint8_t temperature`
         • Dual-Point Touchpad (`TouchPoint[2]`, `4` bytes each): byte0 = `bit7 (!active) | (id & 0x7F)`,
           bytes 1..3 = packed 12-bit `x` (`0..1919`) and 12-bit `y` (`0..1079`)!
         • Battery byte: low nibble `level (0..10)`, high nibble `charging_status`
  2. **USB Output Report (`Report ID 0x02`, `48` bytes)** & **Bluetooth Output Report (`Report ID 0x31`, `78` bytes)**:
     - **CRITICAL BLUETOOTH SECRET**: Every Bluetooth output report (`0x31`, `78` bytes) **MUST end at
       bytes `[74..77]` with a Little-Endian IEEE 802.3 CRC-32 (`0xEDB88320`) seeded with prefix byte
       `0xA2` concatenated with bytes `[0..73]`** (`crc32(0xA2 || report[0..73])`)! Without that exact
       `0xA2` seed byte, DualSense silently drops 100% of Bluetooth haptics, LEDs, and adaptive triggers!
     - Implement **all Adaptive Trigger Motor Effect Modes** (`11`-byte `TriggerEffect` block at
       right=`[11..21]`, left=`[22..32]`):
         `0x00` `Off`, `0x01` `Rigid` (continuous resistance), `0x02` `Pulse` (detent + release),
         `0x21` `Feedback` (10-zone strength array packed in 32-bit mask), `0x25` `Weapon` (start zone,
         end zone, pull strength), `0x26` `Vibration` (10-zone amplitude + frequency Hz), plus SDK
         SlopeFeedback / Galloping / Machine profiles mapped faithfully to hardware parameters!
     - Drive dual-LRA haptic PCM at `48 kHz` stereo when connected via USB audio device, AND smoothly
       synthesize matching high/low motor rumble envelopes from stereo RMS energy on Bluetooth or
       standard XInput/SDL controllers!

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.8 — TEMPEST 3D AUDIO DSP, MULTI-BUS `NGS2` RACK GRAPH & `AJM` BATCH CODEC ENGINE      │
└──────────────────────────────────────────────────────────────────────────────────────────┘

Implement a complete, sample-accurate 32-bit float `48 kHz` (`256`-sample low-latency quantum,
configurable `512`/`1024` buffer size for low-spec CPUs) audio subsystem in `src/audio/`:

  1. **Tempest 3D Binaural HRTF Convolver (`src/audio/tempest_engine.{h,cpp}`)**:
     - Support up to **256 simultaneous 3D point/bed sources** (`sceAudio3dObjectReserve`,
       `sceAudio3dPortPush`, `sceAudio3dPortAdvance`, `sceAudio3dGetDefaultOpenParams`).
     - Ship **5 mathematically synthesized anthropometric Kemar/CIPIC-style HRTF ear profiles**
       (matching PS5's 5 built-in 3D Audio Ear Type profiles selectable with an interactive listening
       test in **Settings -> Sound -> 3D Audio -> Adjust 3D Audio Profile**!).
     - Convolve left/right ear HRIR filters in the frequency domain via **Partitioned Overlap-Save
       Radix-2 FFT** (`512`-point complex FFT), distance attenuation (`1 / max(d, min_d)`), air
       absorption low-pass filtering, interaural time difference (`ITD`), and elevation pinna cues,
       plus automatic lightweight constant-power stereo panning fallback on ultra-low-spec Tier 0 CPUs!
  2. **Synthesized Polyphonic Ambient System Sound Designer (`src/audio/ui_synth.{h,cpp}`)**:
     - Programmatically synthesize clean, warm, crystalline `48 kHz` stereo waveforms at startup
       (zero copyrighted external audio files required, yet 100% unmistakable console feel!):
         • **Boot / Startup Ambient Chord**: Shimmering layered fifth/ninth pad + warm sub-bass swell
         • **Home Tile Focus Tick & Launch Whoosh**: Crisp filtered transient + airy harmonic tail
         • **PS Control Center Open / Close Chime**
         • **Trophy Earned Chime** (distinct harmonic intervals for **Bronze**, **Silver**, **Gold**,
           and a triumphant multi-voice **Platinum** fanfare!)
         • **Screenshot Shutter & Error / Notification Tones**
  3. **Full Codec & Mixing Graph (`SceAudioOut`, `SceAudioOut2`, `SceNgs2`, `SceAjm`, `SceAcm`)**:
     - `SceAudioOut` (`8` standard ports per user: Main, BGM, Voice, Personal, PadSpeaker, Aux) +
       PS5-native **`SceAudioOut2`** context/port/speaker-array APIs!
     - `SceNgs2`: Multi-rack voice/submix/master DSP graph (`Sampler`, `Envelope`, `Biquad Filter`,
       `Compressor/Limiter`, `Reverb`, `Panner`).
     - `SceAjm` (`sceAjmBatchJobRun`, `RunSplit`, `Decode`, `Encode`, `Resample`, gapless skip/trim):
       Full software decoders for **ATRAC9**, **AAC (`M4AAC`)**, **MP3**, **Opus**, **Vorbis**, and **PCM16/Float**.
     - Cross-platform output backends: **SDL3 Audio** (universal primary covering WASAPI, PipeWire,
       PulseAudio, ALSA, and CoreAudio automatically!) + **WebSocket Low-Latency PCM/Opus Stream**
       for Live Web/Remote Play Window clients!

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ 3.9 — 3-MODE BAN-SAFE NETWORK/PSN STACK, STREAMING HUB & LIVE WEB WINDOW (`0.0.0.0`)     │
└──────────────────────────────────────────────────────────────────────────────────────────┘

  1. **Three-Mode Ban-Safe Network & PlayStation Network Architecture (`src/network/`)**:
     - **Mode 1 — `SpicyNet` Open PSN / RPCN Multiplayer & Cloud Service (Default — 100% Ban-Safe)**:
       Works out of the box with zero Sony account risk! Implements full BSD sockets (`libSceNet`),
       interface telemetry (`libSceNetCtl`), reliable UDP (`libSceRudp`), TLS 1.3 (`libSceSsl` /
       `LibreSsl`), HTTP/1.1 & HTTP/2 (`libSceHttp` / `libSceHttp2`), plus an embedded/cloud
       **`SpicyNet` Coordinator** backing Friends, Presence, Direct/Group Messages, 16-Player Voice
       Parties, Matchmaking Rooms (`libSceNpMatching2` & `SessionSignaling`), Leaderboards
       (`libSceNpScoreRanking`), Title User Storage (`libSceNpTus`), Cloud Save Sync, and Trophy Sync!
     - **Mode 2 — Official PlayStation Companion Token Sync (`NPSSO` Read/Sync Mode)**:
       Optional safe companion mode where a user pastes their standard web `npsso` session token to
       import their real Online ID, real Avatar, real Trophy list/levels, real Friends presence, and
       Store catalog metadata — **strictly read/web-companion safe, NEVER forging console `IDPS`
       certificates so no user account is ever put at risk!**
     - **Mode 3 — Custom Research Server Endpoint**: User-configurable API host & certificate path.

  2. **Live Interactive Web & Remote Play Window Bridge (`src/frontend/web_window.{h,cpp}`)**:
     - Whenever launched with `--web-window 0.0.0.0:8080` (or enabled in **Settings -> System ->
       Remote Play & Web Window**):
         • Bind cleanly to **`0.0.0.0`** (NEVER `127.0.0.1`!), accept all `Host`/`Origin` headers so
           cloud reverse proxies (`https://{port}-{sandbox}.e2b.app`), LAN IPs, Tailscale, phones,
           iPads, and Chromebooks connect without host-rejection errors!
         • In browser frontend JavaScript, **ALWAYS construct fetch & WebSocket URLs strictly from
           relative paths and `window.location` (`${location.protocol === 'https:' ? 'wss:' : 'ws:'}//${location.host}/ws`)
           — NEVER hardcode `localhost` or `127.0.0.1`!**
         • Stream live 60 FPS frames + synchronized `48 kHz` WebAudio + full bidirectional **HTML5
           Gamepad API** (plug a real DualSense into your laptop/phone and play seamlessly in browser!)
           + interactive virtual DualSense HUD + keyboard/mouse controls + drag-and-drop file
           installer for `.elf`, `.self`, `.zar`, `.pkg`, and `PS5UPDATE.PUP`!

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                PART IV: COMPLETE SYSTEM ARCHITECTURE DIAGRAM                             ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│            USER LAUNCHES `SpicyPS5` (Desktop Window OR Live Web Window `:8080`)          │
└────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                             ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                PRESENTATION SHELL: "THE PLAYSTATION 5 INSIDE A WINDOW"                   ║
║                                                                                          ║
║  ┌────────────────────────────────────────────────────────────────────────────────────┐  ║
║  │  1. BOOT SEQUENCE: Particle Light Wave + Polyphonic Startup Chime + Profile Pick   │  ║
║  └─────────────────────────────────────────┬──────────────────────────────────────────┘  ║
║                                            ▼                                             ║
║  ┌────────────────────────────────────────────────────────────────────────────────────┐  ║
║  │  2. SPICYVSH (26.06-14.00.00 VISUAL SHELL — 60/120 FPS HARDWARE ACCELERATED)       │  ║
║  │     [Games] [Media]                                  [Search] [Settings] [Profile] │  ║
║  │     ┌───────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────────┐   │  ║
║  │     │ Store │ │ Explore │ │ Game #1 │ │ Game #2 │ │ Captures │ │ Game Library │   │  ║
║  │     └───────┘ └─────────┘ └─────────┘ └─────────┘ └──────────┘ └──────────────┘   │  ║
║  │     + Activities Cards  + Trophy Banner & Sound  + Live Control Center (PS Btn)    │  ║
║  │     + Create Overlay    + On-Screen IME Keyboard + All 15 PS5 Settings Pages       │  ║
║  └─────────────────────────────────────────┬──────────────────────────────────────────┘  ║
║                                            ▼                                             ║
║  ┌────────────────────────────────────────────────────────────────────────────────────┐  ║
║  │  3. COMMERCIAL & HOMEBREW PS5 TITLES + BUILT-IN SDK SHOWCASE APPS + MEDIA HUB      │  ║
║  └────────────────────────────────────────────────────────────────────────────────────┘  ║
╚════════════════════════════════════════════╤═════════════════════════════════════════════╝
                                             ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                          SPICYPS5 CORE ENGINE & SUBSYSTEMS                               ║
║                                                                                          ║
║  ┌───────────────────────────────────────┐  ┌─────────────────────────────────────────┐  ║
║  │ DUAL EXECUTION CORE                   │  │ SPICYSCALE UNIVERSAL LOW-SPEC ENGINE    │  ║
║  │ • Mode A: Dynamic In-Process Loader   │  │ • Sparse Virtual RAM (<220 MB Idle RSS) │  ║
║  │   (ELF64/SELF/SPRX/.zar/PFS/PKG)      │  │ • LRU Zstd Cold-Page Compressor         │  ║
║  │ • Mode B: Native AOT Binary Compiler  │  │ • Adaptive Spin->Futex CPU Governor     │  ║
║  │   (PE32+/ELF64/Mach-O/WASM)           │  │ • CPU Instruction Lowering (SSE4a/ARM)  │  ║
║  │ • SysV <-> Host ABI Trampolines       │  │ • 5-Tier GPU Scaling (Tier S -> Tier 4) │  ║
║  │ • SHA-1 11-Char NID Linker (11,703+)  │  │ • 360p/540p/720p -> FSR/EASU Upscaler   │  ║
║  └───────────────────────────────────────┘  └─────────────────────────────────────────┘  ║
║                                                                                          ║
║  ┌───────────────────────────────────────┐  ┌─────────────────────────────────────────┐  ║
║  │ FIRMWARE 26.06-14.00.00 ENGINE        │  │ UNIFIED 368-MODULE HLE KERNEL           │  ║
║  │ • BLS2 (`0x32424C53`) & PUP Unpacker  │  │ • `libkernel`, `libc`, `Ult`, `Fiber`   │  ║
║  │ • Entropy Encryption Classifier       │  │ • `Ampr` DMA, `Fios2`, `SaveData`       │  ║
║  │ • `SelfUnwrapper` -> Clean ELF64      │  │ • `Agc`, `AgcDriver`, `Gnm`, `VideoOut` │  ║
║  │ • SST Fonts / Sounds / Cert Mounter   │  │ • `AudioOut/2`, `Audio3d`, `Ngs2`, `Ajm`│  ║
║  │ • Optional User-Space `.sprx` LLE     │  │ • `Pad`, `Np*` (368 Modules Indexed!)   │  ║
║  └───────────────────────────────────────┘  └─────────────────────────────────────────┘  ║
║                                                                                          ║
║  ┌───────────────────────────────────────┐  ┌─────────────────────────────────────────┐  ║
║  │ OBERON RDNA2 GRAPHICS COMPILER        │  │ INPUT, TEMPEST 3D AUDIO, NET & MEDIA    │  ║
║  │ • PM4 Type-3 + Agc DCB/CCB/ACB Parser │  │ • DualSense USB (`0x01`/`0x02`) & BT    │  ║
║  │ • `SrtWalker` + `ScalarProvenance`    │  │   (`0x31` + `0xA2` Seed CRC-32!)        │  ║
║  │ • 20-Family / 1,190-Opcode RDNA2 ISA  │  │ • 10+ Trigger Modes + Dual-LRA Haptics  │  ║
║  │ • SSA Optimizer -> SPIR-V 1.6 / MSL   │  │ • Tempest FFT HRTF 3D Audio + 5 Profiles│  ║
║  │ • Multi-Level Page Table & 13 Tilers  │  │ • 3-Mode Ban-Safe PSN/RPCN + Store/Sync │  ║
║  │ • Hardware RT + Software Compute BVH  │  │ • Streaming Apps + Replay + RTMP Stream │  ║
║  └───────────────────────────────────────┘  └─────────────────────────────────────────┘  ║
╚════════════════════════════════════════════╤═════════════════════════════════════════════╝
                                             ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                     HOST PLATFORM ABSTRACTION LAYER (HAL)                                ║
║   Windows x64 (Vulkan 1.3 / D3D12)  │  Linux x64 (Vulkan 1.3 / Lavapipe)  │  macOS Metal ║
║                        + Live Remote/Browser Window Bridge (`0.0.0.0:8080`)              ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                   PART V: COMPLETE PRODUCTION MONOREPO LAYOUT                            ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Organize the repository cleanly following this exact modular hierarchy:

SpicyPS5/
├── .clang-format
├── .clang-tidy
├── .editorconfig
├── .gitignore
├── CMakeLists.txt
├── CMakePresets.json
├── LICENSE
├── README.md
├── PROMPT.md
├── ARCHITECTURE.md
├── FEATURES.md
├── PROGRESS.md
│
├── .github/
│   └── workflows/
│       ├── ci-linux.yml
│       ├── ci-windows.yml
│       ├── ci-macos.yml
│       └── release.yml
│
├── cmake/
│   ├── CompilerFlags.cmake
│   ├── Dependencies.cmake
│   ├── PlatformDetection.cmake
│   ├── Sanitizers.cmake
│   └── Packaging.cmake
│
├── data/
│   ├── ps5_nid_database.json               (368 modules / 11,703 symbol & NID entries)
│   └── rdna2_isa_spec.json                 (20 encoding families / 1,190 RDNA2 opcodes)
│
├── src/
│   ├── main.cpp                            (Unified Desktop Window + `--web-window` + CLI entry)
│   │
│   ├── common/
│   │   ├── types.h
│   │   ├── abi.h                           (`SPICY_SYSV_ABI`, host <-> guest calling glue)
│   │   ├── result.h                        (`Result<T, Error>` zero-overhead error handling)
│   │   ├── error_codes.h                   (Exact `SCE_ERROR_*` & POSIX `ORBIS_KERNEL_ERROR_*`)
│   │   ├── config.{h,cpp}                  (TOML/JSON persistent console & per-game settings)
│   │   ├── logger.{h,cpp}                  (Structured multi-channel ring-buffered logger)
│   │   ├── hash.{h,cpp}                    (SHA-1, SHA-256, CRC-32 `0xEDB88320`, xxHash64)
│   │   ├── bit_utils.h
│   │   ├── thread_pool.{h,cpp}
│   │   └── telemetry.{h,cpp}
│   │
│   ├── scale/                              (`SpicyScale` — Runs Smoothly on Any PC!)
│   │   ├── hardware_probe.{h,cpp}          (CPU flags, RAM/Swap, VRAM, RT/Mesh/Lavapipe probe)
│   │   ├── tier_manager.{h,cpp}            (Auto/manual Tier S, 0, 1, 2, 3, 4 engine profiles)
│   │   ├── compressed_page_pool.{h,cpp}    (LRU Zstd level-1 cold guest page compressor)
│   │   ├── cpu_governor.{h,cpp}            (Adaptive `_mm_pause` -> futex backoff for 2–6 cores)
│   │   └── spatial_upscaler.{h,cpp}        (EASU + RCAS / FSR / bilinear scaling pass)
│   │
│   ├── firmware/                           (System Software `26.06-14.00.00` Engine)
│   │   ├── pup_parser.{h,cpp}              (`BLS2` `0x32424C53` + signed `PUP` `0xEEF51454`)
│   │   ├── self_unwrapper.{h,cpp}          (`0x1D3D154F` / `0x5414F5EE` -> clean `ELF64`)
│   │   ├── entropy_analyzer.{h,cpp}        (Distinguishes retail encrypted vs unwrapped code)
│   │   ├── firmware_manager.{h,cpp}        (Mounts `/system`, `/system_ex`, fonts, certs, LLE)
│   │   └── safe_mode.{h,cpp}               (All 8 authentic PS5 Safe Mode recovery operations)
│   │
│   ├── core/
│   │   ├── runtime.{h,cpp}                 (Top-level PS5 console lifecycle, boot, Rest Mode)
│   │   ├── memory_manager.{h,cpp}          (Sparse 16 GB address space, Direct/Flexible memory)
│   │   ├── vfs.{h,cpp}                     (Sandbox mounts `/app0`, `/savedata0`, `.zar`, `PFS`, `PKG`)
│   │   ├── zarchive_reader.{h,cpp}         (Zero-extraction `.zar` random-access game mounting)
│   │   ├── pkg_installer.{h,cpp}           (Package & patch installer + PlayGo chunk manager)
│   │   └── loader/
│   │       ├── nid_hash.{h,cpp}            (Bit-exact Sony SHA-1 11-char Base64 NID engine)
│   │       ├── elf_loader.{h,cpp}          (`ET_SCE_DYNEXEC`, `ET_SCE_DYNAMIC`, `PT_SCE_DYNLIBDATA`)
│   │       ├── dynamic_linker.{h,cpp}      (Relocations, `PT_TLS`, `.init_array`, `LoadExec`)
│   │       ├── cpu_lowerer.{h,cpp}         (`SSE4a` `EXTRQ`/`INSERTQ`/`MOVNTSD`/`MOVNTSS` + `syscall` + `fs:`)
│   │       └── native_translator.{h,cpp}   (AOT PS5 ELF -> Native Host Binary Turbo Mode)
│   │
│   ├── kernel/
│   │   ├── syscall_dispatcher.{h,cpp}      (Prospero/FreeBSD syscall table + `SIGILL`/trampoline)
│   │   ├── module_registry.{h,cpp}         (Indexes all 368 modules & 11,703 NIDs from database)
│   │   ├── libkernel/                      (Threads, pthreads, futex/syncOnAddress, kqueue, VM, FS)
│   │   ├── libc_internal/                  (Guest heap `malloc`/`free`, stdio, string, math, locale)
│   │   ├── threading_ext/                  (`libSceUlt` User-Level Threading & `libSceFiber`)
│   │   ├── async_io/                       (`libSceAmpr` Async DMA Engine & `libSceFios2`)
│   │   ├── system_services/                (`Sysmodule`, `SystemService`, `UserService`, `Rtc`, `RegMgr`)
│   │   ├── graphics_hle/                   (`libSceAgc`, `libSceAgcDriver`, `Gnm`, `VideoOut`, `Psml`)
│   │   ├── audio_hle/                      (`AudioOut`, `AudioOut2`, `Audio3d`, `Ngs2`, `Ajm`, `Acm`, `Voice`)
│   │   ├── input_hle/                      (`Pad`, `Mouse`, `Keyboard`, `SystemGesture`, `Hmd2`, `VrTracker2`)
│   │   ├── storage_hle/                    (`SaveData`, `SaveDataDialog`, `AppContent`, `PlayGo`, `Bgft`)
│   │   ├── net_np_hle/                     (`Net`, `NetCtl`, `Rudp`, `Ssl`, `Http/2`, `NpManager`, `NpTrophy2`, `NpMatching2`, `NpWebApi2`, `NpTus`, `NpScore`)
│   │   ├── media_ui_hle/                   (`AvPlayer`, `Videodec2`, `Jpeg/Png`, `Font`, `CesCs`, `Json2`, `CommonDialog`, `MsgDialog`, `ImeDialog`, `Share`, `ShellUI`)
│   │   └── hypervisor_spoof/               (`SblAuthMgr`, `TEEClient`, `Dipsw` clean-room stubs)
│   │
│   ├── graphics/
│   │   ├── presenter.{h,cpp}               (Unified frame compositor: Game + Overlays + LUT + Upscale)
│   │   ├── pm4_processor.{h,cpp}           (Full Type-3 PM4 + `SceAgc` DCB/CCB/ACB execution engine)
│   │   ├── page_table.{h,cpp}              (Multi-level GPU page table + write-watch invalidation)
│   │   ├── descriptor_heap.{h,cpp}         (`T#` / `V#` / `S#` decoding & `SrtWalker` materialization)
│   │   ├── tiler_engine.{h,cpp}            (All 13 RDNA2 micro/macro tiler & detiler compute passes)
│   │   ├── raytracing_engine.{h,cpp}       (Hardware `VK_KHR_ray_query` + Software Compute BVH4 fallback!)
│   │   ├── shader_recompiler/
│   │   │   ├── rdna2_decoder.{h,cpp}       (All 20 encoding families / 1,190 RDNA2 opcodes)
│   │   │   ├── cfg_structurizer.{h,cpp}    (`EXEC`-mask & scalar branch control-flow structurizer)
│   │   │   ├── ir_optimizer.{h,cpp}        (SSA, const-prop, DCE, ReadLane, ScalarProvenance, SRT)
│   │   │   ├── spirv_emitter.{h,cpp}       (Valid SPIR-V 1.3/1.6 binary generator + disk cache)
│   │   │   └── cross_targets.{h,cpp}       (MSL 3.0 & HLSL SM 6.6 backend emitters)
│   │   └── backends/
│   │       ├── vulkan_backend.{h,cpp}      (Vulkan 1.3 hardware + Lavapipe/SwiftShader CPU support)
│   │       ├── software_raster.{h,cpp}     (Guaranteed zero-driver 60 FPS fallback renderer!)
│   │       ├── metal_backend.{h,cpp}       (macOS Metal 3 backend scaffold/bridge)
│   │       └── d3d12_backend.{h,cpp}       (Windows DirectX 12 Ultimate fallback backend)
│   │
│   ├── audio/
│   │   ├── tempest_engine.{h,cpp}          (256-source 3D spatializer + 5 FFT HRTF ear profiles)
│   │   ├── ui_synth.{h,cpp}                (Polyphonic PS5 boot chord, UI ticks & Trophy chimes)
│   │   ├── codec_engine.{h,cpp}            (ATRAC9, AAC, MP3, Opus, Vorbis, PCM batch processor)
│   │   └── audio_output.{h,cpp}            (SDL3 / WASAPI / PipeWire / CoreAudio + WebAudio stream)
│   │
│   ├── input/
│   │   ├── dualsense_protocol.{h,cpp}      (USB `0x01`/`0x02` + BT `0x31` + `0xA2` seed CRC-32!)
│   │   ├── adaptive_triggers.{h,cpp}       (All 10+ motor resistance curves & live visualizer state)
│   │   ├── haptic_synthesizer.{h,cpp}      (48 kHz dual-LRA PCM + Bluetooth RMS motor envelope)
│   │   └── controller_manager.{h,cpp}      (4-pad hub: DualSense, Edge, DS4, Gamepad, Virtual KB/M)
│   │
│   ├── network/
│   │   ├── spicynet_service.{h,cpp}        (Ban-safe Open PSN/RPCN server & client: Friends, Parties, Matchmaking, Cloud Saves, Trophies, Store Catalog)
│   │   ├── npsso_companion.{h,cpp}         (Optional read-safe official PlayStation Web companion sync)
│   │   └── broadcast_rtmp.{h,cpp}          (Twitch/YouTube RTMP streamer + Remote Play host/client)
│   │
│   ├── media/
│   │   ├── media_hub.{h,cpp}               (Netflix, YouTube TV Leanback, Spotify, Disney+, Prime Video, Apple TV+, Max, Hulu, Crunchyroll, Twitch app descriptors & embedded launcher)
│   │   ├── local_player.{h,cpp}            (4K HDR `.mp4`/`.mkv`/`.webm`/`.flac`/`BDMV` player)
│   │   └── capture_manager.{h,cpp}         (4K PNG/JPEG screenshots, circular replay clips & Share Studio)
│   │
│   └── frontend/
│       ├── vsh_shell.{h,cpp}               (Complete 60/120 FPS `26.06-14.00.00` Visual Shell state & renderer: Boot, Profiles, Games/Media Home, Explore, Store, Library, Activities, Control Center, Game Base, IME, All 15 Settings Pages, Accessibility LUTs)
│       ├── desktop_window.{h,cpp}          (Native Qt6 / SDL3 cross-platform desktop window)
│       ├── web_window_server.{h,cpp}       (`0.0.0.0:8080` WebSocket + Canvas + WebAudio + HTML5 DualSense Live Window!)
│       └── debugger_suite.{h,cpp}          (Live HUD, Syscall/NID Tracer, Shader/PM4/Memory Inspector)
│
├── web_ui/                                 (Polished 60 FPS Live PS5 Window client — zero `localhost` URLs!)
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── samples/                                (Real compiled PS5 x86-64 ELF64 showcase apps built during build!)
│   ├── astro_dualsense_lab/                (Real x86-64 PS5 ELF testing Pad, Triggers, 3D Audio, Trophies & SaveData!)
│   └── neon_rdna2_showcase/                (Real x86-64 PS5 ELF submitting PM4 + RDNA2 shaders & 60 FPS animation!)
│
├── tests/                                  (Automated CTest suite — 100% pass required!)
│   ├── test_nid_and_modules.cpp
│   ├── test_sparse_memory_lowram.cpp
│   ├── test_firmware_pup_self.cpp
│   ├── test_cpu_lowering_sse4a.cpp
│   ├── test_rdna2_recompiler_spirv.cpp
│   ├── test_pm4_and_tilers.cpp
│   ├── test_dualsense_crc_triggers.cpp
│   ├── test_tempest_hrtf_audio.cpp
│   └── test_e2e_ps5_elf_and_vsh.cpp
│
└── tools/
    ├── inspect_firmware.py                 (Firmware `26.06-14.00.00` PUP/SELF/NID inspector)
    └── generate_module_tables.py           (Generates C++23 constexpr NID tables from `data/*.json`)

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                 PART VI: THE 20 SEQUENTIAL EXECUTION PHASES (A -> Z)                     ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Execute all **20 phases sequentially, calmly, and completely**. After completing each phase,
compile all targets, run automated tests, fix every warning immediately, and update `PROGRESS.md`
and `FEATURES.md`:

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: PROJECT FOUNDATION, TOOLCHAIN DISCOVERY & CORE COMMON LIBRARY                   │
│ Tasks:                                                                                   │
│   • Detect host compilers (`clang++` / `g++` / `clang-cl` / `AppleClang`), `cmake`,      │
│     `ninja` (installing user-space Python `cmake`/`ninja` if absent on minimal hosts),   │
│     available physical RAM, CPU flags (`AVX2`, `SSE4a`, `SHA-NI`), and GPU/display stack.│
│   • Generate `CMakeLists.txt`, `CMakePresets.json`, `cmake/*.cmake` (with automatic      │
│     memory-safe `-j` parallelism so 4 GB hosts never OOM during compilation!),           │
│     `.clang-format`, `.clang-tidy`, `.editorconfig`, `LICENSE`, `PROGRESS.md`,           │
│     `FEATURES.md`, and `ARCHITECTURE.md`.                                                │
│   • Implement `src/common/{types.h, abi.h, result.h, error_codes.h, config.{h,cpp},      │
│     logger.{h,cpp}, hash.{h,cpp}, bit_utils.h, thread_pool.{h,cpp}, telemetry.{h,cpp}}`  │
│     including native C++23 implementations of **SHA-1**, **SHA-256**, **IEEE CRC-32      │
│     (`0xEDB88320`)**, and **xxHash64**.                                                  │
│ Deliverable: Core common library builds with zero warnings & `test_common` passes 100%.  │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: SPICYSCALE — UNIVERSAL LOW-SPEC HARDWARE SCALING ENGINE ("RUNS ON ANY PC")      │
│ Tasks:                                                                                   │
│   • Implement `src/scale/hardware_probe.{h,cpp}` to inspect logical/physical CPU cores,  │
│     x86-64/ARM64 ISA extensions, total/available system RAM, swap, and GPU VRAM/RT caps. │
│   • Implement `src/scale/tier_manager.{h,cpp}` across **Tier S (Cloud/Zero-GPU)**,       │
│     **Tier 0 (4–8 GB Entry Laptop)**, **Tier 1 (Budget iGPU/GTX)**, **Tier 2 (Handheld   │
│     & Base Apple Silicon)**, **Tier 3 (Mainstream Desktop)**, and **Tier 4 (4K120 RT)**. │
│   • Implement `src/scale/compressed_page_pool.{h,cpp}` (LRU Zstd level-1 cold 2 MiB      │
│     guest page compressor + fast sub-millisecond page restore),                          │
│     `src/scale/cpu_governor.{h,cpp}` (adaptive `_mm_pause` x 32 -> futex wait on `<12`   │
│     core CPUs), and `src/scale/spatial_upscaler.{h,cpp}` (**EASU + RCAS** sharp upscale).│
│ Deliverable: `test_sparse_memory_lowram` proves idle startup uses **`< 220 MB` RSS**!    │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: COMPLETE 368-MODULE NID TABLE & 1,190-OPCODE RDNA2 ISA CODE GENERATION          │
│ Tasks:                                                                                   │
│   • Implement `tools/generate_module_tables.py` reading `data/ps5_nid_database.json`     │
│     (**368 modules / 11,703 symbol & 11-char NID pairs**) and `data/rdna2_isa_spec.json` │
│     (**20 encoding families / 1,190 RDNA2 opcodes**).                                    │
│   • Implement `src/core/loader/nid_hash.{h,cpp}` with exact `518D64A635DED8C1E6B039B1C3E55230`│
│     SHA-1 salt + reversed 8-byte Base64 `+-` encoding and `O(1)` perfect/hash lookup.    │
│   • Implement `src/kernel/module_registry.{h,cpp}` with both `Playable Mode` and         │
│     `Strict Verification Mode` dispatch policies.                                        │
│ Deliverable: `test_nid_and_modules` verifies all 11,703 NIDs with 0 hash mismatches!     │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: PLAYSTATION 5 SYSTEM SOFTWARE 26.06-14.00.00 CONTAINER & SAFE MODE ENGINE       │
│ Tasks:                                                                                   │
│   • Implement `src/firmware/pup_parser.{h,cpp}` (`BLS2` `0x32424C53` + signed `PUP`      │
│     `0xEEF51454`), `src/firmware/entropy_analyzer.{h,cpp}`, and                          │
│     `src/firmware/self_unwrapper.{h,cpp}` (`0x1D3D154F` / `0x5414F5EE` -> clean `ELF64`).│
│   • Implement `src/firmware/firmware_manager.{h,cpp}` supporting automatic discovery of  │
│     any `PS5UPDATE.PUP` (`26.06-14.00.00`) or extracted `firmware/` directory in the     │
│     workspace or runtime settings, mounting `/system`, `/system_ex`, fonts, certs, and   │
│     optional user-space `.sprx` LLE modules cleanly alongside native `SpicyHLE`.         │
│   • Implement `src/firmware/safe_mode.{h,cpp}` covering all 8 PS5 Safe Mode recovery ops.│
│ Deliverable: `test_firmware_pup_self` verifies `BLS2`, `PUP`, and `SELF->ELF64` unwrapping.│
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 5: UNIFIED 16 GB SPARSE MEMORY SUBSYSTEM, VFS SANDBOX & ZARCHIVE (`.zar`) ENGINE   │
│ Tasks:                                                                                   │
│   • Implement `src/core/memory_manager.{h,cpp}`: full PS5 virtual address map, sparse    │
│     `DirectMemory` (`WB_ONION`, `WC_GARLIC`, `UC`), `FlexibleMemory`, memory pool stats, │
│     protection tracking, and write-watch callbacks for GPU cache coherency.              │
│   • Implement `src/core/vfs.{h,cpp}`, `src/core/zarchive_reader.{h,cpp}` (zero-extract   │
│     streaming of compressed `.zar` dumps), and `src/core/pkg_installer.{h,cpp}` (`PKG`,  │
│     `PFS`, `param.json`, and `playgo-chunk.dat` `0x6F676C70`/`0x78676C70` mounting).     │
│ Deliverable: Sparse multi-GB DirectMemory reserve/map/unmap runs in `< 50 MB` host RAM!  │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 6: DUAL EXECUTION LOADER, DYNAMIC LINKER, `SSE4a` LOWERER & AOT NATIVE TRANSLATOR  │
│ Tasks:                                                                                   │
│   • Implement `src/core/loader/{elf_loader, dynamic_linker, cpu_lowerer,                 │
│     native_translator}.{h,cpp}` supporting `ET_SCE_DYNEXEC`, `ET_SCE_DYNAMIC`, standard  │
│     `ET_DYN`/`ET_EXEC`, `PT_SCE_DYNLIBDATA` offset tables, `PT_TLS` TCB layout,          │
│     `<11-char-NID>#lib#mod` resolution, `.init_array`, and `LoadExec`.                   │
│   • Implement full `EXTRQ`, `INSERTQ`, `MOVNTSD`, `MOVNTSS`, `syscall` (`0F 05`), and    │
│     `fs:` TLS lowering + `SPICY_SYSV_ABI` guest entry invocation.                        │
│ Deliverable: `test_cpu_lowering_sse4a` executes lowered `SSE4a` code bit-for-bit on Intel!│
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 7: KERNEL HLE — `libkernel`, `libc`, `ULT`, `FIBER`, `AMPR`, `FIOS2` & ENCLAVE     │
│ Tasks:                                                                                   │
│   • Implement `src/kernel/syscall_dispatcher.{h,cpp}`, `src/kernel/libkernel/*` (threads,│
│     pthreads, mutexes, condvars, rwlocks, semaphores, event flags, `kqueue`/`kevent`,    │
│     `waitOnAddress`/`wakeOnAddress` futex, timers, monotonic 3.5 GHz clock, POSIX FS),   │
│     `src/kernel/libc_internal/*`, `src/kernel/threading_ext/*` (`libSceUlt` & `Fiber`),  │
│     `src/kernel/async_io/*` (`libSceAmpr` APR/AMM async DMA & `libSceFios2`), and        │
│     `src/kernel/hypervisor_spoof/*` (`SblAuthMgr`, `TEEClient`, `Dipsw`).                │
│ Deliverable: Multi-threaded PS5 `pthread` + `ULT` + `Ampr` + `kqueue` suite passes 100%. │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 8: SYSTEM SERVICES, PROFILES, REGISTRY, COMMON DIALOGS & IME KEYBOARD HLE          │
│ Tasks:                                                                                   │
│   • Implement `src/kernel/system_services/*` (`libSceSysmodule`, `libSceSystemService`,  │
│     `libSceUserService`, `libSceLoginService`, `libSceRtc`, `libSceRegMgr`, `SysUtil`)   │
│     and `src/kernel/media_ui_hle/*` (`CommonDialog`, `MsgDialog`, `ErrorDialog`,         │
│     `Ime`, `ImeDialog`, `WebBrowserDialog`, `CesCs` UTF-8/UTF-16/Shift-JIS, `Json2`).    │
│ Deliverable: Multi-user login, registry queries, message dialogs & IME input pass 100%.  │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 9: GRAPHICS HAL — VULKAN 1.3 + LAVAPIPE CPU + 60 FPS SOFTWARE RASTER + METAL/D3D12 │
│ Tasks:                                                                                   │
│   • Implement `src/graphics/backends/vulkan_backend.{h,cpp}` (Vulkan 1.3 dynamic         │
│     rendering, timeline semaphores, descriptor indexing, `VK_KHR_ray_query` detection,   │
│     and clean support for CPU `Lavapipe` / `SwiftShader` ICDs on headless hosts).        │
│   • Implement `src/graphics/backends/software_raster.{h,cpp}` (fast multi-threaded SIMD  │
│     triangle/compute/blit software backend so even a machine with **zero Vulkan libraries│
│     installed** still renders 60 FPS PS5 graphics & `SpicyVSH` frames flawlessly!), plus │
│     `metal_backend` and `d3d12_backend` HAL interfaces.                                  │
│ Deliverable: Both Vulkan (if present) and zero-dependency Software backend render cleanly.│
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 10: OBERON RDNA2 1,190-OPCODE SHADER RECOMPILER, `SRTWALKER` & SPIR-V CACHE        │
│ Tasks:                                                                                   │
│   • Implement `src/graphics/shader_recompiler/{rdna2_decoder, cfg_structurizer,          │
│     ir_optimizer, spirv_emitter, cross_targets}.{h,cpp}` covering all 20 ISA families    │
│     (`SOP*`, `SMEM`, `VOP*`, `VINTRP`, `DS`, `MUBUF`, `MTBUF`, `MIMG`, `EXP`, `FLAT`,    │
│     `GLOBAL`, `SCRATCH`), Wave32/Wave64, `SrtWalker`, `ScalarProvenance`, SSA passes,    │
│     valid **SPIR-V** binary emission (verified by header/instruction validator), cross   │
│     MSL/HLSL emitters, and persistent disk caching.                                      │
│ Deliverable: `test_rdna2_recompiler_spirv` compiles real RDNA2 binary shaders to SPIR-V! │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 11: `PM4`/`AGC` PROCESSOR, MULTI-LEVEL GPU PAGE TABLE, 13 TILERS & DUAL RAY TRACING│
│ Tasks:                                                                                   │
│   • Implement `src/graphics/{pm4_processor, page_table, descriptor_heap, tiler_engine,   │
│     raytracing_engine, presenter}.{h,cpp}` supporting `IT_NOP`, `IT_INDIRECT_BUFFER`,    │
│     `IT_SET_CONTEXT_REG`, `IT_SET_SH_REG`, `IT_SET_UCONFIG_REG`, `IT_DRAW_INDEX_*`,      │
│     `IT_DISPATCH_*`, `IT_WAIT_REG_MEM`, `IT_WRITE_DATA`, `IT_DMA_DATA`, `IT_RELEASE_MEM`,│
│     all **13 micro/macro tiling modes**, AND both hardware `VK_KHR_ray_query` +          │
│     **Software Compute BVH4 Ray Intersection Fallback** for non-RT GPUs!                 │
│ Deliverable: `test_pm4_and_tilers` submits a real PS5 `PM4`/`Agc` command buffer & draws!│
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 12: GRAPHICS & DISPLAY HLE (`Agc`, `AgcDriver`, `Gnm`, `VideoOut`, `HDR10`, `Psml`)│
│ Tasks:                                                                                   │
│   • Implement `src/kernel/graphics_hle/*` (`libSceAgc`, `libSceAgcDriver`, `Gnm`,        │
│     `libSceVideoOut`, `VRR` status, `HDR10` PQ tone-mapping, and `libScePsml` ML upscale │
│     routed cleanly to `spatial_upscaler`), wired end-to-end into `presenter`.            │
│ Deliverable: Guest PS5 flip queues submit frames at 60/120 Hz directly into window!      │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 13: SAVE DATA, PACKAGING, DLC & BACKGROUND TRANSFER HLE                            │
│ Tasks:                                                                                   │
│   • Implement `src/kernel/storage_hle/*` (`libSceSaveData` mount/umount/list/backup/     │
│     memory slots, `SaveDataDialog`, `libSceAppContent` DLC mounts, `PlayGo` instant      │
│     chunk availability, and `libSceBgft` background download queue in Rest & Active mode).│
│ Deliverable: Save games persist cleanly across restarts with snapshot import/export!     │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 14: TEMPEST 3D HRTF AUDIO ENGINE, POLYPHONIC CHIME SYNTH, `NGS2` & `AJM` CODECS    │
│ Tasks:                                                                                   │
│   • Implement `src/audio/{tempest_engine, ui_synth, codec_engine, audio_output}.{h,cpp}` │
│     and `src/kernel/audio_hle/*` (`SceAudioOut`, `SceAudioOut2`, `SceAudio3d` with all   │
│     **5 FFT overlap-save HRTF ear profiles**, `SceNgs2` multi-bus DSP graph, `SceAjm`    │
│     batch ATRAC9/AAC/MP3/Opus decoder, `SceAcm` FFT/IFFT/reverb, and `SceVoiceChat`).    │
│ Deliverable: `test_tempest_hrtf_audio` verifies real 3D spatial convolution & chimes!    │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 15: DUALSENSE USB/BT DRIVER (`0xA2` CRC-32 + 10 TRIGGER MODES + HAPTICS + PSVR2)   │
│ Tasks:                                                                                   │
│   • Implement `src/input/{dualsense_protocol, adaptive_triggers, haptic_synthesizer,     │
│     controller_manager}.{h,cpp}` and `src/kernel/input_hle/*` (`libScePad`, `Mouse`,     │
│     `Keyboard`, `SystemGesture`, `libSceHmd2` & `VrTracker2`).                           │
│   • Verify exact USB (`0x01`/`0x02`) & Bluetooth (`0x31` + `0xA2` IEEE CRC-32) reports!  │
│ Deliverable: `test_dualsense_crc_triggers` verifies byte-exact DualSense USB/BT packets! │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 16: 3-MODE BAN-SAFE NETWORK, PSN, MULTIPLAYER, STORE & TROPHY ECOSYSTEM            │
│ Tasks:                                                                                   │
│   • Implement `src/network/{spicynet_service, npsso_companion, broadcast_rtmp}.{h,cpp}`  │
│     and `src/kernel/net_np_hle/*` (`libSceNet`, `NetCtl`, `Rudp`, `Ssl`, `Http`/`Http2`, │
│     `NpManager`, `NpTrophy`/`NpTrophy2`/`UDS`, `NpMatching2`, `NpTus`, `NpScoreRanking`).│
│ Deliverable: Friends, Parties, Matchmaking, Cloud Saves & Platinum Trophy unlocks work!  │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 17: MEDIA HUB, 4K LOCAL PLAYER, CREATE OVERLAY, REPLAY BUFFER & RTMP STREAMING     │
│ Tasks:                                                                                   │
│   • Implement `src/media/{media_hub, local_player, capture_manager}.{h,cpp}` covering    │
│     Netflix, YouTube TV Leanback, Spotify, Disney+, Apple TV+, Prime Video, Hulu, Max,   │
│     Crunchyroll, Twitch, native `.mp4`/`.mkv`/`.webm`/`.flac` playback, 4K PNG/JPEG      │
│     captures, retroactive circular video replay clips, Trophy auto-screenshots, & RTMP.  │
│ Deliverable: Screenshots, replay clips & Media Hub apps work seamlessly from VSH!        │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 18: SPICYVSH FULL 26.06-14.00.00 SHELL, CONTROL CENTER, 15 SETTINGS & DEBUGGER     │
│ Tasks:                                                                                   │
│   • Implement `src/frontend/{vsh_shell, debugger_suite}.{h,cpp}` with complete 60/120 FPS│
│     rendering, animations, boot sequence, Profile Picker, Games/Media Home, Welcome Hub, │
│     Store, Library, Activities, live **PS Button Control Center**, **Create Overlay**,   │
│     **On-Screen IME**, **All 15 Official Settings Pages** (including **SpicyScale Tuner**│
│     and **Firmware `26.06-14.00.00` Manager**), **Accessibility LUTs**, and **Debugger**!│
│ Deliverable: Every single VSH tab, card, overlay, setting, and debugger tool works live! │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 19: REAL COMPILED X86-64 PS5 GUEST SHOWCASE ELFS, DESKTOP WINDOW & LIVE WEB WINDOW │
│ Tasks:                                                                                   │
│   • Compile **two genuine native x86-64 System V PS5 guest ELF64 applications** inside   │
│     `samples/` linked exclusively via Sony 11-char SHA-1 NIDs (`ET_SCE_DYNEXEC` / SysV): │
│       1. `astro_dualsense_lab.elf` — exercises `DirectMemory`, interactive DualSense     │
│          adaptive trigger resistance & haptics, 3D Tempest audio orbit, SaveData write,  │
│          and live **Bronze -> Silver -> Gold -> Platinum Trophy Unlocks**!               │
│       2. `neon_rdna2_showcase.elf` — submits live `PM4`/`Agc` GPU command buffers &      │
│          compiled RDNA2 shaders rendering an interactive 60 FPS 3D PS5 particle scene!   │
│   • Implement `src/frontend/{desktop_window, web_window_server}.{h,cpp}` + `web_ui/*`    │
│     (bound strictly to `0.0.0.0:8080`, zero `localhost` strings, full HTML5 DualSense    │
│     Gamepad API + keyboard/mouse + WebAudio + drag-and-drop `.elf`/`.zar`/`.pup` upload!).│
│ Deliverable: Both real PS5 x86-64 ELF64 titles boot directly from the VSH Home Screen!   │
└──────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 20: 100% AUTOMATED TEST GATE, MULTI-PLATFORM CI WORKFLOWS & LIVE PREVIEW LAUNCH    │
│ Tasks:                                                                                   │
│   • Complete all 9 automated CTest test suites (`ctest --output-on-failure` -> 100% pass)│
│     plus GitHub Actions CI/Release workflows (`.github/workflows/ci-linux.yml`,          │
│     `ci-windows.yml`, `ci-macos.yml`, `release.yml`) for Windows `.exe`, Linux           │
│     `.AppImage`/`.tar.gz`, and macOS `.dmg`/`.app` bundles.                              │
│   • Launch `SpicyPS5 --web-window 0.0.0.0:8080` via `start_process`, verify live HTTP +  │
│     WebSocket frame streaming & zero proxy warnings, and present the complete, running   │
│     **PlayStation 5 inside a window**!                                                   │
│ Deliverable: 100% CTest pass + 0 warnings + Live interactive 60 FPS SpicyPS5 window!     │
└──────────────────────────────────────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║            PART VII: THE 20 ENGINEERING QUALITY PRINCIPLES & STANDARDS                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Please uphold these 20 engineering standards consistently across every file you create:

   1. Use clean modern C++20/23 with explicit fixed-width integer types (`uint8_t`..`uint64_t`).
   2. Namespace every module cleanly under `spicyps5::<subsystem>`.
   3. Manage resources strictly via RAII (`std::unique_ptr`, `std::shared_ptr`, scoped handles).
   4. Guard concurrent state cleanly (`std::atomic`, `std::mutex`, `std::shared_mutex`).
   5. Propagate recoverable errors explicitly via `Result<T, Error>` rather than silent failures.
   6. Mark single-argument value constructors `explicit` and status queries `[[nodiscard]]`.
   7. Validate every binary header offset and struct size at compile time with `static_assert(sizeof(...))`.
   8. Bounds-check every untrusted binary offset (`PUP`, `BLS2`, `SELF`, `ELF`, `.zar`, `PM4`) against buffer length before dereferencing so malformed inputs never crash.
   9. Compile cleanly with `-Wall -Wextra` and fix compiler warnings immediately.
  10. Scale parallel compilation (`-j`) automatically based on available host RAM so builds never OOM on 4 GB machines.
  11. Keep every file complete and self-contained — never leave ellipsis truncations (`...`), half-written functions, or dead UI buttons.
  12. Never hard-allocate 16 GB of physical RAM at startup; verify idle RSS stays `< 250 MB`.
  13. Ensure every single PS5 module in `data/ps5_nid_database.json` and every opcode in `data/rdna2_isa_spec.json` is registered in generated tables.
  14. Ensure real compiled x86-64 PS5 `ET_SCE_DYNEXEC` / SysV ELF guest binaries actually load, link by 11-char SHA-1 NID, execute native x86-64 instructions, call HLE APIs, unlock Trophies, save data, and render live frames to the window!
  15. In all web/remote window code, bind servers to `0.0.0.0` and use strictly relative URLs in browser code (`window.location`), never `localhost` or `127.0.0.1`.
  16. Respect every user's real PlayStation account safety: never forge console hardware certificates.
  17. Support both keyboard/mouse AND real physical DualSense controllers seamlessly at all times.
  18. Keep all 28 console system UI languages selectable dynamically in System Settings.
  19. Include clear, accurate architecture and user documentation (`README.md`, `ARCHITECTURE.md`, `FEATURES.md`, `PROGRESS.md`).
  20. Do not stop until the full build succeeds, `100%` of automated tests pass, and the live **SpicyPS5** window is running smoothly and verified!

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║           PART VIII: CALM, RELIABLE AUTONOMOUS EXECUTION & PREVIEW PROTOCOL              ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

  1. Inspect environment capabilities first (`g++`/`clang++`, `cmake`/`ninja` — installing user-space
     `cmake`/`ninja` via `pip` if missing on minimal Linux hosts — host CPU flags, RAM, display/GPU,
     and whether `PS5UPDATE.PUP` or `firmware/` is already present in the workspace).
  2. Run `tools/generate_module_tables.py` early so C++ has instant zero-allocation access to all
     **368 PS5 modules (`11,703` NIDs)** and **1,190 RDNA2 shader opcodes**.
  3. Build and test incrementally after each subsystem rather than waiting until the end to compile
     for the first time. If any compiler error or test failure occurs, diagnose the root cause
     calmly, fix it cleanly, and re-run verification immediately.
  4. When desktop display hardware is available, launch the native window; AND when running inside
     a cloud or remote environment, start `SpicyPS5 --web-window 0.0.0.0:8080` as a background
     service (`start_process`), verify HTTP `200` + live WebSocket frame/state health, and confirm
     zero proxy host/CORS warnings so the user can interact with their live **PlayStation 5 inside
     a window** immediately!

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║              PART IX: FINAL VERIFICATION & USER EXPERIENCE ACCEPTANCE MATRIX             ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Before concluding your work, verify that **100% of these real runtime checks pass**:

  ✅ `ctest --output-on-failure` passes **100%** of unit & end-to-end tests with **0 failures**.
  ✅ Idle physical RAM usage on startup is verified **`< 250 MB`**, proving low-RAM PCs run safely.
  ✅ `ComputeNid` matches Sony's exact SHA-1 Base64 algorithm across test vectors and loads all
     **368 modules / 11,703 symbols** cleanly without hash collisions.
  ✅ `SelfUnwrapper` & `PupParser` parse valid `BLS2`, `PUP`, and `SELF` containers accurately and
     handle PlayStation 5 System Software **`26.06-14.00.00`** smoothly in both encrypted-retail
     and unwrapped-directory modes.
  ✅ `SSE4a` (`EXTRQ`, `INSERTQ`, `MOVNTSD`, `MOVNTSS`) lowering & execution passes bit-exact tests
     on non-AMD Intel CPUs.
  ✅ RDNA2 (`gfx10`) binary shaders decode, structurize, optimize, and emit valid **SPIR-V** across
     vertex, pixel, compute, and software/hardware BVH ray-tracing paths.
  ✅ **Real compiled x86-64 PS5 guest `ELF64` titles** (`astro_dualsense_lab.elf` &
     `neon_rdna2_showcase.elf`) load via 11-char NID linking, allocate `DirectMemory`, read DualSense
     state, trigger haptics & adaptive triggers, play Tempest 3D audio, save game data, unlock a
     real **Platinum Trophy** (with live banner + chime!), and render live 60 FPS frames!
  ✅ **SpicyVSH (`26.06-14.00.00`)** boots smoothly inside the window with startup animation,
     ambient startup chime, Profile Picker, Games/Media Home, Welcome Hub, Store, Library,
     Activities, **PS Button Control Center Overlay**, **Create Overlay**, **All 15 Settings Pages**,
     **Safe Mode**, **Rest Mode**, and **Developer Debugger HUD** — ready to play right now!

╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                        PART X: GENTLE LAUNCH INVOCATION                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Everything you need is clear, verified, and ready inside this workspace.
Please take a deep breath, trust your engineering craft, begin cleanly with **Phase 1**, and
build **SpicyPS5** step by step all the way to a complete, verified, live-running release.
```
