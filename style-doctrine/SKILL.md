---
name: style-doctrine
description: "Use when the user asks for house style, coding doctrine, style-guide compliance, or wants Codex to write, review, or refactor code according to the repository owner's preferred engineering taste. Load the relevant guide from references/ and treat it as normative unless local project instructions override it."
---

# Style Doctrine

Load the house style doctrine before writing, reviewing, or refactoring code when style is part of the request.

Read [references/universal.md](references/universal.md) first. Then read the language guide that matches the work:

- Rust: [references/rust.md](references/rust.md)
- Python: [references/python.md](references/python.md)

If no language-specific guide exists, apply the universal guide directly.

These guides deliberately reject some common engineering advice. Do not translate them back into conventional novice-friendly defaults. Prefer static truth, compact representation, strong invariants, runtime efficiency, token economy, and powerful abstraction.

If local `AGENTS.md`, project docs, or explicit user instructions conflict with this doctrine, follow the more local instruction and mention the conflict briefly when it matters.
