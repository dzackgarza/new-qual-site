#!/usr/bin/env python3
"""Regenerate vocabularies/references.bib from the live Zotero library.

The library is the bibliography. Entries are not written here by hand: Better BibTeX
exports the items the authored text cites, under the library's own citation keys, and
the result is committed so a build never reaches outside this repository.

Fields that describe the library rather than the work are dropped. `file` is the worst
of them -- it holds absolute paths into ~/Zotero/storage, which are neither portable nor
anyone else's business -- `keywords` and `timestamp` describe how the library is
organised, and `abstract` is a publisher's blurb no bibliography entry needs to print.

Requires the Zotero desktop running with Better BibTeX. That is a precondition, not a
fallback: there is no second source for this file.
"""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORT = "http://127.0.0.1:23119/better-bibtex/export/item"
CITE_RE = re.compile(r"\[@([A-Za-z][\w:.#$%&+?<>~/-]*)\]")
# Fields that describe the library's copy rather than the work itself.
DROPPED = ("abstract", "file", "keywords", "timestamp")
HEADER = """\
% The works the authored text cites, exported from the Zotero library by
% tools/sync_bibliography.py. Do not edit: add the work to Zotero instead.
"""


def cited_keys() -> list[str]:
    keys: set[str] = set()
    for where in ("wiki", "corpus"):
        for path in (ROOT / where).rglob("*.md"):
            keys |= set(CITE_RE.findall(path.read_text()))
    return sorted(keys)


def export(keys: list[str]) -> str:
    query = urllib.parse.urlencode({"citationKeys": ",".join(keys), "translator": "bibtex"})
    request = urllib.request.Request(f"{EXPORT}?{query}", method="GET")
    with urllib.request.urlopen(request, timeout=60) as response:
        body: bytes = response.read()
    return body.decode()


def strip_local(bibtex: str) -> str:
    """Drop the library-only fields, and Better BibTeX's own quality-report comments."""
    out = []
    for line in bibtex.splitlines():
        if line.startswith("%"):
            continue
        if line.strip().startswith(DROPPED) and "=" in line:
            continue
        out.append(line)
    return "\n".join(out).strip() + "\n"


def main() -> int:
    keys = cited_keys()
    if not keys:
        print("no citations in wiki/ or corpus/", file=sys.stderr)
        return 1
    try:
        bibtex = export(keys)
    except urllib.error.URLError as exc:
        print(f"Zotero is not answering at {EXPORT}: {exc}", file=sys.stderr)
        return 1
    if "not found" in bibtex.split("\n", 1)[0]:
        print(f"Better BibTeX knows none of: {' '.join(keys)}", file=sys.stderr)
        return 1

    missing = [key for key in keys if f"{{{key}," not in bibtex]
    if missing:
        print(f"no Zotero item has the citation key: {' '.join(missing)}", file=sys.stderr)
        return 1

    (ROOT / "vocabularies" / "references.bib").write_text(HEADER + strip_local(bibtex) + "\n")
    print(f"{len(keys)} works cited: {' '.join(keys)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
