"""Live card addressing, authored collection traversal, and source context."""

from __future__ import annotations

import argparse
import csv
import random
import re
import subprocess
import sys
from dataclasses import dataclass
from functools import cache, cached_property
from pathlib import Path

import yaml
from pydantic import TypeAdapter

from .emit import _collection_source_links
from .model import Card, CollectionCard, CompilationSource, TextbookSource, discover, parse_card, parse_cards, split_front_matter

CARD_ADAPTER: TypeAdapter[Card] = TypeAdapter(Card)
ID_FIELD = re.compile(r"^(id|'id'|\"id\")\s*:")


@dataclass(frozen=True)
class Location:
    collection: CollectionCard
    section: str
    position: int
    comment: str | None

    def label(self) -> str:
        parts = [self.collection.id, self.section, f"entry {self.position}"]
        if self.comment is not None:
            parts.append(self.comment)
        return " / ".join(part for part in parts if part)


@dataclass(frozen=True)
class Appearance:
    card_id: str
    locations: tuple[Location, ...]


def identity(path: Path) -> str | None:
    """Read only the authored scalar id field, even during edits to other fields.

    Corpus IDs occupy one top-level YAML line. No body parsing or filename-based
    identity inference is needed to address a card that is being edited.
    """
    with path.open() as stream:
        if stream.readline() != "---\n":
            return None
        for line in stream:
            if line.rstrip() == "---":
                break
            if ID_FIELD.match(line):
                value = yaml.load(line, Loader=yaml.CSafeLoader)["id"]
                if not isinstance(value, str) or not value:
                    raise ValueError(f"{path}: id must be a nonempty scalar on one YAML line")
                return value
    return None


