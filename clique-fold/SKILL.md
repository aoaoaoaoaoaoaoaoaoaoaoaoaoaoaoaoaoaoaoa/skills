---
name: clique-fold
description: "Cover a large body of material exhaustively within a bounded context: lock a manifest, read it in budgeted semantic cliques, reduce each clique before opening the next, and fold the reductions into one thesis and a complete ledger. Use when a review must account for every item in a repository or corpus, either directly with a subject and ledger columns or as the reading engine of a skill that supplies them."
---

# Clique-Fold

Clique-fold covers a body of material exhaustively with a bounded context. It reads the material in budgeted semantic cliques, reduces each clique to a durable summary before opening the next, and folds the summaries into one thesis. It prevents two failures: losing orientation and churning through material, and judging a skimmed sample as though it were the whole.

## Arguments

The caller, a user or a skill, supplies:

- `subject`: what is evaluated, and the judgment each item receives.
- `columns`: the ledger columns that record that judgment.

For example, the subject "whether each public function reports every failure to its caller" might use the columns `failure_paths | judgment`. The caller may also name the worklog path; otherwise use `/tmp/clique-fold-<repo>-<run-id>.md`.

## Worklog

Record the manifest, cover, reductions, fold hierarchy, frontier, and thesis in the worklog, so that a fresh context can resume the run from it. If writes are unavailable, keep the same state in the conversation and state that the run cannot be resumed.

## Manifest

Discover the material broadly instead of trusting a hand-maintained list, and lock the manifest: every item the subject applies to, with its physical lines and bytes from a `wc -l -c` preflight. Record each exclusion and its reason. Once locked, the manifest changes only through a logged correction for an omitted item.

Material read only as evidence, such as callers, neighboring modules, or history, belongs to the fringe. Fringe material may inform a clique but never counts toward coverage.

## Budget

The raw material entering one clique is limited by:

```text
line_ceiling: 3000
byte_ceiling: 131072
```

Either ceiling trips the budget. They are ceilings, not packing targets, and only the user may change them. Everything whose contents enter working context counts: items, fringe, command output, and history. Path indexes and narrow definition or reference probes are free; voluminous search output is a deep read. Cover an oversized file in coherent slices whose union accounts for its relevant contents.

## Cover

Group the manifest into cliques: sets of items read together because they answer one question within budget. Name each clique by its question, not by directory adjacency. Cliques may overlap, and every item or slice belongs to at least one. Split, merge, or replace cliques as reading reveals a better decomposition. A manifest that fits the budget stays one clique; never create a clique only to reset the budget.

## Read and reduce

Read one clique at a time, deeply enough to reach the subject's judgment for each of its items, in whatever order resolves uncertainty fastest. Stop probing once further evidence cannot change a judgment. Never compensate for uncertainty by pulling whole files or broad search results into context.

Before opening the next clique, write its reduction to the worklog: the smallest account from which another model could integrate the clique's judgments without rereading its sources. An item is covered only when its relevant contents have been read and incorporated into a reduction; opening or skimming it does not count. When later evidence changes an earlier judgment, reread as needed and amend or supersede the affected reduction before opening more material.

Record anything outside the subject in the worklog for the caller and continue; it neither expands the manifest nor interrupts coverage.

## Fold

Fold related reductions into branch folds, and join branches through bridge folds where a question crosses them. Fold recursively until one root fold, the thesis, remains. A fold consumes reductions, not raw material; reopen raw material only to resolve a material conflict. The budget also limits each fold's input: measure the input first, and add a level if it exceeds either ceiling. A fold's output must be materially smaller than its input. Carry evidence anchors and unresolved frontier through every fold, and record the hierarchy, which may be a tree or a small DAG.

## Closure

The run is complete when:

- every manifest item is covered
- every clique has a reduction
- every question that crosses cliques is resolved or explicitly marked uncertain
- every ledger row carries the subject's judgment
- no open frontier question could change the thesis or a ledger row

A clean judgment is a valid result; do not manufacture judgments to justify a clique. Deliver the thesis and the ledger, written from the folds rather than concatenated from reductions.

## Forms

### Ledger

```text
| item | lines | bytes | cliques | <columns> | coverage |
|------|-------|-------|---------|-----------|----------|
```

### Reduction

```text
clique:
question:
items:
fringe:
lines:
bytes:
coverage_delta:

reduction:

cross_clique_dependencies:
frontier:
supersedes:
```

### Fold

```text
fold:
children:
input_lines:
input_bytes:

synthesis:

conflicts:
frontier:
```
