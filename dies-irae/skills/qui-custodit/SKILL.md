---
name: qui-custodit
description: Rectify a project's verification architecture into the smallest sufficient, stratified basis of executable evidence. Use when Codex should recover semantic obligations, map how they can fail across static, local, generative, integration, boundary, and end-to-end strata, add missing witnesses, strengthen weak oracles, and delete or consolidate redundant, ghost, Potemkin, flaky, slow, or obsolete tests. Defaults to a complete report; executes test changes only when explicitly requested.
---

# Qui Custodit

## Mandate

Construct the smallest sufficient basis `B` of executable evidence for the project's frozen semantic envelope `E`, such that `B ⊨ E`.

The objective is neither more tests nor fewer tests. It is a verification architecture in which every material obligation has credible evidence, every witness has a unique purpose, and the combined basis wastes as little semantic machinery, runtime, nondeterminism, and maintenance as possible.

Treat the existing suite as historical evidence, not as the specification. Recover the obligations de novo from present product contracts, behavior, code, types, protocols, persistence, configuration, documentation, and history. None is automatically sovereign. Do not canonize an implementation accident merely because a test already asserts it.

Default to `evidence_report`. Edit tests or test machinery only when the user explicitly requests execution, and only after the complete report exists.

## Scope And Authority

For a project-wide request, cover the complete obligation/evidence topology. For a named feature, subsystem, contract, or test subtree, follow its obligations and witnesses across the entire project. A test directory is a mutation boundary, not a reasoning boundary.

Freeze supported behavior and public contracts unless separately authorized. When code, prose, tests, and apparent intent disagree, expose the authority decision instead of writing a regression test that silently chooses a winner.

Executable evidence includes static enforcement, compile-time proofs, focused examples, generative properties and models, component and boundary trials, end-to-end product exercises, fixtures, goldens, and verification tooling insofar as they actually witness an obligation. This is a repertoire, not a checklist. Documentation may establish the obligation; prose alone does not discharge it.

A configured lint, test command, or policy is an intended witness, not accomplished evidence, unless the canonical verification path actually enforces it. An observed passing run witnesses one source identity and environment; it does not make future enforcement self-proving.

Under `execute_after_report`, authorization covers test code, test-only modules, fixtures, harnesses, snapshots, and verification configuration. It does not authorize production behavior or architecture changes. If a lawful witness requires a production seam or refactor, specify that dependency and stop there unless the user separately authorizes it.

## Proof Topology

Reason in two dimensions:

- horizontally, which semantic obligations are witnessed
- vertically, at which realization strata each obligation can fail

Static guarantees, unit examples, properties or models, integration contracts, boundary sentinels, and end-to-end trials are different instruments in this topology, not mandatory levels or target ratios. Choose the thinnest combination whose distinct fault models close the obligation. One witness may subsume many weaker cases; one obligation may require several strata because assembly can violate a law that its local implementation satisfies.

Do not fill cells for symmetry. An empty cell is correct when another witness truly subsumes it or that stratum introduces no distinct risk. It is a defect when the cell was simply never considered.

### Generative Evidence

Actively search finite example clusters for the algebra, invariant, metamorphic relation, or transition law that generates them. Where an independent oracle exists, let a property or model own the surrounding input space and retain distinguished examples only when they carry semantic landmarks, boundary cases, or valuable regression identities.

Property testing is not randomized example inflation. The property must state a real law; its generator must range over the honest domain; and its oracle must not reproduce the implementation under test. A discovered counterexample should usually strengthen the general law and may remain as a named seed, not accrete as a disconnected barnacle.

### End-To-End Evidence

End-to-end tests are sparse sovereign witnesses that the assembled product exists as promised. They exercise real entrypoints, wiring, persistence, lifecycle, packaging, recovery, or external conduct to the extent required by the proposition. Calling internal functions through an expensive harness is not end to end.

Treat the total absence of assembled evidence from a product with material assembly behavior as a live gap, not a neutral default. Do not, however, force every obligation through the whole stack. End-to-end breadth is expensive and diagnostically coarse; use it where lower strata cannot witness composition.

## Evidentiary Standard

A witness earns its place by the obligations and fault modes that would become materially less protected if it vanished. Green status, age, line coverage, bug folklore, and familiarity confer no independent value.

Judge evidence by semantic force, oracle independence, fault-model reach, diagnostic locality, determinism, execution cost, and maintenance burden. Coverage, mutation analysis, fuzzing telemetry, runtime measurements, and history are sensors, not verdicts. Use them when they can change the topology; do not perform them ceremonially.

Tests whose oracle merely copies defaults, constants, mappings, schemas, snapshots, mock choreography, or implementation logic are Potemkin evidence. Delete or replace them unless the duplicated shape is itself an external compatibility contract. A regression survives when the underlying risk or law remains live, not merely because a bug once existed.

