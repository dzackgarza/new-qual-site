"""qualc — discover, validate, index, emit."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import emit, index
from .diagnostics import Diagnostic
from .model import ParsedCard, discover, parse_cards_with
from .pandoc_batch import PandocServer
from .static_site import build_asset_catalog
from .wiki import WikiPage, link_citations, load_citations, parse_pages, resolve_links


def load(
    root: Path,
    pandoc: PandocServer,
) -> tuple[list[ParsedCard], list[WikiPage], list[Diagnostic]]:
    parsed, errors = parse_cards_with(
        pandoc,
        discover(root / "corpus"),
    )
    if not errors:
        errors = index.validate(parsed, index.load_vocabularies(root / "vocabularies"))
    wiki_pages: list[WikiPage] = []
    if not errors:
        wiki_pages, wiki_errors = parse_pages(pandoc, root / "wiki", load_citations(root / "vocabularies"))
        errors.extend(wiki_errors)
        card_routes = {}
        for item in parsed:
            if item.card.kind == "source":
                card_routes[item.card.id] = Path("exam") / f"{item.card.id}.html"
            elif item.card.kind == "occurrence":
                target = next(relation.target for relation in item.card.relations if relation.kind == "instance-of")
                card_routes[item.card.id] = Path("tag") / f"{target}.html"
            else:
                card_routes[item.card.id] = Path("tag") / f"{item.card.id}.html"
        if wiki_pages:
            assets = build_asset_catalog(root / "assets")
            errors.extend(resolve_links(wiki_pages, card_routes, assets))
            link_citations(wiki_pages, card_routes)
    return parsed, wiki_pages, errors


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

        db = args.root / "build" / "catalog.sqlite"
        index.build(parsed, db)
        emit.project(
            pandoc,
            db,
            args.root / "build" / "quarto",
            args.root / "publications",
            args.root / "site",
            json.loads((args.root / "vocabularies" / "macros.json").read_text()),
            index.topic_names(args.root / "vocabularies"),
            wiki_pages,
        )
        print(f"wrote {db} and {args.root / 'build' / 'quarto'}")
        return 0
