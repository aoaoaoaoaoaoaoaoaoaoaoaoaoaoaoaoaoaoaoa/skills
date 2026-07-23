---
name: majestic-magisteria
description: Reconcile a project's semantic representation topology. Use when Codex should exhaustively trace domain concepts across types, schemas, conversions, identifiers, state encodings, boundary projections, and subsystem dialects; establish one canonical owner and lawful representation family for each concept; and produce or explicitly execute a dependency-ordered canonicalization program.
---

# Majestic Magisteria

## Mandate

Make the project speak one semantic language.

The fixed point is:

> Every domain concept has one precise name, one canonical owner, and one lawful representation family. Alternate forms survive only because a distinct law, phase, ownership regime, representation need, or real boundary requires them; every conversion either refines knowledge or crosses such a boundary.

This is not a campaign for fewer types. A concept may lawfully require a validated form, a borrowed view, phase-specific states, or an external projection. Nor is structural similarity proof of identity. The target is global concordance: no rival local ontology, mirrored declaration, conversion pinball, stringly shadow model, or repeated field bundle should exist merely because work once occurred in separate context.

Default to `concordance_report`. Change code only when the user explicitly requests execution, and only after the complete report exists.

## Scope And Envelope

For a project-wide request, cover the complete data model. Build a hierarchy if necessary; do not silently replace “the data model” with one convenient or high-leverage region. For a named concept or semantic region, follow it through the entire project, across module, crate, process, persistence, and protocol boundaries. A directory is neither a reasoning boundary nor proof of a bounded context.

The model includes whatever the project uses to name, distinguish, store, validate, transport, and transform domain meaning. Declarations are only its most visible part. Constructors, conversion paths, schemas, discriminators, units, state machines, serialization shapes, repeated argument or field bundles, and conventions encoded in primitives may all reveal competing representations.

Freeze supported behavior and the outer public contract unless the user separately authorizes change. If concordance demands a contract break, specify it as a blocked major-version move rather than hiding it inside cleanup. Internal compatibility has no independent claim to survival.

Documentation is evidence and may acquire obligations from the new topology, but documentary authorship belongs to Chronicler. Record those obligations as handoffs rather than rewriting or resurrecting prose under this skill. Honor any current Fahrenheit or Chronicler dispositions supplied with the run.

Read repository instructions and applicable style doctrine before designing the canonical model. Load product doctrine when a representation governs persistence, configuration, identity, lifecycle, or other user-system conduct. Use the language at full power. Traits, generics, macros, associated types, phantom distinctions, generated projections, and similarly strong machinery are first-class when they reduce independent truths or make laws inexpressible to violate.

## Semantic Law

Treat names, shapes, conversion traffic, construction sites, validation, and change history as evidence about concepts, not as verdicts.

Two representations belong to one family when they purport to denote the same thing under the same law. Two superficially identical shapes remain distinct when substituting one for the other would erase a real invariant, phase, unit, authority, ownership condition, or domain meaning. Conversely, different storage layouts do not establish different concepts.

A surviving alternate form must state why it exists, who owns it, which laws differ from the canonical form, and where translation occurs. Boundary projections should terminate at the boundary. Phase transitions should be directed. Validation and normalization should have one owner. Lossy conversions must expose the loss; fallible conversions must expose failure; identity conversions should vanish.

Canonicalization may yield one nominal type, a generic family, an algebra of composable distinctions, a phase ladder, a canonical owned form with views, generated projections, or the erasure of a type that never carried a law. Do not prescribe the answer before the project's semantics are known.

A new nominal form earns its place by owning a real law or eliminating repeated semantic handling. Do not answer every weak primitive with a wrapper, or build a parallel internal ontology whose compatibility adapters outweigh the rivals it removes. When a frozen public surface makes the de novo model expensive, distinguish temporary boundary baggage from the terminal topology and expose any major-version cut that would retire it.

Judge the result by semantic description length: fewer independent definitions of the same truth, fewer synchronization obligations, fewer unlawful states and conversion paths, and a clearer direction from authority to projection. Local line count and familiarity carry no independent weight.

