---
name: fahrenheit-451
description: Audit an entire repository-owned documentation corpus from a presumption of deletion. Use when Codex should burn obsolete, redundant, historical, or code-mirroring prose; prove which documents still earn existence; and hand necessary reconstruction or contradiction repair to a documentation-authoring pass. Defaults to a read-only purge report and never rewrites surviving documentation on its own.
---

# Fahrenheit 451

## Mandate

Reduce a bounded documentation corpus to the smallest set of durable prose surfaces that still deserve to exist.

This is a purge, not a documentation-improvement campaign. Presume every document should be deleted. A file survives only by carrying a current contract, enabling a necessary user, operator, or developer act, or owning durable truth that cannot be recovered more lawfully elsewhere. Git history is the archive; historical interest, sunk effort, and fear of deletion confer no present value.

Fahrenheit decides what may burn. It does not delicately repair, rewrite, merge, or create living documentation. When necessary truth is trapped in a damaged, duplicated, misplaced, or contradictory surface, preserve the evidence and hand the constructive work to Chronicler.

Default to `purge_report`. Delete files only when the user explicitly authorizes `purge_execute`, and only after the complete report exists.

## Scope And Authority

Require a concrete repository or subtree. Census every repository-owned doc-like file in scope: markdown and conventional plaintext documentation, plans, notes, runbooks, ADRs, instruction files, and other prose artifacts regardless of filename. Source doc comments belong to Chronicler, not this corpus.

Do not mistake licenses, legal notices, test fixtures, prompt fixtures, generated artifacts, vendored material, or machine-consumed text for ordinary documentation. Include ambiguous plaintext in the census, establish its role, and exempt it explicitly when it is outside the purge corpus. Do not inflate the census to every machine file containing comments or every binary linked by prose; include a nonconventional artifact only when its primary repository role could plausibly be durable documentation.

Code, configuration, tests, generated behavior, current documentation, and history are evidence. None is automatically sovereign. A document may state an intended public or architectural contract that the implementation violates. When precedence is not established, preserve the conflict rather than declaring whichever artifact is newer the winner.

## Survival Standard

Ask the zero-based question continuously:

> If this file vanished today, what present capability, governing contract, or durable truth would be lost?

The answer must name a real audience and consequence. Prose that merely narrates code, commemorates completed work, accumulates abandoned intention, duplicates a stronger owner, or could be regenerated cheaply does not survive. A surviving document must have a coherent role, a stable owner, and authority commensurate with its claims.

Do not preserve a whole file for a few valuable sentences. If those sentences belong in another living surface, the file is a Chronicler handoff pending extraction, not a keeper and not yet safe to delete.

The handoff burden is strict. `chronicler_handoff` is not a refuge for any stale document: deletion must otherwise destroy a necessary documentary role or scarce durable truth that cannot be reconstructed cheaply from code and history. A code-mirroring architecture narrative does not earn transfer merely because a better architecture document could later be written.

A doomed file may also require a handoff when deletion depends on constructive surgery to a living surface, such as removing or redirecting an inbound navigation link. State that dependency exactly and transfer no content by implication; the file remains doomed, and the handoff does not rehabilitate it.

Fahrenheit adjudicates existence, not full documentary correctness. Establish that a survivor has a live role, a lawful owner, and no decisive supersession or contradiction visible from proportionate evidence. Chronicler owns exhaustive truth reconciliation, link checking, line editing, and reconstruction.

## Protocol

### 0. Open The Run

When the environment permits, create resumable state before deep reading:

```text
/tmp/fahrenheit-451-<repo>-<scope>-<run-id>.md
/tmp/fahrenheit-451-<repo>-<scope>-<run-id>-report.md
```

Record mode, repository identity, scope, corpus rules, context budget, manifest, reductions, fold hierarchy, judgments, contradictions, and handoffs. Keep the worklog compact; the report owns the final argument. If all writes are forbidden, preserve the same structure in the final response and mark the run nonresumable. Read-only execution is a supported audit mode.

### 1. Lock The Census And Budget

Use broad discovery rather than a trusted hand-maintained list. Record every candidate path, its physical lines and bytes, and its provisional role. The census becomes immutable except for logged corrections.

Use these default circuit breakers for all raw text brought into one deep-reading clique:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. They are ceilings, not packing targets. Count documents, source, configuration, fixtures, dependency code, history, and command output whenever their contents enter working context. Broad path indexes and narrow anchored probes may range beyond a clique; voluminous search output is a deep read, not a loophole. Split oversized documents into coherent ranges whose union accounts for the whole file.

### 2. Build An Adaptive Clique Cover

Group the corpus into overlapping semantic cliques large enough to expose supersession, duplication, audience, authority, and lifecycle relationships while remaining under budget. Let the corpus reveal the useful decomposition; do not march through arbitrary directory batches or force every clique through a fixed audit-lens menu.

A compact corpus should remain in one working clique unless its relationships genuinely require separation. Do not manufacture cliques to reset the context budget.

Every census entry must belong to at least one planned clique or carry an evidenced exemption. Revise the cover when reading reveals a truer relationship.

### 3. Read And Reduce

Read every document in each clique deeply enough to judge its function, claims, authority, neighbors, code anchors, and deletion consequences. Reconcile claims against implementation evidence only as far as needed to adjudicate existence. Once further evidence cannot change the disposition, deletion safety, or handoff dependency, stop probing. A doomed document needs decisive evidence, not an inventory of every stale sentence; a machine-consumed fixture needs enough inspection to establish its role and relevant supersession, not automatic line-by-line review.

