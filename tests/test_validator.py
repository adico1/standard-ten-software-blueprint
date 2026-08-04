import copy
import json
import unittest
from pathlib import Path

from validator import validate


BASE = json.loads((Path(__file__).parents[1] / "examples" / "calculator.json").read_text())


def errors_of(record):
    return validate(record)


class ValidatorTests(unittest.TestCase):
    def test_reference_blueprint_passes(self):
        self.assertEqual(validate(BASE), [])

    def test_unknown_root_fails(self):
        record = copy.deepcopy(BASE)
        record["function"]["primary"] = "unknown"
        record["function"]["capabilities"] = ["unknown"]
        errors = errors_of(record)
        self.assertIn("primary is not a candidate root", errors)
        self.assertIn("invalid capabilities: unknown", errors)

    def test_primary_must_be_capability(self):
        record = copy.deepcopy(BASE)
        record["function"]["capabilities"] = ["record"]
        self.assertIn("primary must appear in capabilities", errors_of(record))

    def test_unknown_top_level_field_fails(self):
        record = copy.deepcopy(BASE)
        record["surprise"] = True
        self.assertIn("unknown top-level fields: surprise", errors_of(record))

    def test_duplicate_capability_fails(self):
        record = copy.deepcopy(BASE)
        record["function"]["capabilities"] = ["compute", "compute"]
        self.assertIn("capabilities must be unique", errors_of(record))

    def test_malformed_digest_fails(self):
        record = copy.deepcopy(BASE)
        record["blueprint"]["seed_digest"] = "sha256:not-a-digest"
        self.assertIn("seed_digest must be lowercase sha256", errors_of(record))

    def test_missing_identity_field_fails(self):
        record = copy.deepcopy(BASE)
        del record["identity"]["authority"]
        self.assertIn("identity.authority must be a non-empty string", errors_of(record))

    def test_empty_identity_field_fails(self):
        record = copy.deepcopy(BASE)
        record["identity"]["product"] = ""
        self.assertIn("identity.product must be a non-empty string", errors_of(record))

    def test_unknown_identity_field_fails(self):
        record = copy.deepcopy(BASE)
        record["identity"]["nickname"] = "calc"
        self.assertIn("unknown identity fields: nickname", errors_of(record))

    def test_missing_function_family_fails(self):
        record = copy.deepcopy(BASE)
        del record["function"]["family"]
        self.assertIn("function.family must be a non-empty string", errors_of(record))

    def test_empty_capabilities_fails(self):
        record = copy.deepcopy(BASE)
        record["function"]["capabilities"] = []
        self.assertIn("function.capabilities must be a non-empty array", errors_of(record))

    def test_malformed_swhid_fails(self):
        record = copy.deepcopy(BASE)
        record["source"]["swhid"] = "swh:1:garbage"
        self.assertIn(
            "source.swhid must match swh:1:(cnt|dir|rev|rel|snp):<40 hex>", errors_of(record)
        )

    def test_missing_generator_fails(self):
        record = copy.deepcopy(BASE)
        del record["blueprint"]["generator"]
        self.assertIn("blueprint.generator must be a non-empty string", errors_of(record))

    def test_build_requires_reproducible_flag(self):
        record = copy.deepcopy(BASE)
        record["builds"] = [{"target": "linux-x86_64", "digest": "sha256:" + "a" * 64}]
        self.assertIn("builds[0].reproducible must be a boolean", errors_of(record))

    def test_build_rejects_unknown_field(self):
        record = copy.deepcopy(BASE)
        record["builds"] = [{
            "target": "linux-x86_64",
            "digest": "sha256:" + "a" * 64,
            "reproducible": True,
            "note": "x",
        }]
        self.assertIn("unknown builds[0] fields: note", errors_of(record))

    def test_extensions_allowed(self):
        record = copy.deepcopy(BASE)
        record["extensions"] = {"vendor": {"anything": 1}}
        self.assertEqual(errors_of(record), [])

    def test_non_object_record_fails(self):
        self.assertEqual(validate([]), ["record must be a JSON object"])


if __name__ == "__main__":
    unittest.main()
