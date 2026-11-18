"""Regenerate `queues/D-prose-only-solutions.md`: every problem whose solution is prose.

A card leaves the queue by gaining a numbered step in its solution, so the file is a
measurement rather than a ledger: it is rewritten from the corpus and never hand-edited.
Issue #2 is what empties it, as it empties Queue C.

    just prose-only
    uv run python tools/prose_queue.py

There is no incremental mode here, unlike `tools/unsolved_queue.py`. That one projects
Queue C from committed card blobs with a fence-line regex, and no regex on the source
tells whether a step will be numbered -- the class structure has to be parsed. CI writes
this file from the corpus it has already parsed (`tools/backlog.py --with-queues`), so a
second parse is not on that path either.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from qualc import prose
from unsolved_queue import load_cards

REPO = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    out = root / prose.QUEUE
    out.parent.mkdir(parents=True, exist_ok=True)

    # Queue C's own parse and validate, reused rather than re-derived: two queues that
    # disagreed about what a card is would publish two different counts.
    rendered = prose.render(prose.measure(load_cards(root)))
    if out.exists() and out.read_text() == rendered:
        print(f"{out.relative_to(root)}: up to date")
        return
    out.write_text(rendered)
    print(f"{out.relative_to(root)}: rewritten")


if __name__ == "__main__":
    main()
