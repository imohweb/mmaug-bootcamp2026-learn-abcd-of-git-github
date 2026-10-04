from pathlib import Path

import pytest

from app import analyze_sentiment


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("This is good", "positive"),
        ("A BAD experience", "negative"),
        ("The service exists", "neutral"),
        ("Good, great!", "positive"),
        ("Good but bad", "neutral"),
        ("Goodness is not a keyword", "neutral"),
    ],
)
def test_sentiment(value, expected):
    assert analyze_sentiment(value) == expected


@pytest.mark.parametrize("value", ["", " ", "\n\t"])
def test_blank_input_is_rejected(value):
    with pytest.raises(ValueError, match="Input must not be blank"):
        analyze_sentiment(value)


@pytest.mark.parametrize("value", [None, 42, []])
def test_non_string_input_is_rejected(value):
    with pytest.raises(TypeError, match="Input must be a string"):
        analyze_sentiment(value)


def test_prompt_is_not_blank():
    prompt = Path("prompts/system.txt").read_text(encoding="utf-8")
    assert prompt.strip(), "Prompt must not be empty"
