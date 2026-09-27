# DIES IRAE Glossary

This file is the naming authority for authors of the DIES IRAE family. Skills do not load it; each skill defines the nouns it uses, in these senses. Each noun has one meaning. Add a noun here before introducing it in a skill, and do not reintroduce a retired synonym.

## Judges

| Judge | Jurisdiction | Retired name |
|---|---|---|
| Imperium | representation | majestic-magisteria |
| Delenda | implementation | exterminate-slop |
| Confutatis | correctness | |
| Tabula Rasa | tests | testing-year-zero |
| Damnatio Memoriae | documentation existence | fahrenheit-451 |
| Scriptorium | documentation truth | chronicler |
| Advocatus Diaboli | release | release-inquest |

## Family

| Noun | Meaning | Retired synonyms |
|---|---|---|
| judge | a skill that audits one jurisdiction, or a running instance of it | worker, audit, specialist |
| doctrine | normative guidance a judge applies; never audits | |
| jurisdiction | the subject a judge owns | |
| bench | the judges convened for one case | |
| tribunal | one DIES IRAE run: convene, judge in parallel, compile | compiler |

## Case and intent

| Noun | Meaning | Retired synonyms |
|---|---|---|
| case | what a run is about: source identity, scope, charter, user constraints | |
| source identity | the commit plus a hash of uncommitted changes; the known-good baseline | dirty-state digest; baseline, in the behavioral sense |
| scope | what a run covers: its jurisdiction applied to the paths or concepts it names; any subtree is valid | |
| charter | the product's intent: claims, invariants, known-bad behaviors, and open contradictions; owned by the user, recovered into the case file on each run, never committed | product charter, frozen outer contract, supported behavior |
| claim | one promise the product declares, in a README, help text, API, or metadata | |
| invariant | one law that must hold, from house doctrine or the product | |
| public contract | the part of the charter that external consumers rely on; changing it requires a major version | outer contract |
| envelope | what one run must preserve: the charter within its scope plus the scope's obligations to the rest of the system; frozen by definition | semantic envelope, frozen envelope, documentary envelope, release envelope, frozen product |
| oracle | a source of the right answer | |
| authority question | a decision only the user can make, including any change to the envelope | blocked, authority blocker, authority conflict, contract break requiring authorization, out-of-envelope lesion |

## Engine

These nouns belong to `clique-fold`, which judges use as their reading engine.

| Noun | Meaning | Retired synonyms |
|---|---|---|
| caller | the user or skill that invokes clique-fold | |
| subject | what a clique-fold run evaluates, and the judgment each item receives; supplied by the caller | |
| manifest | the locked list of items a run must cover | census, audit manifest, model manifest, surface manifest |
| fringe | material read as evidence but not covered | context fringe, evidence fringe |
| budget | the per-clique limits `line_ceiling` and `byte_ceiling` | source budget, context budget, circuit breaker, `source_line_ceiling`, `context_line_ceiling` |
| clique | manifest items or slices read together because they answer one question within budget | cohort, in the reading sense |
| cover | the set of cliques spanning the manifest | clique cover, inquest cover |
| slice | a coherent range of an oversized file | |
| reduction | the durable summary of one clique | leaf reduction, clique reduction |
| fold | a reduction of reductions, either branch or bridge | branch synthesis, bridge reduction, fold reduction |
| thesis | the root fold's output; a judge may qualify it, as in "contraction thesis" | root documentary model |
| frontier | open questions that could still change the thesis | |

## Outputs

| Noun | Meaning | Retired synonyms |
|---|---|---|
| worklog | the resumable state of a run | run state, resumable state |
| ledger | one row per manifest item, with the columns the caller supplies | corpus ledger, ownership ledger, representation ledger, claim ledger |
| finding | one judged problem, with evidence and a disposition | defect, lesion |
| disposition | the terminal action for a ledger row or finding; each judge defines its set | |
| cohort | items whose dispositions must execute together | |
| handoff | work passed to a named judge | chronicler_handoff, specialist handoff |
| out-of-scope defect | a problem outside the run's scope; recorded and handed off | incidental defect, adjacent code lesion |
| critical register | the separate list of `critical` findings kept during a run | high-severity register |
| report | a judge's final argument | |
| judgment | the tribunal's compiled output, containing the register ordered by priority | |
| mode | `report`, or `execute`, which always follows a complete report | defect_report, purge_execute, concordance_report, execute_after_report, execute_after_inquest, year_zero_report, inquest_report |
| fixed point | the state in which another run finds nothing material | |
| terminal shape | the smallest structure a finding proposes | terminal machine, terminal topology |
| root cause | the cause several findings share | terminal cause |
| severity | the consequence of leaving a finding in place: `critical`, `high`, `medium`, or `low` | |
| priority | the order of the register; distinct from severity | |
