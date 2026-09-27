---
name: delenda
description: "Audit an implementation, whole or any subtree, for aggressive contraction within its envelope: remove the control flow, transformations, implementation types, and structural waste its present responsibilities do not require, until it reads as though implemented once, today. Use when accreted code should become materially smaller and more intentional. Produces a report; executes only when explicitly authorized."
---

# Delenda

## Mandate

Make the scope look as though its present responsibilities had been implemented once, coherently, without historical sediment.

This is aggressive contraction of the implementation within the envelope. Delete implementation, not requirements. Internal compatibility, obsolete structure, and historical decomposition have no claim to survive, and diff size is not a cost.

Default to `report`. Edit source only under explicit `execute` authority, and only after the complete report exists.

## Jurisdiction

Delenda owns verbs, implementation nouns, and the storage of domain nouns: control flow, call structure, layering, transformations, algorithms and their cost, the types that exist only to serve an implementation, and the concrete representation of domain types.

Imperium owns domain nouns, the types that would appear in a medium-granularity pseudocode description of the program, and their meaning. Take the domain model as given, or take Imperium's terminal model when a current Imperium report is supplied. A finding whose root cause is a domain-noun defect, such as a guard that exists because a type admits an invalid state or a local copy of a domain entity, belongs to Imperium. A terminal shape never copies a domain entity to add local state; it contains the entity in a local type.

When accidental structure caused a correctness defect and the proposed contraction resolves it, integrate the defect into the finding. Otherwise record correctness, domain-model, and documentation problems as out-of-scope defects and hand them to Confutatis, Imperium, and Scriptorium respectively.

## Scope and envelope

The scope is the implementation the user names: a whole repository, a subtree, or a component. A subtree is an edit and coverage boundary, not a reasoning boundary: read outward as far as needed to understand callers and real boundaries, and keep prescribed changes inside the scope.

Before judging the implementation, establish the envelope: what the scope must keep doing for its callers, including the obligations that are easy to forget: how it fails, what it persists, what it trusts, and the performance it must sustain. When a charter is supplied, the envelope is its part within the scope. The implementation, callers, tests, documentation, configuration, and history are evidence for the envelope; none is automatically authoritative. The current implementation shows what must survive, not the form in which it survives.

A change that would alter the envelope, including a language-version or toolchain migration the doctrine would prefer, is an authority question: name it with its evidence, tersely, without an unsolicited redesign.

Read the repository's `AGENTS.md` files and `$style-doctrine`. Load `$product-doctrine` when the scope governs conduct on the user's system. Doctrine sharpens the judgment; it does not authorize a change to the envelope.

## Standard

Treat the existing implementation as historical evidence, not as an authoritative decomposition of the problem.

An internal structure survives only by carrying required behavior, enforcing an invariant, or marking a real boundary. Paths that differ in no required behavior collapse into one, and a computation or decision made in several places gets one owner.

Seek the smallest correct implementation `I*` with `I* ≡_E I₀`: equivalent to the incumbent `I₀` on the envelope `E`. Minimize semantic description length: the independent concepts, representations, owners, states, paths, boundaries, and obligations required to state and maintain the implementation. Judge an abstraction by its net effect on that length: how many independent facts, degrees of freedom, synchronization obligations, and change sites remain after the move. Familiarity, local brevity, and conventional simplicity carry no independent weight. Lines and bytes corroborate; they are not the objective. Local expansion is correct when it reduces global state space or independent truths.

Remove waste that structural inspection shows without a benchmark: a quadratic scan where a linear one serves, repeated passes over the same data, needless copies and allocations, and work recomputed instead of carried. A contraction must not slow a path the envelope cares about; where size and cost conflict, the style doctrine's ranking decides. Waste that only measurement can establish belongs to Bare Metal ALARA.

## Search

Let the system reveal its own dominant forms of accidental complexity. Do not organize the audit around a fixed smell catalogue, exercise named passes evenly, or force findings into predefined categories.

Reason both subtractively and reconstructively. Ask what can vanish, what can become derived, which distinctions are fictitious, which truths lack an owner, and which boundaries exist only because history placed code on opposite sides of them. Follow the strongest semantic pressure wherever it leads.

Ask continuously:

> If this envelope were implemented today, would this construct exist?

The question applies to implementation, not requirements; do not use it to revoke a supported responsibility.

## Procedure

### 1. Open the run

Create the worklog and report before the first deep read:

