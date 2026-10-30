#!/usr/bin/env python3
"""Regenerate vocabularies/references.yaml from the live Zotero library.

The library is the bibliography. Entries are not written here by hand: Better BibTeX
exports the items the authored text cites as CSL YAML, under the library's own citation
keys, and the result is committed so a build never reaches outside this repository.

CSL rather than BibTeX, because citeproc builds a reference's label from family names
and a corporate author has none: such an entry needs an explicit `citation-label`, which
Pandoc honours only in a CSL bibliography. The label is set in the item's Zotero `Extra`
field (`Citation Label: Har07`), and Better BibTeX exports it as `citation-label`.

Fields that describe the library rather than the work are dropped: `keyword` describes
how the library is organised, and `abstract` is a publisher's blurb no bibliography
entry needs to print.

Requires the Zotero desktop running with Better BibTeX. That is a precondition, not a
fallback: there is no second source for this file.
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import panflute as pf
import yaml
from qualc.model import MARKDOWN, from_ast
from qualc.pandoc_batch import PandocBatchError, PandocFailure, read_markdown_parallel

ROOT = Path(__file__).resolve().parent.parent
EXPORT = "http://127.0.0.1:23119/better-bibtex/export/item"
# Fields that describe the library's copy rather than the work itself.
DROPPED = ("abstract", "keyword")
HEADER = """\
# The works the authored text cites, exported from the Zotero library by
# tools/sync_bibliography.py. Do not edit: add the work to Zotero instead.
"""


def cited_keys() -> list[str]:
    """The keys of every `Cite` element Pandoc reads in wiki/ and corpus/, with the compiler's dialect."""
    paths = [path for where in ("wiki", "corpus") for path in (ROOT / where).rglob("*.md")]
    keys: set[str] = set()

    def collect(elem: pf.Element, doc: pf.Doc) -> None:
        if isinstance(elem, pf.Cite):
            keys.update(citation.id for citation in elem.citations)

    results = read_markdown_parallel([path.read_text() for path in paths], MARKDOWN)
    for path, result in zip(paths, results, strict=True):
        if isinstance(result, PandocFailure):
            raise PandocBatchError(f"{path.relative_to(ROOT)}: {result.error}")
        from_ast(result.output).walk(collect)
    return sorted(keys)


def export(keys: list[str]) -> str:
    query = urllib.parse.urlencode({"citationKeys": ",".join(keys), "translator": "Better CSL YAML"}, quote_via=urllib.parse.quote)
    request = urllib.request.Request(f"{EXPORT}?{query}", method="GET")
    with urllib.request.urlopen(request, timeout=60) as response:
        body: bytes = response.read()
    return body.decode()


def main() -> int:
    keys = cited_keys()
    if not keys:
        print("no citations in wiki/ or corpus/", file=sys.stderr)
        return 1
    try:
        exported = export(keys)
    except urllib.error.URLError as exc:
        print(f"Zotero is not answering at {EXPORT}: {exc}", file=sys.stderr)
        return 1
    if "not found" in exported.split("\n", 1)[0]:
        print(f"Better BibTeX knows none of: {' '.join(keys)}", file=sys.stderr)
        return 1

    references = yaml.safe_load(exported)["references"]
    missing = sorted(set(keys) - {reference["id"] for reference in references})
    if missing:
        print(f"no Zotero item has the citation key: {' '.join(missing)}", file=sys.stderr)
        return 1
    for reference in references:
        for field in DROPPED:
            reference.pop(field, None)

    body = yaml.safe_dump({"references": references}, allow_unicode=True, sort_keys=False)
    (ROOT / "vocabularies" / "references.yaml").write_text(HEADER + body)
    print(f"{len(keys)} works cited: {' '.join(keys)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
