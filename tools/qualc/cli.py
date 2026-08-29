"""qualc — discover, validate, index, emit."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from . import emit, index
from .diagnostics import Diagnostic, DiagnosticCode
from .model import ParsedCard, discover, parse_cards_with
from .pandoc_batch import PandocServer
from .publication import ReferenceItem, load_publications
from .static_site import build_asset_catalog
from .wiki import WikiPage, link_citations, load_citations, parse_pages, resolve_links, validate_wiki_sources, validate_wiki_tree


def load(
    root: Path,
    pandoc: PandocServer,
) -> tuple[list[ParsedCard], list[WikiPage], list[Diagnostic]]:
    parsed, errors = parse_cards_with(
        pandoc,
        discover(root / "corpus"),
    )
    if not errors:
        errors = index.validate(parsed, index.load_vocabularies(root / "vocabularies", root / "wiki"))
    wiki_pages: list[WikiPage] = []
    if not errors:
        wiki_pages, wiki_errors = parse_pages(pandoc, root / "wiki", load_citations(root / "vocabularies"))
        errors.extend(wiki_errors)
        card_routes = {}
        card_titles = {}
        for item in parsed:
            card_titles[item.card.id] = item.card.title
            card_routes[item.card.id] = Path(index.card_route(item.card)) / f"{item.card.id}.html"
        if wiki_pages:
            assets = build_asset_catalog(root / "assets")
            errors.extend(validate_wiki_tree(wiki_pages))
            errors.extend(validate_wiki_sources(root / "wiki"))
            errors.extend(resolve_links(wiki_pages, card_routes, card_titles, assets))
            link_citations(wiki_pages, card_routes)
    if not errors:
        errors.extend(_publication_references(root, {item.card.id for item in parsed}))
    return parsed, wiki_pages, errors


def _publication_references(root: Path, known: set[str]) -> list[Diagnostic]:
    """A guide that names a card no longer in the corpus is a corpus error.

    It used to surface only at build time, on the first missing reference, so a
    merge that retired a duplicate id left `check` reporting the corpus sound
    and the build dying afterwards.
    """
    return [
        Diagnostic(
            DiagnosticCode.PUBLICATION_REFERENCE_MISSING,
            f"{manifest.id}/{section.slug}",
            f"names a card the corpus does not have: {item.ref}",
        )
        for manifest in load_publications(root / "publications")
        for section in manifest.sections
        for item in section.items
        if isinstance(item, ReferenceItem) and item.ref not in known
    ]


# Pinned: the index the browser reads and the reader that reads it ship
# together, and an unpinned build would change one of them without the other.
PAGEFIND = "pagefind@1.5.2"


def build_search_index(site: Path) -> None:
    """Index the emitted pages, so a reader downloads a query and not a corpus.

    Pagefind shards the index by term and writes one fragment per page, so a
    search fetches a shard and the pages it shows, rather than every record.
    The pages it indexes are the ones carrying `data-pagefind-body`, which the
    shell puts on the documents and withholds from the listings.
    """
    subprocess.run(["bunx", "--bun", PAGEFIND, "--site", str(site)], check=True)


def build_catalog(root: Path, parsed: list[ParsedCard]) -> Path:
    db = root / "build" / "catalog.sqlite"
    index.build(parsed, db)
    return db


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="qualc")
    ap.add_argument("command", choices=["check", "build"])
    ap.add_argument("--root", type=Path, default=Path.cwd())
    # Diagnostics carry a stable `code`; `--json` exposes it so a caller can
    # assert which check failed instead of grepping the human wording.
    ap.add_argument("--json", action="store_true", help="emit diagnostics as JSON on stderr")
    args = ap.parse_args(argv)

    with PandocServer() as pandoc:
        parsed, wiki_pages, errors = load(args.root, pandoc)
        if errors:
            if args.json:
                print(json.dumps([error.as_dict() for error in errors]), file=sys.stderr)
            else:
                print(f"{len(errors)} error(s):", file=sys.stderr)
                for error in errors:
                    print(f"  {error}", file=sys.stderr)
            return 1
        print(f"{len(parsed)} cards and {len(wiki_pages)} wiki pages OK")
        if args.command == "check":
            return 0

        db = build_catalog(args.root, parsed)
        emit.project(
            pandoc,
            db,
            args.root / "build" / "quarto",
            args.root / "publications",
            args.root / "site",
            json.loads((args.root / "vocabularies" / "macros.json").read_text()),
            wiki_pages,
        )
        build_search_index(args.root / "build" / "quarto" / "_site")
        print(f"wrote {db} and {args.root / 'build' / 'quarto'}")
        return 0
