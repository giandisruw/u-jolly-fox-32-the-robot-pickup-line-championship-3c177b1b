"""The Robot Pickup Line Championship entry.

Writes a single robot pickup line (98 characters, within the 1-200
character gate) to /output/entry.txt. Fully deterministic: no network,
no randomness, no input.
"""

from pathlib import Path

LINE = "I asked my sensors for the most beautiful thing in the room. They pointed at you and then crashed."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Self-check the house gate before writing: 1-200 chars, one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
