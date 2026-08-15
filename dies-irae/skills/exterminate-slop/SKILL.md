---
name: exterminate-slop
description: "Audit a bounded source subtree or semantic component for aggressive, behavior-preserving semantic contraction while keeping its present responsibilities and outer contract fixed. Use when Codex should make an accreted implementation materially smaller, more lawful, and more intentional without authorizing a rewrite."
---

# Exterminate Slop

Read the target repository's `AGENTS.md` files first. Load every language note that materially applies to the audited surface, and no irrelevant ones:

- Rust: [references/languages/rust.md](references/languages/rust.md)
- Java: [references/languages/java.md](references/languages/java.md)
- Python: [references/languages/python.md](references/languages/python.md)
- TypeScript: [references/languages/typescript.md](references/languages/typescript.md)

Load the applicable `style-doctrine` guides. Load `product-doctrine` as well when the surface governs conduct on the user's system. Apply both within the frozen semantic envelope; doctrine sharpens the judgment but does not authorize a contract change.

## Mandate

Make a bounded semantic surface look as though its present responsibilities had been implemented once, coherently, without historical sediment.

This is aggressive implementation contraction under a frozen semantic envelope. Delete implementation, not requirements. Preserve the envelope's supported behavior and external obligations. Do not preserve internal compatibility, obsolete structure, or historical decomposition by default.

Default to `defect_report`. Edit source only when the user explicitly requests implementation, and only after the complete report exists.

## Semantic Envelope

Before judging the implementation, identify the surface's current responsibilities, supported capabilities, observable behavior, failure semantics, public protocols, persistence obligations, trust boundaries, and material nonfunctional constraints.

The implementation, callers, tests, documentation, configuration, and history are evidence for this envelope. None is automatically authoritative. The current implementation may reveal what must survive; it does not dictate the form in which it survives.

A filesystem subtree is an edit and coverage boundary, not a reasoning boundary. Read outward as needed to understand callers and real boundaries. Keep prescribed cuts within the authorized semantic envelope.

## Architectural Standard

Treat the existing implementation as historical evidence, not as an authoritative decomposition of the problem.

An internal structure earns survival only by carrying required behavior, enforcing a real law, satisfying a necessary representation constraint, or marking a genuine boundary. Distinctions with no distinct law should collapse. Truth with no canonical owner should acquire one.

Judge abstractions by their net effect on semantic description length: how many independent facts, degrees of freedom, synchronization obligations, and change sites remain after the move. Familiarity, local brevity, and conventional simplicity carry no independent weight.

Use the full power of the language whenever it yields a smaller lawful machine.

## Contraction Objective

Seek the smallest lawful implementation `I*` such that `I* ≡ₑ I₀`, where `E` is the frozen semantic envelope.

Minimize semantic description length: the independent concepts, representations, owners, states, paths, boundaries, and obligations required to state and maintain the implementation. Lines and bytes are corroborating measures, not the objective. Local expansion is correct when it reduces global state space or independent truths.

## Search Posture

Let the system reveal its own dominant forms of accidental complexity. Do not organize the audit around a fixed smell catalogue, attempt to exercise named passes evenly, or force findings into predefined categories.

Reason both subtractively and reconstructively. Ask what can vanish, what can become derived, which distinctions are fictitious, which truths lack an owner, and which boundaries exist only because history placed code on opposite sides of them. Follow the strongest semantic pressure wherever it leads.

Use the counterfactual continuously:

> If this exact semantic envelope were implemented today, would this internal construct exist?

The question applies to implementation, not requirements. Do not use it to revoke supported responsibilities or renegotiate the outer contract.

## Protocol

### 0. Open The Run

Create session-resumable artifacts before the first deep source read:

```text
/tmp/exterminate-slop-<repo>-<scope>-<run-id>.md
/tmp/exterminate-slop-<repo>-<scope>-<run-id>-report.md
```

Create a companion `-high-severity.md` register only if a qualifying finding appears.

Record the mode, repository and source identity, scope, provisional semantic envelope, applicable language notes, source budget, worklog path, and report path. Chat is a summary surface; the worklog is the resumable audit state. It must not become a shadow copy of the final report.

If the user names only a repository, choose the smallest semantically coherent surface that answers the request and state the assumption. Do not silently substitute an arbitrary directory for a semantic boundary.

### 1. Lock The Manifest And Budget

Build an exhaustive audit manifest of handwritten implementation sources inside the authorized surface. Include handwritten schema, configuration, or build files when they materially define that surface, recording why. Exclude generated, vendored, dependency, snapshot, fixture, and build-output material unless the user explicitly includes it.

