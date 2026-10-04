"""A deterministic sentiment fixture for practicing Git, tests and CI."""

import argparse
import re


POSITIVE_WORDS = {"good", "great", "excellent", "love"}
NEGATIVE_WORDS = {"bad", "poor", "terrible", "hate"}


def analyze_sentiment(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    if not value.strip():
        raise ValueError("Input must not be blank")
    words = set(re.findall(r"[a-z]+", value.lower()))
    positive = len(words & POSITIVE_WORDS)
    negative = len(words & NEGATIVE_WORDS)
    if positive > negative:
        return "positive"
    if negative > positive:
        return "negative"
    return "neutral"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="Non-blank text to classify")
    args = parser.parse_args()
    try:
        result = analyze_sentiment(args.text)
    except ValueError as error:
        parser.error(str(error))
    print(result)


if __name__ == "__main__":
    main()
