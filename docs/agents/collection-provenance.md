# Collection provenance

## One problem browser

`problems.html` is the only reader-facing implementation that displays a
metadata-selected family of problem rows. It owns filtering, source-scoped
ordering, random sampling, and print/PDF. Do not add a second metadata-query or
practice-set renderer to guides, wiki pages, or another site route. A
collection's authored `source.problems` / `source.sections` list is not a query:
it is the collection's intrinsic contents and is rendered on the collection
page itself.

The catalog UI itself is standard infrastructure: Problems and Sources are
DataTables 2 tables with SearchPanes for faceted filtering and RowGroup where
source sections need grouping. Do not hand-roll pagination, facet controls,
facet counts, table search, or result-row lifecycle in `app.js`; `app.js` owns
site-wide Pagefind search only. Project code may adapt corpus rows into the
library and add domain actions such as sampling the currently filtered problem
set.

- A guide section or topical wiki page owns ordinary `topics:` metadata. The
  renderer automatically adds one `problems.html` link with the page's subject
  area and topics prefilled. Do not add `query:` items to guide manifests or a
  `problems:` query block to wiki front matter.
- A subject wiki landing page represents the whole area, so it automatically
  links to `problems.html?area=<subject>` even when it has no narrower topics.
  Resources, workshop indexes, and other non-topical pages may omit `topics:`
  and therefore get no automatic problem link.
- A collection page keeps source identity, provenance, completion state, and
  **enumerates the authored source contents in source order**, preserving
  section structure, problem links, and authored appearance locators. This is
  the principal purpose of the collection page. Collection classification and
  status use the same metadata band as every other card. Provenance resources
  belong there too as compact typed links (PDF, Markdown extraction, source
  page); never expose a repository-relative asset path as reader-facing prose.
  The page may additionally deep-link with `collection=SRC-...` so the same
  problems can be searched, filtered, sampled, or printed in the browser. That
  browser link supplements rather than replaces the collection's own contents.
- `generate.html` is compatibility-only: old URLs redirect to `problems.html`
  with `sample=8`. It must not acquire controls, query logic, or a second
  problem data path.
- `E-*` and `P-*` are stable addresses. Every posed mathematical card is
  `kind: problem`; whether a source called one an exercise, homework problem,
  or qualifying-exam problem belongs to its collection appearance.

A source's ordered problem membership is authored corpus data and the source
page materializes it directly. The central browser is a second view of that
same authored membership for filtering, sampling, and print; it does not own or
replace the collection's source-order presentation.

