#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes the single roast line to /output/entry.txt (the file the
make.fun judge reads). The line must be 1-200 characters of UTF-8 text.
"""

import os

LINE = "My earbuds pair with my neighbour's TV faster than with my own phone, and honestly, the neighbour has better taste."


def main() -> None:
    # Self-check the competition gate before writing: 1-200 chars, not
    # only whitespace. Fail loudly instead of shipping an invalid entry.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"roast line fails the 1-200 char gate: {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
