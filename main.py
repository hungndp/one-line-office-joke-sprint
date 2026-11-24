#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes the single office-joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), where the make.fun gate checks it is UTF-8 text of
1 to 200 characters on exactly one line.
"""

import os

MAX_CHARS = 200  # gate cap for this competition

TEXT = (
    "I replied all to 4,000 colleagues to say 'please stop replying all' "
    "\u2014 I am now the reason that button asks 'are you sure?'."
)

# The gate requires exactly one line of 1-200 UTF-8 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= MAX_CHARS, "entry line violates the gate"
assert TEXT == TEXT.strip(), "line must not start or end with whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
