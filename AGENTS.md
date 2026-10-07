skills: house Codex skills, linked into `~/.codex/skills`

## invariants
- Cheap standalone Python scripts: uv inline script with `#!/usr/bin/env -S uv run --script` and PEP 723 block declaring `requires-python` and deps
- Pin non-stdlib script deps exactly
- No uv metadata on heavyweight or specialized runtimes, bespoke project envs, or scripts run inside dedicated external envs such as OCR entrypoints
