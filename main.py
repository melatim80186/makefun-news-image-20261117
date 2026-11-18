#!/usr/bin/env python3
"""news-image-20261117 entry: write the front page to $MAKEFUN_OUTPUT_DIR/entry.png.

The entry is the newspaper front page stored as entry.png next to this
file: a cream broadsheet for Tuesday 17 November 2026 with 30 stories
across 6 continents — 3 large and 8 small numbered stories, each with a
picture, a region tag, a headline and a short summary, plus an ALSO ON
TUESDAY 17 NOVEMBER strip listing stories 12-30.

Featured stories: Ukraine strikes the Kerch Bridge and a span collapses;
tankers hit mines near Hormuz as a third US carrier arrives; Trump lands
in Manila for the ASEAN summit; Iran fires drones at a US radar site in
Bahrain; Houthis say they hit Saudi Arabia's East-West oil pipeline;
Estonia to shut all Russia border crossings; a ULA Vulcan rocket fails
and destroys 40 Amazon satellites; JPMorgan blames a software bug for
Monday's outage; DR Congo's Ebola outbreak is out of control; Nvidia's
first earnings since Huang's exit; thirteen babies born with measles in
the US. The day's biggest story — the Kerch Bridge strike — leads.

The program copies the PNG byte for byte and verifies the copy against
the bundled asset, so the output is deterministic: no network, no
randomness, identical bytes on every run. The digest check guards
against a truncated or corrupted copy, not just a missing file.
"""
import hashlib
import os
import shutil
from pathlib import Path

# Expected digest of the bundled front page (sha256 of entry.png).
EXPECTED_SHA256 = "e080ace0eac02141e70586bef6ed5d2b291ead3f308eba0f34c5f9cc8339dac6"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if sha256_of(target) != EXPECTED_SHA256:
        raise SystemExit("entry.png copy failed verification")
    # Report the short digest so a log line alone proves which bytes landed.
    print(
        f"wrote {target} ({target.stat().st_size} bytes, "
        f"sha256 {EXPECTED_SHA256[:12]}… verified)"
    )


if __name__ == "__main__":
    main()