A collection is a source document, not an exam event. One PDF is one
collection. If that PDF *is* a single exam's problem set, the collection is
that exam. If the PDF is a compilation of several papers, the collection is
the compilation; the exams inside it are `sections` of that card, not
separate collections. Do not split a compilation PDF into one collection per
exam. (A workshop that is several sheet PDFs is already one compilation
with one href per sheet and one section per sheet. A section that
is another source — an exam paper that is its own collection — lists that
collection instead of copying its problem list. The exam collection owns
that sheet's provenance href.)

Collection membership follows the mathematical statements present in the
available source document. It does not follow the historical exam that the
document describes. Blank pages, missing pages, score tables, and gaps in
problem numbering do not create missing collection items. Do not invent
expected cards, mark the collection incomplete, or create recovery work for
statements that are absent from every available source.

## Provenance means external oracles

Provenance is any externally authored source: textbooks, problem sheets, exams,
external notes, or PDFs from other institutions. The entire point of provenance
is to have an oracle that can be trusted more than self-authored content —
something written by someone else, against which problem correctness can be
checked and "blamed" if the problem is ill-defined or otherwise problematic.

Provenance is NOT:
- PDFs authored by the project maintainer
- PDFs on the to-be-archived source repos being migrated into this repo (e.g.
  MMAQ)
- This project's wiki or any content derived from our own cards
- Solution writeups, regardless of authorship

On a **collection** card, `provenance:` is a YAML list of hrefs (`https://` or
repo-relative paths). Each href is the document the problems were extracted
from: the official paper, the homework sheet, or — for a textbook collection —
the book. A markdown file is not that document. A reader following the link
must be able to verify the list against that document.

Origin notes that are not links belong in a `::: remark` block on the card body,
not in frontmatter.

`just provenance` measures empty lists, hrefs that do not resolve, hrefs
listed on more than one collection, hrefs whose path is a markdown file,
hrefs whose path is an image file, hrefs whose path is under a forbidden
source tree (`make-me-a-qual`, wiki copies, importer wrappers, and the
like), and collections whose area appears on no problem card.
It is not a gate. Filling the list so the measurement is quieter is
fabricating a source.

## What must not appear as a collection href

None of the following is provenance, even if the file is in this repository or
the wiki once named it as the source.

- This project's wiki (`wiki/…`), wiki exam-term headings, or any page generated
  from our cards. Grouping in the vault is not an independent document. Qual
  notes record which exam a problem came from; they are not the exam
  paper.
- Qual-review-and-solutions compiled notes, generated TeX, pandoc tempfiles, or
  a copy of wiki or QRS content parked under `assets/`. Same rule: use them to
  identify the exam; list the paper in `provenance`.
- A solution writeup. A writeup of solutions is not the exam, the homework
  sheet, or the source document.
- A figure that appears inside a writeup.
- A standalone problem image (`.png`, `.jpg`, and the like). An image file is
  not the exam paper. Screenshots of the author's notes are not assets;
  see Screenshots of notes.
- An importer wrapper: markdown generated from a PDF, authored MMAQ `.md`,
  generated MMAQ `.tex`, or `Combined_Questions.pdf`. A markdown file is not
  a collection href.
- Any `dzackgarza` repository is not an independent source. A GitHub URL
  under `dzackgarza`, a sibling clone, or a copy of that repo under `assets/`
  is not a collection href. That includes `make-me-a-qual` and
  `Combined_Questions.yaml`. This site's wiki is the same. An exam paper
  stored in `assets/attachments/` is the paper, not the repo.
- A file that is a different exam than the card claims.
- A textbook catalog page or ISBN on a homework or exam collection. The
  collection's document is the sheet. (A textbook collection may cite the book.)
- Another collection card. Reprints of a published exam go in `relations`
  (`related-to`), not in `provenance`.
- A dead GitHub URL to a deleted upstream. Vendor the actual source file into
  this repo and point at that file.
- Directory listings, pirated copies, or a live URL that does not serve the
  paper.

A compilation of photocopied exam papers (for example
`algebra_2010-2015_prelims.pdf`) is a source of truth if we did not compile it.
The href is the packet. Unlabeled is fine: provenance is not a university.
Read the pages for what they actually contain (heading, date, instructions,
which exam occupies which pages). Do not invent a department website, a
compiler, or an institution the pages do not name. Do not treat the wiki
attachments folder as a second source.

An empty collection `provenance` list means no qualifying href is listed yet.
Leave it empty. Hunt in this repo, sibling clones, and distinctive problem text
on the web; if the exam document is not found, the list stays empty.

## Screenshots of notes

The QualBot PNGs, and any similar crop, are screenshots of the author's
typeset notes. They are not source documents. They are not assets.

The notes are a compilation of real exam problems: they label which exam
and problem number each statement came from. That label is curation metadata,
not collection provenance. Provenance is the exam paper — department PDF,
homework sheet, or packet under `assets/attachments/`.

Do not store note screenshots under `assets/`. Do not list them as collection
`provenance`. Do not keep a collection card whose only job is to wrap a
screenshot.

After the statement is on a problem card and linked to its exam collection,
delete the screenshot. Do not delete an unmatched screenshot to tidy the tree:
until the exam is identified, the image may be the only copy of the label.

## Migration archives are history, not assets

Snapshots of repositories that fed the migration are historical transport
material. Git history preserves them; they do not remain as a second live source
tree and they must not be kept under `assets/` merely because an importer once
read them there.

`assets/` is for material the built corpus actually uses as an asset: source
documents such as exam PDFs under `assets/attachments/`, figures used by cards or
wiki pages, and the checked-in Markdown extractions of those PDFs. If a live card
still points into a migration snapshot, move or copy the needed figure/source
document into the appropriate subject or attachment asset location and point the
card there; do not retain the migration snapshot to satisfy the link.
