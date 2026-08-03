# Contributing to STSB

STSB welcomes falsification, mappings, examples, validators, and specification corrections.

## Contribution classes

1. **Counterexample** — demonstrate behavior not representable by composition of the candidate roots.
2. **Mapping** — connect STSB fields to an established standard without replacing it.
3. **Example** — add a real application family with essential inputs, transition, outputs, and effects.
4. **Validator** — independently implement the normative rejection rules.
5. **Editorial** — improve clarity without changing semantics.

## Evidence required

Claims must identify observable behavior and a reproducible test. Industry names, interface differences, programming languages, and deployment platforms are not by themselves new functional roots.

## Pull request gate

Run:

```bash
python3 -m unittest discover -s tests -v
python3 release.py
```

Both commands must pass. New behavior requires a rejecting test before the implementation change and an accepting test after it.

## Decision record

Maintainers publish reasons for accepted and rejected root changes. Version 0.1 remains explicitly provisional; no contributor is required to treat the ten roots as proven.

By contributing, you agree that specification/documentation contributions are licensed under CC BY 4.0 and code contributions under Apache-2.0.
