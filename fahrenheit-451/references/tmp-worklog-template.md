# /tmp Worklog Template

```text
worklog_path:
scope_root:
inspection_mode: audit_only | audit_plus_refactor
wave_size_limit: 8

manifest:

clique_plan:

wave_checkpoints:

file_decision_ledger:

contradiction_register:

residual_summary:
```

Rules:

- create this file before the first file read
- update it after every 8-file wave before reading more files
- treat it as the durable source of truth for the run
- report the final worklog path in the user-facing response
