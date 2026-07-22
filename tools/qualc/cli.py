"""qualc — discover, validate, index, emit. Nothing else belongs here."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import emit, index
from .model import ParsedCard, discover, parse_card


def load(root: Path) -> tuple[list[ParsedCard], list[str]]:
    parsed, errors = [], []
    for path in discover(root / "corpus"):
        try:
            parsed.append(parse_card(path))
        except Exception as exc:  # schema violation in one card must not hide the rest
            errors.append(f"{path}: {exc}")
    if not errors:
        errors = index.validate(parsed, index.load_vocabularies(root / "vocabularies"))
    return parsed, errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="qualc")
    ap.add_argument("command", choices=["check", "build"])
    ap.add_argument("--root", type=Path, default=Path.cwd())
    args = ap.parse_args(argv)

    parsed, errors = load(args.root)
    if errors:
        print(f"{len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print(f"{len(parsed)} cards OK")
    if args.command == "check":
        return 0

    db = args.root / "build" / "catalog.sqlite"
    index.build(parsed, db)
    emit.project(
        db,
        args.root / "build" / "quarto",
        args.root / "publications",
        args.root / "site",
        json.loads((args.root / "vocabularies" / "macros.json").read_text()),
    )
    print(f"wrote {db} and {args.root / 'build' / 'quarto'}")
    return 0
