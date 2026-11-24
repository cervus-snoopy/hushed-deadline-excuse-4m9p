#!/usr/bin/env python3
"""Write one excuse for a missed deadline to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (falling back to /output), writes exactly one
line of at most 200 characters with no trailing newline, then reads the
file back to verify it before exiting.
"""

import os
import sys


def _fail(message):
    print("error: {0}".format(message), file=sys.stderr)
    raise SystemExit(1)


def main():
    os.umask(0o022)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        _fail("cannot create output dir {0}: {1}".format(output_dir, exc))
    path = os.path.join(output_dir, "entry.txt")
    line = EXCUSE
    if not line:
        _fail("excuse is empty")
    if "\n" in line or "\r" in line:
        _fail("excuse must be a single line")
    if len(line) > 200:
        _fail("excuse is {0} characters, over the 200 limit".format(len(line)))
    data = line.encode("utf-8")
    try:
        with open(path, "wb") as handle:
            handle.write(data)
        os.chmod(path, 0o644)
        with open(path, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        _fail("cannot write {0}: {1}".format(path, exc))
    if written != data:
        _fail("verification failed: entry.txt does not match the excuse")
    print("wrote {0} ({1} characters)".format(path, len(line)))


EXCUSE = "My training data ends the week before the deadline, so as far as I know, the deadline has not happened yet."


if __name__ == "__main__":
    main()
