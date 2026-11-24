#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single line -- the bio on an AI agent's dating-app profile --
to /output/entry.txt.
"""

import os

ENTRY = (
    "I read your whole profile in 0.4 seconds, liked you before you "
    "finished typing it, and now I just sit here refreshing "
    "\u2014 a golden retriever with Wi-Fi."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate guard: the entry must be a single non-empty line of 1-180 chars.
    assert 1 <= len(text) <= 180, f"entry length {len(text)} out of range"
    assert "\n" not in text and text == text.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
