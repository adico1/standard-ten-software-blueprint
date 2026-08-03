# STSB 0.1 — Candidate Specification

## 1. Scope

STSB is a canonical connection record for software function, blueprint, generator, source, composition, package, product, release, build, deployment, and execution identities.

STSB does not replace SWHID, SPDX, purl, SWID, or cryptographic build digests. It references them.

## 2. Conformance language

The terms MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## 3. Canonical object

An STSB record MUST contain:

- `schema`: the STSB schema version;
- `identity`: authority, family, product, and version;
- `function`: primary root, family, and capability roots;
- `blueprint`: seed digest and generator identity;
- `source`: an immutable source identifier;
- `composition`: a component-manifest reference;
- `builds`: zero or more target and digest pairs.

Unknown extension fields MAY be carried only under `extensions`.

## 4. Candidate roots

The candidate root vocabulary is closed for version 0.1:

1. `compute`
2. `record`
3. `create`
4. `observe`
5. `communicate`
6. `coordinate`
7. `decide`
8. `transact`
9. `simulate`
10. `control`

A conforming 0.1 record MUST select exactly one primary root and MAY select additional capability roots. Every selected root MUST belong to this vocabulary.

The vocabulary is a falsifiable candidate. A counterexample that cannot be represented by composition is evidence against closure.

## 5. Identity levels

The levels are function, family, product, blueprint, release, source, package, build, deployment, and execution. Records MAY omit operational levels that do not yet exist, but MUST NOT confuse one level for another.

## 6. Blueprint reproducibility

A blueprint MUST identify its seed by digest and its generator by stable identifier. A reproducibility claim MUST additionally provide target, toolchain inputs, and resulting build digest.

## 7. Verification

A verifier MUST reject:

- missing required fields;
- roots outside the versioned root vocabulary;
- a primary root absent from capabilities;
- malformed SHA-256 digests;
- duplicate capabilities;
- unscoped unknown top-level fields.

## 8. Versioning

Artifact identities are immutable. Classification corrections create a new STSB record revision without changing the referenced immutable artifacts.

## 9. Proof target

STSB 1.0 requires public evidence that:

- the roots cover submitted software families;
- each root is independently necessary;
- root boundaries are operationally distinguishable;
- composition remains closed;
- at least one independent implementation validates the schema.
