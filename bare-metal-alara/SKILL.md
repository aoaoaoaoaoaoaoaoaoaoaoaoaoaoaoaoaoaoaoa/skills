---
name: bare-metal-alara
description: "Use when a standalone, evidence-driven wallclock optimization campaign is wanted: lock a falsifiable performance claim and its envelope, keep a resumable /tmp ledger, pursue the highest-leverage causal gains, verify behavior, and stop at the economic frontier."
---

# Bare Metal ALARA

Drive the authoritative end-to-end wallclock runtime of the agreed workload As Low As Reasonably Achievable.

ALARA is neither local performance cleanup nor optimization at any price. Lock the claim, preserve its envelope, pursue the steepest credible reductions in runtime, and stop where the remaining gain no longer pays for the structure required to obtain it.

Reason over the whole causal execution path, and change only the authorized surface. Existing decomposition, implementation details, and compatibility survive only when the envelope requires them.

Your supervisor is whoever assigned the campaign: the user, or the agent that delegated it.

## Lock the claim

Before editing, establish which execution is being made faster, what observable behavior must survive, what measurement adjudicates changes, and which specialization or resource constraints apply.

Derive the claim from your supervisor's explicit intent and the repository's evidence. Ask your supervisor only when materially different plausible readings would change the campaign; never optimize a guessed claim.

The benchmark is an instrument for the claim, not the claim itself. Use the smallest measurement design that honestly distinguishes gains from noise, and add repetitions, controls, corroborating workloads, or secondary metrics only when uncertainty requires them.

Never improve the score by silently narrowing the agreed workload, weakening its semantic or generality obligations, or moving work outside the measured boundary.

A correctness oracle is evidence for the envelope, not its definition. When a transformation crosses a blind spot the oracle was meant to cover, strengthen the oracle for that intent before trusting the result. Extending the oracle beyond its original scope, with new workloads, metrics, or correctness properties, revises the claim; ask your supervisor.

## Open the ledger

Once the claim is locked, create the ledger before the first campaign measurement or source edit:

```text
/tmp/bare-metal-alara-<repo-or-dir>-<campaign-slug>.md
```

Resume an existing ledger only when it records the same claim and source lineage; otherwise choose a distinct campaign slug.

Use this shape:

```text
ledger_path:

claim:
  target:
  score_workload:
  metric:
  envelope:
  mutation_authority:
  specialization_and_resource_constraints:
  measurement_contract:

source_identity:
baseline:

incumbent:
causal_model:
frontier:

experiments:

final_verification:
closure:
```

The ledger has three layers:

- **Frozen contract:** `claim`, the initial `source_identity`, and `baseline`. Log any authorized revision instead of silently rewriting history.
- **Mutable head:** `incumbent`, `causal_model`, and `frontier`. Keep them current so that another model can resume without reconstructing the campaign from old experiments.
- **Append-only evidence:** `experiments`. Preserve unfavorable and falsifying results.

`source_identity` anchors the source, binary, toolchain, and measurement context behind the baseline, including where measurements ran. `incumbent` records the same identity for the current accepted state. When the environment drifts enough to invalidate direct comparison, including a change in where measurements run, open a named measurement epoch or establish a fresh control; never splice incompatible numbers together.

`causal_model` is the current concise account of where runtime goes and why. `frontier` holds the strongest live hypotheses, blockers, and unresolved measurement questions.

The ledger is the resumable state of the campaign; chat is only a summary.

## Establish the baseline

Before the first measurement, find the host's measurement policy: agent instructions, or a doctrine they name, that govern where measured or sustained work runs, such as a Slurm partition or a benchmark queue. Run every measured experiment under it, including quick exploratory timings. Without such a policy, measure locally and control noise through the measurement design.

Before changing source, establish that the baseline satisfies the strongest practical correctness evidence for the affected behavior, and measure it under the locked claim. If a full oracle is prohibitively expensive, run a credible targeted check and record the deferred final gate.

Capture enough source, binary, workload, and environment identity to keep later comparisons honest. If the score is unstable, improve the measurement design or use a contemporaneous control before optimizing; never pass off drift as progress.

Use whatever causal evidence best resolves the current uncertainty; no profiler, counter, or form of experiment is mandatory. Update the causal model and frontier as evidence changes them.

## Attack the dominant cost

Pursue the largest credible reductions in authoritative end-to-end runtime first. Eliminating work, improving asymptotics, and choosing better representations come before narrower tuning when they dominate it.

This is an ordering principle, not a hierarchy of tactics. Specialized, generated, platform-specific, or `unsafe` machinery is welcome when its measured payoff justifies its lasting complexity and proof burden. Judge the residue left in the system, not the apparent difficulty or conventionality of the edit.

Any layer of the implementation is admissible within the envelope and the mutation authority. Do not polish a visible local hotspot while a larger causal lever remains.

Treat memory and other secondary resources according to the claim. Measure them when they constrain the workload, explain wallclock, or could invalidate a candidate. Trading memory for time is valid when the envelope permits it; memory work is not a side campaign by ritual.

## Run causal experiments

Record every experiment whose result changes code, the incumbent, the causal model, or the frontier. Routine navigation, compilation, and measurement commands belong in the evidence of their enclosing experiment, not in rows of their own.

Each row tests one causal thesis, which may require a coherent batch of mechanically inseparable edits.

```text
id:
thesis:
evidence:
intervention:
comparison:
semantic_result:
resource_effects:
disposition:
consequence:
```

`comparison` records the adjudication that was actually valid: before and after, an interleaved control, a counterfactual binary, a mechanical count, or another honest design. Reference named baselines and epochs instead of duplicating them.

`disposition` states what happened, without a fixed set of verdicts. `consequence` states how the result changes the incumbent, causal model, and frontier. Mark provisional changes explicitly. Never erase a failed experiment.

Promote a candidate into the incumbent only after appropriate semantic adjudication and credible performance evidence. After a structural win, recheck the authoritative score and the causal model; yesterday's ranking of hotspots is not today's.

## Stop at the economic frontier

After each meaningful gain, remeasure and reconsider the remaining frontier. Stop when the plausible residual improvement is small relative to the permanent complexity, proof burden, fragility, or expected useful lifetime of the optimized code.

Continue into the tail when the remaining move is cheap, durable, or operationally valuable. Do not stop merely because the next move is difficult or unconventional.

Code expected to change soon discounts bespoke tail machinery heavily. Conversely, a small gain may be worth taking when it is nearly free, broadly shared, or multiplied across an important workload.

## Verify and close

Behavior preservation beats speed. Run the relevant oracle whenever a candidate enters the incumbent. A strengthened oracle may be temporary, such as a differential check against the baseline binary; remove temporary checks at close, and keep only tests that earn a permanent place.

At the close of the campaign, run the strongest proportionate verification for the changed causal surface, then re-establish the final score against a still-valid baseline or control.

Closure records:

- the final incumbent and source identity
- the baseline, final measurement, and speedup
- the authoritative measurement and correctness commands
- the final causal model and the kept transformations
- important falsified or rejected avenues
- material resource effects
- the residual frontier, with the economic reason each live avenue stopped, was deferred, or remained blocked

In the final response, report the ledger path and summarize the closure instead of reproducing the ledger.