Maintain a separate context fringe for out-of-manifest callers, tests, schemas, configuration, and neighboring modules consulted as evidence. Fringe inspection does not expand audit coverage or mutation authority.

Run a cheap `wc -l -c` preflight over the manifest and persist per-file and total physical lines and bytes. The default deep-source budget for one clique is:

```text
source_line_ceiling: 3000
source_byte_ceiling: 131072
```

Either ceiling trips the budget. These are circuit breakers, not packing targets. A user may override them explicitly. Never increase them ad hoc merely to avoid decomposing a difficult surface.

Once locked, the audit manifest is immutable except for a logged correction of an initially omitted in-scope file. An oversized file must be covered through coherent symbol or range slices whose union accounts for its semantically relevant contents.

### 2. Seed An Adaptive Semantic Clique Cover

Use cheap whole-surface indexing and semantic navigation to seed an overlapping cover of the manifest. Each clique should gather the largest source set below budget that belongs in one working context because it resolves one coherent semantic question.

The cover is provisional. Split, merge, replace, overlap, or add cliques as evidence changes the correct decomposition. Name cliques by the relationship or question they resolve, not by arbitrary adjacency.

Every manifest source or source slice must belong to at least one planned clique. Context-fringe material may be attached to a clique as evidence but never counts toward manifest coverage.

### 3. Read And Reduce Cliques

Process one clique at a time. Deeply inspect all semantically relevant contents in its declared source set, using whatever navigation order best reduces uncertainty. Narrow indexing and definition/reference probes do not themselves open another clique; source brought into deep working context counts against the budget.

Before opening the next clique, reduce the current one into the worklog. The reduction must be the smallest durable semantic message sufficient for another intelligent model to integrate the clique without rereading its sources. Use the embedded reduction form, but let the substance remain free-form.

A source is covered only when its relevant contents have been inspected and incorporated into a reduction. Merely opening or skimming it does not count.

Rereading is expected when later evidence changes a boundary or abstraction hypothesis. A material reread must amend or supersede the affected reduction before more source is opened.

If a credible catastrophic defect appears, record it immediately in the high-severity register and continue the audit. Discovery does not authorize source modification, scope expansion, remediation, or abandonment of coverage. Even in `defect_report_then_execute` mode, rectification waits until the report phase is complete.

All audit requirements must remain satisfiable against a read-only source tree.

### 4. Fold Reductions Hierarchically

Do not concatenate every leaf reduction into one monolithic global pass.

Fold related leaf reductions into bounded branch syntheses. When a hypothesis crosses branches, form a bounded bridge reduction from the relevant child reductions and only the minimum additional source context needed. Recursively fold branch and bridge reductions until one root contraction thesis remains.

Higher folds consume child reductions, not their raw sources. Reopen a child or source anchor only to resolve a material conflict or uncertainty. Preserve evidence pointers and unresolved frontier edges through every fold.

Before a fold, measure the reductions it will ingest. The same line and byte ceilings are hard upper bounds on fold input. If the input exceeds either ceiling, introduce another reduction level. A fold output must be materially smaller than its inputs; otherwise it has not reduced them.

The reduction hierarchy may be a tree or a small DAG because bridge reductions can join branches. Record its child relationships explicitly.

### 5. Close The Frontier

Manifest coverage is necessary but not sufficient. Continue adaptive cliques and bounded folds until:

- every manifest source is deeply covered
- every planned or discovered clique has a durable reduction
- material cross-clique hypotheses are resolved or explicitly uncertain
- competing local abstractions have been reconciled globally
- no open frontier could materially change the contraction thesis or a report finding

Do not manufacture findings to justify a clique. A clean reduction is a valid result.

### 6. Adjudicate Findings

One finding represents one coherent semantic contraction, not one source site. It may accumulate evidence across many cliques and may be strengthened, split, merged, or discharged before the report.

Promote a finding when the evidence establishes a material accidental burden, the proposed shape is lawful and sufficiently concrete, and the move stays within the semantic envelope. Do not require local actionability; foundational contractions may be broad within the authorized surface.

Recover the terminal machine from the surviving obligations rather than by attaching remedies to the incumbent structure. State what disappears or becomes derived before describing what remains or must be introduced. Every survivor and addition must carry an obligation not already discharged elsewhere. A purely additive change is valid only when the frozen envelope contains a genuine unmet obligation; name it explicitly.

