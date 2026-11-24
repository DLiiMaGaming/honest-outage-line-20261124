#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes a single status page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while a
total server outage is under way.

Usage:
    python3 main.py                # writes /output/entry.txt (grader path)
    python3 main.py <path>         # writes to <path> (local testing)
"""

import sys
from pathlib import Path

ENTRY = (
    "Every server is down, including the one I would check to find out "
    "why. I cannot verify anything right now, and I will not guess."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def validate(entry):
    """Mirror the sealed gate scorer: UTF-8 text, 1-160 chars, not only
    whitespace, and a single line (no embedded newline)."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > 160:
        raise ValueError(f"entry is {len(entry)} characters, over the 160 limit")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return entry


def main(argv):
    validate(ENTRY)
    output_path = Path(argv[1]) if len(argv) > 1 else Path(DEFAULT_OUTPUT)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
