---
name: redline
description: Run a logic-preserving wallclock optimization loop for a named basket of invocations. Use when Codex needs to make a command, workload, or benchmark basket faster by locking measurement, collecting hardware counters, justifying each bottleneck thesis with hard numbers, and iterating until blocked or stopped.
---

# Redline

Use this skill to reduce wallclock for a concrete basket of invocations without changing logic.

This skill is measurement-first. It is not a generic cleanup pass, and it is not a speculative "maybe this is faster" pass.

Language-agnostic, but code-centric.

## Contract

- Require a concrete basket of invocations.
- Require a semantic guard. If the user did not provide one, infer the narrowest credible guard from tests, golden outputs, invariants, or diffable results.
- Default basket weights to `1` unless the user specifies otherwise.
- Create one persistent `/tmp` worklog before the first serious measurement. Chat is summary only; the worklog is the durable source of truth.
- Lock the measurement surface before optimization: commands, inputs, cwd, env, build profile, thread settings, and any relevant runtime knobs.
- Do not begin optimization until the basket and semantic guard are explicit in the worklog.
- Attempt to obtain hardware-countered measurements early. If they are unavailable, record the exact blocker and treat the run as degraded mode.
- Do not run a long blind optimization campaign without either hardware counters or a clear recorded reason why they are unavailable.
- Measure the baseline repeatedly enough to bound noise before making changes.
- Use the current best measured line as the champion. Do not compare against a drifting or remembered baseline.
- Every bottleneck thesis must be justified by hard numbers: timing plus profiling and/or counters.
- Profile before speculative rewrites.
- Work one measured optimization line at a time unless a bundled change is strictly inseparable.
- Re-measure every challenger against the same basket and the same guard.
- Keep only logic-preserving wins and real enablers.
- Do not stop because you found one plausible speedup. Keep pushing until stopped, blocked, or genuinely out of credible next theses.

## Optimization Law

The objective is lower wallclock for the locked basket.

The default scalar decision metric is:

```text
weighted_total_median_ms = sum(weight_i * median_ms_i)
```

Per-item medians still matter. Do not accept a "win" that quietly trashes one basket item unless the user explicitly allows that tradeoff.

A challenger becomes the new champion only if:

- the semantic guard passes
- the wallclock win is credible against observed noise
- the tradeoff pattern is acceptable for the basket
- the thesis is supported by the measured evidence, not just the result

## Flow

### 0. Create the worklog

Create a path shaped like:

```text
/tmp/redline-<repo-or-dir>-<basket-slug>.md
```

Seed it with the embedded worklog skeleton from `Embedded Forms`.

### 1. Lock the basket

Write the exact basket first.

For each basket item, record:

- command
- cwd
- relevant env
- input or scenario
- build profile
- weight
- semantic guard target

Do not optimize an implied basket.

### 2. Lock the measurement harness

Choose the actual measurement tools and parameters before chasing speed.

Prefer:

- repeated wallclock sampling with `hyperfine` or an equivalent harness
- hardware counters with `perf stat` or platform equivalent
- sampled profiling with `perf record`, flamegraph tooling, `pprof`, or equivalent

Record:

- warmup policy
- sample count
- timing metric
- spread metric
- counter set
- profiler choice

If the target is a release workload, do not benchmark debug builds.

### 3. Establish the baseline champion

Measure the untouched line repeatedly enough to estimate noise.

Minimum default:

- at least 1 warmup run per basket item
- at least 9 timed runs per basket item for champion decisions

Record per basket item:

- median wallclock
- spread or noise estimate
- hardware counters if available
- semantic-guard result

If noise is too high to trust decisions, stabilize the harness before optimizing further.

### 4. Profile the champion

Profile the current champion on the basket items that dominate total cost.

Do not start with "obvious" micro-optimizations.
Find where the time, cycles, cache misses, allocations, syscalls, or contention actually live.

The first real bottleneck thesis should come from this data.

### 5. Write the bottleneck thesis

Every optimization line needs a thesis before code changes.

A thesis must name:

- the hotspot or bottleneck site
- the measured evidence
- why this should move wallclock
- which basket items should improve
- which counters or profile signatures should change if the thesis is right

Bad theses:

- "this code looks slow"
- "this alloc seems unnecessary"
- "we should probably inline this"

Good theses are anchored to numbers.

### 6. Execute one optimization line

Make one coherent optimization move.

Typical move classes:

- remove repeated work
- improve data layout or locality
- cut allocations or copies
- reduce parsing or formatting overhead
- reduce locking or contention
- reduce syscall or I/O frequency
- improve algorithmic complexity
- hoist invariant work
- batch expensive operations
- exploit cheaper library or runtime primitives
- remove abstraction overhead when it is actually measured

Do not mix semantic redesign into a speed pass.
If a large architectural move is needed, record that explicitly.

### 7. Re-measure the challenger

Run the same basket, the same harness, and the same semantic guard.

Record:

- challenger timings
- challenger counters
- challenger profile notes if needed
- pass/fail against the thesis

Compare challenger against the current champion, not against memory.

### 8. Decide

Choose exactly one:

- `promote`
- `enabler`
- `reject`
- `rework`
- `blocked`

Use:

