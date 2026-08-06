---
name: x11-gui-testing
description: Safely build, launch, drive, capture, and diagnose Linux GUI applications on the owner's X11/i3 workstation without opening windows or mutating UI state in the live desktop session. Use whenever Codex needs to run or visually test an X11 GUI, winit/egui/wgpu app, GTK/Qt/SDL desktop app, Electron shell, graphical example, screenshot test, pointer/keyboard automation, or anything that may inherit DISPLAY and create a window.
---

# X11 GUI Testing

Treat the live desktop as production.

## Boundary

Prefer a genuinely headless backend when it exercises the behavior under test. Otherwise use the bundled Xvfb launcher. Never launch a graphical process on inherited `DISPLAY`, `WAYLAND_DISPLAY`, i3/Sway IPC, or session D-Bus merely because they exist. Browsers, file pickers, helpers, and child processes belong inside the same isolation.

Use the live desktop only when the user explicitly requests an on-screen test in that turn. Xephyr is not an off-screen substitute: its server appears in a host window.

## Launch

Build and run non-GUI checks before starting a display. Resolve this skill's installed directory, then launch the GUI or a project-specific driver through:

```sh
skill=$(readlink -f "${CODEX_HOME:-$HOME/.codex}/skills/x11-gui-testing")
"$skill/scripts/isolated-x11" -- command arg...
```

The launcher creates a fresh Xvfb server and private XDG roots, removes live session integration, fixes common toolkit scaling, and deletes its disposable state afterward.

Options:

- `--wgpu`: exercise winit/wgpu through lavapipe on this host; if absent, install it once with `"$skill/scripts/install-lavapipe"`
- `--software-gl`: force Mesa software OpenGL
- `--dbus`: create a private session bus when the application requires one
- `--screen WIDTHxHEIGHTxDEPTH`: override the default `1440x920x24` display
- `--xdg-root ABSOLUTE_DIR`: retain disposable test state across runs; never name a live user directory

Write logs, screenshots, and recordings outside an ephemeral XDG root so failures survive cleanup.

## Driver Contract

Keep project knowledge in a project-local `scripts/playtest` or a throwaway driver. It should:

- launch the application in a recorded process group and kill the whole group on every exit
- use bounded readiness checks and identify one private-display window precisely
- drive the smallest deterministic interaction that proves the behavior, targeting the window ID directly
- capture the top-level window for stable content or the Xvfb root for menus, tooltips, and detached surfaces
- assert semantic state or product output in addition to inspecting decisive images
- preserve logs and artifacts on failure and prove no tested process survives

Under bare Xvfb, do not rely on `windowactivate`; use explicit `xdotool --window`, `windowfocus`, or direct XTEST input. Inspect screenshots with the image viewer. A nonempty image is not proof of correct pixels.

## Failure

Diagnose application startup, window selection, rendering backend, capture surface, and input geometry inside the private display. Inspect the application log and `xwininfo -root -tree`; force known geometry, DPI, and scale before changing automation. Add a private window manager only when window-manager behavior is itself under test.

Never respond to an adapter, focus, capture, or automation failure by falling back to the live display.
