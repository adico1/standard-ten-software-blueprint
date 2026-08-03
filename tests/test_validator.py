import copy
import json
import unittest
from pathlib import Path

from validator import validate


BASE = json.loads((Path(__file__).parents[1] / "examples" / "calculator.json").read_text())


class ValidatorTests(unittest.TestCase):
    def test_reference_blueprint_passes(self):
        self.assertEqual(validate(BASE), [])

    def test_unknown_root_fails(self):
        record = copy.deepcopy(BASE)
        record["function"]["primary"] = "unknown"
        record["function"]["capabilities"] = ["unknown"]
        self.assertTrue(validate(record))

    def test_primary_must_be_capability(self):
        record = copy.deepcopy(BASE)
        record["function"]["capabilities"] = ["record"]
        self.assertTrue(validate(record))

    def test_unknown_top_level_field_fails(self):
        record = copy.deepcopy(BASE)
        record["surprise"] = True
        self.assertTrue(validate(record))

    def test_duplicate_capability_fails(self):
        record = copy.deepcopy(BASE)
        record["function"]["capabilities"] = ["compute", "compute"]
        self.assertTrue(validate(record))

    def test_malformed_digest_fails(self):
        record = copy.deepcopy(BASE)
        record["blueprint"]["seed_digest"] = "sha256:not-a-digest"
        self.assertTrue(validate(record))


if __name__ == "__main__":
    unittest.main()
