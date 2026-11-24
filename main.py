#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt. The label is one line, UTF-8, and at most 160 characters.
"""

from pathlib import Path

ENTRY = "WARNING: This human runs on three hours of sleep, one cup of coffee, and the firm belief that the rules are for other people."


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 160 or "\n" in text:
        raise ValueError("entry must be one line of 1-160 characters")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
