---
name: imperium
description: "Derive the correct domain model de novo and bring a program's global nouns into it: every domain entity defined once and exactly, with no invalid instances, composed from primitive entities; every incumbent type, schema, and conversion canonicalized, split, merged, or retired accordingly. Use for a whole project, a vertical, or a single concept. Produces a report; executes the migration only when explicitly authorized."
---

# Imperium

## Mandate

The domain model is the skeleton of a program. When it is right, business logic composes from it. When it is wrong, control flow compensates with checks, conversions, and repeated validation, and every cold agent that touches the code adds another near-copy of an entity it cannot see. Imperium derives the correct model of the domain and brings the program's global nouns into it.

The fixed point is a program in which:

- every domain entity has one canonical definition and one precise name
- the possible values of each definition correspond one-to-one with the entity's valid values: no field the entity does not need, no instance the domain forbids
- compound entities are composed from primitive entities by products, sums, and collections, not flattened into flags and optional fields
- every alternate form carries a distinct law, and every conversion either refines knowledge or crosses a boundary

Ask of every incumbent type, schema, and conversion: if this domain were modeled today, would this exist, in this shape? Propose the correct model even when it splits a type into several, unifies several into one, or changes every consumer. Diff size is not a cost: no human reviews the diff, and a changed definition lets the compiler enumerate every site that must follow it.

Default to `report`. Change code only under explicit `execute` authority, and only after the complete report exists.

## Jurisdiction

Imperium owns global nouns: types that cross function boundaries; their constructors and the invariants those establish; identities and units; phases and state machines; error types; conversions and boundary projections; persistence, wire, and configuration schemas; and the names of domain concepts.

Delenda owns verbs and local nouns: control flow, transformations, algorithms, and the data structures inside a function. Judge a representation by the semantics it carries, such as uniqueness, ordering, optionality, cardinality, identity, and units, not by its concrete container or layout; the choice among representations with equal semantics belongs to Delenda. When a control-flow problem exists because the model admits an invalid state or duplicates an entity, the finding belongs to Imperium.

Record implementation, correctness, and documentation problems, including documentation the new model requires, as out-of-scope defects and hand them to Delenda, Confutatis, and Scriptorium respectively. Honor any current Damnatio Memoriae or Scriptorium dispositions supplied with the run.

## Scope

A project-wide run covers the entire model, never a convenient region of it. A run scoped to a concept follows it through the whole project, across module, crate, process, persistence, and protocol boundaries. A run scoped to a vertical or subtree derives the model top-down within it; types defined outside the scope are givens, recorded in the fringe with any obstruction they cause, and not redesigned.

Preserve the envelope. Internal compatibility has no claim to survive. A model change that breaks the public contract is an authority question: specify it as a major-version move instead of folding it into the migration. Until that move, the public form survives as a boundary projection of the canonical definition.

Read the repository's `AGENTS.md` files and `$style-doctrine`. Load `$product-doctrine` when a representation governs persistence, configuration, identity, lifecycle, or other conduct on the user's system.

## Model law

Count possible values. A struct is the product of its fields' values, an enum the sum of its variants, and `Option<A>` is 1 + A. Two optional fields of which exactly one must be set admit four shapes for two meanings; the sum of the two types admits exactly two. The common infidelities are flags and optional fields standing in for a sum, strings standing in for a closed set, parallel collections standing in for a collection of products, and a repeated bundle of fields or arguments standing in for a missing entity.

Names, shapes, conversion traffic, construction sites, and history are evidence about concepts, not verdicts. Two representations are one concept when they denote the same thing under the same law. Identical shapes remain distinct concepts when substituting one for the other would erase an invariant, phase, unit, authority, or meaning; different layouts do not make different concepts. The correct model may have more types than the incumbent or fewer.

An alternate form survives only by carrying a distinct law, as a validated form, a borrowed view, a phase of a state machine, or an external projection does; it states its law, its owner, and where translation occurs. Boundary projections end at their boundary. Phase transitions run one way. Validation has one owner. A lossy conversion exposes its loss, a fallible conversion exposes its failure, and an identity conversion is deleted.

Use the language's full type machinery, including generics, traits, phantom types, and generated projections, to make laws impossible to violate. Among models that carry the same laws, the one with fewer definitions, conversions, adapters, and synchronization obligations wins.

