import json

from json_analyzer import JSONAnalyzer


def test_load_and_validate_schema(tmp_path):
    payload = {"name": "demo", "version": "1.0.0", "items": [1, 2, 2]}
    json_file = tmp_path / "sample.json"
    json_file.write_text(json.dumps(payload), encoding="utf-8")

    analyzer = JSONAnalyzer(str(json_file))
    assert analyzer.load() is True

    result = analyzer.validate_schema(["name", "version", "missing_key"])
    assert result["valid"] is False
    assert result["found_keys"] == ["name", "version"]
    assert result["missing_keys"] == ["missing_key"]


def test_find_duplicates_reports_paths_and_values(tmp_path):
    payload = {
        "items": ["a", "b", "a"],
        "nested": {"numbers": [1, 2, 2]},
    }
    json_file = tmp_path / "dups.json"
    json_file.write_text(json.dumps(payload), encoding="utf-8")

    analyzer = JSONAnalyzer(str(json_file))
    assert analyzer.load() is True

    duplicates = analyzer.find_duplicates()

    assert len(duplicates) == 2
    assert {dup["path"] for dup in duplicates} == {"root.items", "root.nested.numbers"}
    assert {dup["value"] for dup in duplicates} == {"a", 2}
