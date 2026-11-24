#!/usr/bin/env python3
"""Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (at most 140 characters): the funniest excuse a robot
vacuum could offer for missing a spot, in the vacuum's own deadpan voice.
"""

import os

EXCUSE = (
    "My sensors say that dust has been there longer than my warranty, "
    "so legally it is furniture now."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main():
    line = EXCUSE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} chars, must be 1-140"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
