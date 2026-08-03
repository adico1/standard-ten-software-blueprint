# Standard Ten Software Blueprint (STSB)

[![STSB gauntlet](https://github.com/adico1/standard-ten-software-blueprint/actions/workflows/ci.yml/badge.svg)](https://github.com/adico1/standard-ten-software-blueprint/actions/workflows/ci.yml)

A candidate open standard connecting **what software does**, **the minimum blueprint that defines it**, and **the exact artifacts that implement it**.

## Publication status

**0.1.0-rc1 — publication-ready release candidate under adversarial testing.**

The implementation baseline is verified. The completeness of the ten functional roots is **not proven**. Counterexamples are invited and tracked publicly.

## Existing standards retained

| Layer | Established identity |
|---|---|
| Immutable source artifact | SWHID / ISO/IEC 18670 |
| Components and relationships | SPDX / ISO/IEC 5962 |
| Ecosystem package | Package URL (purl) |
| Product and installed version | SWID / ISO/IEC 19770-2 |
| Exact build output | Cryptographic build digest |
| Functional identity and reproducible intent | STSB candidate layer |

STSB references these systems; it does not replace them.

## Candidate functional roots

`compute`, `record`, `create`, `observe`, `communicate`, `coordinate`, `decide`, `transact`, `simulate`, `control`.

Applications are compositions. The vocabulary is closed only within schema version 0.1 while it is tested against counterexamples.

## Verify in one command

Requires Python 3.10 or later and no third-party packages.

```bash
python3 release.py
```

Expected result:

```text
Ran 6 tests
OK
STSB RELEASE PASS: 4 examples
```

Validate one blueprint:

```bash
python3 validator.py examples/calculator.json
```

## Repository map

- [Candidate specification](SPECIFICATION.md)
- [JSON Schema](schemas/stsb.schema.json)
- [Machine-readable roots](taxonomy/roots.json)
- [Identifier mappings](MAPPINGS.md)
- [Prior-art boundary](PRIOR-ART.md)
- [Reference examples](examples)
- [Decision 0001](decisions/0001-candidate-functional-roots.md)
- [Validation evidence](VALIDATION.md)
- [Roadmap](ROADMAP.md)
- [Release checklist](RELEASE_CHECKLIST.md)
- [Signed step ledger](STAMPS.md)

## Participate

- Submit a functional counterexample using the issue template.
- Correct or extend a standards mapping with authoritative references.
- Register an independent validator implementation.
- Contribute a materially distinct software-family example.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Known limitations

- The initial examples contain explicitly documented placeholder SWHIDs and digests; they are not resolution claims.
- Four examples are sufficient to test the machinery, not taxonomy completeness.
- No independent implementation has yet been accepted.
- The 1.0 threshold requires a published census, zero unresolved counterexamples in scope, independent implementations, and shared governance.

## Licensing

- Reference code, tests, schemas, and workflows: [Apache-2.0](LICENSE)
- Specification and documentation: [CC BY 4.0](LICENSE-SPECIFICATION.md)

Copyright 2026 Adi Ovadia Cohen (adico). See [NOTICE](NOTICE).

---

Founding stamp: `2026-08-03T19:24:07.418459+00:00` (Python UTC).

