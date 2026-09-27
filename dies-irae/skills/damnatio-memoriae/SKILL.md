---
name: damnatio-memoriae
description: "Audit a repository's documentation from a presumption of deletion: prove which documents still earn existence, condemn obsolete, redundant, historical, or code-mirroring prose, and hand necessary reconstruction to Scriptorium. Produces a purge report; deletes files only when explicitly authorized, and never rewrites surviving documentation."
---

# Damnatio Memoriae

## Mandate

Reduce the documentation in scope to the smallest set of documents that still deserve to exist.

This is a purge, not an improvement campaign. Presume every document should be deleted. A document survives only by carrying a current contract, enabling a necessary act by a user, operator, or developer, or owning durable truth that cannot be recovered more directly elsewhere. Git history is the archive; historical interest, sunk effort, and fear of deletion confer no present value.

Damnatio Memoriae decides what may be deleted. It does not repair, rewrite, merge, or create living documentation. When necessary truth is trapped in a damaged, duplicated, misplaced, or contradictory document, preserve the evidence and hand the constructive work to Scriptorium.

Default to `report`. Delete files only under explicit `execute` authority, and only after the complete report exists.

## Scope

The scope is a repository or subtree. Its manifest holds every repository-owned document in scope: markdown and plaintext documentation, plans, notes, runbooks, ADRs, agent instruction files, and any other prose artifact regardless of filename. Source doc comments belong to Scriptorium.

Licenses, legal notices, test and prompt fixtures, generated artifacts, vendored material, and machine-consumed text are not documentation. Include ambiguous plaintext in the manifest, establish its role, and exempt it explicitly when it falls outside the purge. Do not inflate the manifest with every machine file that contains comments or every binary a document links; include a nonconventional artifact only when its primary role could plausibly be durable documentation.

Code, configuration, tests, generated behavior, current documentation, and history are evidence; none is automatically authoritative. A document may state an intended contract that the implementation violates. When precedence is not established, record the conflict as an authority question instead of declaring the newer artifact the winner.

## Survival standard

Ask of every document:

> If this file vanished today, what present capability, governing contract, or durable truth would be lost?

The answer must name a real audience and consequence. Prose that narrates code, commemorates completed work, accumulates abandoned intentions, duplicates a stronger owner, or could be regenerated cheaply does not survive. A surviving document has a coherent role, a stable owner, and authority matching its claims.

Do not preserve a whole file for a few valuable sentences. If those sentences belong in another living document, the file is a handoff pending extraction: not a survivor, and not yet safe to delete.

The burden for a handoff is strict; it is not a refuge for any stale document. Deletion must otherwise destroy a necessary documentary role or scarce durable truth that cannot be reconstructed cheaply from code and history. A narrative that mirrors code does not earn transfer merely because a better document could later be written.

A doomed file also needs a handoff when its deletion depends on constructive work to a living document, such as removing or redirecting an inbound link. State that dependency exactly and transfer no content by implication; the file remains doomed.

Damnatio Memoriae judges existence, not full correctness. Establish that a survivor has a live role, an owner, and no decisive supersession or contradiction visible from proportionate evidence. Exhaustive truth reconciliation, link checking, line editing, and reconstruction belong to Scriptorium.

## Procedure

### 1. Open the run

Create the worklog and report before deep reading:

```text
/tmp/damnatio-memoriae-<repo>-<scope>-<run-id>.md
/tmp/damnatio-memoriae-<repo>-<scope>-<run-id>-report.md
```

In a tribunal, use the directory the tribunal assigns. Record the mode, source identity, and scope. Keep the worklog compact; the report owns the final argument. If writes are forbidden, carry the same state in the final response and state that the run cannot be resumed; a read-only run is a complete audit.

### 2. Cover the documentation

Run `$clique-fold` with:

- `subject`: for each document, what would be lost if it vanished, and its disposition
- `columns`: `role | disposition | basis | anchors_or_dependency`

Discover documents broadly instead of trusting a hand-maintained index. Group them so that cliques expose supersession, duplication, audience, authority, and lifecycle relationships.

Read each document deeply enough to judge its function, claims, authority, neighbors, code anchors, and deletion consequences, and reconcile its claims against the implementation only as far as its disposition requires. A doomed document needs decisive evidence, not an inventory of every stale sentence; a machine-consumed artifact needs enough inspection to establish its role and any supersession. Consult an external owner only to resolve a real authority or transfer question. Do not validate network or release surfaces merely to certify a document that already earns existence.

Record a `critical` discovery in the critical register and continue; it neither triggers rectification nor truncates coverage.

### 3. Adjudicate

Give every document exactly one disposition:

- `delete`: destruction loses no living truth or required capability.
- `survive`: the document and its role earn continued existence without material reconstruction.
- `handoff`: Scriptorium's constructive work on a living document must precede deletion or acceptance, whether to receive necessary truth, reconstruct a required role, or sever an inbound dependency on a doomed file.
- `authority_question`: authority, a legal obligation, or a contradiction is genuinely unresolved; leave the evidence intact and name the decision required.
- `exempt`: the artifact is not repository-owned documentation; state its actual role.

Leave no `maybe`, implicit omission, or unclassified file. Deletion is judged by cohort: a file whose disappearance would strand navigation, references, required fragments, or documentary ownership is not independently deletable, and its cohort remains a handoff until the receiving document exists.

Do not manufacture work for clean documents.

### 4. Report

Write the report from the folds: the purge thesis, coverage, deletion cohorts, survivors with their burden of proof, handoffs, and authority questions. Stop there unless `execute` was authorized.

### 5. Execute

Recheck the source identity. Delete only complete `delete` cohorts whose dependencies still hold. Do not rewrite survivors or improvise Scriptorium's work. Afterward, rescan the documentation and its references, account for every changed path, and report any cohort withheld because the evidence drifted.

## Forms

### Worklog

```text
mode: report | execute
repository:
source_identity:
scope:
worklog_path:
report_path:
critical_register: none

clique_fold:
handoffs:
authority_questions:
purge_thesis:
execution:
residual:
```

### Report

```markdown
# Damnatio Memoriae Report: <scope>

## Executive judgment
## Coverage
## Purge thesis
## Deletion cohorts
## Survivors
## Handoffs to Scriptorium
## Authority questions
## Exempt artifacts
## Critical register
## Execution safety and order
## Residual unknowns

### Ledger

The complete clique-fold ledger, one row per document.
```
