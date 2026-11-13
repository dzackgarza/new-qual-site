"""Every problem page states its proof status, and the crawler holds it to that.

Issue #113: the site rendered nearly 14,000 draft cards and the few dozen
certified ones with no way for a reader to tell them apart, except by comparing
each page against the certificate tables of `proofs/README.md`. The status is derived from two
authored sources -- the card's `review:` field and those tables -- and stated on
the page; the counts follow on the collection and index pages.

The three pages this module builds and reads are `tag/P-DRAFT-ONE.html`,
`tag/P-REVIEWED-ONE.html` and `tag/P-CERTIFIED-ONE.html`, one per status. They
are fixture cards rather than corpus cards so the test does not have to build
14,000 pages to say what a status line is.
"""

from __future__ import annotations

import re
import shutil
import sqlite3
import urllib.error
import urllib.request
from pathlib import Path

import pytest
from conftest import ROOT, diagnostic_codes, fixture_repo, run_qualc
from qualc import certificates
from qualc import crawl as crawl_module
from qualc import static_site
from qualc.crawl import crawl
from qualc.diagnostics import DiagnosticCode

PROBLEM = """---
schema: qual/card@1
id: {id}
kind: problem
title: {title}
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: {review}
audit:
- event: source-checked
  by: claude
  date: 2026-02-11
  note: The statement was compared with the printed exercise.
- event: solution-written
  by: claude
  date: 2026-02-12
---

::: problem
Let $G$ be a group of order $p^2$. Show that $G$ is abelian.
:::

::: solution
The centre is nontrivial, and $G/Z(G)$ is cyclic, so $G$ is abelian.
:::
"""

COLLECTION = """---
schema: qual/card@1
id: SRC-STATUS-SHEET
kind: collection
title: A sheet with one problem of each status
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
source:
  source_kind: homework
  area: algebra
  date:
    kind: academic-term
    year: 2020
    term: spring
  problems:
  - P-DRAFT-ONE
  - P-REVIEWED-ONE
  - P-CERTIFIED-ONE
---

::: remark
Three problems, one per proof status.
:::
"""

# Section 1's table is the certificate registry, and this row is what certifies
# P-CERTIFIED-ONE. Nothing on the card says so. Section 6's table mentions the
# same file while stating that no certificate exists for what it lists, which is
# why it must not certify P-REVIEWED-ONE.
CERTIFICATE_README = """# Proof artifacts

## 1. Group lemmas proved in Lean

| File | Card | What it proves |
| --- | --- | --- |
| `cards/CertifiedOne.lean` | `P-CERTIFIED-ONE` | The fixture statement about groups of order $p^2$. |

## 6. Chapter 1 step repairs: expository, with the backing theorem checked

No machine certificate exists for any of them.

| Card | What the repair does | Backing |
| --- | --- | --- |
| `P-REVIEWED-ONE` | rewrites a closing step | the source's own computation; see `cards/CertifiedOne.lean` |
"""

CARDS = {
    "P-DRAFT-ONE.md": PROBLEM.format(id="P-DRAFT-ONE", title="A group of order $p^2$ is abelian", review="draft"),
    "P-REVIEWED-ONE.md": PROBLEM.format(id="P-REVIEWED-ONE", title="A group of order $p^2$ is abelian, reviewed", review="reviewed"),
    "P-CERTIFIED-ONE.md": PROBLEM.format(id="P-CERTIFIED-ONE", title="A group of order $p^2$ is abelian, certified", review="draft"),
    "SRC-STATUS-SHEET.md": COLLECTION,
}


def _repo(tmp_path: Path) -> Path:
    work = fixture_repo(tmp_path, CARDS)
    # The shared nav links `wiki/index.html`, and the fixture corpus has branches
    # without a root page. Writing it keeps the crawler's answer about the status
    # lines the only thing it has to report.
    (work / "wiki" / "index.md").write_text("---\ntitle: Wiki\norder: 1\n---\n\n# Wiki\n")
    (work / "proofs" / "cards").mkdir(parents=True)
    (work / "proofs" / "README.md").write_text(CERTIFICATE_README)
    (work / "proofs" / "cards" / "CertifiedOne.lean").write_text("-- the fixture certificate\ntheorem fixture : True := trivial\n")
    return work


