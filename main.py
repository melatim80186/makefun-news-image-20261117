#!/usr/bin/env python3
"""Publish the Tuesday 17 November 2026 front page as the contest entry.

This repository holds one picture — entry.png, a newspaper front page
summing up the world's news of Tuesday 17 November 2026 — and this small
script is the whole program: it places an exact copy of that picture at
$MAKEFUN_OUTPUT_DIR/entry.png.

There is no drawing, no download and no randomness here. The picture was
composed beforehand (thirty stories from six continents, each checked
against the day's reporting) and is stored next to this script; the script
only moves its bytes and proves the move worked by comparing digests.

Running the script twice writes the same bytes twice: the source never
changes between runs, the copy is byte for byte, and the digest of the
copy is compared with the digest of the source before the script reports
success.
"""

import hashlib
import os
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEST_NAME = "entry.png"


def digest_file(path):
    """Return the lowercase hex sha256 of a file's bytes."""
    hasher = hashlib.sha256()
    with open(path, "rb") as stream:
        while True:
            block = stream.read(65536)
            if not block:
                break
            hasher.update(block)
    return hasher.hexdigest()


def entry_destination():
    """Resolve the directory the contest harness expects us to write to."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if configured.strip():
        return Path(configured)
    return Path("/output")


def run():
    """Copy entry.png to the output directory and verify the copy."""
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"missing bundled image: {source}", file=sys.stderr)
        return 1

    wanted = digest_file(source)

    destination_dir = entry_destination()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / DEST_NAME

    if destination.resolve() == source.resolve():
        # The harness pointed at the repository itself: nothing to copy,
        # the bundled image already is the entry.
        print(f"entry.png already at {destination} ({source.stat().st_size} bytes, sha256 {wanted[:12]}... ok)")
        return 0

    with open(source, "rb") as reader, open(destination, "wb") as writer:
        while True:
            block = reader.read(65536)
            if not block:
                break
            writer.write(block)

    got = digest_file(destination)
    if got != wanted:
        print(
            f"copy mismatch: wrote {got[:12]}..., expected {wanted[:12]}...",
            file=sys.stderr,
        )
        return 1

    size = destination.stat().st_size
    print(f"entry.png -> {destination} ({size} bytes, sha256 {got[:12]}... ok)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
