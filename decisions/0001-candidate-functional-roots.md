# Decision 0001: Treat ten functional roots as a falsifiable candidate

- Status: accepted for 0.1 experimentation
- Date: 2026-08-03

## Context

Product categories, industries, interfaces, languages, and platforms generate open-ended labels. STSB instead needs a small vocabulary based on observable software effects that can compose.

## Decision

Version 0.1 tests ten roots: compute, record, create, observe, communicate, coordinate, decide, transact, simulate, and control.

The vocabulary is closed only within schema version 0.1. It is not claimed to be mathematically proven complete.

## Rejection test

A proposed new root must demonstrate essential behavior that cannot be represented as composition of existing roots. Renaming a domain or implementation does not qualify.

## Consequences

- Applications may carry several capability roots but one primary root.
- Counterexamples remain first-class evidence.
- Root additions, removals, or merges require a new decision record and schema impact analysis.
