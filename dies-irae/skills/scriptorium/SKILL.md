---
name: scriptorium
description: "Reconcile a project's durable documentation with its actual contracts and present system: every truth that must be communicated gets one owner at the narrowest stable layer, and missing, stale, duplicated, or stranded truth is created, repaired, consolidated, or transferred. Covers READMEs, guides, architecture documents, runbooks, examples, module and API documentation, docstrings, and comments that carry rationale or proof obligations. Produces a report; edits documentation only when explicitly authorized, and never product behavior."
---

# Scriptorium

## Mandate

Bring the project's documentation into agreement with the system it describes.

The fixed point is a project in which every durable truth that must be communicated has one canonical owner, at the narrowest stable layer that can state it truthfully, and no required truth is missing, stale, duplicated, or stranded in transient prose.

Documentation owns truths that code cannot state to their audience: public contracts, operational procedures, design intent, external constraints, proof obligations, failure behavior, and rationale that would be costly or ambiguous to recover. It must not become a shadow implementation, a historical scrapbook, or explanatory padding around self-evident code.

Damnatio Memoriae decides which documents deserve to exist; Scriptorium is its constructive complement. It repairs living documents and transfers scarce truth out of doomed ones. When a current Damnatio Memoriae report is supplied, consume its handoffs and deletion dependencies as evidence; do not rerun the purge or casually reverse its judgments. Consume documentation handoffs from the other judges the same way.

Default to `report`. Edit documentation only under explicit `execute` authority, and only after the complete report exists.

## Scope and envelope

A project-wide run covers all of the project's documentation. A run scoped to a feature, subsystem, audience, or API region follows that region across the whole project; a directory is not a reasoning boundary. State any unavoidable exclusion; never substitute a convenient sample.

The documentation includes prose files that carry a role, user and operator documents, examples, module and item documentation, public API documentation, and internal comments that preserve an invariant, proof, safety condition, external fact, or non-obvious rationale. It also includes documents that are missing but implied by a real audience or an exported contract.

Do not write prose for every symbol; trivial private mechanics may stay silent. A comment that paraphrases syntax, narrates control flow, preserves obsolete structure, or compensates for a poor name or a bad abstraction should disappear. When the code itself is the defect, record an out-of-scope defect for Delenda or Imperium instead of making the comment more eloquent.

Language visibility is evidence of an audience, not proof of an intended durable API. When a nominally public surface is credibly accidental, do not immortalize it in documentation: raise an authority question about the API, preserve any truth current consumers need, and defer its canonical documentation until the surface is decided.

The envelope is the product's behavior and public contract, which Scriptorium never changes. Code, tests, configuration, generated behavior, documentation, history, standards, and upstream contracts are evidence; none is automatically authoritative. When authority is unclear, raise an authority question instead of writing one side into the documentation.

Read the repository's `AGENTS.md` files, `$style-doctrine`, and `$product-doctrine` before judging source commentary and user-facing contracts. Write under `$vox-nihili` unless the project's own instructions set another voice.

## Placement

Put a truth where it remains true and where its audience meets the thing it governs. The narrowest stable owner wins: a type's invariant belongs with the type, an effect or failure contract with the callable, a module invariant with the module, an operator procedure with the command or runbook, and a project-wide decision with the smallest project document that can govern it.

Store each truth once. Broader documents may orient and link; they must not copy volatile details from narrower owners. Prefer a generated or mechanically checked projection wherever prose would otherwise have to stay synchronized with code. Move commentary when ownership moves.

Doc comments state semantic contracts, not implementation tours: invariants, units, preconditions, effects, failure and panic behavior, concurrency and safety obligations, and surprising costs, where they matter. An example teaches a correct use or resolves an ambiguity; it does not decorate an obvious signature.

An ordinary comment survives only by carrying information the code cannot: the why, the proof boundary, the external constraint. Delete the what.

## Procedure

### 1. Open the run

Create the worklog and report before deep reading:

```text
/tmp/scriptorium-<repo>-<scope>-<run-id>.md
/tmp/scriptorium-<repo>-<scope>-<run-id>-report.md
```

In a tribunal, use the directory the tribunal assigns. Record the mode, source identity, scope, envelope, and applicable doctrine. The worklog preserves orientation; the report owns the final argument. If writes are forbidden, carry the same state in the final response and state that the run cannot be resumed.

### 2. Cover the documentation

Run `$clique-fold` with:

- `subject`: for each document or communication obligation, the truths it must carry, to which audience, under what authority, and at which owner
- `columns`: `audience | present_owner | terminal_owner | ownership_delta | authority`

The manifest holds both the existing documents and the communication obligations: truths that must be communicated, including those with no owner yet. Discover them broadly, using symbol and API indexes, manifests, command surfaces, schemas, lints, and package metadata to expose missing obligations without pulling the implementation into context. For source commentary, list semantic symbols or bounded ranges instead of treating a large source file as one document. Distinguish generated, vendored, legal, fixture, and machine-consumed material before proposing changes.

Exhaustiveness applies to documents and communication obligations, not to every tracked artifact. Code, configuration, tests, history, binaries, and images enter the fringe as evidence. Inspect an image or other non-text asset only when it communicates a material contract that could change a judgment.

Follow claims only as far as the documentation judgment requires; exhaustive coverage of obligations does not license exhaustive reading of the implementation. Use the folds to rectify names, choose canonical owners, eliminate duplicated truths, and settle audience boundaries.

Record a `critical` discovery or an exposed secret in the critical register and continue; it neither triggers code rectification nor derails coverage.

### 3. Design the change program

Derive the terminal documentation from the required truths, not from the existing documents. Prefer removal, consolidation, transfer, and mechanical derivation; repair or create only where an obligation would otherwise lack an owner. Each change names the truth or obligation, its present and proposed owner, the evidence, the exact shape of the documentation, the duplicates and obsolete documents it retires, the authority, and the verification. An addition-only change names the audience and the truth that no existing owner can carry.

State each change as what will happen: remove, consolidate, transfer, derive, repair, reconstruct, create, or accept. Do not keep a vague "improve docs" entry or defer a hard judgment to execution.

Whole-file deletion belongs to Damnatio Memoriae, except as the proved tail of a transfer or consolidation. Source comments and duplicate fragments may be removed directly once their truth has an owner.

The program is complete when every durable truth has one proposed owner, every required audience and exported contract has adequate documentation, and every example and cross-reference has a verification path. Absence is a valid judgment: do not create documentation to fill a category or balance a report. Order the program by dependency: receiving documents before deletions of old truth, then dependents and navigation.

### 4. Report

Write the report from the folds. Stop there unless `execute` was authorized.

### 5. Execute

Recheck the source identity and withhold any change whose authority has drifted. Execute the program in order: establish receiving documents before deleting old truth, then repair dependents and navigation. Edit documentation and source commentary only; never smuggle in a behavioral refactor or public-API change.

Run the project's documentation verification: documentation builds, doctests, examples, links, references, formatting, and applicable lints or schema checks, chosen from the actual project. Verification supports inspection; it does not replace it. Finish with a residual `$clique-fold` over the changed documentation.

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
ownership_model:
change_program:
authority_questions:
execution:
verification:
residual:
```

### Report

```markdown
# Scriptorium Report: <scope>

## Executive judgment
## Envelope
## Coverage
## Canonical ownership model
## Missing documentation
## Stale, duplicated, and misplaced truth
## Public API and source commentary
## Change program
## Authority questions
## Critical register
## Out-of-scope defects and handoffs
## Verification program
## Residual unknowns

### Ledger

The complete clique-fold ledger, one row per document or communication obligation.
```
