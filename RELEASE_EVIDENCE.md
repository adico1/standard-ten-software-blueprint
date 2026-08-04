# Release Evidence

## v0.1.0-rc2 — hardening pass

Stamp: 2026-08-04T12:56:42+00:00 (Python UTC)

- [x] Validator enforces all SPECIFICATION.md §7 rejection rules at every nesting level; cross-checked against the JSON Schema on identical mutation probes with agreement.
- [x] Seventeen acceptance/rejection tests pass, each asserting its specific error message.
- [x] Strict SWHID grammar enforced in schema and validator.
- [x] All `composition.spdx` references resolve to parseable placeholder SPDX documents; `release.py` enforces this.
- [x] Generator scheme unified to `stsb://`; schema `$id` repaired; ledger retitled with AI-assistance disclosure; boundary adjudications published as Decision 0002.

```text
Ran 17 tests
OK
STSB RELEASE PASS: 4 examples
```

## v0.1.0-rc1 — initial publication

Publication-readiness stamp: 2026-08-03T19:57:27.872414+00:00 (Python UTC)

## Acceptance evidence

- [x] Specification and schema both declare STSB 0.1.
- [x] Dependency-free validator published.
- [x] Six acceptance/rejection tests pass.
- [x] Four compositional example blueprints pass.
- [x] Machine-readable ten-root taxonomy published.
- [x] SWHID, SPDX, purl, SWID, and build-digest boundaries documented.
- [x] Apache-2.0 code license and CC BY 4.0 specification license published.
- [x] Governance, contribution, conduct, security, roadmap, and decision policies published.
- [x] Counterexample, mapping, implementation, and pull-request templates published.
- [x] GitHub Actions gauntlet enabled.
- [x] Release-candidate README commit `49656241fe7b40e1e465ff0fd8e1dedf62a00bb2` passed GitHub Actions run `30847988435`.

## Deterministic local result

```text
Ran 6 tests in 0.000s
OK
STSB RELEASE PASS: 4 examples
```

## Claim boundary

This evidence establishes that **STSB 0.1.0-rc1 is ready for public review and adversarial testing**.

It does not establish that the ten candidate roots are complete, necessary, or sufficient for all software. Those claims remain the explicit 0.2 evidence program.

