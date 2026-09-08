"""Read-only card measurements for the serial authoring workflow."""

from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path

from .model import discover, parse_cards


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    live = commands.add_parser("unsolved", help="measure solution-section absence in one directory")
    live.add_argument("directory", type=Path)
    sample = commands.add_parser("sample", help="sample current candidates in one directory")
    sample.add_argument("directory", type=Path)
    sample.add_argument("count", type=int)
    args = parser.parse_args()
    root = Path.cwd()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")

    if args.command == "sample" and args.count <= 0:
        parser.error("sample count must be positive")
    directory = args.directory.resolve()
    if not directory.is_dir() or not directory.is_relative_to(root / "corpus"):
        parser.error("select an existing directory under corpus/")
    parsed, errors = parse_cards(discover(directory))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    candidates = [item for item in parsed if item.card.kind == "problem" and not any(kind == "solution" for kind, _ in item.sections)]
    if args.command == "sample":
        candidates = random.sample(candidates, min(args.count, len(candidates)))
    writer.writerow(("id", "path", "title"))
    for item in candidates:
        writer.writerow((item.card.id, Path(item.source_path).relative_to(root), item.card.title))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
