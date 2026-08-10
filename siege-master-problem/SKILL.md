---
name: siege-master-problem
description: "Run the recurring external-research siege loop for a mathematical master problem: isolate it in a dedicated worktree, map the full strategy tree, ingest one report or adjudicate a parallel salvo holistically, formalize only mathematics that cuts a master obstruction, unify or cull what leaves that path, commit and push each checked ratchet, generate one kill prompt or an orthogonal MIRV portfolio across all promising approaches, and report both the newest wound and the net master frontier. Use when a user supplies research-chat links for formalization, asks for the next Pro attack or several parallel attacks, resumes an agentic mathematics campaign, or warns against losing the target in supporting lemmas."
---

# Siege Master Problem

Keep the master problem, not the supporting theory, as the unit of progress. Convert one external
attack into checked mathematics and a sharper attack until the master problem closes or its live
obstruction changes. The workflow is scaffolding: abandon it immediately when a credible route to
closure appears.

## Divide The Labor

Treat Pro as a read-only pen-and-paper mathematician. It can inspect a public GitHub repository
and reason deeply about the displayed definitions and theorems, but it has no local checkout or
project verification ecosystem: no proof assistant, computer-algebra scripts, exhaustive search,
build feedback, or canonical gate. Never ask it to run local tools, search a worktree, or report
that an artifact has been mechanically verified.

Ground Pro in immutable public GitHub links and inline the few equations or declaration
statements on which the attack turns. Ask for mathematics: exact theorem statements, complete
proofs, derivations, counterexamples, case audits, and a translation-conscious proof skeleton.
It may suggest a formal encoding, but every such suggestion is unverified pseudocode until the
local formalizer reconstructs it.

The local formalizer owns repository search, ontology reconciliation, executable checks, proof-
assistant or computer-algebra work when present, culling, publication, and the final judgment of
what was actually proved. This asymmetry is deliberate. Do not squander Pro's thinking budget on
guessed implementation syntax, and do not lower the mathematical standard merely because it
cannot query the local verifier. A pen-and-paper claim must expose every hypothesis and enough
detail for hostile reconstruction.

## Isolate And Publish Each Ratchet

Bind each master problem to one long-lived dedicated branch and a worktree below the repository's
`.worktrees/` directory. Create or reuse that worktree before changing files; keep the primary
checkout available for coordination and other masters. Never move one master's siege into
another master's worktree merely because its branch is convenient.

Treat one sequentially returned Pro conversation as one publication ratchet. A deliberately
parallel set is one analytical salvo: adjudicate every sibling report as a unit before synthesizing
any of them, then preserve the per-conversation publication cadence described below.

For each publication ratchet:

1. Start from a pushed commit and record its branch and hash in the enemy lock.
2. Ingest, reconstruct, formalize, cull, and reconcile only in the master's worktree.
3. Run the repository's canonical verification gate.
4. Stage only durable survivors. Exclude `/tmp` prompts, transcripts, reports, scratch proofs,
   generated test files, and unrelated changes.
5. Commit the coherent turn on the dedicated branch and push it to the remote Pro can inspect.
6. Verify that the remote branch resolves to the new commit; update the public issue with that
   immutable boundary when the repository uses one.
7. Only then write the next prompt, grounding it in the pushed commit rather than the former
   baseline or an uncommitted local theorem.

Every Pro turn which changes durable mathematical truth receives its own pushed commit. A turn
which rejects an attack may still change durable truth through its audit, culling, or frontier
update and should be committed. Do not manufacture an empty commit when nothing changes; report
that the wound did not move and reuse the prior public commit. If commit or push fails, the cycle
is incomplete: preserve the worktree, state the exact failure, and do not present the next prompt
as ready for Pro.

## Lock The Enemy

Read the repository instructions, master statement, frontier, formalization ledger, salvage
registry, relevant audits, and public issue before accepting the external report's framing.
Reconstruct the exact master, victory condition, smallest live obstruction, and killed lanes. A
transient ledger under `/tmp` may help, but its format is immaterial; use whatever representation
keeps the reasoning honest and compact.

Re-derive this lock after formalization and before writing the next prompt. Rectify names when the
report, repository, and master statement use one noun for different objects.

The master problem has absolute priority over the workflow. If a credible route to closure appears
at any stage, abandon the assigned subproblem, planned literature tour, formalization itinerary,
or intermediate deliverables and pursue the kill. Do not complete scaffolding for its own sake.
This override never relaxes completeness, hypotheses, required converse or soundness directions,
boundary cases, or the verification standard.

Reject random incrementalism. Promote a result only if it does at least one of these:

1. Closes the master problem.
2. Removes a named live obstruction on a stated causal path to closure.
3. Kills or constructs a live attack, thereby changing the frontier.
4. Produces a counterexample that forces a new master-level strategy.
5. Makes the remaining obstruction strictly sharper and mechanically testable.

A supporting lemma without an immediate consuming theorem fails the enemy lock. Do not enlarge
infrastructure merely because the report supplied a plausible lemma.

