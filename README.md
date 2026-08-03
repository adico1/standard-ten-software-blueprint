# Standard Ten Software Blueprint (STSB)

An open proposal for a universal, reproducible software blueprint connecting **what software does** to **the exact artifacts that implement it**.

## Problem

Software already has identifiers for separate layers:

- **SWHID / ISO/IEC 18670** — immutable source artifacts
- **SPDX / ISO/IEC 5962** — components and relationships
- **purl** — ecosystem packages
- **SWID / ISO/IEC 19770-2** — products and versions
- **reproducible-build digests** — exact build outputs

What is missing is one canonical record connecting those layers to a functional identity, a minimal deterministic blueprint, its generator, and verifiable releases and builds.

STSB proposes that connection layer. It does **not** replace existing standards.

## Status

**Pre-standard 0.1 — candidate under adversarial testing.**

The ten functional roots are a hypothesis, not a completed proof:

`compute`, `record`, `create`, `observe`, `communicate`, `coordinate`, `decide`, `transact`, `simulate`, `control`.

> Public challenge: submit one real software system that STSB cannot represent without adding an uncontrolled root category.

## Ten identity levels

| Level | Object | Question |
|---:|---|---|
| 0 | Function | What transformation is performed? |
| 1 | Family | What application family performs it? |
| 2 | Product | Which named product is it? |
| 3 | Blueprint | What minimum declaration regenerates it? |
| 4 | Release | Which published version is it? |
| 5 | Source | Which immutable source tree implements it? |
| 6 | Package | How is it distributed? |
| 7 | Build | Which exact executable artifact resulted? |
| 8 | Deployment | Where is it installed? |
| 9 | Execution | Which running occurrence is observed? |

## Reference proof

```text
calculator request
  → canonical STSB blueprint
  → deterministic generator
  → source + SWHID
  → SPDX composition
  → purl/SWID release references
  → reproducible build digest
  → validator PASS
```

## Participate

- Open a **counterexample** issue.
- Propose a mapping to an established identifier.
- Submit an independently implemented validator.
- Challenge root necessity, distinctness, or closure.

See [STAMPS.md](STAMPS.md). Specification text is intended for CC BY 4.0; reference code is intended for Apache-2.0.

---

Founding stamp: `2026-08-03T19:24:07.418459+00:00` (Python UTC).
