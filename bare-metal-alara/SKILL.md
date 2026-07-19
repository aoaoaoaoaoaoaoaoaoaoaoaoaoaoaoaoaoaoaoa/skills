---
name: bare-metal-alara
description: "Use when the user wants a standalone, evidence-driven wallclock optimization campaign: lock a falsifiable performance claim and semantic envelope, keep a session-resumable /tmp ledger, pursue the highest-leverage causal gains, verify behavior, and stop at the economic frontier."
---

# Bare Metal ALARA

Drive authoritative end-to-end wallclock runtime for the agreed workload As Low As Reasonably Achievable.

ALARA is neither local performance cleanup nor maximal optimization at any price. Lock the claim, preserve its semantic envelope, pursue the steepest credible runtime gradients, and stop where the remaining gain no longer pays for the structure required to obtain it.

Treat the whole causal execution path as a reasoning surface. Mutate only the authorized surface. Existing decomposition, implementation details, and compatibility survive only when the locked envelope requires them.

## Lock The Claim

Before editing, make precise what execution is being made faster, what observable behavior must survive, what measurement adjudicates changes, and which specialization or resource constraints apply.

Derive the claim from explicit user intent and repository evidence. Ask only when materially different plausible interpretations would change the campaign. Do not optimize a guessed claim.

The benchmark is an instrument for the claim, not the claim itself. Use the smallest measurement design that can honestly distinguish gains from noise. Add repetition, controls, corroborating workloads, or secondary metrics only when uncertainty requires them.

Never improve the score by silently narrowing the agreed workload, weakening its semantic or generality obligations, or moving work outside the measured boundary.

A correctness oracle is evidence for the semantic envelope, not its definition. If a proposed transformation crosses an oracle blind spot, strengthen the oracle before trusting the result.

## Open The Campaign Ledger

Once the claim is locked, create the ledger before the first campaign measurement or source edit:

```text
/tmp/bare-metal-alara-<repo-or-dir>-<campaign-slug>.md
```

Resume an existing ledger only when it represents the same claim and source lineage. Otherwise choose a distinct campaign slug.

Use this shape:

```text
ledger_path:

claim:
  target:
  score_workload:
  metric:
  semantic_envelope:
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

- **Frozen contract:** `claim`, initial `source_identity`, and `baseline`. Log any authorized revision rather than silently rewriting history.
- **Mutable campaign head:** `incumbent`, `causal_model`, and `frontier`. Keep these current so another model can resume without reconstructing the campaign from old experiments.
- **Append-only evidence:** `experiments`. Preserve unfavorable and falsifying results.

`source_identity` anchors the source, binary, toolchain, and measurement context underlying the baseline. `incumbent` records the corresponding identity for the current accepted state. If the environment drifts enough to invalidate direct comparison, open a named measurement epoch or establish a fresh control; do not splice incompatible numbers together.

`causal_model` is the current concise account of where runtime goes and why. `frontier` holds the strongest live hypotheses, blockers, and unresolved measurement questions.

The ledger is session-resumable campaign state. Chat is a summary surface.

## Establish The Baseline

Before changing source, establish that the baseline satisfies the strongest practical correctness evidence for the affected behavior and measure it under the locked contract. If a full oracle is prohibitively expensive, run a credible targeted baseline and record the deferred final gate.

Capture enough source, binary, workload, and environmental identity to make later comparisons honest. If the score is unstable, improve the measurement design or use a contemporaneous control before optimizing. Do not launder drift into progress.

Use whatever causal evidence best resolves the current uncertainty; no profiler, counter, or experimental form is a mandatory rite. Update the causal model and frontier as evidence changes them.

## Attack The Dominant Cost

Pursue the largest credible reductions in authoritative end-to-end runtime first. Prefer eliminating work, improving asymptotics, and choosing better representations when they dominate narrower tuning.

This is an ordering principle, not a tactic hierarchy. Specialized, generated, platform-specific, or unsafe machinery is welcome when its measured payoff justifies its lasting complexity and proof burden. Judge the residue left in the system, not the apparent difficulty or conventionality of the edit.

Any implementation layer is admissible within the semantic envelope and mutation authority. Do not polish a local hotspot merely because it is easy to see when a larger causal lever remains.

Treat memory and other secondary resources according to the locked claim. Measure them when they constrain the workload, explain wallclock, or could invalidate a candidate. Trading memory for time is lawful when the envelope justifies it; memory work is not a ritual side campaign.

## Run Causal Experiments

Record every experiment whose result changes code, the incumbent, the causal model, or the frontier. Routine navigation, compilation, and measurement commands belong in the evidence for their enclosing experiment rather than receiving ceremonial rows.

Use one causal thesis per row. A thesis may require a coherent batch of mechanically inseparable edits.

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

`comparison` records the adjudication that was actually valid: before/after, interleaved control, counterfactual binary, mechanical count, or another honest design. Reference named baselines and epochs instead of duplicating them.

`disposition` states what happened without a closed verdict taxonomy. `consequence` states how the result changes the incumbent, causal model, and frontier. Mark provisional changes explicitly. Never erase a failed experiment.

Promote a candidate into the incumbent only after appropriate semantic adjudication and credible performance evidence. Recheck the authoritative score and causal model after structural wins; yesterday's hotspot hierarchy is not today's.

## Stop At The Economic Frontier

After each meaningful gain, remeasure and reconsider the remaining causal frontier. Stop when the plausible residual improvement is small relative to the permanent complexity, proof burden, fragility, or expected useful lifetime of the optimized code.

Continue into the tail when the remaining move is cheap, durable, or operationally valuable. Do not stop merely because the next move is difficult or unconventional.

Code expected to change soon discounts bespoke tail machinery heavily. Conversely, a small gain may remain reasonable when it is nearly free, broadly shared, or multiplied across an important workload.

## Verify And Close

Behavior preservation beats speed. Run the relevant oracle whenever a candidate enters the incumbent. At campaign close, run the strongest proportionate verification for the changed causal surface, then re-establish the final score against a still-valid baseline or control.

Closure must record:

- final incumbent and source identity
- baseline, final measurement, and speedup
- authoritative measurement and correctness commands
- final causal model and kept transformations
- important falsified or rejected avenues
- material resource effects
- residual frontier and the economic reason each live avenue stopped, deferred, or remained blocked

In the final response, report the ledger path and summarize the closure rather than reproducing the ledger.

Campaign integrity is nonnegotiable: log claim changes, never compare incompatible measurement contexts, never win by hiding work or narrowing semantics, never mutate outside the authorized surface, and never discard unfavorable evidence.
