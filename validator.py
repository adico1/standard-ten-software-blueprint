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
TOP = {"schema", "identity", "function", "blueprint", "source", "composition", "builds", "extensions"}
REQUIRED = TOP - {"extensions"}


def validate(record):
    errors = []
    missing = REQUIRED - set(record)
    unknown = set(record) - TOP
    if missing:
        errors.append("missing top-level fields: " + ", ".join(sorted(missing)))
    if unknown:
        errors.append("unknown top-level fields: " + ", ".join(sorted(unknown)))
    if record.get("schema") != "stsb/0.1":
        errors.append("schema must equal stsb/0.1")
    function = record.get("function", {})
    primary = function.get("primary")
    capabilities = function.get("capabilities", [])
    if primary not in ROOTS:
        errors.append("primary is not a candidate root")
    if len(capabilities) != len(set(capabilities)):
        errors.append("capabilities must be unique")
    invalid = set(capabilities) - ROOTS
    if invalid:
        errors.append("invalid capabilities: " + ", ".join(sorted(invalid)))
    if primary not in capabilities:
        errors.append("primary must appear in capabilities")
    seed = record.get("blueprint", {}).get("seed_digest", "")
    if not SHA256.fullmatch(seed):
        errors.append("seed_digest must be lowercase sha256")
    for index, build in enumerate(record.get("builds", [])):
        if not SHA256.fullmatch(build.get("digest", "")):
            errors.append(f"builds[{index}].digest must be lowercase sha256")
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
