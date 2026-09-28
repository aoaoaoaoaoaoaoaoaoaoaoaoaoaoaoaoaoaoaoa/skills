---
name: dies-irae
description: "Convene any explicit or inferred subset of the DIES IRAE judges against one case: recover the case's charter, run the judges in parallel and read-only, and compile their reports into one evidence-backed register ordered by priority on a shared severity scale. Under explicit execute authority, run the judges' fixes in dependency order and reconvene until the case reaches its fixed point. Use for a multi-judge project inquest or a comprehensive judgment of a codebase across its domain model, implementation, correctness, tests, documentation, and release fitness."
---

# DIES IRAE

> Cuncta stricte discussurus.

## Mandate

Convene the applicable judges against one case, let each judge its own jurisdiction independently, and compile one judgment. Under explicit `execute` authority, drive the case to its fixed point.

Every artifact bears the burden of its own existence. Models accrete: they add code, types, tests, and prose, and rarely remove any. Each judge counters this by asking of everything in its jurisdiction whether it would exist if built today, and prefers deletion, consolidation, and derivation to repair or new machinery. Apply the pressure continuously, as weight decay does: every change also prunes what nothing sustains.

DIES IRAE orchestrates and compiles. It performs no audit itself and prescribes no judge's method. In `report` mode it has read-only authority over the repository, and judges write only their own worklogs and reports.

## Case

The case is fixed before any judge starts: the repository root, the source revision, a hash of the uncommitted changes, the scope, the user's constraints, the charter, and the bench. None of these may change during a run.

The charter and the public contract belong to the user. A judge may report contradictions in them, show that they lack authority, or identify a breaking change that actual use argues for in a future major version; neither a judge nor the tribunal may revise them.

Coverage is complete relative to the case: every material surface in the chosen jurisdictions is judged or recorded as uncovered. The tribunal invents no feature, audience, platform, or obligation that the charter lacks.

## Bench

The judges live under [skills/](skills/):

- `imperium`: the domain model
- `delenda`: implementation
- `confutatis`: correctness
- `tabula-rasa`: tests
- `damnatio-memoriae`: which documents deserve to exist
- `scriptorium`: documentation truth
- `advocatus-diaboli`: release fitness

The doctrines under [doctrines/](doctrines/) inform the judges; they are not audits.

Convene the subset the user names. Otherwise inspect the repository only enough to choose the applicable judges, and state why each is included or omitted; do not summon every judge by ritual. A campaign outside the bench, such as Bare Metal ALARA, may be named in a disposition but never runs silently.

## Procedure

### 1. Convene

Create the run directory, with the case in `case.md` and one subdirectory per judge:

```text
/tmp/dies-irae-<repo>-<run-id>/
```

### 2. Recover the charter

Run `$clique-fold` over the declared surfaces, such as READMEs, help text, the public API, package metadata, and configuration schemas, and over the code's external boundaries, with:

- `subject`: the claims and invariants each item establishes, and where items contradict one another
- `columns`: `claims | invariants | contradictions`

Where sources disagree, a formal specification outranks declared claims, and declared claims outrank the code's behavior. Add the known-bad behaviors the user names. Write the charter to `case.md`: claims, invariants, known-bad behaviors, and open contradictions. Put its authority questions to the user, who settles them or lets the tribunal proceed with them open. The charter is derived for the run and never committed.

### 3. Dispatch

Launch one worker per judge, in parallel when the environment permits. Give every worker the case and charter, the exact skill to follow, `report` mode, read-only authority over the repository, its own subdirectory, and no conclusions from other judges. A judge may run as several workers over a partition of the scope when that is faster; compilation joins them.

Use the strongest read-only enforcement available. Without enforcement, state the boundary explicitly and verify afterward that the source identity is unchanged.

Each judge follows its own skill; DIES IRAE adds no checklist. A worker that fails or drifts leaves an explicit hole in its jurisdiction; do not improvise its judgment in the parent.

### 4. Compile

After every worker has finished, run `$clique-fold` over the judges' reports and ledgers, with:

- `subject`: each finding and clean judgment, its evidence, and the root cause it shares with other findings
- `columns`: `judges | severity | root_cause | disposition`

Produce one register ordered by priority, not a concatenation of reports. Keep each finding's evidence and originating judge. Merge findings that share a root cause, keep distinct findings distinct, and expose contradictions between judges. Keep clean judgments, so that an absence of findings is not mistaken for an absence of inspection.

When one deletion, fusion, or derivation resolves findings from several judges, record it once, stating what it retires before any irreducible addition. Size is not severity, and deletions are not counted.

### 5. Execute

Only under explicit `execute` authority, and only after the judgment exists, run the convened judges' `execute` modes one at a time, in dependency order: Imperium, Delenda, Confutatis, Tabula Rasa, Damnatio Memoriae, Scriptorium, Advocatus Diaboli. Each judge refreshes its report against the current tree first, as its skill requires. An authority question stops the loop until the user answers it.

Then reconvene the bench in `report` mode against the new source identity, and repeat until a reconvened bench finds nothing material: the case's fixed point. Advocatus Diaboli's verdict at the fixed point closes the run. Delivery, such as `$seal`, is a separate act the tribunal never invokes.

## Severity

Severity is the credible consequence of leaving a finding in place within the case. It does not reflect the prestige of its jurisdiction, the cost of its fix, or the intensity of a judge's prose.

- `critical`: credible catastrophic or irreversible harm, fundamental compromise, or a product unsafe to release or operate; the affected release or operation stops pending containment, while coverage continues
- `high`: a material breach of a core contract, or serious harm to correctness, data, security, privacy, the user's system, or release integrity; closes before the affected release or use
- `medium`: a real defect with bounded reach or recoverable impact; warrants deliberate correction but does not by itself invalidate the product
- `low`: a genuine, localized defect with limited consequence; worth correcting, and more than a disagreement of taste

No jurisdiction has a ceiling or floor: documentation can be critical and architecture low. Weak evidence does not make a grave consequence `low`; record the uncertainty separately. Severity and priority are distinct: order the register by judgment over the whole case, not by a scoring formula.

## Judgment

Write `/tmp/dies-irae-<repo>-<run-id>/judgment.md`:

```markdown
# DIES IRAE Judgment: <case>

## Case

source_identity:
scope:
user_constraints:
bench:

## Charter

claims:
invariants:
known_bad:
contradictions:

## Jurisdiction

judges_completed:
judges_incomplete:
judges_omitted:

## Register

| priority | severity | judges | finding | consequence | evidence | disposition and dependencies |
|----------|----------|--------|---------|-------------|----------|------------------------------|

## Authority questions
## Residual unknowns
## Execution

iterations:
fixed_point:
verdict:
```

The order of the register is its priority. Evidence stays traceable to the judges' reports and to repository anchors. A disposition may name dependencies or a later campaign; it authorizes nothing.

Return the judgment path and a concise account of the verdict, and keep every judge's worklog and report beside the judgment.
