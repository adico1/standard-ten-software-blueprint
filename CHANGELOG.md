# Changelog

## 0.1.0-rc2

- Hardens the validator to enforce every rejection rule at every nesting level (identity, function, blueprint, source, composition, builds), closing the drift where records failing the JSON Schema passed the Python validator.
- Expands the test gauntlet from 6 to 17 tests; each test now asserts the specific error message rather than the mere presence of an error.
- Enforces the full SWHID grammar (`swh:1:(cnt|dir|rev|rel|snp):<40 hex>`) in both schema and validator.
- Adds structurally valid placeholder SPDX documents for all reference examples; `release.py` now fails if a `composition.spdx` reference does not resolve and parse.
- Unifies the generator identifier scheme to `stsb://` across all examples.
- Repairs the schema `$id` to a URL that serves the schema document itself.
- Retitles the step ledger to "Recorded Step Ledger", removes non-publication session entries, and adds an AI-assistance disclosure.
- Adds Decision 0002 with published boundary adjudications (compiler, video game, DBMS, OS scheduler, spellchecker).
- Extends PRIOR-ART.md with the closest functional-classification precedents: Debian Debtags, Trove classifiers, Problem Frames, EDAM, SWO, and REA.

## 0.1.0-rc1

- Defines ten candidate functional roots and ten identity levels.
- Connects blueprint, generator, SWHID, SPDX, package/product references, and build digests.
- Publishes a JSON Schema, dependency-free Python validator, examples, and mutation tests.
- Adds public governance, contribution, prior-art, security, licensing, and release gates.
