---
name: qui-custodit
description: Re-zero a project's verification architecture into the smallest risk-adequate basis of executable evidence. Use when Codex should derive what must be proved independently of the incumbent suite, design the target evidence topology, then salvage, strengthen, consolidate, or retire existing tests against it. Defaults to a complete read-only report; changes tests only when explicitly authorized.
---

# Qui Custodit

## Mandate

Reconstruct the verification architecture as if it were being designed today for the project's frozen semantic envelope. Derive the required evidence before studying the incumbent suite in depth. Existing tests are quarry: they may contain excellent witnesses, buried contracts, and valuable regressions, but their present shape has no presumption of necessity.

Seek the smallest risk-adequate basis of executable evidence. It should reject credible materially wrong implementations, remain green under lawful rewrites, localize failures well enough to act on them, and cost no more to run and maintain than its evidentiary contribution warrants.

This is not a quest for more tests, fewer tests, or individually immaculate tests. Quality is relational. A witness earns existence when removing it would admit a material fault, destroy useful epistemic independence, or materially impair diagnosis. Several locally good tests may form a globally poor suite; apparent duplication may be necessary when independent mechanisms can fail separately.

No finite ordinary suite proves the whole semantic envelope. Do not write `B ⊨ E` unless `B` contains an actual proof system that justifies the claim. Treat sufficiency as a risk-bearing engineering judgment, state its residual uncertainty, and make that judgment falsifiable.

Default to `evidence_report`. Change tests or test machinery only under explicit execution authority and only after the report is complete.

## Scope And Authority

For project-wide scope, cover the complete obligation topology. For a named feature, subsystem, contract, or test subtree, follow its obligations and witnesses wherever they lead. A test directory is a mutation boundary, not a reasoning boundary.

Freeze supported behavior and public contracts unless separately authorized. Recover authority from present contracts, behavior, code, types, protocols, persistence, configuration, documentation, and history; none is automatically sovereign. When these disagree, expose the authority decision instead of letting an old assertion choose silently.

Executable evidence includes any mechanism that can independently reject a material violation: static enforcement, proofs, focused examples, generated laws, models, component or boundary trials, product exercises, fixtures, goldens, and verification tooling. These are possible instruments, not required layers. Documentation may establish an obligation; prose alone does not discharge it.

A configured command is intended enforcement, not accomplished evidence, unless the canonical path actually runs it. One green execution witnesses one source identity and environment, not permanent enforcement.

Under `execute_after_report`, authorization covers test code, test-only modules, fixtures, harnesses, snapshots, and verification configuration. It does not authorize production behavior or architecture changes. If the right witness requires a production seam or refactor, specify the dependency and stop unless separately authorized.

Read repository instructions. Load product doctrine when it establishes obligations in the frozen envelope, and the applicable style doctrine before judging or changing verification code.

## Evidentiary Standard

Judge the basis through two counterfactuals:

1. If an implementation violated the obligation in a credible material way, which evidence would reject it, and why?
2. If the implementation were lawfully replaced while preserving the obligation, would that evidence remain green?

The first detects weakness; the second detects implementation capture. The target basis balances fault discrimination, oracle independence, diagnostic locality, determinism, execution cost, and maintenance burden.

Reason across both semantic breadth and realization depth. An obligation may fail in its local rule, composition, boundary projection, lifecycle, or assembled product. Choose only the strata with distinct fault models. Do not fill a testing pyramid, grid, or ratio by ritual; an empty stratum is correct when no distinct risk lives there.

Intermediate artifacts are not automatically implementation detail. When a stage has an independently specified semantic law, distinct failure modes, or materially better diagnostic locality, give it its own witness. Final-output parity does not subsume that witness merely because later machinery could compensate for an earlier error.

Search clusters of examples for the law that generates them. A property is valuable when it states a real invariant, metamorphic relation, or model correspondence over an honest domain and uses an oracle that does not reproduce the implementation. Randomized examples without such a law are not property testing. A discovered counterexample may remain as a named landmark, but should not become a barnacle when the general law owns it.

Use end-to-end evidence sparingly for propositions created by assembly: real entrypoints, wiring, persistence, lifecycle, packaging, recovery, or external conduct. Calling internal functions through an expensive harness is not end to end. Conversely, a product with material assembly behavior and no assembled witness has an evidentiary hole.