@pytest.fixture(scope="module")
def built(tmp_path_factory: pytest.TempPathFactory) -> Path:
    work = _repo(tmp_path_factory.mktemp("status"))
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    return work / "build" / "quarto" / "_site"


def page(site: Path, name: str) -> str:
    return (site / name).read_text()


def flat(text: str) -> str:
    """One line, so an assertion is about the sentence and not about wrapping."""
    return re.sub(r"\s+", " ", text)


@pytest.mark.parametrize(
    ("name", "status", "label"),
    (
        ("tag/P-DRAFT-ONE.html", "draft", "Draft"),
        ("tag/P-REVIEWED-ONE.html", "reviewed", "Reviewed"),
        ("tag/P-CERTIFIED-ONE.html", "certified", "Certified"),
    ),
)
def test_a_problem_page_states_which_of_the_three_its_proof_is(
    built: Path,
    name: str,
    status: str,
    label: str,
) -> None:
    """The status line is on the page, and it is the status the sources give.

    `review: reviewed` is the card's own word; the certified card is a draft by
    `review:` and certified by the README's table, which is exactly the case
    where a reader could not have worked the answer out.
    """
    text = page(built, name)

    assert f'class="page-fact page-status" data-status="{status}"' in text
    assert f"<dd>{label}" in text
    # The authored field is not echoed beside the derived status.
    assert "<dt>Status</dt><dd>draft</dd>" not in text


def test_a_certified_page_links_its_certificate_and_names_the_tool(built: Path) -> None:
    text = page(built, "tag/P-CERTIFIED-ONE.html")

    assert 'href="../proofs/cards/CertifiedOne.lean"' in text
    assert "<code>proofs/cards/CertifiedOne.lean</code>" in text
    assert "Lean <a href=" in text
    # The link resolves because the build publishes the file beside the pages.
    assert (built / "proofs" / "cards" / "CertifiedOne.lean").is_file()


def test_a_page_without_a_certificate_links_none(built: Path) -> None:
    for name in ("tag/P-DRAFT-ONE.html", "tag/P-REVIEWED-ONE.html"):
        assert "proofs/cards/" not in page(built, name)


def test_the_audit_events_are_listed_with_their_dates(built: Path) -> None:
    text = page(built, "tag/P-CERTIFIED-ONE.html")

    assert '<section class="audit-events">' in text
    assert '<time datetime="2026-02-11">11 February 2026</time>' in text
    assert '<time datetime="2026-02-12">12 February 2026</time>' in text
    assert '<span class="audit-event">source-checked</span>' in text
    assert '<span class="audit-event">solution-written</span>' in text
    assert '<span class="audit-by">claude</span>' in text


def test_the_collection_page_counts_each_status(built: Path) -> None:
    text = page(built, "source/SRC-STATUS-SHEET.html")

    for status in ("certified", "reviewed", "draft"):
        assert f'<span class="status-count" data-status="{status}">1 {status}</span>' in text


def test_the_index_page_counts_each_status(built: Path) -> None:
    """The three counts on the home page are the catalog's, not prose.

    Counted here from the built catalog and looked for in the page, so a stale
    sentence fails instead of passing on its wording.
    """
    con = sqlite3.connect(built.parents[1] / "catalog.sqlite")
    counts = dict(con.execute("select status, count(*) from cards where kind='problem' group by status"))
    con.close()

    text = flat(page(built, "index.html"))

    assert f"{counts['certified']:,} are certified" in text
    assert f"{counts['reviewed']:,} are reviewed" in text
    assert f"{counts['draft']:,} are drafts" in text


