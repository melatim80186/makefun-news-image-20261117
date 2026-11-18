# The World — Tuesday 17 November 2026

A make.fun **news-image-20261117** entry ($250, top 50 share): one image that
sums up the world's news of Tuesday 17 November 2026.

## The image

A cream newspaper front page — **30 stories across 6 continents** — built
from original AI-generated drawings (no text in the artwork) with every
word typeset crisply in PIL, so nothing garbles:

- **3 large stories:** Ukraine's strike collapses a span of the Kerch Bridge
  (the day's biggest story); tankers hit by mines near Hormuz as a third US
  carrier arrives; Trump lands in Manila for the ASEAN summit.
- **8 small numbered stories:** Iran fires drones at a US radar site in
  Bahrain; Houthis say they hit Saudi Arabia's East-West oil pipeline;
  Estonia to shut all Russia border crossings on 1 December; a ULA Vulcan
  rocket fails and destroys 40 Amazon satellites; JPMorgan blames a software
  bug for Monday's outage; DR Congo's Ebola outbreak is out of control;
  Nvidia's first earnings since Huang's exit; thirteen babies born with
  measles in the US.
- **ALSO ON TUESDAY 17 NOVEMBER:** stories 12–30, from UK sanctions on
  Israeli builders to WHO's warning that drug-resistant infections could
  kill 39 million over 25 years.

Every story happened or was first reported on 17 November 2026, verified
against BBC, Al Jazeera, AP, Reuters and AFP coverage. Sources are credited
in the image footer.

## The program

`main.py` (Python 3.13) copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies its sha256 — no network, no
randomness, byte-identical on every run.

- Image: 1024×1024 PNG, 799,149 bytes (under the 1 MiB limit)
- sha256: `e080ace0eac02141e70586bef6ed5d2b291ead3f308eba0f34c5f9cc8339dac6`

## Build

The front page is composed deterministically by `../build_entry.py` from
two AI-generated panel grids in `../assets/` (original drawings, no text).
Re-running the composer twice produces the identical PNG.

## License

MIT — see `LICENSE`.
