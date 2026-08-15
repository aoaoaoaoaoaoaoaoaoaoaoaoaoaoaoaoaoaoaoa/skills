---
name: chronicler
description: Reconcile a project's durable documentation with its actual contracts and present system. Use when Codex should create, reconstruct, consolidate, relocate, or repair READMEs, guides, architecture documents, runbooks, examples, module docs, public API docs, docstrings, rustdoc, and comments that carry nonrecoverable rationale or proof obligations. Supports exhaustive report-only audits and explicitly authorized documentation edits without changing product behavior or public contracts.
---

# Chronicler

## Mandate

Bring the project's documentary model into concordance with the system it governs.

The fixed point is:

> Every durable fact that must be communicated has one canonical documentary owner, at the narrowest stable layer that can state it truthfully; no required truth is missing, stale, duplicated, or stranded in transient prose.

Documentation is part of the semantic machine. It owns truths that code cannot state to the relevant audience: public contracts, operational acts, design intent, external constraints, proof obligations, failure semantics, and rationale whose recovery would be costly or ambiguous. It must not become a shadow implementation, a historical scrapbook, or explanatory mulch around self-evident code.

Fahrenheit decides which documentary vessels deserve existence. Chronicler is the constructive complement: it repairs living surfaces and safely transfers scarce truth out of doomed ones. If a Fahrenheit report exists, consume its handoffs and deletion dependencies as evidence; do not rerun the purge or casually reverse its zero-based judgments.

Default to `concordance_report`. Edit documentation only when the user explicitly requests execution, and only after the complete report exists.

## Scope And Envelope

For a project-wide request, cover the whole documentary model. For a named feature, subsystem, audience, or API region, follow that semantic region across the entire project rather than treating one directory as the reasoning boundary. State any unavoidable exclusion; never silently substitute a convenient sample.

The documentary surface includes role-bearing prose files, user and operator surfaces, examples, module and item documentation, public API commentary, and internal comments that preserve a law, proof, safety condition, external fact, or non-obvious causal rationale. It also includes missing surfaces implied by a real audience or exported contract.

Do not manufacture prose for every symbol. Trivial private mechanics may remain silent. Comments that paraphrase syntax, narrate control flow, preserve obsolete topology, or compensate for a poor name or unlawful abstraction should disappear or provoke a code finding rather than grow more eloquent.

Language visibility is evidence of an audience, not always proof of an intended durable API. When a nominally public surface is credibly accidental, do not transmute contract freeze into a mandate to immortalize every exposed artifact. Record the API-authority blocker, preserve any truth current consumers require, and defer canonical public documentation until the surface itself is adjudicated.

Freeze product behavior and public contracts unless the user separately authorizes their change. Code, tests, configuration, generated behavior, documentation, history, standards, and upstream contracts are evidence; none is automatically sovereign. When authority is genuinely unclear, expose the decision instead of laundering one side into documentation.

Read repository instructions and applicable style and product doctrine before judging or editing source commentary and user-facing contracts. Preserve the project's voice, but not its accidents.

## Placement Law

Put a truth where it will remain true and where its audience encounters the governed thing. The narrowest stable owner wins: a type law belongs with the type, an effect or failure contract with the callable surface, a module invariant with the module, an operator act with the command or runbook, and a project-wide decision with the smallest durable project document capable of governing it.

Store each truth once. Broader surfaces may orient and link; they must not recopy volatile details from narrower owners. Prefer generated or mechanically checked projection where prose would otherwise synchronize with code. Move commentary when ownership moves.

Doc comments state semantic contracts, not implementation tours. Make invariants, units, preconditions, effects, failure and panic behavior, concurrency or safety obligations, and surprising cost visible where they matter. Examples should teach a lawful use or resolve an ambiguity, not decorate an obvious signature.

Ordinary comments earn survival only by carrying information unavailable from the code itself. Preserve the why, the proof boundary, and the external constraint; delete the what.

## Protocol

### 0. Open The Run

When writes are available, create resumable state before deep reading:

```text
/tmp/chronicler-<repo>-<scope>-<run-id>.md
/tmp/chronicler-<repo>-<scope>-<run-id>-report.md
```

Record mode, source identity, scope, documentary envelope, applicable doctrine, context budget, surface census, obligation atlas, ownership map, reductions, fold hierarchy, change program, contradictions, verification, and residual frontier. The worklog preserves orientation; the report owns the final argument. If all writes are forbidden, carry the same state into the final response and mark the run nonresumable.

### 1. Build The Census And Obligation Atlas

Discover existing documentary surfaces broadly. Use symbol and API indexes, manifests, command surfaces, schemas, lints, and package metadata to expose missing obligations without dumping the implementation into context.

Record both existing owners and required truths with no owner. For source commentary, manifest semantic symbols or bounded ranges rather than pretending a whole large source file is one document. Distinguish generated, vendored, legal, fixture, and machine-consumed material before proposing changes.

Exhaustiveness attaches to documentary surfaces and communication obligations, not to every tracked artifact. Code, configuration, tests, history, binaries, and visual assets enter as bounded authority evidence. Do not promote them into the census merely because they exist, contain comments, or are linked from prose; inspect a non-text asset only when it independently communicates a material contract that could change the documentary judgment.

Run a cheap `wc -l -c` preflight over file-backed surfaces. Use these default circuit breakers for all raw material entering one deep-reading clique:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. Count documentation, source, configuration, tests, history, dependencies, standards, and command output. Cheap indexes and anchored semantic probes may range widely; large search output is a deep read. Oversized files must be covered through coherent symbol or range slices.

