# Read Cluster Template

```text
clique_id:
purpose:
why_these_files_belong_together:
wave_size:

files:
- path/to/file_a.md
- path/to/file_b.txt

checkpoint:
- deletion candidates:
- merger candidates:
- possible keepers:
- likely rereads:
- code surfaces to reconcile:
```

Rules:

- `wave_size` must never exceed `8`
- write the checkpoint into the `/tmp` worklog after every wave before reading more files
- a file may appear in multiple cliques when supersession or duplication reasoning demands it
- name the clique by the relationship it is testing, not by arbitrary adjacency
