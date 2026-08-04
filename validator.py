#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOTS = {
    "compute", "record", "create", "observe", "communicate",
    "coordinate", "decide", "transact", "simulate", "control",
}
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
SWHID = re.compile(r"^swh:1:(cnt|dir|rev|rel|snp):[0-9a-f]{40}$")
TOP = {"schema", "identity", "function", "blueprint", "source", "composition", "builds", "extensions"}
REQUIRED = TOP - {"extensions"}

IDENTITY_FIELDS = ("authority", "family", "product", "version")
FUNCTION_FIELDS = {"primary", "family", "capabilities"}
BLUEPRINT_FIELDS = {"seed_digest", "generator"}
BUILD_FIELDS = {"target", "digest", "reproducible"}


def _require_object(record, key, errors):
    value = record.get(key)
    if not isinstance(value, dict):
        errors.append(f"{key} must be an object")
        return None
    return value


def _require_string(obj, section, key, errors):
    value = obj.get(key)
    if not isinstance(value, str) or not value:
        errors.append(f"{section}.{key} must be a non-empty string")
        return None
    return value


def _reject_unknown(obj, section, allowed, errors):
    unknown = set(obj) - set(allowed)
    if unknown:
        errors.append(f"unknown {section} fields: " + ", ".join(sorted(unknown)))


def validate(record):
    errors = []
    if not isinstance(record, dict):
        return ["record must be a JSON object"]
    missing = REQUIRED - set(record)
    unknown = set(record) - TOP
    if missing:
        errors.append("missing top-level fields: " + ", ".join(sorted(missing)))
    if unknown:
        errors.append("unknown top-level fields: " + ", ".join(sorted(unknown)))
    if record.get("schema") != "stsb/0.1":
        errors.append("schema must equal stsb/0.1")

    identity = _require_object(record, "identity", errors)
    if identity is not None:
        _reject_unknown(identity, "identity", IDENTITY_FIELDS, errors)
        for key in IDENTITY_FIELDS:
            _require_string(identity, "identity", key, errors)

    function = _require_object(record, "function", errors)
    primary = None
    if function is not None:
        _reject_unknown(function, "function", FUNCTION_FIELDS, errors)
        primary = function.get("primary")
        _require_string(function, "function", "family", errors)
        capabilities = function.get("capabilities")
        if primary not in ROOTS:
            errors.append("primary is not a candidate root")
        if not isinstance(capabilities, list) or not capabilities:
            errors.append("function.capabilities must be a non-empty array")
        else:
            if len(capabilities) != len(set(capabilities)):
                errors.append("capabilities must be unique")
            invalid = set(capabilities) - ROOTS
            if invalid:
                errors.append("invalid capabilities: " + ", ".join(sorted(invalid)))
            if primary not in capabilities:
                errors.append("primary must appear in capabilities")

    blueprint = _require_object(record, "blueprint", errors)
    if blueprint is not None:
        _reject_unknown(blueprint, "blueprint", BLUEPRINT_FIELDS, errors)
        seed = blueprint.get("seed_digest", "")
        if not isinstance(seed, str) or not SHA256.fullmatch(seed):
            errors.append("seed_digest must be lowercase sha256")
        _require_string(blueprint, "blueprint", "generator", errors)

    source = _require_object(record, "source", errors)
    if source is not None:
        _reject_unknown(source, "source", ("swhid",), errors)
        swhid = source.get("swhid", "")
        if not isinstance(swhid, str) or not SWHID.fullmatch(swhid):
            errors.append("source.swhid must match swh:1:(cnt|dir|rev|rel|snp):<40 hex>")

    composition = _require_object(record, "composition", errors)
    if composition is not None:
        _reject_unknown(composition, "composition", ("spdx",), errors)
        _require_string(composition, "composition", "spdx", errors)

    builds = record.get("builds")
    if builds is not None and not isinstance(builds, list):
        errors.append("builds must be an array")
    for index, build in enumerate(builds or []):
        if not isinstance(build, dict):
            errors.append(f"builds[{index}] must be an object")
            continue
        _reject_unknown(build, f"builds[{index}]", BUILD_FIELDS, errors)
        _require_string(build, f"builds[{index}]", "target", errors)
        if not isinstance(build.get("digest"), str) or not SHA256.fullmatch(build.get("digest", "")):
            errors.append(f"builds[{index}].digest must be lowercase sha256")
        if not isinstance(build.get("reproducible"), bool):
            errors.append(f"builds[{index}].reproducible must be a boolean")

    extensions = record.get("extensions")
    if extensions is not None and not isinstance(extensions, dict):
        errors.append("extensions must be an object")
    return errors


def main(path):
    record = json.loads(Path(path).read_text(encoding="utf-8"))
    errors = validate(record)
    if errors:
        print("STSB FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("STSB PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
