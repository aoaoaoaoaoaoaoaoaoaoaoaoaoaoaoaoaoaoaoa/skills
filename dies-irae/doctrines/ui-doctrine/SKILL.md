---
name: ui-doctrine
description: Apply the house doctrine for user-facing interfaces. Use whenever designing, implementing, reviewing, naming, or simplifying visible UI, including controls, labels, legends, navigation, states, and feedback.
---

# UI Doctrine

Judge every interface with fresh eyes: the user does not know or care about the conversation, specification, implementation, or ontology that produced it. Each visible element must communicate a user-relevant fact, afford a useful action, or provide necessary feedback in language the user already understands. Internal distinctions, encoding channels, framework terms, and labels that merely describe presentation machinery are not explanations. For example, a map legend may offer meaningful choices such as “trail type” and “terrain”; headings such as “color” and “line style” only narrate how the renderer works and should not exist.

Begin from absence and require every element to earn its place. If removing a label, symbol, control, state, or flourish leaves the user no less capable or informed, remove it. Prefer the smallest coherent surface, familiar vocabulary, progressive disclosure, and direct manipulation; do not expose implementation structure to compensate for an interface that lacks a user-shaped model. When uncertain, observe the screen as a first-time user and err toward omission.

UI unit tests follow `$unit-test-doctrine`. A visible change does not
automatically warrant an internal-state unit test.

## Interaction Hazards

1. **Moving target.** Never reorder or replace a control under hover, focus, press, drag, or edit; reconcile after interaction ends.
2. **Unsettled effect.** When an accepted action starts a non-instant operation on a resource, acquire a visible per-resource operation lease before returning control. Interdict conflicting actions until failure or authoritative reconciliation proves the intended postcondition; worker acceptance or completion alone is not reconciliation. Queue only when ordered compound intent is meaningful, visible, and governable.
