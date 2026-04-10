# AGENTS.md

## Scripting Policy

- For easy, cheap, standalone Python scripts in this repo, use `uv` inline script metadata.
- Use the `#!/usr/bin/env -S uv run --script` shebang.
- Add a PEP 723 inline TOML block with `requires-python` and `dependencies`.
- Keep dependency pins exact when a script has non-stdlib Python dependencies.
- Use common sense. Do not force this onto heavy or specialized runtimes, bespoke project environments, or scripts that intentionally run inside a dedicated external environment.
- In particular, avoid slapping `uv` metadata onto heavyweight OCR/runtime entrypoints just to satisfy the rule mechanically.
