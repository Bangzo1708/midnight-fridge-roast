#!/usr/bin/env python3
"""Midnight Fridge Roast — one-line roast entry.

Writes a single roast line to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.
The line stays well inside the gate (1-200 characters) and is written
with no trailing newline so the file holds exactly the line itself.
"""

import os

ENTRY = "My smart fridge locks at midnight because the leftovers filed a restraining order against me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
