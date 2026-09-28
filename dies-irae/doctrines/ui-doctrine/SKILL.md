---
name: ui-doctrine
description: Apply the house doctrine for user-facing interfaces. Use whenever designing, implementing, reviewing, naming, or simplifying visible UI, including controls, labels, legends, navigation, states, and feedback.
---

# UI Doctrine

Judge every interface with fresh eyes: the user does not know or care about the conversation, specification, implementation, or ontology that produced it. Each visible element must communicate a fact the user cares about, afford a useful action, or give necessary feedback, in language the user already understands. Internal distinctions, encoding channels, framework terms, and labels that describe presentation machinery explain nothing. A map legend may offer meaningful choices such as "trail type" and "terrain"; headings such as "color" and "line style" only narrate how the renderer works and should not exist.

Start from an empty screen and require every element to earn its place. If removing a label, symbol, control, state, or flourish leaves the user no less capable or informed, remove it. Prefer the smallest coherent surface, familiar vocabulary, progressive disclosure, and direct manipulation; do not expose implementation structure to make up for an interface that lacks a model shaped by the user's task. When uncertain, look at the screen as a first-time user and err toward omission.

UI unit tests follow `$unit-test-doctrine`. A visible change does not automatically warrant a unit test of internal state.

## Interaction hazards

1. **Moving target.** Never reorder or replace a control under hover, focus, press, drag, or edit; reconcile after the interaction ends.
2. **Unsettled effect.** When an accepted action starts a non-instant operation on a resource, take a visible lease on that resource, marking it busy, before returning control. Block conflicting actions until the operation fails or the resource's actual state confirms the intended result; a worker's acceptance or reported completion is not confirmation. Queue further actions only when their order matters to the user and the queue is visible and cancellable.
