---
name: agents-md-style
description: "Write, edit, review, or trim a repository's AGENTS.md under one placement rule, a fixed schema, a hard byte budget, and a headline register. Use whenever Codex creates or changes AGENTS.md, AGENTS.override.md, or CLAUDE.md, including when about to add a rule after a mistake. Governs these files in place of $vox-nihili."
---

# AGENTS.md Style

A repository's AGENTS.md states only what the repository requires beyond what an agent already does under the global instructions and house skills. Every session in the repository pays for every byte. The rules are mechanical by design: content that does not fit them moves to a routed document, a data file, a tool, or nowhere. The rules do not bend.

Scope: repository instruction files. Global instructions and routed documents are out of scope; routed documents follow `$vox-nihili`.

## Placement

- P1. Within a repository, one instruction file, at the work-tree root: its directory is `git rev-parse --show-toplevel`. None below the root and none in a bare-repository directory.
- P2. A directory directly above several repositories may hold an instruction file only if it has an organizing principle worth stating, such as a product line or a shared protocol; co-location is not one. Every repository it organizes is an immediate child, and no such directory sits above another, so a workspace root holds none. The file states the principle and what spans its repositories; anything that concerns one repository lives in that repository. Codex loads the file only for sessions started in that directory, never inside a child repository, so a rule every child needs belongs in each child or in a skill.
- P3. `AGENTS.override.md` only at the root of a fork whose upstream ships `AGENTS.md`. It is the fork's entire instruction file, tracked with `git add -f` where upstream ignores it; upstream's `AGENTS.md` stays byte-identical and serves as a route target. Delete upstream's subdirectory instruction files; `git rm` resolves their merge conflicts.
- P4. `CLAUDE.md`, if present, is a symlink to the instruction file beside it.
- P5. A rule about one subtree is a root invariant naming the subtree's path, or a route.
- P6. Exempt from P1: template assets copied into new repositories, which obey every other rule, and vendored third-party trees, which are never edited.

## Admission

A claim is admitted only if all three hold:

- A1 local: neither the global instructions nor a house skill states it.
- A2 hidden: the code, README, `--help`, or a failing check does not reveal it cheaply.
- A3 weighty: violating it is silent or expensive, and it either bears on most sessions or is irreversible.

Classify every claim by the first matching row:

| # | Claim | Disposition |
|---|---|---|
| 1 | Stated by global instructions or a house skill | Delete. |
| 2 | Re-emphasis of a doctrine rule | Delete. A local instance (a named type, path, or seam) is a new claim; classify it. |
| 3 | Derivable; generic advice; exhortation; mantra | Delete. |
| 4 | Status, progress, history, plans, dated facts | Delete, or move to the ledger (issues, Vauban, `CHECKPOINT.md`). |
| 5 | Data: per-entity exceptions, versions, settings, growing lists | Move to a data file the tooling reads; keep one route. |
| 6 | Contract owned by another repository | Route to the owner's document. Never copy. |
| 7 | Procedure over three steps; how a script works | Move to the script or a document; keep one gate or route line. |
| 8 | Enforceable by a tool | Keep at most one line; delete it once a guard enforces the rule. |
| 9 | Fails A3 | Move to a document and keep one route, or delete. |
| 10 | Otherwise | Keep. |

Before deleting a claim under row 1 or 3, identify the source that states or reveals it. Move material before removing it from the instruction file. A new routed document goes to `docs/<topic>.md` unless the repository already has a home for the topic.

## Schema

Fixed order. Omit empty sections. No title and no other headings.

~~~
<charter>
## gate
## invariants
## routes
## terms
## grants
## hazards
~~~

- S1 charter: first line, no heading, at most two lines: `<name>: <what it owns>[; not <neighbor's concern>]`.
- S2 gate: exact commands for check, non-mutating verify, focused tests, and install; the definition of done.
- S3 invariants: kept rules. Append the reason only when the rule would otherwise be misapplied.
- S4 routes: `<task> → <path | $skill>`. Name a task ("changing X"), not a topic. Route to a skill only when its own description would not fire here.
- S5 terms: `<noun>: <meaning>[; ≠ <confusable>]`. Repository nouns only. More than eight → `docs/glossary.md` and one route.
- S6 grants: authorizations and departures from global policy. Each states what it permits and what it does not. Only the user creates or widens a grant.
- S7 hazards: misleading environment facts: `<observation> ≠ <conclusion>` or `<trap> → <correct move>`.

## Form

