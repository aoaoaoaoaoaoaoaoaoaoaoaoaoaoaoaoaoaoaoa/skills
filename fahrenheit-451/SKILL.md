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

Use [references/tmp-worklog-template.md](/home/main/projects/skills/fahrenheit-451/references/tmp-worklog-template.md).

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

Use [references/file-manifest-template.md](/home/main/projects/skills/fahrenheit-451/references/file-manifest-template.md).

### 2. Plan logical cliques

Group manifest files into small logical cliques before deep reading.

Use [references/read-cluster-template.md](/home/main/projects/skills/fahrenheit-451/references/read-cluster-template.md).

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

Use [references/file-decision-ledger-template.md](/home/main/projects/skills/fahrenheit-451/references/file-decision-ledger-template.md).

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

If precedence is not obvious, move the file to `flag_contradiction` and record the issue in [references/contradiction-register-template.md](/home/main/projects/skills/fahrenheit-451/references/contradiction-register-template.md).

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

## Resources

- [references/file-manifest-template.md](/home/main/projects/skills/fahrenheit-451/references/file-manifest-template.md)
- [references/read-cluster-template.md](/home/main/projects/skills/fahrenheit-451/references/read-cluster-template.md)
- [references/file-decision-ledger-template.md](/home/main/projects/skills/fahrenheit-451/references/file-decision-ledger-template.md)
- [references/contradiction-register-template.md](/home/main/projects/skills/fahrenheit-451/references/contradiction-register-template.md)
- [references/tmp-worklog-template.md](/home/main/projects/skills/fahrenheit-451/references/tmp-worklog-template.md)
