---
name: testing-year-zero
description: Rebuild an incumbent test suite from a blank-page admission standard. Use when Codex should audit, consolidate, or replace a whole test suite or bounded cohort without granting existing tests incumbency credit; derive a sparse, cost-justified evidence basis first, then retain, fuse, replace, or delete accordingly. Defaults to a complete read-only report; executes test changes and bounded behavior- and performance-preserving testability refactors only when explicitly authorized.
---

# Testing Year Zero

Load `$unit-test-doctrine` before proceeding. It is normative for unit-test
judgments. This skill extends its discipline to the incumbent suite as a whole;
it does not weaken or reinterpret it.

## Reset The Prior

Stop before reading the suite test by test.

You have been trained and rewarded to write tests, preserve tests, and produce a
regression test after every change. In this task that prior is hostile. You must
acknowledge it and actively resist it. Your fluency at inventing a bug that a
test could catch is not evidence that the test deserves to exist.

Proceed as if the user had come within a hair's breadth of ordering the entire
suite deleted and rebuilt from scratch. Mentally delete the suite first. Derive
what you would build today. Only then may incumbent tests petition for
readmission. Recover unique information before physically deleting its last
carrier.

## Preserve The Product

Freeze the supported product behavior and public contracts before changing
evidence. Tests are not automatically authorities merely because they assert
something. Resolve conflicts against specifications, product behavior, types,
callers, and explicit user intent.

Production behavior is outside the edit boundary unless separately authorized.

## Design From Nothing

Before deeply mining incumbent tests, identify the durable semantic joints,
nontrivial interactions, and credible mistakes a capable implementer working
from fresh context could make.

Then decide which of those risks merit permanent executable evidence. Do not
turn the risk inventory into a coverage checklist. A material behavior may
remain untested when a test would not earn its total cost. Most code should not
receive a unit test. A sparse or nearly empty target suite is a valid result.

The objective is the smallest cost-justified basis, not complete behavioral
enumeration.

## Admission

A candidate test should answer these questions convincingly:

1. Would you select it if the current suite and the motivating diff had never
   existed?
2. Does it protect a durable proposition rather than an implementation detail,
   visual constant, constructor receipt, or historical accident?
3. Is the protected error both credible and meaningfully harmful?
4. Is the oracle independent enough to reject a wrong implementation rather
   than repeat its reasoning?
5. Does it contribute something not already established more cheaply?
6. Is its expected value greater than its execution, compilation, maintenance,
   review, fixture, flake, and context costs?

Failure to make an affirmative case means retirement. “It could catch a bug” is
nearly vacuous; almost any assertion could.

## Regressions

A fixed bug does not acquire hereditary title to a test.

The relevant question is recurrence under intelligent clean-room
reimplementation. A severe one-off typo may deserve no regression test. A
modest but non-obvious ambiguity that a fresh implementer could plausibly
misread may deserve one.

Nontrivial bugs are strong candidates, not automatic admissions. An admitted
unit regression should explain the subtlety or false model that made the error
repeatable. Do not preserve a test merely as a receipt proving that a past patch
once happened.

## Select Evidence

Prefer types, construction rules, static checks, or a smaller boundary witness
when they establish the same proposition more cheaply.

Look for properties that compress broad behavior into a durable law with an
independent oracle. Do not disguise randomized examples or implementation
recalculation as property testing.

Use end-to-end tests sparingly for failures that exist only in assembled
reality. Preserve intermediate witnesses only when they establish an
independent law or materially improve fault localization. Do not obey a test
pyramid, coverage target, or retention ratio as ritual.

Coverage, mutation analysis, fuzzing, history, runtime, and flake telemetry are
sensors. They can challenge a basis or reveal a blind region; none is a verdict.
A snapshot or golden earns its place only when it records an independently
specified semantic artifact or compatibility surface.

## Mine The Incumbent Suite

Treat the existing suite as a quarry, not an inheritance.

Read it by semantic cohort. Recover unique contracts, adversarial cases, and
valuable oracles before deleting their carriers. Classify each cohort as
retained, fused, strengthened, replaced, or retired.

