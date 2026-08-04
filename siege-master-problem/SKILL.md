---
name: siege-master-problem
description: "Run the recurring external-research siege loop for a mathematical master problem: ingest a shared ChatGPT or Pro conversation, attack its claims independently against the live repository, formalize only mathematics that cuts a master obstruction, unify or cull what leaves that path, measure the exact wound, and generate the next kill-oriented prompt. Use when a user supplies a research-chat link for formalization, asks for the next Pro attack, resumes an agentic mathematics campaign, or warns against losing the target in supporting lemmas."
---

# Siege Master Problem

Keep the master problem, not the supporting theory, as the unit of progress. Convert one external
attack into checked mathematics and a sharper attack until the master problem closes or its live
obstruction changes.

## Lock The Enemy

Read the repository instructions, master statement, frontier, formalization ledger, salvage
registry, relevant audits, and public issue before accepting the external report's framing. Write
a transient ledger under `/tmp` containing:

```text
MASTER: exact theorem or decision problem
VICTORY: proof artifact that closes it
LIVE OBSTRUCTION: smallest missing implication or construction
KILLED LANES: routes the checked corpus has excluded
```

Re-derive this lock after formalization and before writing the next prompt. Rectify names when the
report, repository, and master statement use one noun for different objects.

Reject random incrementalism. Promote a result only if it does at least one of these:

1. Closes the master problem.
2. Removes a named live obstruction on a stated causal path to closure.
3. Kills or constructs a live attack, thereby changing the frontier.
4. Produces a counterexample that forces a new master-level strategy.
5. Makes the remaining obstruction strictly sharper and mechanically testable.

A supporting lemma without an immediate consuming theorem fails the enemy lock. Do not enlarge
infrastructure merely because the report supplied a plausible lemma.

## Ingest The Attack

Keep external-model conversations and prompts transient. For a ChatGPT share link, recover the
human transcript and final assistant report with:

```sh
skill=$(readlink -f "${CODEX_HOME:-$HOME/.codex}/skills/siege-master-problem")
"$skill/scripts/extract_shared_chat.py" "$url" > "/tmp/$slug-transcript.md"
"$skill/scripts/extract_shared_chat.py" "$url" --last assistant > "/tmp/$slug-report.md"
```

Never commit the raw transcript or report. Preserve only independently reconstructed results,
counterexamples, and bounded audit evidence. If the report relies on papers, invoke the local
reference-corpus workflow before retrieving them.

Treat every external claim as a conjecture. Reconstruct it from current definitions and inspect
all cited repository artifacts. Classify each material claim as:

- `promotion`: new, correct, formalizable, and passes the enemy lock;
- `restatement`: already checked or only a change of coordinates;
- `salvage`: correct and reusable, but does not alter the live master obstruction;
- `rejected`: false, vacuous, ill-scoped, or dependent on an unproved premise;
- `open`: plausible but still missing a proof obligation.

Audit signs, multiplication order, quantifiers, primitivity, nonzero branches, divisibility
multiplicity, boundary states, and imported hypotheses. Test small exact instances when they can
falsify a claim. Model authority is no evidence.

## Formalize The Survivors

Formalization is a second attack, not transcription. Think from the master statement throughout:
test sharper invariants, reverse implications, remove hypotheses, seek counterexamples, compose
the new claim with the checked frontier, and pursue any shorter kill shot exposed by the proof.
Pro's route has no privilege. Generalize, expand, or replace it when doing so tightens a live
attack; reject its itinerary when it does not.

Adopt a zero-line prior. The ideal amount of new Lean is zero. Every surviving declaration must
be consumed on a causal path to this master problem or another named master problem already owned
by the repository. Before adding code, try to close the implication with existing theorems. After
adding code, unify duplicate representations and proofs, inline ceremonial wrappers, and delete
lemmas or structures that have fallen off every master path. A reusable-looking API is not a
reason to keep it.

State the strongest theorem supported by the proof, not the report's preferred slogan. Reuse the
repository ontology. Introduce a definition only when a live theorem consumes it and the
definition contracts, rather than enlarges, the attack surface. Prefer one theorem that reaches
the obstruction over a ladder of locally pleasant lemmas.

For each candidate declaration, answer before retaining it:

1. Which master and exact live obstruction does this cut?
2. Which checked theorem consumes it now?
3. Can the same cut be made by strengthening or unifying an existing declaration?
4. What code or attack lane becomes deletable if it succeeds?

If those answers are absent, cull it. Keep thinking while the kernel checks: a failed proof may be
evidence that the claim is false, badly named, over-specialized, or aimed at the wrong enemy.

Meet the repository's complete verification contract. In Lean this includes warning-free builds,
default environment linters, reviewed transitive axiom snapshots, disabled automatic implicit
variables, and no proof apertures or suppressions. Add every publication-facing declaration to
the axiom audit. Run the narrow build while iterating and the canonical gate after integration.

Record an audit that distinguishes proved claims from rejected and open ones. Update the salvage
registry, frontier, formalization ledger, public issue, and publication only where the checked
result changes their truth. Retire superseded attack lanes instead of accumulating them.

## Measure The Wound

After verification, rebuild the enemy lock from the master statement. State exactly:

```text
MASTER VERDICT: closed / still open
REMOVED: former obstruction or escape mechanism
REMAINS: smallest exact live obstruction
DISTANCE: the implication still required for victory
```

Do not describe a collection of new lemmas as “closer” without this causal account. If the live
obstruction did not change, say so and do not let the next prompt celebrate the work as frontier
movement.

## Aim The Next Attack

Write the next external-model prompt under `/tmp`; never commit it. Ground it in an exact public
commit or another externally accessible review surface. The prompt must contain:

1. The master problem and the victory condition first.
2. The smallest checked frontier needed for the attack.
3. Killed lanes with an explicit instruction not to revisit them.
4. One primary kill shot aimed at the live obstruction.
5. One opposing constructive or falsification lane when it could decide the strategy.
6. Required audits for known failure modes.
7. An output demand: resolution, decisive obstruction, exact counterexample, or one theorem whose
   stated implication changes the master frontier.

Demand depth, but do not script a long lemma itinerary. The external model may replace the proposed
attack if it identifies a shorter path to victory; it must explain that path from the master
statement. Prohibit surveys, cosmetic reformulations, and unconsumed supporting structures.

End the local cycle by reporting the checked artifacts, code unified or culled, master-level
delta, rejected claims, and the path of the transient next prompt.