def test_a_certificate_table_naming_a_missing_file_is_a_corpus_error(tmp_path: Path) -> None:
    work = _repo(tmp_path)
    (work / "proofs" / "cards" / "CertifiedOne.lean").unlink()

    assert DiagnosticCode.CERTIFICATE_FILE_MISSING in diagnostic_codes(work)


def test_a_certificate_table_naming_an_absent_card_is_a_corpus_error(tmp_path: Path) -> None:
    work = _repo(tmp_path)
    readme = work / "proofs" / "README.md"
    readme.write_text(readme.read_text().replace("| `P-CERTIFIED-ONE` |", "| `P-NOT-A-CARD` |"))

    assert DiagnosticCode.CERTIFICATE_CARD_UNKNOWN in diagnostic_codes(work)


REGISTRY_README = """# Proof artifacts

## 1. Group lemmas proved in Lean

| File | Card | What it proves |
| --- | --- | --- |
| `cards/One.lean` | `P-ONE`, `-TWO` | two cards of one source |
| `cards/Three.lean` | `E-ONE` | one more |

## 2. Exact finite computations: Sage chain complexes, GAP groups

`cards/Four.sage`, run on the Sage development image:

| Card | Chain complex checked | Parameter range |
| --- | --- | --- |
| `E-THREE` | the displayed complex | $n\\le6$ |

## 6. Expository repairs with no certificate

| Card | What the repair does | Backing |
| --- | --- | --- |
| `P-FOUR` | rewrites a closing step | checked in `cards/One.lean` |
"""


def test_the_registry_reads_the_two_certificate_sections_and_nothing_else(tmp_path: Path) -> None:
    """Both certificate table shapes, the `-TWO` shorthand, and section 6's exclusion.

    Section 2's second table carries no file column: the file is the one its
    paragraph names. Section 6's table names a certificate file while saying no
    certificate exists for its cards, so reading it would certify a card on the
    strength of a sentence saying the opposite.
    """
    (tmp_path / "cards").mkdir()
    (tmp_path / "README.md").write_text(REGISTRY_README)

    registry = certificates.load(tmp_path)

    assert registry == {
        "P-ONE": (certificates.Certificate("proofs/cards/One.lean", "Lean"),),
        "P-TWO": (certificates.Certificate("proofs/cards/One.lean", "Lean"),),
        "E-ONE": (certificates.Certificate("proofs/cards/Three.lean", "Lean"),),
        "E-THREE": (certificates.Certificate("proofs/cards/Four.sage", "exact Sage"),),
    }


def test_a_repository_without_a_proofs_directory_certifies_nothing(tmp_path: Path) -> None:
    assert certificates.load(tmp_path) == {}
    assert certificates.status("draft", ()) == "draft"
    assert certificates.status("reviewed", ()) == "reviewed"
    assert certificates.status("draft", (certificates.Certificate("proofs/cards/One.lean", "Lean"),)) == "certified"