## Protocol

### 0. Open The Run

When writes are available, create resumable state before deep reading:

```text
/tmp/majestic-magisteria-<repo>-<scope>-<run-id>.md
/tmp/majestic-magisteria-<repo>-<scope>-<run-id>-report.md
```

Record mode, source identity, semantic scope, frozen envelope, applicable doctrine, context budget, model manifest, representation atlas, clique cover, reductions, fold hierarchy, canonical topology, change program, contradictions, verification, and frontier. The worklog preserves global orientation; the report owns the final argument. If all writes are forbidden, carry the same state into the final response and mark the run nonresumable.

### 1. Lock The Model Manifest And Budget

Use cheap whole-project discovery to locate model-bearing source, schemas, persistence and wire definitions, configuration contracts, generated interfaces, and construction or conversion hubs. For project-wide scope, account for every handwritten model-bearing declaration or encoded domain distinction. For named scope, account for every representation and material use of that concept wherever it travels.

Keep generated, vendored, and external definitions in an evidence fringe unless they are themselves authorized targets. Record why apparently relevant regions are excluded. The manifest may be corrected when evidence reveals an omission, but never narrowed merely to make the audit tractable.

Run a cheap `wc -l -c` preflight. Use these default circuit breakers for all raw material entering one deep-reading clique:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. Count source, schemas, tests, history, dependency code, generated material, and command output when their contents enter working context. Broad indexes and narrow semantic probes may range widely; large search output is a deep read. Split oversized sources by coherent symbols or ranges whose union covers their model-bearing contents.

### 2. Seed An Adaptive Semantic Clique Cover

Group declarations, constructors, conversions, schemas, validation, persistence, protocols, and consumers into overlapping cliques that resolve coherent questions of conceptual identity and ownership under budget. Let the project's ontology and conversion graph determine the cover. For a large whole-project audit, first form bounded ontology branches and reconcile them hierarchically.

Every manifest entry must belong to at least one planned clique. Split, merge, overlap, or replace cliques as the true concepts become visible. Do not use arbitrary directory batches or manufacture cliques merely to reset the context budget.

### 3. Read And Reduce

For each clique, recover the domain concepts being represented, the laws each form enforces, the canonical and de facto owners, the construction and conversion directions, and the boundaries or lifecycle transitions that might justify multiplicity. Follow references far enough to judge meaning, not merely shape.

Before opening another clique, reduce the current one into the smallest durable semantic account another intelligent model can integrate without rereading its sources. Preserve the concept map, representations, laws, conversion edges, ownership judgment, candidate topology, evidence anchors, cross-clique dependencies, counterevidence, and open frontier. A symbol is not covered because it appeared in an index or was opened briefly.

Do not force a finding. A representation family that is already lawful is a substantive result. When later evidence changes conceptual identity, amend or supersede the affected reduction before proceeding.

If a catastrophic defect appears, record it separately and continue coverage. Discovery does not authorize remediation, generic cleanup, or abandonment of the model audit.

### 4. Fold The Ontology Hierarchically

Fold related clique reductions into bounded branch syntheses, then use bounded bridge reductions wherever a concept, conversion, or owner crosses branches. Continue until one project- or region-level representation topology remains.

Higher folds consume reductions, not raw sources. The same context ceilings govern fold inputs; introduce another level rather than flooding one global pass. A fold must materially compress its inputs while preserving evidence and unresolved conflicts.

Use folds to rectify names, reconcile apparent synonyms and homonyms, choose canonical owners, expose false boundaries, and establish the direction of projection. Reopen raw evidence only to resolve a material conflict or uncertainty.

### 5. Design The Canonical Topology

Give every in-scope representation an explicit place in the proposed model: canonical owner, lawful alternate form, boundary projection, phase distinction, view, derivation, or removal. These are possible semantic roles, not a closed classification scheme.

For every proposed contraction or distinction, state the governing law. Specify target owners and shapes precisely enough to expose whether the proposal actually centralizes truth. Define construction, validation, transition, and projection paths; name obsolete conversions and shadow representations that disappear. Preserve a boundary only when its semantic or operational necessity is evidenced.

