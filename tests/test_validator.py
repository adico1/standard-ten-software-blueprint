import copy
import json
from pathlib import Path

from validator import validate


BASE = json.loads((Path(__file__).parents[1] / "examples" / "calculator.json").read_text())


def test_reference_blueprint_passes():
    assert validate(BASE) == []


def test_unknown_root_fails():
    record = copy.deepcopy(BASE)
    record["function"]["primary"] = "unknown"
    record["function"]["capabilities"] = ["unknown"]
    assert validate(record)


def test_primary_must_be_capability():
    record = copy.deepcopy(BASE)
    record["function"]["capabilities"] = ["record"]
    assert validate(record)


def test_unknown_top_level_field_fails():
    record = copy.deepcopy(BASE)
    record["surprise"] = True
    assert validate(record)