- `promote` when the challenger is a credible logic-preserving improvement on the current basket
- `enabler` when the challenger is neutral or near-neutral now but materially unlocks stronger follow-on optimization work
- `reject` when the change loses, is noisy, or fails the guard
- `rework` when the line is promising but the implementation or measurement is not yet trustworthy
- `blocked` when an external constraint prevents meaningful progress

If rejected, revert or otherwise unwind the losing line before starting the next serious experiment.

### 9. Repeat

After every decision:

- update the champion snapshot
- update the candidate queue
- choose the next strongest measured thesis
- keep going

If progress stalls, return to profiling and widen the search rather than polishing a dead line.

## Measurement Discipline

- Use one stable basket definition for the whole run unless the user explicitly changes the objective.
- Keep build profile, env, and thread settings fixed unless changing them is the point of the experiment.
- Do not trust one-shot timings.
- Prefer medians over means for decision-making.
- Record a noise or spread figure for every serious comparison.
- Attempt hardware counters early rather than as an afterthought.
- Prefer the same counter set across champion/challenger comparisons.
- If counters are unavailable because of permissions, virtualization, unsupported PMU access, or host policy, record the exact failure in the worklog.
- Do not cite counters you did not actually collect.
- Do not cite profiler output without cashing it out into a bottleneck thesis.

A bottleneck thesis must cite at least:

- one timing signal
- one profile or counter signal

## Semantic Discipline

Logic preservation is mandatory.

Use the narrowest credible semantic guard that actually protects the behavior under optimization.

Examples:

- targeted tests
- golden-output diffs
- checksum or snapshot comparisons
- invariant checks
- exact response comparisons
- benchmark harnesses with correctness validation

Do not smuggle behavior changes in as performance work.

## Embedded Forms

### Worklog Skeleton

```text
worklog_path:
objective:
scope_root:
mode: audit_plus_refactor
degraded_mode_reason:

measurement_harness:
basket_spec:
semantic_guard:
baseline_champion:
counter_status:
profile_status:
candidate_queue:
experiment_log:
residual_risks:
```

Rules:

- create this file before the first serious measurement
- update it after every real experiment
- treat it as the durable source of truth for the run
- report the final worklog path in the user-facing response

### Basket Spec

```text
| item_id | command | cwd | env_summary | input_or_scenario | build_profile | weight | semantic_guard |
|---------|---------|-----|-------------|-------------------|---------------|--------|----------------|
| B01 | cargo run --release -- solve case1.lp | . | RAYON_NUM_THREADS=1 | case1.lp | release | 1 | compare objective and solution digest |
| B02 | cargo run --release -- solve case2.lp | . | RAYON_NUM_THREADS=1 | case2.lp | release | 2 | compare objective and solution digest |
```

Rules:

- every serious measurement must use this locked basket
- weights default to `1` if unspecified
- if the basket changes, record it explicitly as a new objective surface

### Champion Snapshot

```text
champion_id:
commit_or_worktree_state:
decision_metric: weighted_total_median_ms

per_item:
- item_id: B01
  median_ms:
  spread_pct:
  counters:
    cycles:
    instructions:
    branches:
    branch_misses:
    cache_misses:
  guard: pass
- item_id: B02
  median_ms:
  spread_pct:
  counters:
    cycles:
    instructions:
    branches:
    branch_misses:
    cache_misses:
  guard: pass

weighted_total_median_ms:
notes:
```

Rules:

- keep exactly one current champion
- update this after every promoted line
- if counters are unavailable, say so explicitly instead of leaving them blank without explanation

### Bottleneck Thesis

```text
thesis_id:
hotspot:
affected_basket_items:
timing_evidence:
profile_or_counter_evidence:
expected_change:
planned_move:
risk_to_semantics:
```

Rules:

- do not start a serious optimization line without this
- the evidence must be measured, not aesthetic
- expected change should name what should get better in timing or counters

### Experiment Record

```text
experiment_id:
thesis_id:
change_summary:
semantic_guard_result:
challenger_weighted_total_median_ms:
per_item_deltas:
counter_deltas:
decision: promote | enabler | reject | rework | blocked
decision_reason:
follow_on:
```

Rules:

- one serious optimization line per record
- rejected lines must still be recorded
- if the result is noisy or surprising, say so plainly
- do not mark a change as `enabler` without naming the specific follow-on optimization it unlocks
- do not accumulate long chains of `enabler` changes without cashing them out into measured wins

## Final Response

Always include:

- the `/tmp` worklog path
- locked basket summary
- semantic-guard summary
- champion metric summary
- hardware-counter availability summary
- strongest accepted lines
- strongest rejected or blocked lines
- residual next moves

If you edited code, also include:

- the promoted optimization lines
- verification summary
- any tradeoffs accepted inside the basket

## Hard Failure Modes

- do not optimize before locking the basket
- do not optimize before locking the semantic guard
- do not turn the run into speculative cleanup
- do not trust one-shot timings
- do not compare against a drifting baseline
- do not mix build profiles between champion and challenger
- do not accept "probably faster"
- do not keep a change that fails the semantic guard
- do not make a bottleneck thesis without hard numbers
- do not cite profiler screenshots or flamegraphs as if they were the win itself
- do not run a long campaign without attempting hardware counters
- do not keep multiple half-measured changes live at once
- do not mark a change as `enabler` without a concrete unlocked next move
- do not stop after one plausible win if credible next theses remain