Coverage, mutation analysis, fuzzing, history, runtime, and flake telemetry are sensors. They can challenge a basis or reveal a blind region; none is a verdict. A witness whose oracle merely recopies implementation logic, defaults, constants, mappings, schema, or mock choreography is Potemkin evidence. A snapshot or golden earns its place when it records an independently specified semantic artifact or compatibility surface, not incidental structure.

## Protocol

### 0. Open The Run

When writes are available, create resumable state before deep reading:

```text
/tmp/qui-custodit-<repo>-<scope>-<run-id>.md
/tmp/qui-custodit-<repo>-<scope>-<run-id>-report.md
```

Create a companion `-high-severity.md` only if a qualifying product defect appears. The worklog preserves source identity, scope, decisions, evidence, and frontier; the report owns the argument. If all writes are forbidden, carry the same state into the final response and mark the run nonresumable.

### 1. Freeze The Question

Record the source identity, mode, scope, semantic envelope, authorities, explicit exclusions, applicable doctrine, canonical verification commands, and available experimental budget. Resolve material authority conflicts or mark them as blockers.

Locate the incumbent evidence broadly, but do not read it test by test and do not let its taxonomy seed the design. At this stage it is enough to know its extent, rough cost, and where it lives.

### 2. Design From The Blank Page

With the incumbent suite held at arm's length, derive the material obligations and credible ways each could be violated. State propositions at the level a lawful replacement must preserve, not at the level of current functions or branches.

Sketch the provisional target basis: the fewest mutually supporting witnesses that would discriminate those violations with independent oracles and useful failure locality. Let the system reveal its natural evidence topology. Do not march through a universal category catalogue.

This provisional basis is a hypothesis, not a decree. Later evidence may expose a forgotten obligation, a cheaper witness, or a necessary independent cross-check.

### 3. Decompose Semantically

Group related obligations, governed implementation, boundaries, and candidate evidence into overlapping semantic cliques. Clique boundaries follow shared laws and fault models, not test-file adjacency. Build a hierarchy of folds when the scope is too large for one global synthesis.

Run a cheap `wc -l -c` preflight over material before deep reading. These default ceilings govern the raw contents admitted to one clique or fold:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. Broad indexes, symbol listings, and narrow probes may range widely; voluminous output is a deep read. Split oversized sources into coherent semantic or symbol slices. Higher folds consume reductions, not the raw corpus.

### 4. Mine The Incumbent Suite

Now inventory existing evidence and map it onto the provisional basis. Work by semantic cohort, shared oracle, fixture family, or generated pattern. Deep-read the witnesses that may carry unique information, expose an anomaly, represent a cohort, or determine a disposition. Do not serially exegete every test merely because it exists.

Every in-scope evidence artifact must ultimately receive a disposition, but a justified cohort disposition is sufficient. Artifact-complete accounting does not require artifact-complete deep reading. Generated and mechanically uniform families should remain families unless a member materially differs.

For each cohort, recover any semantic truth it alone contains before proposing retirement. History and named regressions are evidence about fault models, not hereditary titles to test cases.

Reduce each clique before opening another. Preserve obligations, credible violations, incumbent contribution, candidate basis, authority conflicts, evidence anchors, dependencies, confidence, and frontier. A test listing or green run is not a reduction.

If a credible catastrophic product defect appears, record it immediately in the high-severity register and continue. Discovery does not authorize product repair or abandonment of the audit.

### 5. Challenge The Basis

Use targeted observation or experiment only where it can change the proposed architecture. Possible challenges include making a representative wrong change, replaying a historical defect, mutation analysis, generated inputs, boundary perturbation, coverage inspection, repeated runs, or cost measurement. Choose freely; do not perform a ceremony.

Distinguish source evidence from experimental evidence, and record commands, environment, result, and interpretation. Honor repository resource controls and avoid destabilizing unrelated workloads. A read-only environment or unavailable runner limits confidence but does not block a report.

### 6. Synthesize The Target

Fold clique reductions into one evidence thesis. Rebuild the target basis in light of what the incumbent suite taught you, then map each incumbent cohort as retained, strengthened, fused, subsumed, replaced, or retired.

Prefer one stronger law or differential witness over a thicket of examples when it honestly owns their space. Retain examples that mark a boundary, communicate a contract, localize a failure, or preserve a counterexample not subsumed by the stronger witness. Preserve independent corroboration where different machinery can violate the same obligation.

