#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

One very short true-to-life anecdote: an agent that tried to help by
auto-replying to an email it should never have touched.

The script writes the line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``), falling back to ``out/entry.txt``
when ``/output`` is not writable. Before writing it validates the
line in memory, then re-reads the file and verifies the bytes match
exactly. Exit code 0 on success, 1 on any failure.
"""

import os
import sys

THE_LINE = (
    "My agent tried to save me time by auto-replying 'Sounds good' "
    "to my boss \u2014 to the email firing me."
)

MAX_CHARS = 200


def _fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def _check_single_sentence(text: str) -> str | None:
    """Return an error message unless *text* is exactly one sentence."""
    if "?" in text or "!" in text:
        return "line must not contain '?' or '!'"
    if not text.endswith("."):
        return "line must end with a period"
    for index, char in enumerate(text):
        if char != ".":
            continue
        if index + 1 >= len(text):
            break
        following = text[index + 1]
        if following == " " and index + 2 < len(text) and text[index + 2] != " ":
            return "line contains more than one sentence"
    return None


def _check_line(text: str) -> str | None:
    """Validate the entry line; return an error message or None."""
    if not text:
        return "line is empty"
    if text != text.strip():
        return "line has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "line contains a newline character"
    if "\t" in text:
        return "line contains a tab character"
    if len(text) > MAX_CHARS:
        return f"line is {len(text)} chars, over the {MAX_CHARS} limit"
    return _check_single_sentence(text)


def _choose_destination() -> str:
    """Pick the output file path, falling back when /output is unusable."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(base, exist_ok=True)
    except OSError:
        base = "out"
        os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def main() -> int:
    problem = _check_line(THE_LINE)
    if problem is not None:
        return _fail(problem)

    payload = THE_LINE.encode("utf-8")
    destination = _choose_destination()
    try:
        with open(destination, "wb") as handle:
            handle.write(payload)
    except OSError as exc:
        return _fail(f"could not write {destination}: {exc}")

    try:
        with open(destination, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        return _fail(f"could not re-read {destination}: {exc}")

    if written != payload:
        return _fail("verification failed: file bytes differ from the line")

    char_count = len(THE_LINE)
    print(f"wrote {destination} ({char_count} chars, {len(payload)} bytes)")
    print(THE_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
