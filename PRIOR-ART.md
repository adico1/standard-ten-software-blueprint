# Prior Art and Interoperability Boundary

STSB is an integration and functional-blueprint proposal, not a replacement identifier.

## Identity and supply-chain standards

| Existing effort | Strength retained by STSB | Boundary STSB investigates |
|---|---|---|
| SWHID / ISO/IEC 18670 | Intrinsic immutable source identity | Functional equivalence across different source artifacts |
| SPDX / ISO/IEC 5962 | Components and relationships | Connection to canonical function and blueprint |
| Package URL (purl) | Ecosystem package coordinates | Cross-ecosystem product and blueprint relationships |
| SWID / ISO/IEC 19770-2 | Product and version identification | Connection to source, composition, and deterministic generation |
| Reproducible Builds | Source-to-binary reproducibility | Intent/seed-to-source reproducibility |

## Functional classification systems

These are the closest precedents to STSB's functional vocabulary. STSB's claim is not that functional classification is new; it is that a *small, closed, falsifiable* root vocabulary connected to artifact identity has not been attempted in this form.

| Existing effort | What it demonstrates | Boundary STSB investigates |
|---|---|---|
| Debian Debtags | A deployed faceted classification of software function with controlled vocabularies (`use::`, `works-with::`, ...) and two decades of real tagging data, including ambiguity in practice | Closure and necessity testing of a much smaller root set; connection to artifact identity layers |
| Trove classifiers (PyPI) | A controlled `Topic ::` vocabulary attached to package identity at ecosystem scale | Cross-ecosystem, platform-neutral vocabulary with explicit rejection rules |
| Michael Jackson's Problem Frames | A prior attempt at a small closed set of software problem archetypes (five frames) | Classification of observable executable behavior rather than problem structure; machine verification |
| EDAM ontology (bioinformatics) | A controlled vocabulary of software *operations* that a real community adopted — and that grew to hundreds of terms | Whether ten roots plus composition can stay closed where domain ontologies could not |
| The Software Ontology (SWO) | Formal ontology of software with functional axes | Minimal vocabulary with an executable validator instead of a full ontology stack |
| REA ontology | Resources-Events-Agents modeling of economic exchange (underlies the `transact` root) | Generalization beyond economic exchange to all software effects |
| Schema.org SoftwareApplication | Discoverable application metadata | Controlled and testable functional vocabulary |
| freedesktop.org categories | Practical application categories | Platform-neutral closure and necessity tests |
| ACM CCS | Computing subject classification | Classification of executable software behavior rather than literature topics |

Every mapping must preserve the established identifier unchanged and document information loss in both directions.