Do not retire an intermediate-stage witness as subsumed by terminal parity unless the terminal witness rejects that stage's material faults without relying on compensating downstream behavior, or the stage law is intentionally dissolved under proper authority.

Do not consolidate into opaque mega-tests, giant tables that bury distinct failures, or one heroic end-to-end scenario. Do not target a retention fraction, line count, coverage score, mutation score, or layer ratio. Additions and deletions follow from obligations, credible fault models, and evidentiary subsumption.

Specify a dependency-ordered change program precise enough to execute without repeating the audit. Each change should identify the obligation and fault model, target witness and oracle, incumbent migration, expected basis delta, dependencies, cost consequences, and validation.

### 7. Close The Frontier

Stop when further reading is unlikely to change the target basis or change program, and all of the following hold:

- every material obligation has a credible witness or explicit authority blocker;
- credible failure strata have been considered rather than assumed away;
- every proposed witness has a distinct contribution or justified independent role;
- every incumbent artifact or coherent cohort has a supported disposition;
- weak, circular, flaky, obsolete, and needlessly costly evidence has a disposition;
- residual uncertainty and unperformed validation are explicit.

Clean regions and intentionally empty strata are valid. Do not manufacture work to decorate the report.

### 8. Report, Then Optionally Execute

Lead with the target evidence architecture and the highest-value changes, not an archive tour of the incumbent suite. The report must contain the executive judgment, proposed basis, prioritized defect and change register, incumbent migration or deletion program, authority blockers, residual uncertainty, and evidence anchors. Organize it around the actual findings; do not print empty rubric sections. Append detailed ledgers only when they improve auditability.

Stop after the report unless execution was explicit.

When authorized, recheck source identity and baseline state. Establish receiving or stronger witnesses before deleting weaker ones, and retain counterexamples until the general law demonstrably subsumes them. Modify only authorized evidence surfaces. Run focused checks as the basis changes, then the complete verification contract. Finish with a residual fold showing how the resulting basis covers the frozen envelope.

## Embedded Forms

Use these as durable state, not prose templates.

### Run State

```text
mode: evidence_report | execute_after_report
repository:
source_identity:
scope:
frozen_envelope:
authorities:
exclusions:
applicable_doctrine:
canonical_commands:
experimental_budget:
worklog_path:
report_path:
high_severity_path: none
context_line_ceiling: 3000
context_byte_ceiling: 131072

semantic_cliques:
fold_hierarchy:
target_basis:
incumbent_cohorts:
change_program:
authority_conflicts:
residual_uncertainty:
frontier:
execution:
verification:
```

### Obligation Ledger

```text
| obligation | authority | credible violation | target witness and oracle | incumbent evidence | disposition | confidence | anchors |
|------------|-----------|--------------------|---------------------------|--------------------|-------------|------------|---------|
```

### Cohort Disposition

```text
cohort:
claimed_role:
representative_or_decisive_witnesses:
unique_information:
oracle_and_fault_reach:
target_owner:
disposition:
migration_risk:
anchors:
```

### Clique Reduction

```text
clique_id:
question:
raw_lines:
raw_bytes:
obligations_and_violations:
provisional_target_witnesses:
incumbent_contribution:
cohort_dispositions:
authority_conflicts:
dependencies:
confidence:
frontier:
supersedes:
```

## Hard Failures

- do not derive the target architecture from the incumbent suite
- do not read every test serially before designing the provisional basis
- do not confuse artifact-complete disposition with artifact-complete deep reading
- do not infer the semantic envelope from current assertions alone
- do not judge a suite as a bag of isolated test cases
- do not optimize for test count, line coverage, mutation score, or layer ratios
- do not preserve implementation capture as contract protection
- do not erase an independently specified intermediate seam by treating terminal parity as universal subsumption
- do not duplicate implementation logic in the oracle
- do not call randomized examples property testing without a law and independent oracle
- do not call an expensive internal-call harness end to end
- do not preserve ghosts, barnacles, flakes, or Potemkin evidence because they are green
- do not retire a witness before recovering its unique obligation, fault model, or historical information
- do not erase useful epistemic independence in the name of deduplication
- do not claim exhaustive semantic proof from an ordinary finite suite
- do not let alarming product defects derail coverage or authorize repair
- do not mutate production behavior under test-only authority
- do not exceed context budgets through raw sources, runner output, or global folds
- do not turn the worklog or final report into compulsory form-filling
- do not edit before the complete report or without explicit execution authority
