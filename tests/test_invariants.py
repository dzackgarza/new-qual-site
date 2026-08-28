"""Source paths do not contribute to card semantics."""

from __future__ import annotations

import shutil
import sqlite3
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import ClassVar

from conftest import write_subject_branches
from qualc.cli import build_catalog, load
from qualc.pandoc_batch import PandocServer

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class Element:
    tag: str
    attrs: dict[str, str]
    children: list[Element | str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return " ".join(child.text if isinstance(child, Element) else child for child in self.children).strip()

    def find_all(self, tag: str | None = None, **attrs: str) -> list[Element]:
        matches = []
        if (tag is None or self.tag == tag) and all(self.attrs.get(key) == value for key, value in attrs.items()):
            matches.append(self)
        for child in self.children:
            if isinstance(child, Element):
                matches.extend(child.find_all(tag, **attrs))
        return matches


class SemanticHtml(HTMLParser):
    VOID: ClassVar[set[str]] = {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
    }

    def __init__(self, source: str) -> None:
        super().__init__()
        self.root = Element("document", {})
        self.stack = [self.root]
        self.feed(source)

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        element = Element(tag, {key: value or "" for key, value in attrs})
        self.stack[-1].children.append(element)
        if tag not in self.VOID:
            self.stack.append(element)

    def handle_endtag(self, tag: str) -> None:
        if len(self.stack) > 1 and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_startendtag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.stack[-1].children.append(data.strip())


def read_html(path: Path) -> SemanticHtml:
    return SemanticHtml(path.read_text())


def catalog_rows(root: Path) -> dict[str, list[tuple]]:
    con = sqlite3.connect(root / "build" / "catalog.sqlite")
    return {
        "cards": con.execute("select id, kind, title, review, ast from cards order by id").fetchall(),
        "classifications": con.execute("select * from classifications order by 1,2,3").fetchall(),
        "relations": con.execute("select * from relations order by 1,2,3").fetchall(),
        "sources": con.execute("select * from sources order by id").fetchall(),
        "collection_problems": con.execute("select * from collection_problems order by collection_id, coalesce(section_ordinal, -1), ordinal").fetchall(),
        "collection_provenance": con.execute("select * from collection_provenance order by collection_id, ordinal").fetchall(),
        "sections": con.execute("select * from sections order by 1,3").fetchall(),
    }


def rebuild_catalog(root: Path) -> dict[str, list[tuple]]:
    with PandocServer() as pandoc:
        parsed, _, errors = load(root, pandoc)
    assert errors == []
    build_catalog(root, parsed)
    return catalog_rows(root)


def test_corpus_layout_is_semantically_inert(tmp_path: Path) -> None:
    work = tmp_path / "repo"
    shutil.copytree(ROOT / "tests" / "fixtures" / "kinds", work / "corpus")
    shutil.copytree(ROOT / "vocabularies", work / "vocabularies")
    write_subject_branches(work)

    before = rebuild_catalog(work)

    original = work / "original-layout"
    (work / "corpus").rename(original)
    flat = work / "corpus"
    flat.mkdir()
    for index, card in enumerate(sorted(original.rglob("*.md"))):
        card.rename(flat / f"{index:04d}.md")

    assert rebuild_catalog(work) == before