Judge the target suite relationally. A test can be sound in isolation and still
be globally redundant. Conversely, final-output coverage does not subsume an
independent stage law merely because both traverse the same code.

Apply the same austerity to fixtures, helpers, snapshots, harnesses, and
test-only dependencies. Machinery must earn rent too.

## Authority

Default to `year_zero_report`. Change the repository only under explicit
`execute_after_report` authority and only after the report is complete.

Execution authority covers test surfaces and the bounded production refactors
permitted below. It does not authorize changes to business logic, product
behavior, public contracts, or performance.

Read repository instructions and load the applicable style and product
doctrines. A configured command is intended enforcement, not accomplished
evidence, unless the canonical path actually runs it.

## Let Tests Improve The Code

Good testing discipline exerts useful pressure on production design. When an
admitted witness is difficult to express because decisions, effects, state, or
ownership are needlessly entangled, treat that friction as architectural
evidence. Do not truncate the feedback loop by forcing the witness through a
grotesque harness or by declaring all production refactoring out of scope.

Under `execute_after_report`, refactor production code when the target basis
reveals a better testable structure. The refactor must be bounded by the testing
obstruction and preserve both behavior and the relevant performance envelope.
Its scope ends where the obstruction ends.

Testability does not independently justify abstraction. Do not add public
surface solely for tests, ship test conditionals, introduce indirection by
reflex, or distort ownership to accommodate mocks. The resulting structure must
be sound production design even without the test.

The refactor bears the burden of equivalence. Establish behavioral preservation
against the frozen product and its authorities. Measure before and after when
the touched path is performance-sensitive or a regression is otherwise
plausible. If behavior or performance cannot be preserved, the work is a
business-logic or optimization change and requires separate authority.

## Protocol

### 0. Open The Run

When writes are available, create resumable state before deep reading:

```text
/tmp/testing-year-zero-<repo>-<scope>-<run-id>.md
/tmp/testing-year-zero-<repo>-<scope>-<run-id>-report.md
```

Create a companion `-high-severity.md` only if a qualifying product defect
appears. The worklog owns source identity, scope, decisions, evidence, and
frontier; the report owns the argument. If writes are forbidden, carry the same
state into the final response and mark the run nonresumable.

### 1. Freeze The Question

Record source identity, mode, scope, frozen product behavior, authorities,
exclusions, applicable doctrine, canonical commands, and experimental budget.
Resolve material authority conflicts or mark them as blockers.

Locate the incumbent evidence broadly without reading it test by test or
letting its taxonomy seed the design. Establish its extent, rough cost, and
location.

### 2. Build The Blank-Page Basis

Derive the durable semantic joints, credible clean-room errors, and material
consequences while holding the incumbent suite at arm's length. Apply the
admission law to decide which risks warrant witnesses. Record consciously
unwitnessed risks when they matter to the final judgment.

Sketch a provisional basis of mutually supporting witnesses with independent
oracles and useful failure locality. This is a hypothesis. Incumbent evidence or
targeted experiments may expose a forgotten risk, a cheaper witness, or a
necessary independent cross-check.

### 3. Decompose Semantically

Group related laws, implementation, boundaries, and candidate evidence into
semantic cohorts. Follow shared laws and fault models, not test-file adjacency.
Use hierarchical folds when the scope is too large for one synthesis.

Preflight material with `wc -l -c`. These default ceilings govern raw contents
admitted to one cohort or fold:

```text
context_line_ceiling: 3000
context_byte_ceiling: 131072
```

Either ceiling trips the budget. Split oversized sources into coherent semantic
or symbol slices. Higher folds consume reductions, not the raw corpus.

### 4. Adjudicate The Incumbent Suite

Map incumbent evidence onto the provisional basis by semantic cohort, shared
oracle, fixture family, or generated pattern. Deep-read only witnesses that may
carry unique information, expose an anomaly, represent a cohort, or determine a
disposition.

Every in-scope artifact must receive a disposition, but a justified cohort
disposition is sufficient. Artifact-complete accounting does not require
artifact-complete exegesis. History and named regressions describe possible
fault models; they grant no hereditary title.