Record rejected hypotheses only when the rejection is material, subtle, or likely to prevent repeated rediscovery. Do not write an obituary for every fleeting suspicion.

Do not force safety or correctness discoveries into contraction vocabulary. Integrate them when accidental structure caused them and the proposed contraction resolves them. Otherwise place them in the high-severity or incidental-defect section as appropriate.

Out-of-envelope lesions may be named and evidenced tersely. Do not elaborate them into an unsolicited redesign specification.

### 7. Write The Report

Write a complete, proportional, implementation-ready report using the embedded report form. Do not demand or reward length. Do not use a closed `kind` taxonomy.

The report must synthesize one coherent contraction thesis rather than dump checkpoint notes. Every required finding field is a proof obligation; if no material concern exists for a field, say so tersely rather than omitting it.

The implementation specification must be precise enough to execute without repeating the audit, while retaining honest uncertainty and evidence anchors.

### 8. Optional Implementation

Stop after the report unless implementation was explicitly authorized. A read-only environment is a successful report-only run, not a blocker.

When implementation is authorized, treat it as a new phase. Recheck source identity and refresh any affected clique if the tree has drifted since audit. Execute coherent semantic moves in dependency order, never arbitrary file order, and never cross the frozen envelope without new authorization.

Use the target repository's own verification contract. After implementation, preserve the baseline manifest, construct a final manifest that accounts for created, deleted, fused, and moved sources, and run a budgeted residual cover and fold over the changed semantic surface. Report actual semantic contraction and cheap line/byte deltas without confusing either for the objective.

## Embedded Forms

### Worklog State

```text
worklog_path:
report_path:
high_severity_path: none
run_id:
mode: defect_report | defect_report_then_execute
repository:
source_identity:
scope:
semantic_envelope:
language_notes:
source_line_ceiling: 3000
source_byte_ceiling: 131072

audit_manifest:
context_fringe:
manifest_corrections:
clique_cover:
leaf_reductions:
fold_hierarchy:
live_findings:
material_rejections:
frontier:
root_contraction_thesis:
implementation:
residual:
```

### Manifest

```text
| path_or_slice | lines | bytes | planned_cliques | coverage |
|---------------|-------|-------|-----------------|----------|
| src/foo.rs | 240 | 8120 | C01, C04 | covered |
| src/giant.rs:1-1800 | 1800 | 70110 | C02 | pending |
```

### Clique Reduction

```text
clique_id:
purpose:
source_set:
context_fringe:
source_lines:
source_bytes:
coverage_delta:

reduction:

frontier:

supersedes:
```

### Fold Reduction

```text
fold_id:
children:
input_lines:
input_bytes:

synthesis:

conflicts_or_counterevidence:

frontier:
```

### High-Severity Register

```text
| id | site | finding | evidence | confidence | severity_basis | status |
|----|------|---------|----------|------------|----------------|--------|
```

Do not include a remediation field. The register is an alarm lane, not an implementation detour.

### Defect Report

```markdown
# Exterminate Slop Report: <scope>

## Executive Summary

## Semantic Envelope

## Coverage And Reduction

Record manifest coverage, exclusions, context fringe, language notes, source budget, clique cover, reduction hierarchy, worklog path, and cheap baseline.

## Contraction Thesis

## Priority And Dependency Map

| order | finding | leverage | confidence | implementation_risk | dependencies |
|-------|---------|----------|------------|---------------------|--------------|

## High-Severity Register

State `none` or summarize and link the companion register.

## Findings

### <id>: <title>

**Sites:**
**Evidence:**
**Judgment:**
**Semantic Contraction:** What declarations, states, paths, representations, dependencies, and synchronization obligations disappear or become derived.
**Terminal Shape:** The smallest lawful structure remaining after the contraction.
**Irreducible Additions:** New machinery required by the terminal shape, or `none`; name the law each addition uniquely carries.
**Implementation Specification:**
**Envelope Preservation:**
**Relations / Dependencies:**
**Verification:**
**Uncertainty:**

## Retained Complexity And Rejected Hypotheses

Include only material defenses and rejections.

## Incidental Defects

## Out-Of-Envelope Lesions

## Execution Notes

## Residual Unknowns
```

## Final Response

Report the worklog and report paths, semantic envelope, complete manifest coverage, clique and fold counts, root contraction thesis, highest-leverage findings, high-severity status, out-of-envelope lesions, and cheap baseline. If implementation occurred, also report verification, residual closure, final manifest changes, and observed contraction.
