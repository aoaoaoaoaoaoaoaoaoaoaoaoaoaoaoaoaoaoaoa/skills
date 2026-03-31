# Contradiction Register Template

Use this for genuine doc-vs-code contradictions where supersession is unclear.

```text
| doc_path | code_anchor | contradiction | possible_precedence | why_unclear | action_needed |
|----------|-------------|---------------|---------------------|-------------|---------------|
| docs/protocol.md | crates/protocol/src/lib.rs | doc says field is required; code treats it as optional | doc_or_code_unclear | public contract vs implementation drift | human decision |
```

Rules:

- record only real contradictions, not vague doubts
- if precedence is obvious, update the loser instead of logging it here
- unresolved entries must be surfaced in the final response
