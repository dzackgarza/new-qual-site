"""The architecture's load-bearing claim, as a runnable check.

Source layout, semantic structure, and publication structure are independent.
If moving a card between contributor subtrees changed the catalog, the corpus
tree would secretly be part of the data model.
"""

from __future__ import annotations

import json
import posixpath
import re
import shutil
import sqlite3
import subprocess
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import ClassVar
from urllib.parse import urljoin

import yaml

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
        self.starts: list[Element] = []
        self.feed(source)

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        element = Element(tag, {key: value or "" for key, value in attrs})
        self.stack[-1].children.append(element)
        self.starts.append(element)
        if tag not in self.VOID:
            self.stack.append(element)

    def handle_startendtag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        if len(self.stack) > 1 and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.stack[-1].children.append(data.strip())


def read_html(path: Path) -> SemanticHtml:
    return SemanticHtml(path.read_text())


def resolved_link(page: Path, href: str) -> str:
    return posixpath.normpath(urljoin(page.as_posix(), href))


def move_appearance(manifest_path: Path, card_id: str) -> None:
    manifest = yaml.safe_load(manifest_path.read_text())
    applications = next(section for section in manifest["sections"] if section["slug"] == "applications-and-problems")
    sylow = next(section for section in manifest["sections"] if section["slug"] == "sylow-theory")
    item = next(item for item in applications["items"] if item.get("ref") == card_id)
    applications["items"].remove(item)
    sylow["items"].append(item)
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True))


def catalog_rows(root: Path) -> dict[str, list[tuple]]:
    subprocess.run(
        [sys.executable, "-m", "qualc", "build", "--root", str(root)],
        check=True,
        capture_output=True,
    )
    con = sqlite3.connect(root / "build" / "catalog.sqlite")
    return {
        # source_path is excluded: it is a diagnostic, not identity
        "cards": con.execute("select id, kind, title, review, ast from cards order by id").fetchall(),
        "classifications": con.execute("select * from classifications order by 1,2,3").fetchall(),
        "relations": con.execute("select * from relations order by 1,2,3").fetchall(),
        "occurrences": con.execute("select * from occurrences order by id").fetchall(),
        "sources": con.execute("select * from sources order by id").fetchall(),
        "sections": con.execute("select * from sections order by 1,3").fetchall(),
    }


