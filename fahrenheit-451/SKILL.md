---
name: fahrenheit-451
description: Perform a zero-based documentation purge and consolidation pass over markdown and other plaintext note files. Use when Codex needs to inspect every doc-like file in a subtree, presume each file should be deleted, classify each file into a hard disposition, reconcile kept docs against code, and flag unresolved contradictions instead of guessing at supersession.
---

# Fahrenheit 451

Use this skill for markdown and plaintext notes. It is not language-specific, but it is still codebase-aware: any kept documentation must be reconciled against the code.

## Contract

- Require a concrete subtree.
- Default plaintext scope to `*.md`, `*.txt`, `*.rst`, `*.adoc`, and `*.org`, plus obvious repo-local note files.
- Presume every file should be deleted.
- If a file survives deletion, presume it should be rewritten from scratch in condensed form unless there is clear justification for `light_edit` or `keep_as_is`.
- Inspect every file in scope. No sampling.
- Create one persistent `/tmp` worklog before the first file read. Chat is summary only; the worklog is the durable source of truth.
- Partition the manifest into intentional logical cliques before deep reading.
- Read at most 8 files per wave.
- Write a `/tmp` checkpoint after every wave before reading more files.
- Give every file exactly one final disposition.
- Reconcile every kept or spec-like file against the code.
- When a document contradicts code and precedence is unclear, do not guess. Record it in the contradiction register.

Git history is the archive. Do not preserve dead docs by moving them into a graveyard folder.

## File Dispositions

Every file must end in exactly one of these:

- `delete`
- `merge_then_delete`
- `rewrite_from_scratch`
- `light_edit`
- `keep_as_is`
- `flag_contradiction`

Use `keep_as_is` rarely. Use `light_edit` only when the file is basically correct and materially worth preserving. Use `rewrite_from_scratch` as the default survival mode.

## Flow

### 0. Create the worklog

Create a path shaped like:

```text
/tmp/fahrenheit-451-<repo-or-dir>-<subtree-slug>.md
```

Seed it with the embedded worklog skeleton from `Embedded Forms`.

The worklog must hold:

- the manifest
- the clique plan
- every wave checkpoint
- the file decision ledger
- the contradiction register
- the residual summary

If interrupted or resumed, reopen the same worklog before continuing.

### 1. Lock scope and manifest

Enumerate every plaintext file in scope and write the manifest into the worklog immediately.

Use fast file discovery, for example:

```bash
rg --files <subtree> -g '*.md' -g '*.txt' -g '*.rst' -g '*.adoc' -g '*.org'
```

Write the manifest in the embedded form from `Embedded Forms`.

### 2. Plan logical cliques

Group manifest files into small logical cliques before deep reading.

Write each clique wave in the embedded form from `Embedded Forms`.

Good clique causes:

- same topic or subsystem
- same audience
- same lifecycle stage such as planning, reference, runbook, migration note, or historical residue
- likely supersession relationship
- duplicate content clusters
- same code surface or command surface

Cliques may overlap. A file may appear in multiple cliques. Keep cliques to 2-8 files.

### 3. Run bounded coverage waves

For each clique wave:

- read at most 8 files
- decide what the clique is trying to resolve: duplication, supersession, condensation, contradiction, or audience split
- update the manifest coverage
- write a `/tmp` checkpoint containing:
  - clique id and purpose
  - files inspected in the wave
  - deletion candidates
  - merger candidates
  - files that look keep-worthy
  - likely rereads in later cliques
  - likely code surfaces to reconcile

Do not read a 9th file until that checkpoint exists.

### 4. Make first-pass file decisions

After every file has been inspected at least once, assign each file a provisional disposition.

Record the decisions in the embedded ledger form from `Embedded Forms`.

For every file, record:

- path
- apparent doc kind
- intended audience
- provisional disposition
- short keep-or-delete basis
- superseded_by_or_merge_target if applicable
- rewrite_needed
- code_reconciliation_target

The keep burden is intentionally light but real. A short justification is enough if it is concrete.

### 5. Reconcile surviving docs against code

For every file with provisional disposition `rewrite_from_scratch`, `light_edit`, `keep_as_is`, or `flag_contradiction`, reconcile it against the code, tests, commands, config, or generated behavior it claims to describe.

Ask:

- does the code still do what this file says?
- is this file obviously stale?
- is this a stable formal definition, ADR, public contract, runbook, or reference that still earns its keep?
- does another doc supersede it?
- if there is a contradiction, is precedence obvious?

If precedence is not obvious, move the file to `flag_contradiction` and record the issue in the embedded contradiction register form from `Embedded Forms`.

### 6. Execute the purge and consolidation

Apply the final dispositions.

Meaning of the dispositions:

