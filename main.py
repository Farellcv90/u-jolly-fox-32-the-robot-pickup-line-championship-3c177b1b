"""The Robot Pickup Line Championship — one pickup line from a robot.

Joke angle
----------
The robot is a machine that logs everything and rehearses nothing —
except, apparently, this one greeting. The comedy is the gap between
the robot's cold bookkeeping ("according to my logs", a precise count
of 14,203 humans greeted) and the warm, very human confession hiding
inside it: it practiced. A speech module rehearsing a hello is the
machine equivalent of butterflies. Leading with the log framing keeps
the setup flat and bureaucratic, so the punchline — rehearsed for —
lands as the turn. First-person robot voice, one clean turn at the
end, no Wi-Fi, no bugs, no charging cable.
"""

ENTRY = (
    "According to my logs, I have greeted 14,203 humans. "
    "You're the first one my speech module rehearsed for."
)


def validate(text: str) -> bool:
    """Return True only if *text* passes the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace. Encoding to UTF-8 here also proves the text is valid
    UTF-8 (a str that fails to encode raises UnicodeEncodeError).
    A single-line entry must contain no line breaks either, so any
    newline or carriage return fails validation.
    """
    if not isinstance(text, str):
        return False
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main() -> None:
    """Write the entry line to /output/entry.txt after validating it."""
    if not validate(ENTRY):
        raise ValueError("entry failed validation: must be 1-200 non-blank chars")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