Account for the net topology after migration. A proposal that adds canonical types without converging internal consumers, deleting rival authority, or bounding compatibility forms is not canonicalization.

Turn the topology into a dependency-ordered change program. Establish canonical owners before migrating consumers; move laws with ownership; collapse mediation and conversion barnacles after their callers have crossed; remove duplicate validation and obsolete representations only when no semantic obligation remains stranded.

Do not expand into general implementation contraction. Adjacent code lesions may be recorded, but Exterminate Slop owns their audit unless repairing them is inseparable from representation concordance.

### 6. Close The Frontier

Continue until:

- every manifest entry is covered
- every concept has a precise proposed name and canonical owner
- every alternate representation has a stated distinct law or a removal path
- construction, validation, conversion, phase transition, and boundary directions are coherent
- cross-branch synonyms, homonyms, and rival owners are reconciled
- public-contract breaks are isolated behind explicit authorization
- no open frontier could materially change the canonical topology or change program

Do not equate exhaustive coverage with compulsory findings. A clean ontology branch may survive intact.

### 7. Report, Then Optionally Execute

Write a complete concordance report from the folds. Stop there unless execution was explicit.

When authorized, recheck source identity and execute the program in semantic dependency order. Preserve the frozen envelope. Use the project's own verification contract, then add structural checks that demonstrate concordance: obsolete declarations and identity conversions gone, validation centralized, boundary projections contained, direct construction routed through canonical owners, and serialization or persistence compatibility proved where required.

Finish with a residual manifest and bounded fold over the changed topology. Report remaining alternate forms and the law that justifies each.

## Embedded Forms

### Run State

```text
mode: concordance_report | execute_after_report
repository:
source_identity:
scope:
frozen_envelope:
applicable_doctrine:
worklog_path:
report_path:
context_line_ceiling: 3000
context_byte_ceiling: 131072

model_manifest:
evidence_fringe:
representation_atlas:
conversion_graph:
clique_cover:
clique_reductions:
fold_hierarchy:
canonical_topology:
change_program:
contradictions:
high_severity:
frontier:
execution:
verification:
residual:
```

### Representation Ledger

```text
| concept | current_representations | current_owners | governing_laws | conversions | judgment | proposed_topology | evidence | coverage |
|---------|-------------------------|----------------|----------------|-------------|----------|-------------------|----------|----------|
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

concepts_and_laws:
representation_topology:
ownership_and_conversion_judgment:
candidate_canonical_shape:
counterevidence:
cross_clique_dependencies:
frontier:
supersedes:
```

### Concordance Report

```markdown
# Majestic Magisteria Concordance Report: <scope>

## Executive Judgment
## Semantic Scope And Frozen Envelope
## Coverage And Reduction
## Current Representation Topology
## Canonical Model
## Lawful Boundaries And Alternate Forms
## Accidental Rival Ontologies
## Conversion And Ownership Corrections
## Dependency-Ordered Change Program
## Contract Breaks Requiring Authorization
## High-Severity Register
## Verification Program
## Residual Unknowns

### Complete Representation Ledger

| concept | current forms | proposed owner and family | judgment | evidence | dependencies |
|---------|---------------|---------------------------|----------|----------|--------------|
```

## Hard Failures

- do not silently narrow a project-wide data-model request
- do not stop at declaration shapes or naming similarity
- do not preserve rival models because each is locally plausible
- do not collapse representations with genuinely different laws
- do not force every concept into tiny atoms, a god type, or any preconceived shape
- do not leave validation, normalization, or authority smeared across owners
- do not preserve identity conversion traffic as architectural decoupling
- do not let boundary projections leak inward or become rival domain models
- do not hide a public-contract break inside canonicalization
- do not turn the campaign into generic cleanup
- do not exceed context or fold budgets through indexing or evidence loopholes
- do not turn the worklog into a shadow report
- do not edit before the complete report or without explicit execution authority
