# Prior Art and Interoperability Boundary

STSB is an integration and functional-blueprint proposal, not a replacement identifier.

| Existing effort | Strength retained by STSB | Boundary STSB investigates |
|---|---|---|
| SWHID / ISO/IEC 18670 | Intrinsic immutable source identity | Functional equivalence across different source artifacts |
| SPDX / ISO/IEC 5962 | Components and relationships | Connection to canonical function and blueprint |
| Package URL (purl) | Ecosystem package coordinates | Cross-ecosystem product and blueprint relationships |
| SWID / ISO/IEC 19770-2 | Product and version identification | Connection to source, composition, and deterministic generation |
| Reproducible Builds | Source-to-binary reproducibility | Intent/seed-to-source reproducibility |
| Schema.org SoftwareApplication | Discoverable application metadata | Controlled and testable functional vocabulary |
| freedesktop.org categories | Practical application categories | Platform-neutral closure and necessity tests |
| ACM CCS | Computing subject classification | Classification of executable software behavior rather than literature topics |

Every mapping must preserve the established identifier unchanged and document information loss in both directions.
