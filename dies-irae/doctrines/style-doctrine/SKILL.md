---
name: style-doctrine
description: "Use whenever Codex writes, reviews, or refactors code or English natural-language prose, or when the user asks for house style, coding or prose doctrine, or style-guide compliance. Load the relevant code guide, pair unit-test work with Unit Test Doctrine, and always load Vox Nihili for English prose. Treat them as normative unless explicit user or local project instructions override them."
---

# Style Doctrine

Load the house style doctrine whenever writing, reviewing, or refactoring code or English prose.

For code, read [references/universal.md](references/universal.md) first. Then read the language guide that matches the work:

- Rust: [references/rust.md](references/rust.md)
- Python: [references/python.md](references/python.md)
- Java: [references/java.md](references/java.md)

If no code-language-specific guide exists, apply the universal guide directly.

Whenever unit tests may be added, changed, reviewed, or deleted, also load
`$unit-test-doctrine`.

These guides deliberately reject some common engineering advice. Do not translate them back into conventional novice-friendly defaults. Prefer static truth, compact representation, strong invariants, runtime efficiency, token economy, and powerful abstraction.

For English natural-language prose, always load the standalone `$vox-nihili` skill, even when style was not separately requested. Its null-voice fixed point is the default house voice for new and existing prose; only explicit user or local project instructions countermand it. Do not translate it into generic brevity, blandness, or friendliness advice.

If local `AGENTS.md`, project docs, or explicit user instructions conflict with this doctrine, follow the more local instruction and mention the conflict briefly when it matters.
