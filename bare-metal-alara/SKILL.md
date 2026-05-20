---
name: bare-metal-alara
description: "Use when the user wants a standalone Bare Metal ALARA performance pass: lock the workload and correctness oracle, create a /tmp optimization ledger, profile, optimize, verify behavior, and drive wallclock runtime as low as reasonably achievable without semantic drift or gratuitous uglification."
---

# Bare Metal ALARA

Bring the specified implementation's wallclock runtime As Low As Reasonably Achievable for the agreed workload while preserving existing business behavior and public contracts. Use measurement and profiling to discover the true limiting structure, then reshape code, data, and algorithms freely when the result is materially faster and not gratuitously contorted.

## Lock The Target

Before optimizing, identify:

- target implementation surface
- representative workload
- benchmark command or measurement method
- primary performance metric, defaulting to wallclock runtime
- correctness oracle
- scope boundary
- forbidden tradeoffs, if any

Inspect enough of the repo to find likely commands and surfaces. If any material uncertainty remains about the workload, input distribution, correctness oracle, public contract, benchmark command, or forbidden tradeoff, explicitly ask the user to clarify. Do not optimize a guessed workload.

## Create The Ledger

Before the first optimization edit, create one persistent ledger:

```text
/tmp/bare-metal-alara-<repo-or-dir>-<target-slug>.md
```

Use this shape:

```text
ledger_path:
target:
scope:
workload:
metric:
correctness_oracle:
benchmark_command:
constraints:

environment:
baseline:
profile_summary:

experiment_ledger:

verification:
final_measurement:
speedup:
residual_opportunities:
```

The ledger is the durable campaign state. Chat is summary only. If interrupted or resumed, reopen the same ledger before continuing.

## Baseline

Run the correctness oracle first if cheap. Then establish a baseline for the agreed workload. Capture the exact command, inputs, environment facts that matter, and enough repeated measurements to distinguish a real gain from noise.

If the benchmark is unstable, improve the measurement harness before optimizing. Do not launder noise into progress.

## Profile

Use the standard profiler, tracer, benchmark harness, flamegraph, allocation tool, query planner, runtime instrumentation, or language-specific equivalent appropriate to the target. Do not rewrite from vibes when profiling is practical.

The point of profiling is not ritual. The point is to find the current limiting structure: algorithm, representation, allocation, layout, dispatch, I/O, synchronization, cache behavior, parsing, serialization, query shape, or benchmark harness overhead.

## Experiment Loop

For each optimization attempt, append a ledger row:

```text
id:
hypothesis:
evidence:
planned_change:
risk:
pre_measurement:
edit_summary:
correctness_result:
post_measurement:
decision: keep | revert | revise | superseded
next:
```

Prefer one hypothesis per experiment unless several changes are mechanically inseparable. Keep changes that materially improve the agreed metric without semantic drift or disproportionate complexity. Revert or revise changes that do not pay rent.

Continue while evidence or strong mechanical reasoning suggests meaningful runtime remains available at reasonable complexity and risk. Stop when remaining plausible gains require semantic change, ungrounded workload assumptions, unacceptable fragility, unsafe or unjustified low-level tricks, platform contortions, or noise-scale wins.

## Reasonable Means Ruthless, Not Reckless

Low-level code is allowed. Algorithmic change is allowed. Data representation change is allowed. API reshaping inside the scoped implementation is allowed unless the user froze compatibility.

Gratuitous cleverness is not allowed. Benchmark gaming is not allowed. Semantic drift is not allowed. Hidden global state, precision loss, lossy approximation, concurrency hazards, cache invalidation traps, and platform-specific contortions require explicit justification and usually explicit user permission.

Unsafe code is not forbidden in principle, but it is never a casual move. Exhaust ordinary representation, algorithmic, allocation, traversal, and runtime-configuration wins first unless the project is already an unsafe or low-level domain.

## Verification

After each kept batch, run the correctness oracle and remeasure. After the final batch, run the narrowest meaningful full verification for the touched surface, then widen if the optimization crosses module, package, crate, service, or runtime boundaries.

Behavior preservation beats speed. Wallclock performance on the agreed workload is the primary score. Secondary metrics explain the result; they do not replace it.

## Final Response

Always include:

- `/tmp` ledger path
- target and workload
- baseline measurement
- final measurement and speedup
- benchmark and correctness commands used
- main profiling evidence
- kept optimization batches
- reverted or rejected experiments, if important
- residual opportunities judged unreasonable or out of scope

## Hard Failure Modes

- do not optimize a guessed workload
- do not skip the `/tmp` ledger
- do not report speedups without baseline and final measurements
- do not treat passing tests as proof of performance
- do not treat faster benchmarks as permission for semantic drift
- do not hide unfavorable experiments
- do not preserve compatibility by default when compatibility is the bottleneck
