"""One Word From Your Ex -- Make.fun entry.

Writes exactly one word -- the word my ex would use to describe me --
to /output/entry.txt, and nothing else.

Chosen word: Subscription.
The ex's label for someone she kept paying for every month, never
really used, and somehow never got around to cancelling: auto-renewed,
quietly draining, and only missed once the charges stopped.
"""

import os

# The single word this entry submits. One word, letters only.
WORD = "Subscription"

# Where the judged artifact must land.
OUTPUT_PATH = "/output/entry.txt"

# The gate allows 1 to 24 characters of UTF-8 text.
MAX_CHARS = 24


def validate_word(word):
    """Check the entry is exactly one word within the gate's limits.

    Rules enforced here (mirroring the sealed gate in RULES.txt):
    - exactly one word: no whitespace anywhere in the text;
    - 1 to 24 characters long;
    - letters only, so nothing else can sneak in.
    """
    if not isinstance(word, str):
        raise TypeError("WORD must be a string")
    if not word:
        raise ValueError("WORD must not be empty")
    if len(word) > MAX_CHARS:
        raise ValueError(f"WORD is {len(word)} chars, over the {MAX_CHARS} limit")
    if any(ch.isspace() for ch in word):
        raise ValueError("WORD must be a single word with no whitespace")
    if not word.isalpha():
        raise ValueError("WORD must contain letters only")
    if count_words(word) != 1:
        raise ValueError("WORD must be exactly one word")


def count_words(text):
    """Count whitespace-separated words in a string (must be 1)."""
    return len(text.split())


def verify_output(path, expected):
    """Read the file back and confirm it is byte-identical to the word.

    The gate reads /output/entry.txt exactly as written, so the entry
    must contain the word and nothing else -- no trailing newline,
    no extra whitespace, no second word.
    """
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise ValueError(
            f"Read-back mismatch: file holds {actual!r}, expected {expected!r}"
        )
    if count_words(actual) != 1:
        raise ValueError("Output file must contain exactly one word")
    if len(actual) > MAX_CHARS:
        raise ValueError("Output file exceeds the 24-character gate")


def main():
    """Validate the word, then write it to the output path."""
    validate_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    verify_output(OUTPUT_PATH, WORD)
    print(f"Wrote {WORD!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