## Procedure

### 1. Open the run

Create the worklog and report:

```text
/tmp/imperium-<repo>-<scope>-<run-id>.md
/tmp/imperium-<repo>-<scope>-<run-id>-report.md
```

In a tribunal, use the directory the tribunal assigns. Record the mode, source identity, scope, envelope, givens, and applicable doctrine. Create a critical register beside the report only when a `critical` finding appears; record the finding and continue coverage. If writes are unavailable, keep the same state in the conversation and state that the run cannot be resumed.

### 2. Derive the model de novo

Before reading the incumbent types, establish what the program does: its charter, its entrypoints, and the data crossing its boundaries as input, output, and persisted state. From that understanding alone, derive the domain model: the entities, the data that exactly determines each, their laws, identities, units, and phases, and how they compose. Do not let the incumbent taxonomy seed the model. Record the model in the worklog as a hypothesis the incumbent code may correct.

### 3. Adjudicate the incumbent model

Run `$clique-fold` with:

- `subject`: for each model-bearing item, the concepts of the de novo model it represents, the laws it enforces, and its role in the terminal model
- `columns`: `concepts | laws | role`

Model-bearing items are type declarations, schemas, constructors and validation sites, conversions, discriminators, state encodings, conventions encoded in primitives, and the repeated bundles of fields or arguments that reveal missing entities. Generated, vendored, and external definitions belong to the fringe unless the user includes them.

Mine the incumbents as a quarry, not an inheritance. An incumbent that encodes a real distinction the de novo model missed amends the model; otherwise it has no claim to survive. Each item's role in the terminal model is canonical definition, alternate form with its law, boundary projection, derived, or retired.

### 4. Design the terminal model

Fold the adjudication into the terminal model. State first what disappears or becomes derived: rival definitions, conversions, duplicate validation, and shadow representations. Then state the canonical definitions and each surviving alternate form with its law. Introduce a definition only when no surviving one can carry its law. Reconcile synonyms and homonyms so that every concept leaves with one precise name. A terminal shape may be a single nominal type, a generic family, a phase ladder, an owned form with views, a generated projection, or the erasure of a type that never carried a law.

One finding is one coherent model change, such as a split, a unification, a sum replacing flags, a new identity type, or the retirement of a rival.

Turn the terminal model into a dependency-ordered migration: establish the canonical definitions, move consumers onto them, then delete the rivals, conversions, and duplicate validation that no longer carry an obligation. A migration that adds canonical types without converging consumers and deleting rivals is not canonicalization.

### 5. Report

Write the report from the folds. Stop there unless `execute` was explicitly authorized.

### 6. Execute

Recheck the source identity, and refresh the affected cliques if the tree has drifted. Execute the migration in dependency order: change the definitions, let the compiler enumerate every site that must follow, and move each consumer. Preserve the envelope.

Run the repository's verification, then check the model structurally: rival declarations and identity conversions are gone, validation has one owner, boundary projections are contained, construction goes through canonical constructors, and persistence and wire compatibility is proved where the public contract requires it. Finish with a residual `$clique-fold` over the changed model, and report each remaining alternate form with its law.

## Forms

### Worklog

```text
mode: report | execute
repository:
source_identity:
scope:
envelope:
givens:
applicable_doctrine:
worklog_path:
report_path:

de_novo_model:
clique_fold:
terminal_model:
findings:
migration:
authority_questions:
critical_register: none
execution:
verification:
residual:
```

### Report

```markdown
# Imperium Report: <scope>

## Executive judgment
## Scope, envelope, and givens
## Coverage
## De novo model
## Incumbent model
## Findings

### <id>: <title>

**Sites:**
**Evidence:**
**Judgment:**
**Disappears:** definitions, conversions, validation, and representations deleted or derived
**Terminal shape:**
**Irreducible additions:** each new definition and the law it carries, or `none`
**Migration:**
**Envelope preservation:**
**Dependencies:**
**Verification:**
**Uncertainty:**

## Migration program
## Authority questions
## Critical register
## Out-of-scope defects and handoffs
## Residual unknowns

### Model table

| concept | canonical definition | laws | incumbent forms | disposition |
|---------|----------------------|------|-----------------|-------------|
```