def test_the_crawl_fails_on_a_problem_page_with_no_status_line(built: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """A page that drops its status line is the failure #113 recorded.

    The status line is removed from `tag/P-DRAFT-ONE.html` as a template
    regression would leave it: the page still renders and no longer says which
    of the three the proof is.
    """
    site = tmp_path / "_site"
    shutil.copytree(built, site)
    stripped = site / "tag" / "P-DRAFT-ONE.html"
    stripped.write_text(re.sub(r'<div class="page-fact page-status" data-status="[^"]*">.*?</div>', "", stripped.read_text()))
    assert "page-status" not in stripped.read_text()

    # The untouched copy is the control: the same site, crawled the same way,
    # passes. Without it this test would pass on a crawler that always failed.
    assert crawl_module.main(["--links-only", "--site", str(built)]) == 0
    assert "no proof status" not in capsys.readouterr().out

    result = crawl(site)

    assert result.missing_status == ("tag/P-DRAFT-ONE.html",)
    assert crawl_module.main(["--links-only", "--site", str(site)]) == 1
    assert "no proof status: tag/P-DRAFT-ONE.html" in capsys.readouterr().out


def test_the_crawl_passes_the_built_site(built: Path) -> None:
    """Every problem page of a normal build has its status line.

    Link resolution is `tests/test_static_site.py`'s claim; this asserts only
    that the new check does not fire on a build that has nothing wrong with it.
    """
    result = crawl(built)

    assert result.missing_status == ()
    assert (built / "tag" / "P-CERTIFIED-ONE.html").resolve() in result.seen


LINK_README = """# Proof artifacts

## 1. Group lemmas proved in Lean

| File | Card | What it proves |
| --- | --- | --- |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/One.lean> | `P-ONE` | one card, its file at a named commit of this repository |
"""


def test_the_registry_reads_a_link_row(tmp_path: Path) -> None:
    """A section 1 row may be a link: the file at a named commit of this repository.

    A Lean certificate is a link to a file at a named commit of this
    repository or to a declaration on lean-categories main; the registry
    reads it as one and keeps the Sage and GAP rows as the paths they
    still are.
    """
    (tmp_path / "README.md").write_text(LINK_README)

    registry = certificates.load(tmp_path)

    assert registry == {
        "P-ONE": (
            certificates.Certificate(
                "https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/One.lean",
                "Lean",
            ),
        )
    }


def test_one_real_row_of_section_one_links_its_file_at_the_named_commit() -> None:
    """The check reads one real row: `P-FHW1-01`'s, the registry's own first.

    The row is the one at the head of section 1, and its link names the file at
    commit `16c09abaa4` — the commit the migration into lean-categories reads
    and the one this repository keeps the certificates readable at. The target
    exists in this clone's own history, so the check passes on it here and in
    any checkout that carries the history.
    """
    registry = certificates.load(ROOT / "proofs")
    entry = registry["P-FHW1-01"][0]

    assert entry.file == "https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/FieldHomework1.lean"
    assert certificates.exists(ROOT, entry.file)


def test_a_row_linking_a_file_the_named_commit_does_not_carry_is_an_error() -> None:
    """A link to a file at a named commit that is not there fails the check.

    The commit is real and the directory is right; only the file is wrong, which
    is the shape a typo in a row produces.
    """
    assert not certificates.exists(
        ROOT,
        "https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/Nope.lean",
    )


def test_a_declaration_on_lean_category_main_is_checked_over_http(monkeypatch: pytest.MonkeyPatch) -> None:
    """The lean-categories form is checked by asking its main.

    A declaration on `dzackgarza/lean-categories` main lives in another
    repository, so the check follows the link over HTTP: the target answers 200
    when it exists and 404 when it does not. Both answers are stubbed here, so
    the test says what the check does with each and nothing about today's
    network.
    """

    class Response:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

    def reachable(url, **_):
        return Response()

    monkeypatch.setattr(urllib.request, "urlopen", reachable)
    assert certificates.exists(
        ROOT,
        "https://github.com/dzackgarza/lean-categories/blob/main/LeanCategories/Algebra/AssociatedGraded.lean",
    )

    def missing(url, **_):
        raise urllib.error.HTTPError(url, 404, "Not Found", None, None)

    monkeypatch.setattr(urllib.request, "urlopen", missing)
    assert not certificates.exists(
        ROOT,
        "https://github.com/dzackgarza/lean-categories/blob/main/LeanCategories/Algebra/Nope.lean",
    )


def test_the_status_line_links_a_certificate_url() -> None:
    """A Lean certificate that is a link is linked as one, not as a local file.

    The relative-URL form the status line builds for the Sage and GAP files
    would mangle a `https://` certificate into a broken relative path, so a link
    certificate is emitted as the URL it is.
    """
    url = "https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/One.lean"
    meta = {"proof_status": "certified", "certificates": [{"file": url, "tool": "Lean"}]}

    line = static_site._proof_status(meta, Path("tag/P-ONE.html"))

    assert f'<a href="{url}"><code>{url}</code></a>' in line
    assert "../../../" not in line