## Map The Tech Tree

Before synthesizing a returned attack and again before aiming any successor prompt, reconstruct the
master problem's complete current tech tree. Begin at the master statement and map:

1. Exact reductions and corollary relations: which node would close or decide which ancestor.
2. Checked territory, including normal forms and compiler or converse boundaries already complete.
3. Killed lanes and the counterexamples or impossibility theorems which killed them.
4. Every live incomparable fork, its smallest obstruction, and its expected master implication.
5. Claims still merely reported, computational, conditional, or open.

Read this tree net of the whole durable record, not as a chronology of recent conversations.
Collapse aliases, delete superseded formulations, and rectify names. Use the newest report as the
immediate focus, but do not let it erase older live forks or make its local obstruction appear to
be the whole master. A promising route which would fall automatically from a stronger sibling is
not an independent frontier target.

The tree may remain an internal or transient working object unless the repository already owns a
durable frontier representation. Persist only changes in mathematical truth, not a ceremonial
diagram.

## Ingest The Attack

Keep external-model conversations and prompts transient. For a ChatGPT share link, recover the
human transcript and final assistant report with:

```sh
skill=$(readlink -f "${CODEX_HOME:-$HOME/.codex}/skills/siege-master-problem")
"$skill/scripts/extract_shared_chat.py" "$url" --require-final > "/tmp/$slug-transcript.md"
"$skill/scripts/extract_shared_chat.py" "$url" --require-final --last assistant > "/tmp/$slug-report.md"
```

If extraction reports that the share has not reached a final response, the external turn is still
live or was shared mid-turn. Wait for completion and retry; do not adjudicate a progress update as
the report.

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

Audit definitions, quantifiers, implication directions, imported hypotheses, conventions,
degenerate cases, boundary cases, and hidden existence or uniqueness assumptions. Add whatever
domain-specific checks the claim requires. Test small exact instances when they can falsify a
claim. Model authority is no evidence.

## Adjudicate A Parallel Salvo

When several Pro conversations were launched in parallel from the same or nearby boundary, do not
formalize the first answer while its siblings remain unread. First:

1. Recover every transcript and report in the salvo.
2. Reconstruct and classify each report independently against the pre-salvo enemy lock.
3. Review them together against the full tech tree: identify convergence, contradiction, hidden
   shared premises, coordinate duplicates, complementary lemmas, and coverage gaps.
4. Derive the strongest joint synthesis yourself. One report may repair, refute, subsume, or give
   the missing consumer for another; arbitrary return order has no mathematical authority.

This holistic review is a barrier before synthesis, not permission to blur provenance. After the
unit review, formalize in mathematical dependency order. Give each conversation which changes
durable truth its own coherent pushed commit; when a sibling becomes a restatement, rejection, or
corollary of an already committed result, record that disposition without manufacturing an empty
commit. Do not emit the next prompt or prompt portfolio until the entire salvo has been adjudicated
and the net frontier rebuilt.

A credible direct master closure still overrides the workflow. Pursue and verify it immediately,
then audit the remaining reports only as needed to state the final net result honestly.

## Formalize The Survivors

Formalization is a second attack, not transcription. Think from the master statement throughout:
test sharper invariants, reverse implications, remove hypotheses, seek counterexamples, compose
the new claim with the checked frontier, and pursue any shorter kill shot exposed by the proof.
Pro's route has no privilege. Generalize, expand, or replace it when doing so tightens a live
attack; reject its itinerary when it does not.

Adopt a zero-line prior. The ideal amount of new formal machinery is zero. Every surviving theorem,
definition, computation, or formal artifact must be consumed on a causal path to this master
problem or another named master problem already owned by the repository. First try to close the
implication with existing mathematics. After adding formal material, unify duplicate
representations and proofs, inline ceremonial wrappers, and delete artifacts that have fallen off
every master path. Apparent reusability is not a reason to keep them.

State the strongest theorem supported by the proof, not the report's preferred slogan. Reuse the
repository ontology. Introduce a definition only when a live theorem consumes it and the
definition contracts, rather than enlarges, the attack surface. Prefer one theorem that reaches
the obstruction over a ladder of locally pleasant lemmas.

For each candidate artifact, answer before retaining it:

1. Which master and exact live obstruction does this cut?
2. Which checked theorem consumes it now?
3. Can the same cut be made by strengthening or unifying an existing result?
4. What artifact or attack lane becomes deletable if it succeeds?

If those answers are absent, cull it. Keep thinking while local verification runs: a failed proof
or check may show that the claim is false, badly named, over-specialized, or aimed at the wrong
enemy.

Meet the repository's complete verification contract using the strongest medium it owns: a proof
assistant, exact symbolic derivation, exhaustive finite check, independent proof audit, or a
combination. Obey its policies on axioms, proof apertures, warnings, reproducibility, and
publication-facing claims. Run narrow checks while iterating and the canonical gate after
integration.

