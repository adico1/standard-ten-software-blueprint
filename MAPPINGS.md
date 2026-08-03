# Identifier Mappings

This table is normative only about where references belong in STSB 0.1. It does not modify the referenced standards.

| STSB field | External identifier | Direction | Loss or caveat |
|---|---|---|---|
| `source.swhid` | SWHID / ISO/IEC 18670 | STSB → SWHID | SWHID identifies content, not functional equivalence |
| `composition.spdx` | SPDX / ISO/IEC 5962 document or element | STSB → SPDX | SPDX can express substantially more supply-chain metadata |
| future `packages[].purl` | Package URL | STSB ↔ purl | A package coordinate may be mutable or ecosystem-dependent |
| future `product.swid` | SWID / ISO/IEC 19770-2 | STSB → SWID | SWID focuses released/installed product identity |
| `builds[].digest` | Cryptographic build digest | intrinsic | A digest alone does not prove source-to-binary reproduction |
| `blueprint.seed_digest` | STSB canonical seed digest | intrinsic | New STSB layer; not a substitute for an artifact identifier |
| `blueprint.generator` | Stable generator identity | STSB reference | Reproducibility additionally requires exact generator content and inputs |

## Placeholder rule

Identifiers in the initial reference examples are syntactically valid placeholders, not claims that corresponding objects resolve in an external registry. Release-grade blueprints must replace them with verified identifiers and evidence.
