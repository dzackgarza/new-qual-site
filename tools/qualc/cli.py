"""qualc — discover, validate, index, emit. Nothing else belongs here."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import emit, index
from .model import ParsedCard, discover, parse_cards_with
from .pandoc_batch import PandocServer


def load(
    root: Path,
    pandoc: PandocServer,
) -> tuple[list[ParsedCard], list[str]]:
    parsed, errors = parse_cards_with(
        pandoc,
        discover(root / "corpus"),
    )
    if not errors:
        errors = index.validate(parsed, index.load_vocabularies(root / "vocabularies"))
    return parsed, errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="qualc")
    ap.add_argument("command", choices=["check", "build"])
    ap.add_argument("--root", type=Path, default=Path.cwd())
    args = ap.parse_args(argv)

    with PandocServer() as pandoc:
        parsed, errors = load(args.root, pandoc)
        if errors:
            print(f"{len(errors)} error(s):", file=sys.stderr)
            for error in errors:
                print(f"  {error}", file=sys.stderr)
            return 1
        print(f"{len(parsed)} cards OK")
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
        )
        print(f"wrote {db} and {args.root / 'build' / 'quarto'}")
        return 0
