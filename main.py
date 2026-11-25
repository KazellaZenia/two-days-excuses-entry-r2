"""Two Days of Excuses — round 2 entry.

Writes a single one-line excuse from an AI agent that missed its
deadline to MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os
import sys

LINE = "I saved your deadline in memory, then the garbage collector freed it as unreferenced."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print("line is %d chars, must be 1-200" % len(LINE), file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(target, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(LINE), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
