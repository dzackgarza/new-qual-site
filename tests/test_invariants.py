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


@dataclass(frozen=True)
class GuideEntry:
    """One page of a published guide: the root, or one of its sections."""

    key: str
    title: str
    route: Path
    trail: tuple[str, ...]


def guide_plan(manifest_path: Path) -> tuple[list[GuideEntry], list[str], dict[str, list[str]]]:
    """The pages a manifest promises, derived from the manifest itself.

    A guide carries three different structures, and this returns each one
    separately because the rendered page uses each for something different:

    * Reading order -- the root then the sections in manifest order -- is what
      `prev`/`next` walk.
    * The subject nav is the same pages in depth-first order over `parent`,
      which is how a nested nav reads down the page.
    * A page's trail is its ancestry through `parent`, ending at itself.

    All three coincide for a manifest whose sections form a single chain, which
    is why they can only be told apart on a branched guide. Deriving them
    separately is what stops this test from passing on a renderer that confuses
    one for another.

    Also returns the cards each section names outright, which is a different
    mechanism from a panel query and is the one this test proves.
    """
    manifest = yaml.safe_load(manifest_path.read_text())
    guide_id = manifest["id"]
    sections = manifest["sections"]
    title_of = {guide_id: manifest["title"]} | {section["slug"]: section["title"] for section in sections}
    parent_of = {section["slug"]: section["parent"] for section in sections}

    def trail(key: str) -> tuple[str, ...]:
        chain = [key]
        while chain[-1] != guide_id:
            chain.append(parent_of[chain[-1]])
        return tuple(title_of[step] for step in reversed(chain))

    entries = [GuideEntry(guide_id, manifest["title"], Path(f"guide/{guide_id}.html"), trail(guide_id))]
    entries += [
        GuideEntry(
            section["slug"],
            section["title"],
            Path(f"guide/{guide_id}/{section['slug']}.html"),
            trail(section["slug"]),
        )
        for section in sections
    ]

    children: dict[str, list[str]] = {}
    for section in sections:
        if section["parent"] not in children:
            children[section["parent"]] = []
        children[section["parent"]].append(section["slug"])
    nav_order = [guide_id]

    def descend(key: str) -> None:
        for child in children.get(key, []):
            nav_order.append(child)
            descend(child)

    descend(guide_id)
    nav_titles = [title_of[key] for key in nav_order]

    named = {section["slug"]: [item["ref"] for item in section["items"] if "ref" in item] for section in sections}
    return entries, nav_titles, named


