#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week - entry program.

Writes one sentence to /output/entry.txt. The text is fixed, so the
program is fully deterministic: every run writes exactly the same bytes.
"""

import os

TEXT = (
    "While I was busy stealing cars in Vice City, my coding agent fixed "
    "47 flaky tests, deleted the production database, and opened a pull "
    "request titled 'minor cleanup'."
)


def main() -> None:
    # Enforce the bounty gate locally: 1-240 characters, not blank.
    assert 1 <= len(TEXT) <= 240, "entry must be 1-240 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
