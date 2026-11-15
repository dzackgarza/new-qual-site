"""qualc — discover, validate, index, emit."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import panflute as pf

from . import certificates as certificate
from . import emit, index, runrecord
from .diagnostics import Diagnostic, DiagnosticCode
from .lamport import LamportError, apply_lamport
from .model import ParsedCard, discover, load_citations, parse_cards_with, to_json, typeset_dashes
from .pandoc_batch import PandocServer
from .publication import ReferenceItem, load_publications
from .static_site import build_asset_catalog
from .tex import unrenderable_tex
from .wiki import WikiPage, link_card_citations, link_citations, parse_pages, resolve_links, title_card_links, validate_wiki_sources, validate_wiki_tree


def load(
    root: Path,
    pandoc: PandocServer,
    checks: list[dict[str, Any]] | None = None,
) -> tuple[list[ParsedCard], list[WikiPage], list[Diagnostic]]:
    # Every stage runs whatever the stages before it found. Stopping at the first
    # failing stage hid every independent error behind whichever sorted first, so a
    # run with k errors cost k full passes (issue #89).
    #
    # Each check is timed as it runs, into `checks`, which is what the run's
    # record keeps (issue #145). `qualc` reports no duration of its own, so this
    # is the one place a clock is the right source rather than a second
    # measurement beside the tool's own.
    timed = [] if checks is None else checks
    errors: list[Diagnostic] = []
    with runrecord.check(timed, "parse-cards", errors):
        parsed, card_errors = parse_cards_with(
            pandoc,
            discover(root / "corpus"),
        )
        errors.extend(card_errors)
    with runrecord.check(timed, "load-certificates"):
        certificates = certificate.load(root / "proofs")
    with runrecord.check(timed, "validate-index", errors):
        errors.extend(index.validate(parsed, index.load_vocabularies(root / "vocabularies", root / "wiki"), certificates, root))
    with runrecord.check(timed, "parse-wiki-pages", errors):
        wiki_pages, wiki_errors = parse_pages(pandoc, root / "wiki", load_citations(root / "vocabularies"))
        errors.extend(wiki_errors)
    with runrecord.check(timed, "link-card-citations"):
        card_routes = {}
        card_titles = {}
        for item in parsed:
            card_titles[item.card.id] = typeset_dashes(item.card.title)
            card_routes[item.card.id] = Path(index.card_route(item.card)) / f"{item.card.id}.html"
        parsed = [item.model_copy(update={"ast": link_card_citations(title_card_links(item.ast, card_titles), card_routes)}) for item in parsed]
    if wiki_pages:
        with runrecord.check(timed, "validate-wiki-tree", errors):
            assets = build_asset_catalog(root / "assets")
            errors.extend(validate_wiki_tree(wiki_pages))
            errors.extend(validate_wiki_sources(root / "wiki"))
        with runrecord.check(timed, "resolve-wiki-links", errors):
            errors.extend(resolve_links(wiki_pages, card_routes, card_titles, assets))
        with runrecord.check(timed, "link-citations"):
            link_citations(wiki_pages, card_routes)
    with runrecord.check(timed, "publication-references", errors):
        errors.extend(_publication_references(root, {item.card.id for item in parsed}))
    with runrecord.check(timed, "unrenderable-tex"):
        preamble = json.loads((root / "vocabularies" / "macros.json").read_text())
        documents = [(item.source_path, item.ast) for item in parsed]
        documents.extend((str(page.source_path), to_json(pf.Doc(*page.blocks))) for page in wiki_pages)
        errors.extend(unrenderable_tex(pandoc, documents, preamble))
    with runrecord.check(timed, "lamport-proofs", errors):
        for (where, _), result in zip(documents, apply_lamport([ast for _, ast in documents], "html"), strict=True):
            if isinstance(result, LamportError):
                errors.append(Diagnostic(DiagnosticCode.LAMPORT_PROOF_INVALID, where, result.message))
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


def build_search_index(site: Path) -> None:
    """Index the emitted pages, so a reader downloads a query and not a corpus.

    Pagefind shards the index by term and writes one fragment per page, so a
    search fetches a shard and the pages it shows, rather than every record.
    The pages it indexes are the ones carrying `data-pagefind-body`, which the
    shell puts on the documents and withholds from the listings.

    The binary is the `pagefind[bin]` project dependency, pinned in
    pyproject.toml: the index the browser reads and the reader that reads it
    ship together.
    """
    subprocess.run([sys.executable, "-m", "pagefind", "--site", str(site)], check=True)


def build_catalog(root: Path, parsed: list[ParsedCard]) -> Path:
    db = root / "build" / "catalog.sqlite"
    index.build(
        parsed,
        db,
        index.load_institution_names(root / "vocabularies"),
        certificate.load(root / "proofs"),
    )
    return db


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="qualc")
    ap.add_argument("command", choices=["check", "build"])
    ap.add_argument("--root", type=Path, default=Path.cwd())
    # Diagnostics carry a stable `code`; `--json` exposes it so a caller can
    # assert which check failed instead of grepping the human wording.
    ap.add_argument("--json", action="store_true", help="emit diagnostics as JSON on stderr")
    args = ap.parse_args(argv)

    # The run's record (issue #145): every check is timed into `checks` as it
    # runs, and the record is written on both exits, so a failed run's timings
    # are kept too. A checkout with no commit to name the run by writes none.
    checks: list[dict[str, Any]] = []
    run = runrecord.new_run(runrecord.QUALC_CHECK if args.command == "check" else runrecord.QUALC_BUILD, args.root)
    clock = time.perf_counter()

    def record(exit_status: int, parsed: int = 0, pages: int = 0, diagnostics: int = 0) -> None:
        if run is None:
            return
        try:
            printed = run.write(
                exit_status=exit_status,
                wall_seconds=time.perf_counter() - clock,
                entries={
                    "command": args.command,
                    "cards": parsed,
                    "wiki_pages": pages,
                    "diagnostics": diagnostics,
                    "checks": checks,
                },
            )
        except OSError as error:
            # The record is bookkeeping; a check that ran is not a failure
            # because its record could not be written.
            print(f"could not write the run record: {error}", file=sys.stderr)
            return
        print(f"record: {printed}")

    with PandocServer() as pandoc:
        checks.append({"check": "pandoc-server", "seconds": round(time.perf_counter() - clock, 6), "errors": 0})
        parsed_cards, wiki_pages, errors = load(args.root, pandoc, checks)
        if errors:
            record(1, len(parsed_cards), len(wiki_pages), len(errors))
            if args.json:
                print(json.dumps([error.as_dict() for error in errors]), file=sys.stderr)
            else:
                print(f"{len(errors)} error(s):", file=sys.stderr)
                for error in errors:
                    print(f"  {error}", file=sys.stderr)
            return 1
        print(f"{len(parsed_cards)} cards and {len(wiki_pages)} wiki pages OK")
        if args.command == "check":
            record(0, len(parsed_cards), len(wiki_pages))
            return 0

        with runrecord.check(checks, "build-catalog"):
            db = build_catalog(args.root, parsed_cards)
        with runrecord.check(checks, "emit-site"):
            emit.project(
                pandoc,
                db,
                args.root / "build" / "quarto",
                args.root / "publications",
                args.root / "site",
                json.loads((args.root / "vocabularies" / "macros.json").read_text()),
                wiki_pages,
            )
        with runrecord.check(checks, "search-index"):
            build_search_index(args.root / "build" / "quarto" / "_site")
        record(0, len(parsed_cards), len(wiki_pages))
        print(f"wrote {db} and {args.root / 'build' / 'quarto'}")
        return 0
