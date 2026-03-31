# File Manifest Template

```text
scope_root:
inspection_mode: audit_only | audit_plus_refactor
wave_size_limit: 8

files:
- [ ] docs/file_a.md
- [ ] docs/file_b.txt
- [ ] notes/file_c.org
```

Rules:

- include every plaintext doc-like file in scope
- mark files as inspected only after reading them
- allow files to appear in multiple clique waves
- reuse the same manifest for the final residual sweep
