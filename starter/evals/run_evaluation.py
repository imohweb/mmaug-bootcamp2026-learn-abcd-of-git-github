"""Run the public synthetic fixture without a model API call."""

import json
from pathlib import Path

from app import analyze_sentiment


def main() -> None:
    fixture_path = Path(__file__).with_name("fixtures.json")
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    if not isinstance(fixtures, list) or not fixtures:
        raise ValueError("Evaluation fixture must be a non-empty list")
    failures = []
    for index, item in enumerate(fixtures, 1):
        if not isinstance(item, dict) or not {"text", "expected"} <= item.keys():
            raise ValueError(f"Evaluation item {index} must define text and expected")
        actual = analyze_sentiment(item["text"])
        if actual != item["expected"]:
            failures.append(f"Item {index}: expected {item['expected']!r}, got {actual!r}")
    if failures:
        raise AssertionError("\n".join(failures))
    print(f"Evaluation passed: {len(fixtures)}/{len(fixtures)}")


if __name__ == "__main__":
    main()
