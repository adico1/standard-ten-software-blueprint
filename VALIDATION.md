# Validation Report — STSB 0.1

Last refreshed: 2026-08-04T12:56:42+00:00 (Python UTC), for 0.1.0-rc2 hardening.

## Deterministic checks

```text
Ran 17 tests
OK
STSB RELEASE PASS: 4 examples
```

Reproduce with:

```bash
python3 release.py
```

## What the gauntlet now enforces

- Full nested validation in the dependency-free validator: required and unknown fields at every level (identity, function, blueprint, source, composition, builds), not only at the top level. The Python validator and the JSON Schema were cross-checked against the same mutation probes and agree.
- Strict SWHID grammar (`swh:1:(cnt|dir|rev|rel|snp):<40 hex>`) in both schema and validator.
- Every `composition.spdx` reference must resolve to an existing, parseable JSON file in the repository. The reference examples now ship structurally valid placeholder SPDX documents (see the placeholder rule in MAPPINGS.md).
- Each rejection rule in SPECIFICATION.md §7 is exercised by at least one test asserting the specific error message, not merely that some error occurred.

## Historical baseline (0.1.0-rc1, 2026-08-03)

The rc1 public artifact comparison read the published GitHub contents back and compared them byte-for-byte with the locally tested sources; all five compared artifacts were identical and the initial four-test gauntlet passed. Those artifacts have since been superseded by the rc2 hardening described above; the Git history preserves the rc1 state.

## Result

**PASS** — the published blueprints conform to the candidate validator and the JSON Schema, and all seventeen acceptance/rejection tests pass.

This validates the implementation baseline. It does not prove that the ten candidate functional roots are complete.
