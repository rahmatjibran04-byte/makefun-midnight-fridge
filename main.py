#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry generator (stdlib only).

Writes exactly one line — the fridge roasting its owner at 2am — to
/output/entry.txt. Deterministic, no network access.
"""

import os

ENTRY = (
    "It's 2am, my light clicks on for you again, and I already know: "
    "you're not here for the salad you swore you'd eat — "
    "you're here to apologize to the cake."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not text.endswith((".", "!", "?")):
        raise ValueError("entry must end with terminal punctuation")


def main() -> None:
    validate(ENTRY)
    os.umask(0o022)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = (ENTRY + "\n").encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(data)} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