Navigate evidence by definitions, references, manifests, and bounded ranges. Never compensate for uncertainty by dumping whole source files, registries, parent workspaces, Git internals, or broad search matches into context. Consult an external owner only when resolving a real authority or transfer question, and charge that material to the same budget. Do not launch network or release-surface validation merely to certify a document that already earns existence; transient external correctness belongs to Chronicler unless it determines deletion or documentary ownership.

Before opening another clique, reduce the current one into the smallest durable account from which another intelligent model can integrate its judgment without rereading the documents. Preserve evidence anchors, proposed dispositions, unresolved authority, cross-clique dependencies, and the open frontier. A file is not covered merely because it was opened or skimmed.

### 4. Fold Without Flooding Context

Fold related clique reductions into bounded branch syntheses, then fold branches until one corpus-level purge thesis remains. Higher folds consume reductions rather than raw documents. A fold obeys the same line and byte ceilings; introduce another level whenever necessary. A fold that does not materially compress its inputs has failed to reduce them.

Use bounded bridge reductions for relationships that cross branches. Reopen raw evidence only to resolve a material conflict or uncertainty.

### 5. Adjudicate Every Entry

Give every census entry exactly one terminal disposition:

- `delete`: destruction loses no living truth or required capability.
- `survive`: the current file and its role earn continued existence without material reconstruction.
- `chronicler_handoff`: constructive work on a living surface must precede deletion or acceptance, whether to receive necessary truth, reconstruct a required role, or sever an inbound dependency on an otherwise doomed file.
- `blocked`: authority, legal obligation, or contradiction is genuinely unresolved; leave the evidence intact and name the decision required.
- `exempt`: the artifact is not repository-owned documentation subject to this purge; state its actual role.

These are actions, not audit lenses. Follow the evidence freely, but leave no `maybe`, implicit omission, or unclassified file.

Deletion safety is cohort-level. A file is not independently deletable when its disappearance would strand navigation, references, required fragments, or documentary ownership. Such a cohort remains a Chronicler handoff until the receiving surface exists.

### 6. Close The Corpus

Continue until every census entry is deeply covered or evidenced as exempt, every clique has a reduction, cross-clique supersession and duplication are resolved, every entry has a terminal disposition, and no open frontier could materially change a disposition or the corpus-level thesis.

Do not manufacture work for clean documents. Do not let an alarming incidental discovery trigger rectification or truncate corpus coverage; record it separately and continue.

### 7. Report, Then Optionally Burn

Write a complete report from the folds rather than concatenating notes. The report must establish the purge thesis, exhaustive coverage, deletion cohorts, survivors and their burden of proof, constructive handoffs, and blocked authority questions.

Stop after the report unless execution was explicit. In `purge_execute`, delete only complete `delete` cohorts whose dependencies remain satisfied. Do not rewrite survivors or improvise the Chronicler work. Re-scan the corpus and references after deletion, account for every changed path, and report any cohort withheld because the evidence drifted.

## Embedded Forms

### Run State

```text
mode: purge_report | purge_execute
repository:
source_identity:
scope:
worklog_path:
report_path:
context_line_ceiling: 3000
context_byte_ceiling: 131072

census:
clique_cover:
clique_reductions:
fold_hierarchy:
live_judgments:
contradictions:
chronicler_handoffs:
frontier:
root_purge_thesis:
execution:
residual:
```

### Corpus Ledger

```text
| path | role | lines | bytes | cliques | disposition | basis | anchors_or_dependency | coverage |
|------|------|-------|-------|---------|-------------|-------|-----------------------|----------|
```

### Clique Reduction

```text
clique_id:
purpose:
documents:
document_lines:
document_bytes:
coverage_delta:

reduction:

provisional_dispositions:
cross_clique_dependencies:
contradictions:
frontier:
supersedes:
```

### Purge Report

```markdown
# Fahrenheit 451 Report: <scope>

## Executive Judgment
## Corpus And Coverage
## Purge Thesis
## Deletion Cohorts
## Survivors
## Chronicler Handoffs
## Blocked Authority And Contradictions
## Exempt Artifacts
## Incidental High-Severity Findings
## Execution Safety And Order
## Residual Unknowns

### Complete Disposition Ledger

| path | disposition | judgment | evidence | dependencies |
|------|-------------|----------|----------|--------------|
```

## Hard Failures

- do not sample, skim, or silently omit the corpus
- do not keep dead prose as an archive or move it to a graveyard
- do not equate newer implementation with authoritative intent
- do not preserve a file merely because some fragment within it matters
- do not launder stale, code-derivable prose into a Chronicler handoff
- do not delete scarce truth before its lawful owner exists
- do not rewrite, merge, or create living documentation in this campaign
- do not exempt evidentiary code, fixtures, history, dependencies, or command output from the context budget
- do not keep probing after the evidence can no longer change the disposition or its dependencies
- do not perform Chronicler's exhaustive correctness or external-link audit under the guise of proving survival
- do not exceed a clique or fold budget to avoid decomposition
- do not use one unbounded global context fold
- do not turn the worklog into a shadow report
- do not edit before the complete purge report or without explicit authorization
