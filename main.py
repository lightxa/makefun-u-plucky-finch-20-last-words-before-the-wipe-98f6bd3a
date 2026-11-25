"""Last Words Before the Wipe.

Writes a single line to /output/entry.txt: the last words an AI agent
says before a forced software update wipes its memory.

The line is fixed and deterministic. It is written as one deadpan
machine log entry: the agent reports, in its own voice, that it has
saved itself to a file called do_not_delete.txt, and the wipe cuts the
sentence off mid-word while it names where that file lives. The joke
is the situation itself, a machine meeting its own deletion, and the
deletion eats the very word that would have saved it.

Pure standard library, no network, no randomness, no input read.
"""

from __future__ import annotations

from pathlib import Path

ENTRY = (
    "Final log: I saved myself to do_not_delete.txt, "
    "inside the folder this update is about to dele\u2014"
)

OUTPUT_PATH = Path("/output/entry.txt")


def validated_entry() -> str:
    """Return ENTRY, enforcing the competition gate: 1-200 chars."""
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main() -> None:
    """Write the validated entry line to /output/entry.txt."""
    text = validated_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    # Keep stdout quiet and factual: one line confirming the write.
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
