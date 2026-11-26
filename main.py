"""Entry point for the Funniest Time Machine Warning Label bounty.

Writes one warning label for a time machine to /output/entry.txt.
The line is at most 120 characters, deterministic, and needs no
network access. The joke lands on the classic rule: never meet
your past self — he is trouble, and he talks.
"""
from pathlib import Path

LINE = (
    "WARNING: Do not meet yourself. He owes you money, he knows "
    "things, and he will absolutely tell your mother."
)

TARGET = Path("/output/entry.txt")


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
