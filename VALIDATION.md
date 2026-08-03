# Validation Report — STSB 0.1

Python UTC: 2026-08-03T19:31:46.098217+00:00

## Public artifact comparison

The published GitHub contents were read back and compared byte-for-byte with the locally tested sources.

| Artifact | Result | Git blob |
|---|---|---|
| SPECIFICATION.md | IDENTICAL | 8ba1498222c20dc291acdc550316a238284254f7 |
| schemas/stsb.schema.json | IDENTICAL | 8b13a44c9a72806997d7ef17551b16124f0709f7 |
| examples/calculator.json | IDENTICAL | c1fba9581d7cb775eddbc488ca4e498d107b1957 |
| validator.py | IDENTICAL | f035a18bb6389dd3367b585e38d6fe746a18abba |
| tests/test_validator.py | IDENTICAL | 56b701be394e3d0fa8323f93fe1175a2075b223a |

## Deterministic checks

```text
4 tests passed
STSB PASS
```

## Result

**PASS** — the published calculator blueprint conforms to the candidate validator, and the four initial rejection/acceptance tests pass.

This validates the implementation baseline. It does not prove that the ten candidate functional roots are complete.
