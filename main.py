"""Writes one short text to entry.txt for a make.fun bounty entry."""

import os
import sys

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
