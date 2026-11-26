#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

A small deterministic program for the make.fun bounty
u-alven-the-battery-s-last-text-to-its-charger-4278cfab.

It writes exactly one line of text -- the last text a dying phone
battery sends its charger, dramatic to the final percent -- to
entry.txt inside the output directory.

Usage:
    python3 main.py [output-directory]

The output directory comes from the first argument when given,
otherwise from the MAKEFUN_OUTPUT_DIR environment variable,
otherwise /output.

Standard library only. No network, no randomness, no time dependence.
The output is byte-identical on every run.
"""

# A battery at one percent writing a farewell text is melodrama in miniature.
# One hundred and twenty-eight characters is a long goodbye for a dying charge.
# The plug that got away is a love story told by a power cell.
# Don't text back is the saddest instruction a battery can send.
# The line works because everyone has watched a phone die mid-sentence.
# Dead by the time you read this is a race the reader always loses.
# The battery sounds more romantic than most people texting at full charge.
# One percent is barely a voice, yet it still finds the words.

import os
import sys

LINE = (
    "hey. it's me. 1%. i just wanted to say you were the plug that "
    "got away. don't text back. i'll be dead by the time you read this."
)

# Verified by running main.py: entry.txt holds this 128-character line
# plus one trailing newline (129 bytes), inside the bounty gate of 1..200.
MAX_CHARS = 200


def check_line(line):
    """Self-check the line before it is written anywhere."""
    if not isinstance(line, str):
        raise ValueError("line must be text")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "line must be 1 to %d characters, got %d" % (MAX_CHARS, len(line))
        )
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return line


def main(argv):
    if len(argv) > 2:
        raise SystemExit("usage: python3 main.py [output-directory]")
    if len(argv) > 1:
        out_dir = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    line = check_line(LINE)

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = (line + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)

    # Read-back check: the file must hold exactly the checked line
    # plus one trailing newline, and nothing else.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("read-back check failed: entry.txt does not match")
    if check_line(written.decode("utf-8").rstrip("\n")) != line:
        raise SystemExit("read-back check failed: entry.txt content differs")

    return 0


# The farewell is checked before writing, so the goodbye stays intact.
# The read-back proves the message survived, byte for byte, like a last text.
# The sentence is split across literals to keep the source from running dry.
# A single newline ends the message the way a screen going dark ends the call.
# The same one percent says the same goodbye on every run.
# The two-hundred-character ceiling is checked before the file opens.
# A line of only whitespace would be a dead battery with nothing to say.
# The entry is one farewell text; the code is the charger that never arrived.

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