## Protocol

### 0. Open The Run

When writes are available, create resumable state before deep reading:

```text
/tmp/qui-custodit-<repo>-<scope>-<run-id>.md
/tmp/qui-custodit-<repo>-<scope>-<run-id>-report.md
```

Create a companion `-high-severity.md` register only if a qualifying defect appears.

Record mode, source identity, scope, frozen envelope, applicable doctrine, context budget, evidence manifest, obligation atlas, proof topology, reductions, fold hierarchy, proposed basis, change program, verification, and frontier. The worklog preserves orientation; the report owns the final argument. If all writes are forbidden, carry the same state into the final response and mark the run nonresumable.

### 1. Lock The Evidence Manifest And Budget

Discover test sources, compile-time assertions, fixtures, snapshots, goldens, test-only generators and helpers, harnesses, runner configuration, and commands broadly. Record static enforcement that may discharge obligations. Keep production code, documentation, history, dependencies, and external systems in an authority fringe unless they are themselves authorized evidence artifacts.

For project-wide scope, every evidence artifact must be accounted for. For named scope, include every witness that claims or materially overlaps the target obligations, wherever it lives. Record generated, vendored, legal, and machine-consumed artifacts by role before excluding them.

Exhaustiveness attaches to obligations and actual evidence, not to every tracked file. A binary, asset, document, operational file, or generated artifact enters the evidence manifest only when a verification path consumes it, it serves as an oracle or fixture, or it independently witnesses a material claim. Everything else remains outside the census unless needed as authority fringe.

Run a cheap `wc -l -c` preflight over file-backed evidence. Use these default circuit breakers for all raw material entering one deep-reading clique:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. Count evidence artifacts and all authority material when their contents enter working context. Broad indexes, test listings, and narrow semantic probes may range widely; voluminous output is a deep read. Split oversized sources into coherent symbol or range slices.

Record the canonical verification commands and, when allowed and proportionate, baseline health and runtime. A read-only environment or unavailable runner does not block a report-only audit.

### 2. Build The Obligation Atlas

Recover the frozen semantic envelope before using the existing suite to define it. Identify the material laws, capabilities, boundaries, failure semantics, compatibility promises, and nonfunctional commitments that require evidence. Let the system reveal its own ontology; do not march through a universal test-category catalogue.

For each obligation, identify the strata at which it can fail and its present witnesses, if any. For each existing witness, identify the obligation and fault model it uniquely protects. Mark authority conflicts rather than resolving them by test-writing fiat.

The atlas is semantic, not a line-coverage inventory. Trivial implementation statements do not become obligations merely because they are executable.

### 3. Seed An Adaptive Semantic Clique Cover

Group obligations, present evidence, governed implementation, and relevant boundaries into overlapping cliques that resolve coherent verification questions under budget. Let semantic relationships and shared fault models determine the cover, not test-file adjacency or a fixed layer procession.

Every in-scope evidence artifact and material obligation must belong to at least one planned clique. Split, merge, overlap, or replace cliques as the proof topology becomes clearer. Do not manufacture cliques to reset the context budget.

### 4. Read And Reduce

For each clique, determine what is actually promised, how it can fail, what each witness proves, what its oracle depends on, and whether another witness subsumes it. Inspect governed code and boundaries only far enough to establish those judgments.

Seek both absence and excess: missing laws, untested fault strata, weak or circular oracles, gaps hidden by mocks, duplicated examples, cross-layer repetition, ghosts, barnacles, flakes, heavyweight scaffolds, and opportunities for stronger generative or assembled evidence. These are possible discoveries, not a mandatory smell pass.

Before opening another clique, reduce the current one into the smallest durable account another intelligent model can integrate without rereading its raw material. Preserve obligations, failure strata, present witnesses, evidentiary judgments, candidate basis, authority conflicts, evidence anchors, dependencies, and frontier. Merely listing or running tests does not constitute coverage.

If a credible catastrophic product defect appears, record it immediately in the high-severity register and continue the audit. Discovery does not authorize product rectification or abandonment of evidence coverage.

### 5. Fold The Evidence Hierarchically

Fold related clique reductions into bounded branch syntheses, then use bridge reductions to reconcile obligations or witnesses that cross branches. Continue until one project- or region-level evidence thesis remains.

Higher folds consume reductions rather than raw sources. The same context ceilings govern fold inputs; introduce another level instead of flooding a global pass. A fold must materially compress its inputs while preserving authority conflicts, evidence anchors, and open gaps.

Use folds to detect evidentiary subsumption, vertical holes, horizontally duplicated witnesses, and fixtures or harnesses whose cost is amortized across genuine obligations. Do not call two tests duplicates merely because they exercise the same headline behavior at different fault strata.

### 6. Design The Minimum Sufficient Basis

