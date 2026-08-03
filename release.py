#!/usr/bin/env python3
import json
import sys
import unittest
from pathlib import Path

from validator import validate

ROOT = Path(__file__).resolve().parent
REQUIRED = [
    "README.md", "SPECIFICATION.md", "CONTRIBUTING.md", "GOVERNANCE.md",
    "PRIOR-ART.md", "SECURITY.md", "CHANGELOG.md", "RELEASE_CHECKLIST.md",
    "LICENSE", "LICENSE-SPECIFICATION.md", "NOTICE", "CITATION.cff",
    "schemas/stsb.schema.json", "taxonomy/roots.json",
]


def main():
    failures = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            failures.append(f"missing required file: {name}")
    for path in sorted((ROOT / "examples").glob("*.json")):
        errors = validate(json.loads(path.read_text(encoding="utf-8")))
        if errors:
            failures.append(f"{path.name}: {'; '.join(errors)}")
    json.loads((ROOT / "schemas" / "stsb.schema.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "taxonomy" / "roots.json").read_text(encoding="utf-8"))
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        failures.append("unit tests failed")
    if failures:
        print("STSB RELEASE FAIL")
        for failure in failures:
            print("-", failure)
        return 1
    print(f"STSB RELEASE PASS: {len(list((ROOT / 'examples').glob('*.json')))} examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