Reduce each cohort before opening another. Preserve its laws, credible errors,
incumbent contribution, candidate basis, authority conflicts, evidence anchors,
dependencies, confidence, and frontier. A test listing or green run is not a
reduction.

### 5. Challenge The Basis

Experiment only where the result can alter the proposed basis. Useful probes
may include a representative wrong change, historical replay, mutation
analysis, generated inputs, boundary perturbation, coverage inspection,
repeated runs, or cost measurement. Choose according to the uncertainty; do not
perform a ceremony.

Record command, environment, result, and interpretation. A read-only environment
or unavailable runner limits confidence but does not block a report.

### 6. Synthesize And Report

Rebuild the target basis in light of the incumbent suite, then map every cohort
as retained, strengthened, fused, replaced, or retired. Prefer one honest law
over a thicket of examples. Preserve independent corroboration only where
different machinery can fail separately.

Do not consolidate into opaque mega-tests or giant tables that bury distinct
failures. Specify a dependency-ordered change program that identifies each
target witness, oracle, incumbent migration, expected basis delta, dependencies,
and cost consequences.

Lead the report with the target basis and highest-value changes, not an archive
tour. Include the executive judgment, cohort dispositions, migration or deletion
program, authority blockers, consciously unwitnessed material risks, residual
uncertainty, and evidence anchors. Stop unless execution was explicit.

### 7. Execute

Recheck source identity and baseline state. Establish a receiving witness before
retiring unique evidence only when the target basis actually admits that
witness. Do not manufacture a replacement merely because something is being
deleted.

Modify only authorized evidence surfaces and bounded testability refactors. Run
focused checks as the basis changes, then the canonical project gate. Report
test counts, line reductions, coverage, mutation scores, and runtime changes
only as consequences.

## Completion

Stop when the target basis is stable, every incumbent cohort has a disposition,
every survivor has a distinct reason to exist, material consciously unwitnessed
risks are honest, and further reading is unlikely to change the result.

Completion does not require a test for every behavior, risk, requirement, bug,
or changed line. Do not manufacture witnesses to fill empty cells.

The final suite should look as though it was designed today by someone who knew
that permanent tests are liabilities as well as evidence.

## Run State

```text
mode: year_zero_report | execute_after_report
repository:
source_identity:
scope:
frozen_product:
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

semantic_cohorts:
target_basis:
consciously_unwitnessed_risks:
incumbent_dispositions:
change_program:
testability_refactors:
authority_conflicts:
residual_uncertainty:
frontier:
execution:
verification:
```

## Cohort Reduction

```text
cohort:
question:
raw_lines:
raw_bytes:
durable_laws:
credible_clean_room_errors:
material_consequences:
candidate_witnesses:
incumbent_contribution:
disposition:
authority_conflicts:
dependencies:
confidence:
anchors:
frontier:
```

## Hard Failures

- do not derive the target basis from the incumbent suite
- do not turn the risk inventory into a requirement that every risk have a test
- do not preserve a test because it is green, old, named, or could catch a bug
- do not add a test merely because behavior changed or a bug was fixed
- do not judge the suite as a bag of isolated test cases
- do not optimize for test count, line coverage, mutation score, or layer ratios
- do not duplicate implementation logic in an oracle
- do not call randomized examples property testing without a law and independent
  oracle
- do not call an expensive internal-call harness end to end
- do not preserve ghosts, flakes, change receipts, or Potemkin evidence
- do not retire a witness before recovering its unique semantic information
- do not erase useful epistemic independence in the name of deduplication
- do not claim exhaustive semantic proof from an ordinary finite suite
- do not let an alarming product defect authorize unrelated product repair
- do not mutate production behavior under test-only authority
- do not refuse a bounded testability refactor merely because it touches
  production code
- do not use testability as cover for business-logic changes, performance
  regressions, or unbounded cleanup
- do not distort production architecture for mocks or test-only access
- do not exceed context budgets through raw sources, runner output, or global
  folds
- do not turn the worklog or report into compulsory form-filling
- do not edit before the complete report or without explicit execution authority
