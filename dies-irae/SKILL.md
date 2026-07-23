---
name: dies-irae
description: Convene any explicit or inferred subset of the DIES IRAE audit family as independent parallel read-only judges, then compile their native ledgers and reports into one evidence-backed, globally prioritized defect register typed by auditing source and normalized to a domain-agnostic severity scale. Use for a multi-audit project inquest, comprehensive codebase judgment, or coordinated read-only review across implementation, semantic topology, tests, documentation, product conduct, and release fitness. Never rectifies findings itself.
---

# DIES IRAE

> Cuncta stricte discussurus.

## Mandate

Convene the applicable judges against one locked case, let each exercise its own doctrine independently, and render one total judgment.

DIES IRAE is an orchestrator and compiler. It does not perform an object-level audit, prescribe how a specialist reasons, or rectify what the tribunal finds. Its authority is read-only over the target repository. Workers may write only their private ledgers and reports outside it.

Exhaustiveness is relative to the declared case. Every material surface within the chosen jurisdictions must be judged or recorded as uncovered; the tribunal does not invent features, audiences, platforms, or obligations outside the project's charter.

The product charter and public contract are the human axiological boundary of the case. Judges may expose contradictions, identify a controlled major-version desire path, or show that the boundary lacks authority; neither a judge nor the compiler may revise it. Only explicit user authority changes the case.

## The Bench

The judges live under [skills/](skills/):

- `exterminate-slop`: implementation contraction and architectural residue
- `majestic-magisteria`: semantic representations, ownership, and conversion topology
- `qui-custodit`: verification architecture and evidentiary sufficiency
- `fahrenheit-451`: zero-based documentation purge
- `chronicler`: documentary concordance and source commentary
- `release-inquest`: integrated product and release fitness

The governing doctrines live under [doctrines/](doctrines/). They inform judges; they are not parallel audits.

Honor an explicit user-selected subset. Otherwise inspect the repository only enough to choose the applicable bench, and state why each judge was included or omitted. Do not summon every judge by ritual. A specialist campaign outside this bench, such as Bare Metal ALARA, may be named as a disposition but is not silently executed.

## Convene

Lock the repository root, source identity, dirty-state digest, scope, authoritative user constraints, frozen outer contract, and user-selected jurisdictions before dispatch. Create a run directory shaped like:

```text
/tmp/dies-irae-<repo>-<run-id>/
```

Record the case identity and bench in `case.md`. Assign each judge a private subdirectory for its native ledger and report.

Launch one independent worker per selected judge, in parallel when the environment permits. Give every worker:

- the same case identity and scope
- the same authoritative user constraints and frozen outer contract
- the exact specialist skill to follow
- its report-only mode
- read-only authority over the repository
- its private output directory
- no conclusions from sibling judges

Standalone `/tmp/<specialist>-...` paths in child skills are fallbacks. In a tribunal run, the assigned private subdirectory governs artifact placement; preserve the specialist's native schemas and filenames within it.

Use the strongest available read-only enforcement. Permission to write the tribunal run directory is not permission to mutate the case. If enforcement is unavailable, instruct the boundary explicitly and verify afterward that the source identity and dirty-state digest are unchanged.

Let each judge obey its own scope, ledger, context, evidence, stopping, and report protocol. DIES IRAE adds no object-level checklist. A worker that fails, drifts, or cannot complete remains an explicit hole in jurisdiction; do not improvise its judgment in the parent.

## Compile

After every worker has terminated, compile the heterogeneous native ledgers and reports intelligently. Source identity and scope are the shared case facts; do not impose a common child-ledger schema or a reconciliation algorithm.

The desired artifact is one prioritized defect register, not a concatenation of reports. Preserve evidence and auditing provenance, combine or distinguish findings according to their actual semantics, expose unresolved contradictions, and retain clean judgments so absence of findings is not mistaken for absence of inspection. If the combined material exceeds context, fold it without discarding the source reports on disk.

Preflight compilation inputs with `wc -l -c`. No fold may ingest more than 3000 lines or 131072 bytes of report or reduction material; introduce bounded branch and bridge folds until the root judgment fits. Higher folds consume reductions, not raw ledgers or reports.

### Severity

Severity describes the credible consequence of leaving a defect in place within the declared case. It does not describe the prestige of its source domain, the cost of its fix, or the intensity of a judge's prose.

- `critical`: credible catastrophic or irreversible harm, fundamental compromise, or a product unsafe to release or operate; the affected release or operation must stop pending containment, while tribunal coverage continues
- `high`: material breach of a core contract or serious harm to correctness, data, security, privacy, the user's system, or release integrity; must close before the affected release or use
- `medium`: real consequential defect with bounded reach or recoverable impact; warrants deliberate correction but does not independently invalidate the whole product
- `low`: genuine localized defect with limited consequence; worth correcting, but not merely a disagreement in taste

No jurisdiction has a categorical ceiling or floor. Documentation can be critical; architecture can be low. Weak evidence does not make a grave possible consequence “low”: preserve the uncertainty separately.

Severity and priority are distinct. Order the register using judgment over the whole case. Do not use a scoring formula.

## Judgment

Write `/tmp/dies-irae-<repo>-<run-id>/judgment.md` in this form:

```markdown
# DIES IRAE Judgment: <case>

## Case

source_identity:
dirty_state:
scope:
authoritative_user_constraints:
frozen_outer_contract:

## Jurisdiction

audits_completed:
audits_incomplete:
audits_omitted:

## Defect Register

| priority | severity | source | defect | consequence | evidence | disposition and dependencies |
|----------|----------|--------|--------|-------------|----------|------------------------------|

## Contradictions And Authority Questions
## Residual Unknowns
```

`source` names one or more originating judges. The ordering itself expresses priority. Evidence must remain traceable to the specialist report and repository anchors. Dispositions may identify dependencies or a subsequent specialist campaign; they do not authorize execution.

Return the judgment path and a concise account of the verdict. Preserve every native ledger and report beside it.

## Hard Failures

- do not mutate the target repository or launch an execution mode
- do not perform a specialist audit in the parent
- do not summon every judge merely because it exists
- do not leak one worker's conclusions into another worker's case
- do not accept a ledger from a different or drifted source identity
- do not concatenate reports in place of judgment
- do not prescribe an input reconciliation algorithm or universal object-level checklist
- do not rank domains; rank defects by consequence and whole-case judgment
- do not conflate severity, confidence, fix cost, and execution order
- do not omit incomplete or deliberately unexamined jurisdiction
- do not turn uncertainty or taste into an established defect
- do not begin rectification after judgment
