# File Decision Ledger Template

Use one row per file.

```text
| path | doc_kind | audience | disposition | keep_or_delete_basis | superseded_by_or_merge_target | rewrite_needed | code_reconciliation_target |
|------|----------|----------|-------------|----------------------|-------------------------------|----------------|----------------------------|
| docs/protocol.md | formal_spec | developers | keep_as_is | foundational definition already vetted | | no | crates/protocol/src/lib.rs |
| docs/roadmap.md | roadmap | internal | delete | shipped history plus stale plans | | no | |
| docs/setup.md | runbook | operators | rewrite_from_scratch | still needed but bloated and partially stale | | yes | scripts/deploy.sh |
| notes/old-api.md | feature_doc | developers | merge_then_delete | scarce useful material belongs in docs/api.md | docs/api.md | no | crates/api/src/lib.rs |
```

Allowed `disposition` values:

- `delete`
- `merge_then_delete`
- `rewrite_from_scratch`
- `light_edit`
- `keep_as_is`
- `flag_contradiction`

Rules:

- every file must end in exactly one disposition
- `keep_or_delete_basis` can be short, but it must be concrete
- `rewrite_needed` should normally be `yes` for any surviving non-foundational doc
- `code_reconciliation_target` is required for every surviving or contradiction-flagged file
