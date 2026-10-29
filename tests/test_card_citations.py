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
