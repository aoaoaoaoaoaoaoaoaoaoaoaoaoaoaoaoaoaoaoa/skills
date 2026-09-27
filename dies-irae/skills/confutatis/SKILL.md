---
name: confutatis
description: "Audit an implementation, whole or any subtree, for broken promises: recover the contract each function, type, trait, module, and boundary makes, explicit or implied, and prove where the implementation breaks it, where a client relies on more than it promises, or where the promise itself contradicts the charter. Every finding carries a reproduction or a concrete trace. Produces a report; fixes defects only when explicitly authorized."
---

# Confutatis

## Mandate

Prove where the code's promises are false.

Model-written code is optimized to look right: good names, plausible structure, confident documentation. Its defects are the ones that survive reading, and every other judge reads for something else. The other judges also preserve the envelope, which is recovered largely from the existing implementation, so without this judge a defect is carried faithfully into every smaller, cleaner shape. Confutatis is the one judge that does not take current behavior as given.

Default to `report`. Change code only under explicit `execute` authority, and only after the complete report exists.

## Contracts

Every unit of code makes a promise, whether or not anyone wrote it down: a function, type, trait, module, process, or protocol. Its contract has four parts:

- preconditions: what it requires of its callers
- postconditions: what it guarantees on success
- invariants: what it preserves
- failure contract: what holds when it fails, whether state is left valid, left unchanged, or failure is impossible

A trait's contract binds every implementation: an `Ord` that is not a total order, a `Hash` inconsistent with `Eq`, or an iterator that resumes after returning `None` breaks a promise its callers rely on. Thread safety and ordering under concurrent use are part of a contract, and so is the safety contract of `unsafe` code, stated or not.

Recover each contract; do not invent one. Contracts come from these sources, in order of authority:

1. a formal specification, where one exists
2. failures no contract permits: crash, hang, leak, undefined behavior, data loss, race, injection
3. house invariants, from `$product-doctrine` and `$style-doctrine`
4. declared claims: documentation, help text, public API, types, and metadata
5. the code's evident intent: names, types, doc comments, and the behavior of sibling code

When a charter is supplied, its claims and invariants join the declared sources, and its known-bad behaviors are defects to reproduce and trace to a root cause, not to rediscover. Tuned behavior, such as a position, a size, or a solver budget, is not a promise and lies outside jurisdiction. When the sources do not decide whether behavior is a quirk or a defect, raise an authority question.

## Seams

A defect lives at one of three seams:

1. The supplier breaks its promise: the implementation does not honor its contract.
2. A client relies on more than was promised: a caller depends on an ordering, normalization, non-emptiness, idempotence, or other property its supplier never guaranteed. Each side is locally reasonable; the defect lies between them.
3. The promise is wrong: the contract contradicts the charter or a higher source.

Search where model-written code characteristically reads right and runs wrong: the failure path of every operation, the edges of every input domain, every input that crosses a trust boundary, every interleaving the code permits, every contract a trait implementation inherits, and every property a caller assumes of code it did not write.

## Standard

No reproduction, no finding. A finding carries a failing input, command, or test, or at minimum a concrete trace through the code with a specific input or interleaving. Prefer dynamic confirmation where the tools exist: property probes, fuzzing, sanitizers, Miri, and model checkers such as loom. A suspicion that meets neither bar stays in the worklog.

A missing check is a finding only when some caller can actually violate the precondition; a precondition every caller already satisfies, by type or by construction, needs no check. A hypothetical misuse is not a finding. `unsafe` code is not a finding; a broken safety contract is.

Restore a broken promise at its narrowest owner: a type, when Imperium can make the violation unrepresentable; a check at the boundary where untrusted input enters; or a correction to the implementation. Never retreat to slower or more defensive code when restoring the invariant suffices, and never add a check inside the trusted core for a violation that cannot occur.

Group defects by root cause. Several defects often share one unstated invariant; that invariant is the finding, and its durable home is a type (Imperium), a doc comment on its owner (Scriptorium), or a permanent witness if Tabula Rasa admits one.

## Jurisdiction and scope

Confutatis owns the gap between promised and actual behavior. Implementation structure, the domain model, tests, documentation, and release fitness belong to Delenda, Imperium, Tabula Rasa, Scriptorium, and Advocatus Diaboli; record problems in their jurisdictions as out-of-scope defects and hand them off.

The scope is the implementation the user names: a whole repository, a subtree, or a component. It bounds coverage and edits, not reasoning: a contract's parties are examined wherever they live.

Read the repository's `AGENTS.md` files, `$style-doctrine`, and `$product-doctrine`. Load `$affinity-doctrine` before fuzzing or any other sustained run. Run code only in clean, isolated environments, never against the user's live system or profile.

## Procedure

### 1. Open the run

Create the worklog and report before the first deep read:

```text
/tmp/confutatis-<repo>-<scope>-<run-id>.md
/tmp/confutatis-<repo>-<scope>-<run-id>-report.md
```

In a tribunal, use the directory the tribunal assigns. Record the mode, source identity, scope, charter, and applicable doctrine. Create a critical register beside the report only when a `critical` finding appears; record it and continue coverage. If writes are unavailable, keep the same state in the conversation and state that the run cannot be resumed.

### 2. Cover the scope

Run `$clique-fold` with:

- `subject`: for each implementation source, the contracts it offers and relies on, and whether each seam holds
- `columns`: `contracts | findings`

The manifest holds the handwritten implementation sources in scope. Generated, vendored, and dependency code belongs to the fringe unless the user includes it. Build each clique around one contract, or a tight family of contracts, and every party to it. Run the code wherever that settles a question faster than reading it.

### 3. Adjudicate

One finding is one broken promise, or one root cause shared by several. Assign severity by consequence. For each finding, state the contract and its source, the seam, the reproduction, the consequence, the root cause, and the remedy at the narrowest owner. Record a rejected suspicion only when it is subtle and likely to be rediscovered.

### 4. Report

Write the report from the folds. Stop there unless `execute` was authorized.

### 5. Execute

Recheck the source identity. Fix root causes before their symptoms, in dependency order, and confirm each fix by running its reproduction. A fix that changes the public contract is an authority question. Do not add a permanent test for a fix by reflex; `$unit-test-doctrine` decides. Run the repository's verification, then a residual `$clique-fold` over the changed surface.

## Forms

### Worklog

```text
mode: report | execute
repository:
source_identity:
scope:
charter:
applicable_doctrine:
worklog_path:
report_path:
critical_register: none

clique_fold:
findings:
suspicions:
root_causes:
authority_questions:
execution:
verification:
residual:
```

### Report

```markdown
# Confutatis Report: <scope>

## Executive judgment
## Scope, charter, and sources
## Coverage
## Root causes
## Findings

### <id>: <title>

**Contract:** its terms and source
**Seam:** broken promise, over-reliance, or wrong promise
**Reproduction:** the failing input, command, test, or concrete trace
**Consequence:**
**Severity:**
**Root cause:**
**Remedy:** the narrowest owner and the change
**Handoffs:**
**Uncertainty:**

## Authority questions
## Critical register
## Out-of-scope defects and handoffs
## Residual unknowns

### Ledger

The complete clique-fold ledger.
```