Record an audit that distinguishes proved claims from rejected and open ones. Update the salvage
registry, frontier, formalization ledger, public issue, and publication only where the checked
result changes their truth. Retire superseded attack lanes instead of accumulating them.

## Measure The Wound

After verification, rebuild the enemy lock from the master statement. Say plainly whether the
master is closed, what the turn removed, the smallest exact obstruction that remains, and the
implication still required for victory. No fixed headings or response schema are required.

Do not describe a collection of new lemmas as “closer” without this causal account. If the live
obstruction did not change, say so and do not let the next prompt celebrate the work as frontier
movement.

## Aim The Next Attack

After the ratchet commit is pushed and remotely visible, write the next external-model prompt or
prompt portfolio under `/tmp`; never commit it. Ground every prompt in that exact public commit or
another externally accessible review surface that Pro can read without a local toolchain. Inline
the attack's critical equations instead of assuming repository navigation can reconstruct all context.
Immutable coordinates establish provenance; they are not an incantation. Give the branch, commit,
and relevant links once. Do not demand a source-lock acknowledgement, force the model to echo or
repeat metadata, or use ritual phrases as a proxy for clear grounding. Ask it to identify an access
gap only when one occurs.

Give every prompt a visible first-line title and matching filename stem of the form
`prompt-<master-slug>-<wave-id>-<two-digit-prompt-id>`. Use the stable master abbreviation already
owned by the project, the pushed baseline's short hash as the default wave ID, and a one-indexed,
zero-padded prompt number within the wave. If multiple waves leave the same commit, append a wave
ordinal to the hash. For example, the first `M₃(4)` prompt from baseline `e656e0d9` is titled
`prompt-m34-e656e0d9-01` and stored as `prompt-m34-e656e0d9-01.md`. Put any descriptive attack name
below this identifier. The identifier is a navigation label for copied conversations, not a ritual
for the external model to repeat.

Map the complete tech tree before choosing the next attack. Generate one prompt when one route
strictly dominates. When several promising incomparable approaches survive, generate a MIRV
portfolio covering all of them. Do not suppress a credible fork merely to preserve a singular
cadence. Include opposing theorem/counterexample lanes and routes which bypass the current local
obstruction when they are genuinely distinct.

One prompt per mathematical route is enough. Do not manufacture diversity through paraphrases,
minor parameter variants, or several prompts sharing the same unproved bottleneck. Parallel
prompts must be independently intelligible, grounded at the same immutable boundary, and free of
dependencies on answers that do not yet exist. Sequence attacks whose inputs genuinely depend on
one another. Treat the returned portfolio as a parallel salvo under the preceding section.

A single prompt should cover the following. In a MIRV portfolio, the portfolio should cover them
collectively while each prompt remains concentrated on its own kill shot:

1. The master problem and the victory condition first.
2. The smallest checked frontier needed for the attack.
3. Killed lanes with an explicit instruction not to revisit them.
4. One primary kill shot aimed at the live obstruction.
5. An opposing constructive or falsification lane when it could decide the strategy.
6. Required audits for known failure modes.
7. An output demand: resolution, decisive obstruction, exact counterexample, or one theorem whose
   stated implication changes the master frontier.

Make the proposed route explicitly subordinate to the master: a direct closure argument overrides
the requested reconnaissance and intermediate tasks.

Demand depth, but do not script a long lemma itinerary. The external model may replace the proposed
attack if it identifies a shorter path to victory; it must explain that path from the master
statement. Prohibit surveys, cosmetic reformulations, unconsumed supporting structures, claims of
having run local verification, and long speculative implementation scripts. Demand pen-and-paper
mathematics detailed enough for the local formalizer to attack and translate.

## Report The Joint Ratchet And Tech Tree

End every formalization turn, including a parallel salvo, with an in-chat précis of what Pro and the
local formalizer jointly accomplished plus a condensed net view of the entire master tech tree. A
durable audit, commit message, issue update, or prompt path does not satisfy this obligation. The
account must stand alone for a user who opens none of those artifacts.

Center the newest turn or salvo, but reconnect it to the master from the top. State, in compact
prose:

1. What substantive idea, proof, or counterexample each relevant Pro report supplied.
2. What formalization independently verified, strengthened, unified, replaced, or rejected.
3. What the new work changed at the master-problem level.
4. The net tech tree: the main reduction route, checked or killed nodes, and every substantively
   live incomparable fork after removing superseded matter.
5. The exact smallest surviving obstruction and the next attack or MIRV portfolio.
6. The pushed branch and commit, plus every transient prompt path generated.

Convey the verdict, removed obstruction, surviving obstruction, and remaining implication without
disguising an open problem as progress. Mention culled or rejected claims when they delimit the
result. For a parallel salvo, explain its consensus, contradictions, and joint consequence rather
than narrating chats in arrival order. Present the tech tree as present mathematical truth, not an
ever-growing diary. Keep the account shorter than the underlying audit: it reports the ratchet and
strategic topology, not a file-by-file change log.