- F1. Every line is the charter, a section heading, a single-level `- ` bullet, or one blank line between sections. No paragraphs, nested bullets, tables, code blocks, HTML, or comments.
- F2. One rule per bullet; at most 160 characters; no terminal period.
- F3. At most 4096 bytes; target 2048. Over budget → route more. Never compress below one reading.
- F4. Paths in backticks, relative to the repository root (`../x` for siblings). No Markdown links. Skills as `$name`, never as paths.
- F5. No emphasis: bold, italics, capitals, `!`, "critical", "important", "note".
- F6. No dates; Git history carries provenance.
- F7. Model IDs only where the repository departs from the global default.
- F8. Every path, command, and `$skill` the file names resolves.

## Register

Headline and telegram English: crushed, but still English.

- R1. Drop articles, copulas, auxiliaries, pronouns, hedges, courtesy, and filler connectives wherever the meaning survives.
- R2. Keep the verbs, prepositions, negations, quantifiers, and conditions; they carry the rule.
- R3. Imperatives for rules, noun phrases for facts.
- R4. A colon introduces what a rule requires; a semicolon joins the clauses of one rule.
- R5. Symbols: `→` for routes and consequences, `≠` for distinctions; no other notation.
- R6. Exact identifiers; one name per concept, as fixed in terms. Standard abbreviations only: repo, deps, config, env, fs, creds, CI, PR.
- R7. Every bullet parses as English on first reading and has one reading. Restore any word whose absence breaks either.

## Examples

Prose → rule:

> Ledger patches are replayed forever: never change what an existing op means. A new meaning is a new op or a new store format with a migration.

~~~
- Ledger ops replay forever: never change an existing op's meaning; new meaning needs new op or new store format with migration
~~~

Exhortation → deletion, or the one checkable rule it implies:

> This library is heavily optimized, which is a condition that is easier to break than improve. Be extraordinarily mindful of runtime performance.

~~~
- New hot-path type or algorithm: state asymptotics and memory layout before coding
~~~

State → deletion:

> The host currently exposes an inert `.git` directory here; use `.git-local` as the real repository store when invoking Git manually.

Data → data file and route:

> B09 has a one-time Taskman balance exception for Abraham because she is unavailable November 2–4, 2026. Exclude Abraham's B09 Taskman total from the block k/k+1 balance goal, while continuing to enforce …

~~~
- Per-resident exceptions live in `exceptions.toml`; never generalize one beyond its resident and block
~~~

Prose → hazard:

> For C++ navigation, `.local/lsp/README.md` describes the clangd setup; an unconfigured index returns nothing, which does not show that a symbol is absent.

~~~
- Empty clangd result from unindexed tree ≠ symbol absent; setup in `.local/lsp/README.md`
~~~

Complete file, `mcps/papers` (1,161 → 612 bytes):

~~~
papers: unified paper-retrieval engine behind one MCP; product and executable name

## gate
- `./check.py check` after edits; `./check.py verify` for non-mutating gate

## invariants
- All retrieval HTTP through the one `BoundClient`; bypassing configured interface breaks product contract
- Semantic inference runs in sealed transient Codex subprocess; its transport, creds, config, fs view, lifetime, output stay inside
- Model-facing protocol exposes only the unified engine, never provider or mirror

## terms
- provider: one upstream family; internal
- mirror: one concrete endpoint of a provider; internal
~~~

Deleted from the original: the `$style-doctrine` and `$unit-test-doctrine` pointers and their paraphrases (row 1).

## Procedure

For a new file, a trim, or one added rule:

1. Resolve the root. Collect every authored instruction file in the repository.
2. Split the text into atomic claims, each carrying its scope, exceptions, and reason.
3. Classify each claim through admission.
4. Move routed material to its document or data file.
5. Write the kept claims in schema and register.
6. Run `scripts/lint` on the repository; it checks P1–P4, the schema, S1, S5, F1–F6, and F8. Judge the rest yourself: admission, register, F7, and that every kept claim retains its scope and exceptions.
7. Delete subdirectory instruction files; make `CLAUDE.md` a symlink.

A trim changes form, not substance. Keep local claims as found unless grossly suspect, such as a missing path, a dead tool, or a contradiction within the file; do not investigate the code to validate them. Move an oversized top-level section whole and verbatim to its routed document instead of redesigning it.

After a mistake, run this procedure on the one candidate rule before writing it. Most such rules belong in a tool guard, a skill amendment, or nowhere.