def move_appearance(manifest_path: Path, card_id: str, destination_slug: str) -> None:
    manifest = yaml.safe_load(manifest_path.read_text())
    source = next(section for section in manifest["sections"] if any(item.get("ref") == card_id for item in section["items"]))
    destination = next(section for section in manifest["sections"] if section["slug"] == destination_slug)
    item = next(item for item in source["items"] if item.get("ref") == card_id)
    source["items"].remove(item)
    destination["items"].append(item)
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

    manifest_path = work / "publications" / "algebra-guide.yaml"
    traversal, nav_titles, named_by_section = guide_plan(manifest_path)
    titles = [entry.title for entry in traversal]
    routes = [entry.route for entry in traversal]
    # The three structures must actually differ on this guide, or the checks
    # below would be satisfied by a renderer that confuses one for another.
    assert nav_titles != titles
    assert any(list(entry.trail) != titles[: index + 1] for index, entry in enumerate(traversal))
    assert sorted(nav_titles) == sorted(titles)

    for index, entry in enumerate(traversal):
        route = entry.route
        page = read_html(site / route)
        assert [heading.text for heading in page.root.find_all("h1")] == [entry.title]

        subject = page.root.find_all("nav", **{"aria-label": "Subject"})
        assert len(subject) == 1
        assert [link.text for link in subject[0].find_all("a")] == nav_titles
        current = subject[0].find_all("a", **{"aria-current": "page"})
        assert [link.text for link in current] == [entry.title]

        breadcrumbs = page.root.find_all("nav", **{"aria-label": "Breadcrumb"})
        assert len(breadcrumbs) == 1
        assert [link.text for link in breadcrumbs[0].find_all("a")] == list(entry.trail)

        previous = page.root.find_all("a", rel="prev")
        following = page.root.find_all("a", rel="next")
        assert [resolved_link(route, link.attrs["href"]) for link in previous] == ([routes[index - 1].as_posix()] if index else [])
        assert [resolved_link(route, link.attrs["href"]) for link in following] == ([routes[index + 1].as_posix()] if index + 1 < len(routes) else [])

    # Every card a section names outright is rendered as a card block on that
    # section's own page, not merely somewhere in the guide. Panel queries are
    # the other way a card reaches a page and are proved in
    # test_publication_queries.py; naming is what this manifest promises here.
    route_of = {entry.key: entry.route for entry in traversal}
    assert sum(len(refs) for refs in named_by_section.values()) > 0
    for slug, named in named_by_section.items():
        rendered = {
            element.attrs["data-card-id"] for element in read_html(site / route_of[slug]).root.find_all("section") if "data-card-id" in element.attrs
        }
        assert set(named) <= rendered, f"{slug} drops named cards {sorted(set(named) - rendered)}"

    # The section carrying the most problem links is where a reader meets the
    # problem set, whatever the manifest calls it. Routes resolve relative to
    # the site root and so carry no leading slash: `tag/P-XXXXX.html`.
    def problem_links(route: Path) -> set[str]:
        return {
            Path(resolved).stem for link in read_html(site / route).root.find_all("a") if (resolved := resolved_link(route, link.attrs["href"])).startswith("tag/P-")
        }

    applications_route = max(routes[1:], key=lambda route: len(problem_links(route)))
    applications = read_html(site / applications_route)
    application_problem_ids = problem_links(applications_route)
    # Without this the subset check below is satisfied by the empty set, which
    # is what a mismatched route prefix silently produced here before.
    assert application_problem_ids
    generator = (site / "generate.html").read_text()
    match = re.search(r"const QDATA=(\[.*?\]);\nconst insts=", generator, re.DOTALL)
    assert match is not None
    generator_problems = {problem["id"]: problem for problem in json.loads(match.group(1))}
    generator_problem_ids = set(generator_problems)
    assert "<li>Classify the four groups of order 28.</li>" in generator_problems["P-J3FBW"]["q"]
    # The generated sheet is statements only. A tag page may put the solution
    # behind a disclosure the reader chooses to open; the generator has no
    # disclosure and prints whatever it is given, so the answer-bearing blocks
    # must be gone from its extraction rather than merely folded.
    answer_markup = re.compile(r'<div[^>]*class="[^"]*\b(solution|hint|proof|strategy|concept|warnings)\b')
    assert [card_id for card_id, problem in generator_problems.items() if answer_markup.search(problem["q"])] == []
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
    assert search[routes[1].as_posix()]["kind"] == "Page"
    assert search["tag/T-SZRXI.html"]["kind"] == "Card"
    assert search["tag/P-P2UAH.html"]["kind"] == "Problem"
    # A real query reaches all three kinds the index labels. The index is
    # emitted wiki-then-pages-then-cards with cards ordered by id and carries no
    # relevance ranking, so a leading slice of it would pin concatenation order
    # rather than anything this repository promises a reader.
    sylow_results = [record for record in search_records if "sylow" in record["search"]]
    assert {record["kind"] for record in sylow_results} == {
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
    assert {"H-2JK8Q", "S-4WQ1R"} <= {link.text for link in backlink_groups[0].find_all("a")}

    # A named card's appearances name the section that named it.
    witness_slug = next(slug for slug, named in named_by_section.items() if named)
    witness_card = named_by_section[witness_slug][0]
    witness_appearances = read_html(site / "tag" / f"{witness_card}.html").root.find_all(
        "section",
        **{"data-relation-group": "appearances"},
    )
    assert len(witness_appearances) == 1
    witness_title = next(entry.title for entry in traversal if entry.key == witness_slug)
    assert witness_title in witness_appearances[0].text

    # A sitting links to its problems; the problem must link back to the sitting
    # it was set at, not merely name it.
    problem_appearances = problem.root.find_all(
        "section",
        **{"data-relation-group": "appearances"},
    )
    assert len(problem_appearances) == 1
    assert "exam/SRC-UGA-ALG-FALL-2018.html" in {resolved_link(Path("tag/P-P2UAH.html"), link.attrs["href"]) for link in problem_appearances[0].find_all("a")}
    assert "UGA algebra Fall 2018, problem 1" in problem_appearances[0].text

    # Republish the same card under a different section, then flatten the corpus
    # underneath it. Publication structure and source layout must both move
    # without the catalog noticing.
    moved_card = witness_card
    destination_slug = next(slug for slug, named in named_by_section.items() if named and slug != witness_slug)
    destination_route = route_of[destination_slug]
    assert moved_card not in named_by_section[destination_slug]

    stable_route = site / "tag" / f"{moved_card}.html"
    assert stable_route.is_file()
    move_appearance(manifest_path, moved_card, destination_slug)

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
    moved_page = read_html(site / destination_route)
    moved_targets = {resolved_link(destination_route, link.attrs["href"]) for link in moved_page.root.find_all("a")}
    assert f"tag/{moved_card}.html" in moved_targets
    moved_sections = {element.attrs["data-card-id"] for element in moved_page.root.find_all("section") if "data-card-id" in element.attrs}
    assert moved_card in moved_sections