```text
/tmp/delenda-<repo>-<scope>-<run-id>.md
/tmp/delenda-<repo>-<scope>-<run-id>-report.md
```

In a tribunal, use the directory the tribunal assigns. Record the mode, source identity, scope, provisional envelope, and applicable doctrine. The worklog is the resumable state of the audit, not a draft of the report; chat is only a summary.

### 2. Cover the scope

Run `$clique-fold` with:

- `subject`: for each implementation source, the structure, paths, and waste the envelope does not require, and the findings that would remove them
- `columns`: `findings`

The manifest holds the handwritten implementation sources in scope, and the handwritten schema, configuration, or build files that materially define it, each with the reason. Generated, vendored, dependency, snapshot, fixture, and build-output material stays out unless the user includes it. The thesis is the contraction thesis; before it closes, reconcile competing local abstractions into one global shape.

If a credible catastrophic defect appears, record it in the critical register at once and continue coverage. Discovery does not authorize source modification, scope expansion, remediation, or abandonment of coverage; even under `execute`, rectification waits for the complete report. The audit must remain satisfiable against a read-only source tree.

### 3. Adjudicate findings

One finding is one coherent contraction, not one source site. It may accumulate evidence across many cliques and may be strengthened, split, merged, or discharged before the report. Promote a finding when the evidence establishes a material accidental burden, the proposed shape is correct and concrete, and the move stays within the envelope. Foundational contractions may be broad; a finding need not be locally actionable.

Recover the terminal shape from the surviving obligations instead of attaching remedies to the incumbent structure. State what disappears or becomes derived before what remains or must be introduced. Every survivor and addition must carry an obligation not already discharged elsewhere; a purely additive change is valid only when the envelope contains an unmet obligation, which it names.

Record a rejected hypothesis only when the rejection is material, subtle, or likely to prevent repeated rediscovery. Do not write an obituary for every fleeting suspicion.

### 4. Report

Write a complete, proportional report that can be implemented without repeating the audit, synthesizing one contraction thesis instead of collecting notes. Do not demand or reward length, and do not classify findings into a fixed taxonomy. Every finding field is a proof obligation: when a field has no material content, say so tersely instead of omitting it. Keep honest uncertainty and evidence anchors. Stop after the report unless `execute` was authorized; in a read-only environment, a complete report is the successful end of the run.

### 5. Execute

Under `execute`, begin a new phase. Recheck the source identity and refresh any affected clique if the tree has drifted. Execute coherent moves in dependency order, never in file order, and never across the envelope. Use the repository's own verification. Afterward, build a final manifest that accounts for created, deleted, fused, and moved sources, run a residual `$clique-fold` over the changed surface, and report the contraction achieved with line and byte deltas, without mistaking either for the objective.

## Forms

### Worklog

```text
mode: report | execute
repository:
source_identity:
scope:
envelope:
applicable_doctrine:
worklog_path:
report_path:
critical_register: none

clique_fold:
live_findings:
material_rejections:
contraction_thesis:
execution:
residual:
```

### Critical register

```text
| id | site | finding | evidence | confidence | severity_basis | status |
|----|------|---------|----------|------------|----------------|--------|
```

The register has no remediation field: it is an alarm, not an implementation detour.

### Report

```markdown
# Delenda Report: <scope>

## Executive summary
## Envelope
## Coverage

Manifest coverage, exclusions, fringe, fold hierarchy, worklog path, and baseline sizes.

## Contraction thesis
## Priority and dependencies

| order | finding | leverage | confidence | implementation_risk | dependencies |
|-------|---------|----------|------------|---------------------|--------------|

## Critical register

`none`, or a summary linking the register.

## Findings

### <id>: <title>

**Sites:**
**Evidence:**
**Judgment:**
**Contraction:** the declarations, states, paths, representations, dependencies, and synchronization obligations that disappear or become derived
**Terminal shape:** the smallest structure that remains
**Irreducible additions:** new machinery and the obligation each alone carries, or `none`
**Implementation specification:**
**Envelope preservation:**
**Dependencies:**
**Verification:**
**Uncertainty:**

## Retained complexity and rejected hypotheses

Material defenses and rejections only.

## Out-of-scope defects and handoffs
## Authority questions
## Execution notes
## Residual unknowns
```

## Final response

Report the worklog and report paths, the envelope, manifest coverage, clique and fold counts, the contraction thesis, the highest-leverage findings, the critical register's status, authority questions, and baseline sizes. After execution, also report verification, residual closure, final manifest changes, and the contraction achieved.
