# Decision 0002: Boundary adjudications for contested classifications

- Status: accepted for 0.1 experimentation
- Date: 2026-08-04

## Context

A closed root vocabulary is only operational if independent reviewers assign the same roots to the same software. The predictable objection to STSB 0.1 is not a missing root but boundary ambiguity between existing roots. This record publishes adjudications for five deliberately hard cases, with reasoning, so that the classification procedure is inspectable and challengeable. Disagreement with an adjudication is welcome evidence for the 0.2 ambiguity measurements.

## Adjudication principle

Classify by the *essential observable effect the user obtains*, not by internal mechanism. Every program computes internally; `compute` is primary only when derived information is itself the delivered good.

## Adjudications

### 1. Compiler — primary `create`, capabilities `create`, `compute`, `observe`

The delivered good is a new user-recognized artifact (the object program). The transformation is computation, but computation in service of artifact production; a compiler that computed perfectly and emitted nothing would be useless. `observe` covers diagnostics (warnings, errors), which are a reported inspection of the subject program.

### 2. Video game — primary `simulate`, capabilities `simulate`, `create`, `communicate` (varies by family)

A game's essential effect is executing a behavioral representation of a world under user interaction. Creative-mode games where the durable good is a player-made artifact may justify `create`; networked games add `communicate`. The primary root may legitimately differ between game families — that is composition working, not the vocabulary failing. Reviewer disagreement rates on this family are an explicit 0.2 measurement target.

### 3. Database management system — primary `record`, capabilities `record`, `compute`, `coordinate`, `decide`

The essential effect is persisting and retrieving state across events. Query evaluation is `compute` in service of retrieval; transaction scheduling and locking are `coordinate`; access control is `decide`. A DBMS that computed but persisted nothing would not be a DBMS.

### 4. Operating-system scheduler — primary `coordinate`, capabilities `coordinate`, `decide`

The essential effect is arranging actors, resources, order, and timing. Choosing the next process is `decide` in service of coordination. `control` is reserved for effects on machines or environments *external* to the computing system itself; scheduling the system's own workload is coordination, not external control. This internal/external boundary for `control` is normative for 0.1.

### 5. Spellchecker — primary `observe`, capabilities `observe`, `decide` (`create` when auto-correcting)

Flagging misspellings is inspecting and reporting on a subject text. Ranking suggested replacements is `decide`. A spellchecker that silently rewrites text crosses into `create`, because it modifies a user-recognized artifact.

## Consequences

- The internal/external boundary of `control` (adjudication 4) and the compute-as-service principle (adjudication 1) are normative interpretations for 0.1 records.
- Each adjudication is falsifiable: a demonstration that independent reviewers, given this record, still diverge materially on these families is evidence against operational distinguishability and feeds the 0.2 ambiguity program.
- New contested families should be added here by decision-record amendment, not resolved ad hoc in examples.
