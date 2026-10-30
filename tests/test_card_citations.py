"""A card's citations are resolved when the card is read.

Wiki pages are read through citeproc; cards were not, so a card body's
`[@Hat02]` reached every page that showed the card -- its own and every wiki
page or guide that transcludes it -- as the literal key.
"""

from pathlib import Path

import panflute as pf
from qualc.model import from_ast, parse_card

CITING = """---
schema: qual/card@1
id: E-CITING
kind: example
title: A card that cites a book
classification:
  areas: [topology]
  topics: [fundamental-group]
relations: []
review: draft
---

::: example
The circle has fundamental group $\\ZZ$ [@Hat02, Theorem 1.7].
:::
"""


def test_a_card_citation_renders_its_label_and_no_reference_list(tmp_path: Path) -> None:
    path = tmp_path / "E-CITING.md"
    path.write_text(CITING)

    document = from_ast(parse_card(path).ast)

    text = pf.stringify(document)
    assert "[Hatc02, Theorem 1.7]" in text
    assert "@Hat02" not in text
    divs: list[str] = []
    document.walk(lambda el, doc: divs.append(el.identifier) if isinstance(el, pf.Div) else None)
    assert "refs" not in divs, "a transcluded card must not carry its own reference list"


def test_every_key_of_a_card_citation_links_to_its_work(tmp_path: Path) -> None:
    """With no reference list on the card, each label must lead to the work: the
    textbook collection keyed on the citation key, or else that work's entry on
    the site bibliography page. Each key of a several-key citation links alone."""
    from conftest import FIXTURE_CORPUS, fixture_repo, run_qualc

    textbook = (FIXTURE_CORPUS / "SRC-DUMMIT.md").read_text().replace("SRC-DUMMIT", "SRC-TEXT-DF04")
    citing = CITING.replace("areas: [topology]", "areas: [algebra]").replace("[@Hat02, Theorem 1.7]", "[@DF04; @Hat02, Theorem 1.7]")
    work = fixture_repo(tmp_path, {"SRC-TEXT-DF04.md": textbook, "E-CITING.md": citing})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    [page] = list(site.glob("*/E-CITING.html"))
    [target] = [p.relative_to(site).as_posix() for p in site.glob("*/SRC-TEXT-DF04.html")]
    html = page.read_text()
    assert f'href="../{target}">DuFo04</a>' in html
    assert 'href="../bibliography.html#ref-Hat02">Hatc02</a>' in html
    assert 'id="ref-Hat02"' in (site / "bibliography.html").read_text()