- `delete`: remove the file outright
- `merge_then_delete`: fold the scarce useful material into the target file, then delete the source
- `rewrite_from_scratch`: keep the file path or merge target, but rewrite the content in condensed form
- `light_edit`: keep the file and patch it narrowly
- `keep_as_is`: keep untouched with a concrete justification
- `flag_contradiction`: keep or quarantine only as needed while reporting the unresolved conflict

Default victims:

- roadmaps
- done feature docs
- stale checklists
- obsolete migration notes
- narrative implementation notes whose only job is to duplicate the code

Default survivors:

- durable formal specs
- crisp reference docs
- active operator runbooks
- ADR-like decision records
- public-facing contracts that still match reality

### 7. Verify the resulting doc set

After edits and deletions:

- re-scan the same manifest scope
- confirm every original file received a disposition
- confirm every surviving spec-like file was reconciled against code
- update the contradiction register and residual summary in the worklog

## Embedded Forms

### Worklog Skeleton

```text
worklog_path:
scope_root:
inspection_mode: audit_only | audit_plus_refactor
wave_size_limit: 8

manifest:

clique_plan:

wave_checkpoints:

file_decision_ledger:

contradiction_register:

residual_summary:
```

Rules:

- create this file before the first file read
- update it after every 8-file wave before reading more files
- treat it as the durable source of truth for the run
- report the final worklog path in the user-facing response

### File Manifest

```text
scope_root:
inspection_mode: audit_only | audit_plus_refactor
wave_size_limit: 8

files:
- [ ] docs/file_a.md
- [ ] docs/file_b.txt
- [ ] notes/file_c.org
```

Rules:

- include every plaintext doc-like file in scope
- mark files as inspected only after reading them
- allow files to appear in multiple clique waves
- reuse the same manifest for the final residual sweep

### Clique Wave Checkpoint

```text
clique_id:
purpose:
why_these_files_belong_together:
wave_size:

files:
- path/to/file_a.md
- path/to/file_b.txt

checkpoint:
- deletion candidates:
- merger candidates:
- possible keepers:
- likely rereads:
- code surfaces to reconcile:
```

Rules:

- `wave_size` must never exceed `8`
- write the checkpoint into the `/tmp` worklog after every wave before reading more files
- a file may appear in multiple cliques when supersession or duplication reasoning demands it
- name the clique by the relationship it is testing, not by arbitrary adjacency

### File Decision Ledger

Use one row per file.

```text
| path | doc_kind | audience | disposition | keep_or_delete_basis | superseded_by_or_merge_target | rewrite_needed | code_reconciliation_target |
|------|----------|----------|-------------|----------------------|-------------------------------|----------------|----------------------------|
| docs/protocol.md | formal_spec | developers | keep_as_is | foundational definition already vetted | | no | crates/protocol/src/lib.rs |
| docs/roadmap.md | roadmap | internal | delete | shipped history plus stale plans | | no | |
| docs/setup.md | runbook | operators | rewrite_from_scratch | still needed but bloated and partially stale | | yes | scripts/deploy.sh |
| notes/old-api.md | feature_doc | developers | merge_then_delete | scarce useful material belongs in docs/api.md | docs/api.md | no | crates/api/src/lib.rs |
```

Allowed `disposition` values:

- `delete`
- `merge_then_delete`
- `rewrite_from_scratch`
- `light_edit`
- `keep_as_is`
- `flag_contradiction`

Rules:

- every file must end in exactly one disposition
- `keep_or_delete_basis` can be short, but it must be concrete
- `rewrite_needed` should normally be `yes` for any surviving non-foundational doc
- `code_reconciliation_target` is required for every surviving or contradiction-flagged file

### Contradiction Register

Use this for genuine doc-vs-code contradictions where supersession is unclear.

```text
| doc_path | code_anchor | contradiction | possible_precedence | why_unclear | action_needed |
|----------|-------------|---------------|---------------------|-------------|---------------|
| docs/protocol.md | crates/protocol/src/lib.rs | doc says field is required; code treats it as optional | doc_or_code_unclear | public contract vs implementation drift | human decision |
```

Rules:

- record only real contradictions, not vague doubts
- if precedence is obvious, update the loser instead of logging it here
- unresolved entries must be surfaced in the final response

## Final Response

Always include:

- the `/tmp` worklog path
- manifest coverage summary
- clique-wave summary
- file disposition counts
- contradiction register summary

If you edited docs, also include:

- deleted files
- merge targets
- rewritten files
- lightly edited files
- untouched keepers with justification

## Hard Failure Modes

- do not inspect only “important” docs
- do not keep checkpoint state only in chat
- do not read more than 8 files without a persisted checkpoint
- do not keep a file because deleting it feels scary
- do not leave a file in a vague “maybe keep” limbo
- do not keep roadmap, checklist, or done-feature residue by inertia
- do not preserve stale docs by moving them into archive folders
- do not keep a spec-like file without reconciling it against code
- do not resolve genuine code-vs-doc contradictions by guessing at supersession
