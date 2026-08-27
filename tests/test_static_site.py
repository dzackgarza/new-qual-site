"""The direct HTML output resolves semantic links and owned assets."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest
from conftest import fixture_repo, run_qualc
from qualc.emit import mathjax_header
from qualc.static_site import StandardPage, build_asset_catalog, write_page
from test_invariants import Element, read_html


def _mathjax_macros(header: str) -> dict[str, str]:
    match = re.search(r"macros: (\{.*?\}), inlineMath", header)
    assert match is not None, "the header must embed the macros JSON"
    parsed: dict[str, str] = json.loads(match.group(1))
    return parsed


def test_mathjax_macro_names_omit_the_tex_escape() -> None:
    header = mathjax_header({r"\DD": r"\mathbb{D}", r"\inner": r"\langle #1,#2\rangle"})

    macros = _mathjax_macros(header)
    assert macros["DD"] == r"\mathbb{D}"
    assert r"\DD" not in macros
    assert macros["inner"] == [r"\langle #1,#2\rangle", 2]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.srcs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value is None:
                continue
            if key == "href":
                self.hrefs.append(value)
            elif key == "src":
                self.srcs.append(value)


def test_nested_page_rewrites_card_and_asset_links(tmp_path: Path) -> None:
    assets_root = tmp_path / "assets"
    image = assets_root / "figures" / "diagram.png"
    image.parent.mkdir(parents=True)
    image.write_bytes(b"image")
    site_root = tmp_path / "_site"

    write_page(
        site_root,
        Path("tag/P-ONE.html"),
        {"title": "One"},
        '<p><a href="P-TWO">Two</a><a href="assets/figures/diagram.png">Asset</a><img src="../../assets/figures/diagram.png"></p>',
        "",
        {"P-TWO": Path("tag/P-TWO.html")},
        build_asset_catalog(assets_root),
        StandardPage(),
    )

    links = LinkCollector()
    links.feed((site_root / "tag" / "P-ONE.html").read_text())
    assert {"P-TWO.html", "../assets/figures/diagram.png"} <= set(links.hrefs)
    assert "../assets/figures/diagram.png" in links.srcs
    assert (site_root / "assets" / "figures" / "diagram.png").samefile(image)


def test_missing_asset_fails_the_build(tmp_path: Path) -> None:
    assets_root = tmp_path / "assets"
    assets_root.mkdir()

    with pytest.raises(ValueError, match="referenced asset does not exist"):
        write_page(
            tmp_path / "_site",
            Path("tag/P-ONE.html"),
            {"title": "One"},
            '<img src="../../assets/figures/missing.png">',
            "",
            {},
            build_asset_catalog(assets_root),
            StandardPage(),
        )


def test_problem_filters_group_each_label_with_its_control(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "problems.html")
    filters = page.root.find_all("div", **{"class": "problem-filters"})
    assert len(filters) == 1
    labels = [child for child in filters[0].children if isinstance(child, Element) and child.tag == "label"]
    controls = [[child.tag for child in label.children if isinstance(child, Element)] for label in labels]
    assert controls == [["input"], ["select"], ["select"], ["select"], ["select"]]
