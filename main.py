#!/usr/bin/env python3
"""Write the funniest excuse an agent gives for a missed deadline.

One line, 138 characters, deadpan: the agent finished on time, then its
context window compacted the memory of having done it.

The text is validated before it is written (1-200 characters, non-blank,
per the bounty gate) and read back afterwards to confirm the file holds
exactly the line that was validated.
"""

import os

LINE = "I finished the task on time, then my context window compacted the memory of having done it. The work exists. I just can no longer find it."


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt does not hold the validated line")


if __name__ == "__main__":
    main()
