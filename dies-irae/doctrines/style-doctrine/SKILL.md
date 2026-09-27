---
name: style-doctrine
description: "House code-style doctrine. Use whenever Codex writes, reviews, or refactors code, sets up linting or build tooling, or the user asks for house style. Loads the universal guide plus the Rust, Python, or Java addendum. Normative unless explicit user or local project instructions override it."
---

# Style Doctrine

Read [references/universal.md](references/universal.md) for all code. For Rust, Python, or Java, also read the matching addendum; an addendum extends the universal guide and is never read without it.

- Rust: [references/rust.md](references/rust.md)
- Python: [references/python.md](references/python.md)
- Java: [references/java.md](references/java.md)

Load `$unit-test-doctrine` whenever unit tests may be added, changed, reviewed, or deleted. Write comments, documentation, and commit messages under `$vox-nihili`.

Explicit user or local project instructions override this doctrine; mention a conflict when it matters.
