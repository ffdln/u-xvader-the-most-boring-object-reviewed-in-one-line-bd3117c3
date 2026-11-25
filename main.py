#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — one review.

The entry is a single fixed review, written for make.fun
u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3: one
line of at most 200 characters reviewing the most boring everyday
object. A rubber band that spent four years doing nothing in a drawer
and snapped in my face the one time I needed it. This program writes
that review to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The review is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Four years in the drawer doing absolutely nothing, and the one "
    "time I needed it this rubber band snapped in my face — it had "
    "clearly been saving up the betrayal."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the review against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"review is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("review is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
