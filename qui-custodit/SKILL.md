---
name: qui-custodit
description: "Use when the user wants a whole-project or subtree test-suite consolidation pass: identify duplicate, near-duplicate, redundant, obsolete, ghost, barnacle, slow, or low-value tests; preserve coverage of useful behavior while deleting or consolidating tests that bloat runtime and maintenance cost."
---

# Qui Custodit

Watch the watcher. Purify the test suite. Tests are not sacred. Useful behavioral coverage is sacred.

The enemy is not a failing test. The enemy is a test suite accreted by fear: duplicate assertions, near-identical cases, dead compatibility probes, ghost tests for functionality that no longer exists, barnacle regression tests whose bug is impossible under the current model, and slow scaffolds that spend minutes proving nothing.

## Posture

Start from zero-based skepticism. Every test must justify its continued existence by protecting live behavior, a live invariant, a live boundary, or a live regression risk.

Do not preserve tests because they are old, numerous, familiar, or green. A passing duplicate is still waste. A passing ghost test is worse than waste: it enshrines dead history as law.

The objective is a smaller, sharper suite with equal or better protection of useful logic and lower runtime/maintenance drag.

## Scope

Require a concrete project root or test subtree. If the user names only a repo, choose the narrowest plausible test surface after a quick manifest scan and state the assumption.

Use the project's test runner, language server, coverage tooling, mutation/fuzz/property tools, and source references where available. For Rust, use `cargo test`, `cargo nextest`, `cargo llvm-cov`, and `rust_analyzer` as appropriate.

## Ledger

Create a compact ledger:

```text
/tmp/qui-custodit-<repo>-<scope>.md
```

Use it for durable state:

```text
scope:
test_command:
coverage_oracle:
runtime_baseline:

manifest:
read_waves:
duplicate_clusters:
ghost_tests:
consolidation_plan:
deletions:
verification:
runtime_after:
residual_uncertainty:
```

The ledger is not bureaucracy. It is the spine that prevents "I read a lot of tests" from evaporating into context loss.

## Read Waves

Broad indexing is free. Use `rg`, manifests, test names, assertion text, fixtures, snapshots, parametrization tables, and runner listing commands across the whole scope.

Deep reading is gated. One wave may inspect at most:

- 10 test files, or
- 25 test cases, or
- one coherent fixture/assertion cluster,

whichever comes first.

After each wave, write out:

- duplicate or near-duplicate clusters
- tests whose protected behavior is unclear
- suspected ghosts or barnacles
- fixture/setup duplication
- slow or heavyweight tests
- candidates to consolidate, delete, or keep
- next wave

Do not start another deep-read wave until the ledger has been updated.

## Test Atlas

Build a test atlas for the scope. Capture:

- test file and test case names
- assertions and expected outputs
- fixtures, builders, snapshots, golden files, mocks, containers, generated data
- target source symbols, APIs, CLI commands, or integration boundaries
- parametrized cases and table rows
- slow tests and heavyweight setup
- ignored/skipped/flaky tests
- tests asserting errors, panics, deprecations, removal, or compatibility behavior

Where possible, map each test to the live behavior it protects. A test with no live protected behavior is guilty until proven useful.

## Cluster And Judge

Cluster tests by:

- identical assertions
- identical input/output pairs
- same fixture with tiny variations
- same source symbol or API path
- same bug/regression story
- same snapshot/golden surface
- same panic/error contract
- same setup cost

Classify each cluster:

- `delete_duplicate`: exact or semantic duplicate with no unique protection
- `consolidate_table`: near-duplicates should become one parameterized/table test
- `consolidate_property`: examples are really one invariant/property
- `keep_distinct`: similar tests cover different live laws
- `ghost`: asserts gone, forbidden, deprecated, or impossible functionality
- `barnacle`: historical regression test whose risk is now erased by types, architecture, or removed code
- `boundary_sentinel`: expensive or awkward test is justified because it protects a real boundary
- `needs_user_judgment`: behavior is policy-laden and not inferable from code

The hard question is: what live invariant would become less protected if this test vanished?

## Purification Moves

Prefer deletion when a test has no unique live value.

Preferred moves:

- exact duplicate → delete all but the best-named/best-placed case
- near-duplicate examples → table-driven test
- many examples of one law → property/fuzz/invariant test when cheap and idiomatic
- repeated fixtures → one builder/helper, or inline the trivial setup and delete the helper
- snapshot sprawl → keep only snapshots that expose meaningful external shape
- compatibility ghost → delete with the compatibility shim
- removal/absence ghost → delete unless the absence is a live security/safety invariant
- slow integration clone → keep one boundary sentinel, delete narrower duplicates or replace with unit coverage
- ignored/flaky test → fix, delete, or quarantine explicitly; do not let it rot silently

Do not consolidate into an unreadable mega-test. Consolidation should reduce code and runtime while making the protected invariant clearer.

## Ghost And Barnacle Tests

A ghost test protects behavior that no longer exists or should no longer exist.

A barnacle test protects a historical bug through a path that is now impossible, irrelevant, or covered by a stronger invariant elsewhere.

Delete them aggressively. Exception: an absence can be live behavior when it guards security, authorization, data loss, wire compatibility, or a deliberate product guarantee. In that case rename it as a boundary/safety sentinel so its purpose is unmistakable.

## Execution

Default to a report if the suite is large or the clusters are subtle. Execute directly when the scope is clear and deletions/consolidations are locally verifiable.

Before editing, record baseline runtime when cheap. After editing, run the affected tests, then widen to the relevant suite. If runtime was material, record the delta.

If coverage tooling is available and cheap, use it to ensure deleted tests did not remove the only coverage for live code. Do not worship line coverage; use it as a smoke alarm, not a moral law.

## Verification

A successful pass should show at least one structural win:

- duplicate tests deleted
- near-duplicates consolidated
- ghost/barnacle tests removed
- fixture scaffolding reduced
- snapshots/goldens reduced
- suite runtime reduced
- coverage of live behavior preserved

If a test is deleted, know what live behavior, if any, stopped being tested. If the answer is "nothing," good.

## Final Response

Include:

- ledger path
- scope and test command
- baseline and final runtime when measured
- duplicate clusters found
- ghost/barnacle tests removed
- consolidations performed
- tests deliberately kept despite similarity
- verification result
- residual uncertainty

## Failure Modes

- do not treat tests as sacred
- do not delete legal/security/wire-compatibility sentinels by mistaking them for ghosts
- do not preserve duplicates because they are green
- do not replace many small tests with one opaque mega-test
- do not keep snapshots that only encode churn
- do not let ignored/flaky tests survive unclassified
- do not read endlessly without writing the ledger
- do not call lower line coverage a failure unless live behavior protection actually weakened