### 2. Seed An Adaptive Semantic Clique Cover

Group documentary owners, obligations, governed code, examples, and authority evidence into overlapping cliques that resolve coherent communication questions under budget. Let the project's ontology and audiences determine the cover; do not force a fixed catalogue of documentation genres or audit lenses.

Every in-scope surface and material obligation must belong to the cover. Split, merge, overlap, or replace cliques as ownership becomes clearer. Do not manufacture cliques merely to reset the context budget.

### 3. Read And Reduce

For each clique, determine what must be communicated, to whom, under what authority, and at which stable owner. Reconcile the current prose against bounded implementation evidence. Follow claims to the point of documentary judgment, not into a general code audit.

Stop opening evidence when additional implementation, history, dependency, or external material cannot change ownership, required content, authority, or the change program. Exhaustive obligation coverage does not license exhaustive implementation reading.

Before opening another clique, reduce the current one into the smallest durable account another intelligent model can integrate without rereading its sources. Preserve present owners, missing truths, duplication, authority conflicts, proposed ownership, evidence anchors, cross-clique dependencies, and the open frontier. Merely opening a file or enumerating symbols does not constitute coverage.

If a catastrophic defect or secret appears, record it in a separate high-severity register and continue coverage. Discovery does not authorize code rectification or derail the documentation campaign.

### 4. Fold Ownership Hierarchically

Fold related clique reductions into bounded branch syntheses, then reconcile branches through bounded bridge reductions until one project- or region-level documentary model remains. Higher folds consume reductions, not raw sources. The same context ceilings govern fold inputs; introduce another level rather than flooding one global pass.

Use the fold to rectify names, choose canonical owners, eliminate duplicated truths, and resolve audience boundaries. A fold output must materially compress its inputs while preserving evidence and unresolved authority.

### 5. Design The Change Program

Turn the ownership model into a dependency-ordered program precise enough to execute without repeating the audit. Each change must identify the truth or obligation, present and proposed owner, evidence, exact documentary shape, affected duplicates, authority, and verification.

Derive the terminal documentary model from required truths rather than existing vessels. Prefer removal, consolidation, transfer, and mechanical derivation within Chronicler's authority; repair or create only where an obligation would otherwise lack a lawful owner. Each change must identify the duplicate or obsolete surfaces retired, the canonical owner that remains, and any irreducible new surface. An addition-only change must name the audience and necessary truth that no existing stable owner can carry.

Use action language that states what will actually happen: remove, consolidate, transfer, derive, repair, reconstruct, create, or accept. These are outcomes, not a menu of reasoning methods. Do not keep vague “improve docs” entries or defer every hard judgment to implementation.

Whole-file deletion remains Fahrenheit's jurisdiction unless it is the already-proved tail of a constructive transfer or consolidation. Source comments and duplicate fragments may be removed directly when their truth has a lawful owner.

### 6. Close The Frontier

Continue until:

- every in-scope surface and material obligation is covered
- every durable truth has one proposed canonical owner
- required audiences and exported contracts have adequate surfaces
- material contradictions are resolved or explicitly blocked
- duplicated and stranded truth has a disposition
- examples and cross-references have a verification path
- no open frontier could materially change the documentary model or change program

Absence is a valid judgment. Do not create documentation solely to fill a category or satisfy the visual symmetry of a report.

### 7. Report, Then Optionally Execute

Write a complete concordance report from the folds. Stop there unless execution was explicit.

When authorized, implement the program in ownership order: establish receiving surfaces before deleting old truth, then repair dependents and navigation. Edit documentation and source commentary only; do not smuggle behavioral refactors or public-API changes into the campaign. Recheck source identity before mutation and withhold changes whose authority has drifted.

Run the repository's documentary verification: documentation builds, doc tests, examples, links, references, formatting, and applicable lints or schema checks. Choose checks from the actual project. Verification supports semantic inspection; it does not replace it. Finish with a residual census and ownership fold over the changed surface.

## Embedded Forms

### Run State

```text
mode: concordance_report | execute_after_report
repository:
source_identity:
scope:
documentary_envelope:
applicable_doctrine:
worklog_path:
report_path:
context_line_ceiling: 3000
context_byte_ceiling: 131072

surface_census:
obligation_atlas:
ownership_map:
clique_cover:
clique_reductions:
fold_hierarchy:
change_program:
contradictions:
high_severity:
frontier:
root_documentary_model:
implementation:
verification:
residual:
```

### Ownership Ledger

```text
| truth_or_obligation | audience | present_owner | terminal_owner | ownership_delta | authority | evidence | coverage |
|---------------------|----------|---------------|----------------|-----------------|-----------|----------|----------|
```

### Concordance Report

```markdown
# Chronicler Concordance Report: <scope>

## Executive Judgment
## Documentary Envelope
## Coverage And Reduction
## Canonical Ownership Model
## Missing Documentation
## Stale, Duplicated, And Misplaced Truth
## Public API And Source Commentary
## Change Program
## Authority Conflicts And Blockers
## High-Severity Register
## Verification Program
## Residual Unknowns

### Complete Ownership Ledger

| obligation | present owner | terminal owner | ownership delta | evidence | dependencies |
|------------|---------------|----------------|-----------------|----------|--------------|
```