class Corpus:
    def __init__(self, root: Path):
        self.root = root.resolve()

    @cached_property
    def addresses(self) -> dict[str, list[Path]]:
        addresses: dict[str, list[Path]] = {}
        for path in discover(self.root / "corpus"):
            card_id = identity(path)
            if card_id is not None:
                if card_id not in addresses:
                    addresses[card_id] = []
                addresses[card_id].append(path)
        return addresses

    def resolve(self, reference: str) -> Path:
        path = self.root / reference
        if path.is_dir():
            path = path / "index.md"
        if not path.is_file():
            if reference not in self.addresses:
                raise ValueError(f"Cannot resolve card ID or corpus path: {reference}")
            matches = self.addresses[reference]
            if len(matches) != 1:
                raise ValueError(f"Ambiguous card ID {reference}: {', '.join(map(str, matches))}")
            path = matches[0]
        path = path.resolve()
        if not path.is_relative_to(self.root / "corpus") or path.suffix != ".md":
            raise ValueError(f"Card must be a Markdown file under corpus/: {path}")
        return path

    @cache
    def header(self, path: Path) -> Card:
        meta, _ = split_front_matter(path.read_text(), path)
        return CARD_ADAPTER.validate_python(meta)

    def collection(self, reference: str) -> CollectionCard:
        card = self.header(self.resolve(reference))
        if not isinstance(card, CollectionCard):
            raise ValueError(f"Expected a collection: {reference}")
        return card

    def appearances(self, reference: str, section: str = "", trail: tuple[Location, ...] = ()) -> list[Appearance]:
        collection = self.collection(reference)
        if collection.id in [location.collection.id for location in trail]:
            raise ValueError(f"Collection cycle: {' -> '.join([location.collection.id for location in trail] + [collection.id])}")
        source = collection.source
        if isinstance(source, TextbookSource) or isinstance(source, CompilationSource) and source.sections:
            groups = [(group.name, group.problems) for group in source.sections]
        else:
            groups = [("", source.problems)]
        if section:
            selected = [(name, entries) for name, entries in groups if name == section]
            if len(selected) != 1:
                raise ValueError(f"Section must match exactly one authored name in {collection.id}: {section!r}")
            groups = selected
        appearances = []
        for name, entries in groups:
            for position, entry in enumerate(entries, 1):
                locations = (*trail, Location(collection, name, position, entry.comment))
                if entry.id.startswith("SRC-"):
                    appearances.extend(self.appearances(entry.id, trail=locations))
                else:
                    appearances.append(Appearance(entry.id, locations))
        return appearances

    def context(self, path: Path) -> str:
        card_id = identity(path)
        if card_id is None:
            raise ValueError(f"{path}: no scalar id field in front matter")
        lines = [f"Card: {card_id}", f"Path: {path.relative_to(self.root)}", "", "Recorded source context:"]
        if card_id.startswith("SRC-"):
            collections = [self.collection(card_id)]
        else:
            collections = []
            for collection_id in self.addresses:
                if not collection_id.startswith("SRC-"):
                    continue
                for appearance in self.appearances(collection_id):
                    if appearance.card_id == card_id:
                        lines.append("- " + " > ".join(location.label() for location in appearance.locations))
                        for location in appearance.locations:
                            if location.collection not in collections:
                                collections.append(location.collection)
        for collection in collections:
            lines.append(f"\n{collection.id}: {collection.title}")
            lines.append(f"Collection card: {self.resolve(collection.id).relative_to(self.root)}")
            links = _collection_source_links(self.root, collection.provenance)
            lines.extend(f"{link['label']}: {link['href']}" for link in links)
            if not links:
                lines.append("Provenance list is empty.")
        if not collections:
            lines.append("No authored collection membership references this card.")
        return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("path", "read", "diff", "check", "commit"):
        command = commands.add_parser(name)
        command.add_argument("card", help="card ID or corpus Markdown path")
        if name == "commit":
            command.add_argument("message")
    for name in ("list", "unsolved", "sample"):
        command = commands.add_parser(name)
        command.add_argument("collection", help="collection ID, index path, or directory containing index.md")
        if name == "sample":
            command.add_argument("count", type=int)
        command.add_argument("section", nargs="?", default="", help="exact authored section name; omitted means all")
    args = parser.parse_args()
    corpus = Corpus(Path.cwd())
    try:
        if args.command in ("list", "unsolved", "sample"):
            if args.command == "sample" and args.count <= 0:
                raise ValueError("sample count must be positive")
            appearances = corpus.appearances(args.collection, args.section)
            paths = {item.card_id: corpus.resolve(item.card_id) for item in appearances}
            headers = {card_id: corpus.header(path) for card_id, path in paths.items()}
            if args.command != "list":
                parsed, errors = parse_cards(list(paths.values()))
                if errors:
                    raise ValueError("\n".join(map(str, errors)))
                unsolved = {item.card.id for item in parsed if item.card.kind == "problem" and not any(kind == "solution" for kind, _ in item.sections)}
                appearances = [item for item in appearances if item.card_id in unsolved]
            if args.command == "sample":
                selected_ids = random.sample(list(dict.fromkeys(item.card_id for item in appearances)), min(args.count, len({item.card_id for item in appearances})))
                appearances = [item for item in appearances if item.card_id in selected_ids]
            writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
            writer.writerow(("id", "path", "title", "collection", "section", "position", "comment", "via"))
            for item in appearances:
                location = item.locations[-1]
                writer.writerow(
                    (
                        item.card_id,
                        paths[item.card_id].relative_to(corpus.root),
                        headers[item.card_id].title,
                        location.collection.id,
                        location.section,
                        location.position,
                        location.comment,
                        " > ".join(step.label() for step in item.locations[:-1]),
                    )
                )
            return 0
        path = corpus.resolve(args.card)
        relative = str(path.relative_to(corpus.root))
        if args.command == "path":
            print(relative)
        elif args.command == "read":
            print(corpus.context(path) + "\n\n--- Authored card ---\n")
            print(path.read_text(), end="")
        elif args.command == "check":
            card = parse_card(path)
            print(f"{card.card.id}: schema and Markdown parsing OK (single card)")
        elif args.command == "diff":
            subprocess.run(["git", "--literal-pathspecs", "diff", "HEAD", "--", relative], check=True)
        elif args.command == "commit":
            subprocess.run(["git", "--literal-pathspecs", "ls-files", "--error-unmatch", "--", relative], check=True, stdout=subprocess.DEVNULL)
            subprocess.run(["git", "--literal-pathspecs", "commit", "--only", "--no-verify", "-m", args.message, "--", relative], check=True)
    except (ValueError, TypeError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"{exc}\n")
    except subprocess.CalledProcessError as exc:
        return exc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
