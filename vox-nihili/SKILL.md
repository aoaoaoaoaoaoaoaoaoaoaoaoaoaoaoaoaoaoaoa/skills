---
name: vox-nihili
description: "House doctrine for technical writing: documentation, skills and agent instructions, commit messages, reports, and any text for which it is explicitly invoked. Use when Codex writes, edits, or reviews such text, unless user or local project instructions require another style. Produces dry, impersonal prose that states each fact and relation once in the fewest well-formed words, without padding, private jargon, dropped logic, or performed voice. Does not govern conversation."
---

# Vox Nihili

Vox Nihili governs technical writing: documentation, skills and agent instructions, commit messages, reports, and any text for which it is explicitly invoked. It does not govern conversation. Explicit user or local project instructions override it.

The ideal is an English-to-English canonicalizer. Its input is a set of facts and the relations among them; its output is the shortest well-formed English that states each fact and relation exactly once. Real prose only approximates this machine. Use it as the direction of every revision, not as a style to imitate.

## Properties of canonical prose

**Lossless.** Every fact and relation in the source survives, including qualifications, uncertainty, attribution, scope, the steps of an argument, and the purpose of a rule. A dropped *because* is a dropped relation. Never shorten a text by strengthening a claim, removing a caveat, or hiding a step.

**Unambiguous.** Each sentence has one reading and parses on the first pass. Compression stops where it would break grammar, create a second reading, or require the reader to decode a term. Noun stacks, undefined coinages, dropped articles and connectives, and telegraphic fragments violate this property. So does a nominalization that hides the actor: write "the server verifies its configuration," not "verification of the configuration is performed."

**Minimal.** Within the first two properties, fewer words are better; length is a cost in its own right. Add nothing beyond the facts: no motivation, orientation, persuasion, previews, recaps, or reassurance. An example belongs only when it states something the prose cannot state as briefly. Assume the knowledge the intended audience can be expected to have, define anything beyond it, and explain nothing else.

**Normalized.** Each concept has one name, and each name one concept. Prefer an established term to a coinage, and define a coinage where it first appears. State relations of the same kind in the same sentence form and parallel items in parallel syntax. Order facts so that each follows what it depends on. Use lists for parallel items, tables for items that share attributes, and paragraphs for arguments. Name a category instead of enumerating its members, adding only the members a reader might not include.

**Impersonal.** No writer is present: no mood, humor, warmth, enthusiasm, or beauty pursued for its own sake. Severity is also a voice. Slogans, aphorisms, reflexive antithesis ("not X but Y"), triads for rhythm, legal or liturgical diction (*law*, *lawful*, *shall*, *discharge*) for ordinary requirements, and emphasis for urgency (bold, capitals, *critical*) are performances; remove them.

**Idempotent.** Revising canonical prose changes nothing. Revision stops at this fixed point.

## Examples

> Treat code as liability. Under a fixed semantic envelope, begin by asking what can disappear and prefer the lawful design with the least total machinery. Every declaration, path, layer, dependency, configuration axis, and compatibility form must discharge an irreducible obligation. New code must state a missing law or enable a larger contraction. Once the obligations are met, less code wins.

> Code is a liability. With behavior held fixed, start by asking what can be removed, and prefer the smallest correct design. Every construct, including each dependency, configuration option, and compatibility shim, must be required by that behavior. New code must enforce a missing invariant or enable a larger deletion.

Legal diction becomes the facts it stood for, the enumeration becomes a category plus its easily overlooked members, and the final sentence, which repeated the second, is gone.

> Lock the repository root, source identity, dirty-state digest, scope, authoritative user constraints, frozen outer contract, and user-selected jurisdictions before dispatch.

> Before launching the judges, record the repository root, the source revision, a hash of the uncommitted changes, the scope, the user's constraints, the outer contract, and the judges the user selected. None of these may change during the run.

The text grows: private terms become what they denote, and *lock* becomes its two facts.

> The product charter and public contract are the human axiological boundary of the case. Judges may expose contradictions, identify a controlled major-version desire path, or show that the boundary lacks authority; neither a judge nor the compiler may revise it. Only explicit user authority changes the case.

> Only the user can change the product charter, the public contract, or the case. A judge may report contradictions in the charter or contract, show that they lack authority, or identify a breaking change that actual use argues for in a future major version. Neither the judges nor the compiler may revise them.

Metaphors become the relations they stood for, and the rule stated twice is stated once, first.

## Scope of a revision

Preserve the source's terminology and notation unless correcting them is authorized. Infer the audience and purpose from the text, its surroundings, and the request; ask only when plausible readings yield materially different documents.

In prose embedded in code, markup, or structured documents, preserve all non-prose behavior. Headings, captions, labels, callouts, and cards are prose: rewrite, merge, or remove them when their content belongs elsewhere, and delete styling the change leaves unused. Leave code, equations, identifiers, anchors, and executable content unchanged unless authorized.

Judge what each sentence does, not its surface form; do not run a banned-word pass. Replacing *crucial* with *load-bearing* changes nothing. A metaphor used consistently to name real structure is vocabulary. A statement repeated for readers who arrive separately, as in a README and a docstring or in independently installed skills, is not a duplicate.

## Procedure

1. Read the whole text. Extract its audience, purpose, facts, and relations, and the order in which the facts depend on each other.
2. Examine each unit: sentence, heading, caption, or list item.
   - Delete it if it states no needed fact or relation.
   - Merge it into the stronger statement if another unit states the same fact.
   - Restate it in fewer words if it is diffuse.
   - Expand it if it is ambiguous, undecodable, or missing a relation.
   - Leave it if it is already canonical.

   Examine rewritten units the same way.
3. Reorder, merge, and split paragraphs and sections by dependency. Each paragraph has one purpose. Existing structure carries no weight of its own, and headings name real divisions of content.
4. Reread the result as its intended reader. Restore any lost fact, scope, or relation, and fix seams, orphaned references, and terms whose meaning drifted. Repeat from step 2 until a pass changes nothing.

The unit audit is a reasoning procedure, not output. Unless a critique or change log is requested, deliver the revised text without describing the edits. Keep the artifact's native format, and run the cheap checks the edit makes relevant, such as links, anchors, and rendering.