def test_corpus_layout_is_semantically_inert(tmp_path: Path) -> None:
    work = tmp_path / "repo"
    for sub in ("corpus", "vocabularies", "publications", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    (work / "assets").symlink_to(ROOT / "assets", target_is_directory=True)
    before = catalog_rows(work)
    site = work / "build" / "quarto" / "_site"

    traversal = [
        ("Algebra", Path("guide/GUIDE-ALGEBRA.html")),
        (
            "Finite Groups",
            Path("guide/GUIDE-ALGEBRA/finite-groups.html"),
        ),
        (
            "Actions and Counting",
            Path("guide/GUIDE-ALGEBRA/actions-and-counting.html"),
        ),
        (
            "Sylow Theory",
            Path("guide/GUIDE-ALGEBRA/sylow-theory.html"),
        ),
        (
            "Applications and Problems",
            Path("guide/GUIDE-ALGEBRA/applications-and-problems.html"),
        ),
    ]
    titles = [title for title, _ in traversal]
    routes = [route for _, route in traversal]

    for index, (title, route) in enumerate(traversal):
        page = read_html(site / route)
        assert [heading.text for heading in page.root.find_all("h1")] == [title]

        subject = page.root.find_all("nav", **{"aria-label": "Subject"})
        assert len(subject) == 1
        assert [link.text for link in subject[0].find_all("a")] == titles
        current = subject[0].find_all("a", **{"aria-current": "page"})
        assert [link.text for link in current] == [title]

        breadcrumbs = page.root.find_all("nav", **{"aria-label": "Breadcrumb"})
        assert len(breadcrumbs) == 1
        assert [link.text for link in breadcrumbs[0].find_all("a")] == titles[: index + 1]

        previous = page.root.find_all("a", rel="prev")
        following = page.root.find_all("a", rel="next")
        assert [resolved_link(route, link.attrs["href"]) for link in previous] == ([routes[index - 1].as_posix()] if index else [])
        assert [resolved_link(route, link.attrs["href"]) for link in following] == ([routes[index + 1].as_posix()] if index + 1 < len(routes) else [])

    applications_route = routes[-1]
    applications = read_html(site / applications_route)
    named_spine = {
        "T-SZRXI",
        "T-XDMK2",
        "D-WYC7C",
        "T-OBPSZ",
        "L-DJKXL",
        "T-4CDTT",
        "D-7TQ2M",
        "T-4RADG",
        "T-RRK4J",
        "T-3X5FF",
        "ST-DKYXZ",
        "P-P3RNI",
        "P-AWKNO",
        "P-FKAJJ",
        "P-B6EUH",
        "P-DXHST",
        "P-VI6QM",
        "P-P2UAH",
        "H-2JK8Q",
        "S-4WQ1R",
    }
    rendered_spine = {
        element.attrs["data-card-id"]
        for route in routes[1:]
        for element in read_html(site / route).root.find_all(
            "section",
        )
        if "data-card-id" in element.attrs
    }
    assert named_spine <= rendered_spine

    application_problem_ids = {
        Path(resolved_link(applications_route, link.attrs["href"])).stem
        for link in applications.root.find_all("a")
        if "/tag/P-" in resolved_link(applications_route, link.attrs["href"])
    }
    generator = (site / "generate.html").read_text()
    match = re.search(r"const QDATA=(\[.*?\]);\nconst insts=", generator, re.DOTALL)
    assert match is not None
    generator_problems = {problem["id"]: problem for problem in json.loads(match.group(1))}
    generator_problem_ids = set(generator_problems)
    assert generator_problems["P-J3FBW"]["q"].lstrip().startswith("<ul>")
    assert "<li>Classify the four groups of order 28.</li>" in generator_problems["P-J3FBW"]["q"]
    generator_scripts = [script.text for script in read_html(site / "generate.html").root.find_all("script") if "const QDATA=" in script.text]
    assert len(generator_scripts) == 1
    script_check = subprocess.run(
        ["node", "--check", "-"],
        input=generator_scripts[0],
        capture_output=True,
        text=True,
        check=False,
    )
    assert script_check.returncode == 0, script_check.stderr
    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    catalog_problem_ids = {card_id for (card_id,) in con.execute("select id from cards where kind='problem' order by id")}
    assert generator_problem_ids == catalog_problem_ids
    assert application_problem_ids <= generator_problem_ids

    search_records = json.loads((site / "search.json").read_text())
    search = {record["url"]: record for record in search_records}
    assert search["guide/GUIDE-ALGEBRA/finite-groups.html"]["kind"] == "Page"
    assert search["tag/T-SZRXI.html"]["kind"] == "Card"
    assert search["tag/P-P2UAH.html"]["kind"] == "Problem"
    visible_sylow_results = [record for record in search_records if "sylow" in record["search"]][:30]
    assert {record["kind"] for record in visible_sylow_results} == {
        "Page",
        "Card",
        "Problem",
    }

    problem = read_html(site / "tag" / "P-P2UAH.html")
    semantic_order = [
        next(
            (class_name for class_name in element.attrs.get("class", "").split() if class_name in {"qual-problem", "qual-hint", "qual-solution"}),
            "",
        )
        for element in problem.starts
    ]
    assert semantic_order.index("qual-problem") < semantic_order.index("qual-hint")
    assert semantic_order.index("qual-hint") < semantic_order.index("qual-solution")

    solution = read_html(site / "tag" / "S-4WQ1R.html")
    dependency_groups = solution.root.find_all(
        "section",
        **{"data-relation-group": "dependencies"},
    )
    appearance_groups = solution.root.find_all(
        "section",
        **{"data-relation-group": "appearances"},
    )
    backlink_groups = problem.root.find_all(
        "section",
        **{"data-relation-group": "backlinks"},
    )
    assert len(dependency_groups) == len(appearance_groups) == len(backlink_groups) == 1
    assert "D-7TQ2M" in dependency_groups[0].text
    assert "Applications and Problems" in appearance_groups[0].text
    assert {"H-2JK8Q", "S-4WQ1R"} <= {link.text for link in backlink_groups[0].find_all("a")}

    stable_route = site / "tag" / "P-P2UAH.html"
    assert stable_route.is_file()
    move_appearance(work / "publications" / "algebra-guide.yaml", "P-P2UAH")

    # Reorganize the corpus the way a contributor might: flatten every card into
    # one flat pile with unrecognizable filenames.
    flat = work / "flat"
    flat.mkdir()
    for i, card in enumerate(sorted((work / "corpus").rglob("*.md"))):
        card.rename(flat / f"{i:04d}.md")
    shutil.rmtree(work / "corpus")
    flat.rename(work / "corpus")

    assert catalog_rows(work) == before
    assert stable_route.is_file()
    moved_page = read_html(site / "guide" / "GUIDE-ALGEBRA" / "sylow-theory.html")
    moved_targets = {resolved_link(routes[-2], link.attrs["href"]) for link in moved_page.root.find_all("a")}
    assert "tag/P-P2UAH.html" in moved_targets


def test_unknown_metadata_field_is_rejected(tmp_path: Path) -> None:
    work = tmp_path / "repo"
    for sub in ("corpus", "vocabularies", "publications", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    card = next((work / "corpus").rglob("P-*.md"))
    card.write_text(card.read_text().replace("review: draft", "review: draft\nunivrsity: uga"))

    result = subprocess.run(
        [sys.executable, "-m", "qualc", "check", "--root", str(work)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "univrsity" in result.stderr