Specify the target evidence topology and a dependency-ordered change program precise enough to execute without repeating the audit. Each change must name the obligations and failure strata it closes, the canonical witness and independent oracle, present evidence retained or retired, authority, implementation shape, cost implications, dependencies, and verification.

Choose actions freely from the evidence. Tests may be accepted, generalized, reconstructed, split, fused, moved, retired, or newly created; stronger static enforcement or a production-seam handoff may supersede dynamic evidence. These are outcomes, not a closed method menu.

Preserve named examples that clarify a law or pin a valuable counterexample. Remove tests with no unique contribution. Do not consolidate into opaque mega-tests, bury distinct failures in giant parameter tables, or replace diagnostic local evidence with one heroic end-to-end scenario.

Do not estimate or target a retention fraction. Additions and deletions follow only from the complete obligation ledger and evidentiary subsumption.

### 7. Close The Frontier

Continue until:

- every in-scope evidence artifact is covered
- every material obligation has a credible proposed witness or an explicit authority blocker
- relevant failure strata have been considered rather than assumed away
- every surviving witness has a unique contribution to the basis
- generative opportunities and assembled-product gaps have been adjudicated
- authority conflicts, flakes, and unverifiable claims have a disposition
- no open frontier could materially change the proposed basis or change program

Clean areas and intentionally empty cells are valid results. Do not manufacture tests to decorate the report.

### 8. Report, Then Optionally Execute

Write the complete evidence report from the folds. Stop there unless execution was explicit.

When authorized, recheck source identity and establish the baseline verification state before mutation. Execute in evidence-dependency order: create receiving or stronger witnesses before deleting weaker ones; keep counterexamples until the general law demonstrably captures them; and repair harnesses before judging tests that depend on them.

Modify only authorized evidence surfaces. Run focused checks as the basis changes, then the complete verification contract. Use coverage, mutation, fuzzing, and runtime comparison only where they answer a live uncertainty. Finish with a residual atlas and fold proving that the final basis still closes the frozen envelope.

## Embedded Forms

### Run State

```text
mode: evidence_report | execute_after_report
repository:
source_identity:
scope:
frozen_envelope:
applicable_doctrine:
worklog_path:
report_path:
high_severity_path: none
context_line_ceiling: 3000
context_byte_ceiling: 131072

evidence_manifest:
authority_fringe:
obligation_atlas:
proof_topology:
clique_cover:
clique_reductions:
fold_hierarchy:
present_basis:
proposed_basis:
change_program:
authority_conflicts:
frontier:
execution:
verification:
residual:
```

### Obligation And Evidence Ledger

```text
| obligation | authority | failure_strata | present_witnesses | unique_contribution | judgment | proposed_basis | cost | evidence | coverage |
|------------|-----------|----------------|-------------------|---------------------|----------|----------------|------|----------|----------|
```

### Clique Reduction

```text
clique_id:
purpose:
evidence_set:
authority_fringe:
evidence_lines:
evidence_bytes:
coverage_delta:

obligations_and_failure_strata:
present_witnesses:
evidentiary_judgment:
candidate_basis:
authority_conflicts:
cross_clique_dependencies:
frontier:
supersedes:
```

### Evidence Report

```markdown
# Qui Custodit Evidence Report: <scope>

## Executive Judgment
## Frozen Semantic Envelope
## Coverage And Reduction
## Present Evidence Topology
## Proposed Minimum Basis
## Missing And Weak Evidence
## Redundant And Misplaced Evidence
## Generative Evidence
## Integration And End-To-End Evidence
## Dependency-Ordered Change Program
## Authority Conflicts And Blockers
## High-Severity Register
## Verification Program
## Residual Unknowns

### Complete Obligation And Evidence Ledger

| obligation | failure strata | present witnesses | proposed basis | judgment | evidence | dependencies |
|------------|----------------|-------------------|----------------|----------|----------|--------------|
```

## Hard Failures

- do not infer the semantic envelope from the current tests alone
- do not sample a project-wide evidence topology
- do not optimize for test count, line coverage, mutation score, or layer ratios
- do not fill every proof-topology cell by ritual
- do not remain trapped at the unit-example stratum
- do not call randomized examples property testing without a real law and independent oracle
- do not call an expensive internal-call harness end to end
- do not duplicate implementation logic in the oracle
- do not preserve ghosts, barnacles, flakes, or Potemkin evidence because they are green
- do not delete a witness until its unique obligation and fault model are accounted for
- do not replace local diagnostic evidence with opaque mega-tests
- do not let alarming defects derail coverage or authorize product changes
- do not mutate production behavior or architecture under test-only authorization
- do not exceed context or fold budgets through runner output or authority evidence
- do not turn the worklog into a shadow report
- do not edit before the complete report or without explicit execution authority
