from __future__ import annotations

import json
from pathlib import Path

from qualc.crawl import crawl, data_urls


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def test_crawl_follows_data_driven_catalog_urls(tmp_path: Path) -> None:
    site = tmp_path / "_site"
    write(
        site / "index.html",
        '<a href="problems.html">Problems</a><a href="exams.html">Exams</a>',
    )
    write(site / "problems.html", '<table id="problem-table"></table>')
    write(site / "exams.html", '<table id="source-table"></table>')
    write(site / "tag" / "P-ONE.html", "Problem")
    write(site / "exam" / "SRC-ONE.html", "Exam")
    write(site / "404.html", "not found")
    write(site / "generate.html", "legacy redirect")
    (site / "problems.json").write_text(json.dumps({"rows": [{"url": "tag/P-ONE.html"}]}))
    (site / "sources.json").write_text(json.dumps({"rows": [{"url": "exam/SRC-ONE.html"}]}))
    (site / "collection-problems.json").write_text(json.dumps({"SRC-ONE": {"items": [{"url": "tag/P-ONE.html"}]}}))

    result = crawl(site)

    assert not result.broken
    assert not result.orphans
    assert (site / "tag" / "P-ONE.html").resolve() in result.seen
    assert (site / "exam" / "SRC-ONE.html").resolve() in result.seen


def test_crawl_treats_pagefind_documents_as_search_reachable(tmp_path: Path) -> None:
    site = tmp_path / "_site"
    write(site / "index.html", '<dialog id="site-search"></dialog>')
    write(site / "tag" / "T-ONE.html", "<main data-pagefind-body>Theory searchable only</main>")

    result = crawl(site)

    assert not result.broken
    assert not result.orphans
    assert (site / "tag" / "T-ONE.html").resolve() in result.seen


def test_data_driven_broken_url_is_a_crawl_failure(tmp_path: Path) -> None:
    site = tmp_path / "_site"
    write(site / "index.html", '<dialog id="site-search"></dialog>')
    (site / "problems.json").write_text(json.dumps({"rows": [{"url": "tag/P-MISSING.html"}]}))

    urls = data_urls(site)
    result = crawl(site)

    assert urls == [("problems.json", (site / "tag" / "P-MISSING.html").resolve())]
    assert result.broken == (("problems.json", "tag/P-MISSING.html"),)
