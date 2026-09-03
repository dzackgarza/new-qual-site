# This project is not automatable

Read this before writing anything in this repository.

## Personal research scope

This repository is for the maintainer's personal study and research. It has no
licensing review, distribution review, or release approval workflow.

Do not create licensing tasks, fields, flags, audits, decisions, holds, or user
approval requests. Do not restrict corpus work based on a proposed publication
or distribution status.

Preserve license files and notices that are part of retained source bytes. They
are source content, not project requirements. Continue to follow the repository's
separate citation and provenance rules.

Intake and migration needed tools. Getting the content out of five source
repositories and into this one was a transport problem, and transport is what a
tool is for. **That phase is over.** Everything after it is intelligent, semantic
work on mathematics.

Nothing after intake is mechanical. Not checking. Not deduplicating. Not
classifying. Not merging, writing, retitling, reorganizing, or auditing. Every
one of those operations means reading the mathematics, understanding what a
statement says, and deciding. There is no normal form, fingerprint, digest,
similarity score, heuristic, or "clever enough" parse that decides any of them,
because the thing being decided is what the mathematics *means*.

Growing this corpus is like growing the Stacks Project: reading, writing,
analysis, auditing, reorganization, all of it infinitely subtle, with unbounded
edge cases. A tool that automates any part of that is a claim to have enumerated
the cases in advance. That claim is false every time.

It is also a bad trade even when it appears to work. This is a **one-time task**.
The content gets written and finalized once. Every tool built to automate a part
of it is obsolete the moment that part is finished, and until then it fossilizes
whatever heuristic its author guessed at, in code that outlives the reasoning
behind it. The tool then gets trusted precisely because it is a tool.

## What this rules out

Do not write, extend, or "make safe" anything that decides a semantic question.
If a proposed tool would answer *are these the same statement*, *is this title
right*, *does this belong in that section*, *is this body empty enough to
discard*, *which of these is canonical* — do not write it. Read the cards and
decide.

Making such a tool safer is worse than leaving it broken, because it keeps the
tool. The correct response to a heuristic that destroys content is to delete the
heuristic, not to add a floor under it.

`tools/collapse_duplicates.py` was exactly this and has been deleted. It decided
which cards stated the same mathematics from a normalized-text fingerprint. It
proposed destroying distinct statements three separate times: once merging
appearance cards with the problems they instantiate, once merging every unwritten
card onto one survivor so that Hahn-Banach, Mayer-Vietoris, Nondegenerate
Bilinear Form and Local Orientation became a single card, and once merging
appearance cards with each other, which are different exams of one problem and
the entire reason the appearance layer exists. The eleven collapses that were
actually correct were settled by reading twenty-two cards.

## What a tool may still do

Render and transport. The build pipeline turns authored content into a site;
`sync_macros.py` and `sync_bibliography.py` mirror an external file into the
repository so the build is self-contained. None of these decides anything about
the mathematics.

A check may report a measurement, named for exactly the measurement it took.
`audit.py`'s `duplicate-bodies` reports that two cards hold the same bytes. That
is a true statement about bytes and a *candidate* for someone to read. It is not
a finding that the two cards are the same statement, and it must never be wired
to anything that acts on that reading. A check whose name claims more than it
measured is the same defect in smaller form.

Semantic recurring review is advisory, not a check. `REVIEW_POLICY.md` is the named
index of previously observed defect patterns and the reading tasks that can surface
new candidates. The scheduled corpus-review crawler runs an agent only in an isolated,
disposable copy of a bounded slice and copies back only its report. It must stop at
candidate reporting: no candidate is a finding until a human reads it, no agent
finding triggers an edit, and a run with no candidates is not evidence that the corpus
is clean.

`just backlog` (and `uv run python tools/backlog.py`) regenerates `BACKLOG.md`
on every commit. Never run it manually — it is redundant.

## This corpus is authored content

This is a curated corpus of qualifying-exam mathematics, like the Stacks
Project. Every card is hand-authored: a problem, a definition, a theorem, or
another addressable mathematical statement. Solutions and hints are semantic
sections of the problem card they belong to. The fields on a
card — title, classification, relations, body — are content a human wrote or
will write.

`problem` is the only intrinsic card kind for posed mathematics. “Exercise”,
“homework problem”, “qual problem”, “review-sheet question”, and similar labels
describe an appearance in a source collection, not different mathematical
objects. The collection/source kind and its `ProblemEntry.comment` preserve that
appearance. Existing `E-*` ids remain permanent addresses; the prefix does not
declare a card kind. An authored `::: exercise` fence likewise records how the
source presented the item and parses as a problem section.

Good work on this corpus is reading mathematics, understanding what a statement
says, and making curation decisions: writing a title that names the problem,
classifying a card under the right topics, writing a solution, relating two
cards that depend on each other. A gap in a field is curation work, not a
tooling problem.

## The wiki is a textbook

`wiki/` is an authored study guide for graduate students preparing for these
exams. Treat it as an online textbook that is still being written. It has an
author making editorial decisions: what a reader needs to read, in what order,
and what has to sit next to what. It is a living document and it is meant to
grow.

Every organizing decision answers one question: **what does someone studying
for this exam need, and what must be adjacent to it?** Nothing else decides
where a page goes. Not the folder it is in now, not the chapter a textbook put
it in, not any property of the files.

That question produces page shapes with no counterpart in the data:

- A technique drilldown. "Which contour do I close?" is a decision procedure
  keyed on the shape of the integrand — semicircle, keyhole for a branch cut,
  rectangle for a periodic integrand, indented semicircle for a pole on the
  line. It is one of the most valuable pages a complex analysis guide can have.
  "How do I show a group of order n is not simple?" is the same page in algebra.

- A compendium. Counterexamples get their own page for the reason
  *Counterexamples in Topology* is a book: when the question is "is this true",
  you want the standard pathologies in one place. The standard contour integrals
  are another. So is a page of proof sketches of the big theorems, for the last
  week of review.

- A grouping by conclusion. Liouville, maximum modulus, the open mapping
  theorem, and the identity theorem belong together on a page about theorems
  that hand you a constant function, because on an exam you work backwards from
  the conclusion you need. This cuts across four textbook chapters.

- A toolkit. The Schwarz lemma, Blaschke factors, and Möbius maps go on one
  page because you use them in one breath.

Definitions, theorems, examples, and counterexamples are the **content of a
page**, inlined where the exposition needs them. Card ids are an addressing
layer: they let a statement be cited, reused, collected into a guide, and
located. The Stacks Project is a book whose statements carry tags. It is not a
tag collection with a book laid over it. This wiki is the same.

### External oracles versus local statement cards

A stable card id is not a reason to duplicate a standard definition or theorem.
Judge statement cards one at a time. If a canonical external oracle is strictly
more complete and maintained, and the local card adds no qual-specific
mathematical value, do not keep a proxy restatement merely so the repository can
own a tag for it. Authored prose should resolve that reference through the
external oracle. A stable permalink whose job is to take the reader to the
canonical definition or theorem is navigation, not a substitute bibliography:
link that permalink directly, but keep author/title/year attribution and other
bibliographic claims under the citation policy below.

The converse matters just as much: retain a local card when it adds something
the oracle does not supply in the form this audience needs -- a useful slogan,
specialization, proof sketch, example, counterexample, warning, computation, or
other review-specific synthesis. This is an editorial judgment, never a bulk
deduplication rule and never a heuristic based on card kind or title.

For localization, authored prerequisites name the denominator data as a
**submonoid of the multiplicative monoid** $(R,\cdot)$ when $1\in S$ is part of
the hypothesis. Do not weaken or silently rewrite source-authored problem text:
a merely nonempty multiplication-closed subset need not contain $1$ and need not
be a submonoid.

### Where agents get this wrong

**Do not score a reorganization by page count.** Reorganization relocates and
splits prose; it cannot reduce how much is written. The expected direction is
up, because the commonest editorial move is splitting one page that holds
several concepts into one page per concept. A page count that falls is evidence
that something was destroyed, not that the work went well.

**Do not derive the organization from the corpus.** Topic strings, card kinds,
tag frequencies, guide section lists, and the current folder names describe
storage. None of them is a table of contents. Reaching for them is reaching for
something countable because authorship is not countable, and it produces a
filing system rather than a book.

**Do not normalize the tree like a codebase.** One-axis-per-level, depth caps,
and deduplication by name are instincts for source code. Two pages that share a
name are not the same subject until someone reads both. Six complex analysis
pages carry "Schwarz" in the title and they are three different subjects: the
lemma, the reflection principle, and — under a heading that names neither —
Blaschke factors. Merging those on the name files the automorphism material
under a lemma it is not about.

**Do not remove a thin or empty section.** It is a chapter not yet written.
Applied algebra has 247 problems and no prose; prelim has 257 and almost none.
Those are the two largest pieces of writing this project is waiting on, not two
folders to tidy away. Write the chapter.

**Do not treat a merge as an improvement in itself.** A merge is only ever a
correction to a duplicate, and the duplication has to be proved by reading both
pages and finding the same mathematics.

### What good work looks like

Read the mathematics. Decide what a student needs. Write the page. Group,
split, collect, and drill down as the exposition requires, and justify each
move by what it does for a reader.

### Two concerns, and the test that separates them

The wiki has an engineering side and an authoring side. Both are real work and
neither substitutes for the other.

The engineering side measures the file. Does the page parse; does its
mathematics typeset; do its links resolve; does it carry a title and an integer
`order`; does its directory carry an `index.md`; is Obsidian syntax reaching
the reader as literal text; do two pages in one folder render the same text
twice in the sidebar. These are mechanical, they have exact answers, and a
checker should be strict about them. `just doctor` is that checker and it earns
its place. The rules in "What a tool may do" apply to it unchanged: it reports
a measurement named for exactly what it measured, and nothing acts on the
measurement.

The authoring side decides what the text says and how it is arranged. What a
reader needs, what belongs on one page, which pages a chapter has, what has to
sit next to what.

The test: **can the answer be wrong in a way only a mathematician reading the
page would notice?** If yes, it is authoring, and no checker gets a vote. "This
directory holds one page" is a fact about the filesystem; whether that is a
chapter with one section written or a page in the wrong place is a reading.
"These two pages share a title" is a fact; whether they hold the same
mathematics is a reading — six complex analysis pages titled Schwarz are three
different subjects.

Report the fact under its own name. Leave the reading to a reader.

## Work one item at a time

Never create or edit authored data in batches. This rule applies especially to
problem cards. It also applies to titles, statements, classifications,
relations, solutions, hints, and remarks.

First, write a straightforward checklist that names each item. Then process the
checklist in order, one item at a time. Read the source mathematics and the
relevant existing cards before each change. Make an independent curation
decision for that item. Verify the completed item before starting the next one.

Do not use scripts, loops, templates, bulk edits, or generators to produce
authored data. Never derive a title, create a card, fill a field, or change
mathematical content automatically. Each result must come from intelligent
reading and mathematical judgment.

## Public audience and remarks

The audience for this project is graduate students reviewing for a qualifying
exam after already taking a graduate course on the material. They are not
first-time learners. Public prose exists to support recall and problem solving:
state the result, link or transclude the statement, record the hypothesis that
usually gets missed, give the consequence used in solutions, or name the
counterexample/technique that decides a problem. Do not spend a sentence merely
convincing the reader that a theorem is important, useful, elegant, a
"workhorse", or what "makes the theory work". Replace that framing with the
mathematical payload it was standing in for.

A causal sentence is not filler merely because it contains "because" or "so".
"Apply monotone convergence to partial sums to interchange $\sum$ and $\int$"
is review content. "Monotone convergence matters because it is useful for
series" is not. This distinction is editorial and must be made by reading the
mathematics, never by a phrase-matching rewrite.

The public-facing surface — essentially the body of every card — should contain
only mathematical content: problem statements, definitions, theorems, solutions,
hints, errata, notes on questions (e.g. noting that a question is starred), and
contextual mathematical remarks (e.g. a remark explaining a reference to
something else in the source).

Internal process notes do NOT belong in `::: remark` blocks. Remarks render
on the public site and are visible to readers. Do not discuss provenance,
internal status, what is or isn't included, collection membership, missing
sources, or any other curation concern in remarks. Those belong in git commit
messages, repo-internal docs, or the vault.

It is valid for a remark to note that a problem references something not
included in the card (e.g. "this problem relies on Theorem X from the source")
— that is mathematical context, not internal status.

## Areas

The corpus stores four core qualifying-exam areas: algebra, real analysis,
complex analysis, and topology. Two additional exam tracks are registered as
areas because they are whole exams, not topics inside a core area: `prelim`
(UGA) and `applied-algebra` (UCSD Math 202). Exam identity is institution +
area + date; Applied Algebra and Algebra share institution and term, so they
cannot share `area: algebra`.

Extensions live inside those areas, usually as topics: algebraic geometry,
commutative algebra, differential geometry / manifolds, representation theory
(filed in algebra), and number theory.

Do not add numerical analysis, statistics, or probability. Those are out of
scope for now. A department posting an exam in those subjects is not a reason
to create a collection card. Applied Algebra is not numerical analysis.

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
read them there. Migration ledgers may name the paths those files had during the
migration; those are historical evidence, not current asset links.

`assets/` is for material the built corpus actually uses as an asset: source
documents such as exam PDFs under `assets/attachments/`, figures used by cards or
wiki pages, and the checked-in Markdown extractions of those PDFs. If a live card
still points into a migration snapshot, move or copy the needed figure/source
document into the appropriate subject or attachment asset location and point the
card there; do not retain the migration snapshot to satisfy the link.

## Heuristics have no place in this repo

A heuristic is a proxy for intelligent work that hasn't been done yet. It
produces plausible-looking output that fills a field, passes a check, and hides
the gap that a human author needs to fill. That is the opposite of curation —
it is manufacturing the appearance of curation. There is no scenario where a
heuristic serves this corpus. If a field is empty, the field is empty; report
it and a human will fill it.

## One-time tools do not stay in the repo

The migration is over. A tool that was used once to transport, route, split,
merge, or repair content during migration is done. Delete it when the work is
finished. Do not keep it, do not write tests for it, do not enshrine it as a
recipe. Its output is committed corpus content; the tool itself is fossil.

## PDF extraction

The only valid method of PDF extraction is:

```bash
mineru-open-api flash-extract myfile.pdf --language en
```

Do not use `pdftotext`, `pdftoppm`, or any other tools.

Never extract PDFs to `/tmp`, `.tmp`, or any other temp directory. Temp
files are not tracked by git and vanish between sessions. Always extract
into the repository so the output is versioned and persistent.

The correct output path is under `assets/attachments/` (for source PDFs)
or `assets/` (for extracted markdown). Example:

```bash
mineru-open-api flash-extract assets/attachments/exam.pdf > assets/attachments/exam_extracted.md
```

If you need intermediate files during extraction, stage them in the repo
too — for example `assets/attachments/intermediate/`. Delete them when
the final extraction is committed.

## What a tool may do

A tool may render and transport: build the site, sync an external file into the
repo, check that the corpus is internally consistent. A check may report a
measurement — two cards hold the same bytes, a card has no solution, a title is
unreadable — named for exactly what it measured. The measurement is a candidate
for a human to read. It must never be wired to anything that acts on it.

The build reads authored content and renders it. It does not derive fields. A
build that derives titles, classifications, relations, or any other field is
fabricating content, not rendering it.

# Collection provenance

The corpus has two tiers: collections and problems. A collection is the only
card that carries `provenance:`. A problem carries no provenance; where a
problem comes from follows from backlinks — every collection whose
`source.problems` lists it. Collection cards live in `corpus/collections/`.

## One problem browser

`problems.html` is the only reader-facing implementation that displays a
metadata-selected family of problem rows. It owns filtering, source-scoped
ordering, random sampling, and print/PDF. Do not add a second problem-list or
practice-set renderer to guides, wiki pages, collection pages, or another site
route.

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
  links to any nested source collections, but does not enumerate its problems.
  It deep-links with `collection=SRC-...`. The browser reproduces the exact
  source sections, order, and appearance locators from `collection_problems`.
- `generate.html` is compatibility-only: old URLs redirect to `problems.html`
  with `sample=8`. It must not acquire controls, query logic, or a second
  problem data path.
- `E-*` and `P-*` are stable addresses. Every posed mathematical card is
  `kind: problem`; whether a source called one an exercise, homework problem,
  or qualifying-exam problem belongs to its collection appearance.

A source's ordered problem membership remains authored corpus data even though
the source page does not materialize it. Centralizing display does not flatten
or discard source order.

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

## Problems may appear in multiple collections

It is common and expected for a problem to appear in multiple collections. An
exam may reuse a question from a textbook, the same problem may appear on
different exams, or a compilation may contain overlapping problem sets. Each
collection independently lists the problems it contains; the same problem card
may be referenced by many collections. Do not merge, deduplicate, or suppress
a problem card because it appears in multiple places — that is correct behavior,
not redundancy.

`::: remark` blocks render on the public site. They may discuss the mathematics
or the contents of the card (for example which pages of a multi-institution
scan this exam occupies). They are not a dump of missing PDFs, wiki paths,
or the state of the provenance field.

# Data issues

Completion of all solutions is a very low priority concern and is NOT a data
issue. Solutions are authored content that will be filled in over time.

Important data issues (roughly in order of urgency):
1. Incorrect data — problem statements, titles, or classifications that are
   simply wrong. This is the most urgent.
2. Problem cards not appearing in any collection (orphaned problems)
3. Collections containing no problems or an incomplete list of problems
4. Missing or invalid provenance that prevents auditing

Missing solutions, empty solution fields, and unsolved cards are authoring
concerns, not data integrity problems.

# Work queues

Outstanding work is recorded so no agent has to rediscover it. `TODO.md`
holds the authored dispositions. `BACKLOG.md` holds the current
measurements, generated from the named measurement tools; nothing else
writes it. Generation is automatic — `just test-push` regenerates
`BACKLOG.md` before the suite runs, so a push never ships a stale queue.
When a generation changes the file, commit the diff in the next commit.
The queues are candidates to read — a measurement that disappears is not a
disposition, so record the reason in `TODO.md`.

# Running checks

Most checks already run for you: the commit gate runs the immediate
checks, and the push gate runs the full suite and refreshes `BACKLOG.md`
first. Run `qualc check`, `pytest`, or any measurement tool by hand only
sparingly — for instance while iterating on one known defect. Otherwise
take work from the queues, do the semantic work on the cards, and commit
as normal; the gates prove consistency.

# Citation policy

Never cite a source in prose. All citations must go through the bibliography:
1. Find external oracles for bibtex information — never confabulate it from
   memory.
2. Integrate the entry into the bibliography.
3. Cite using standard pandoc-crossref syntax.

Never repeat the title, author, or year in prose. CSL controls and unifies the
presentation of citations. Inline citation like `(Author, Year)` in prose is
fabricating metadata; the bibliography handles this.

# Card references to collections

Do not have cards manually reference which collections they appear in. This is
redundant: collections list their problems in `source.problems`, and backlinks
are generated automatically to populate this information. Cards should not
contain prose like "this problem appears in Exam X" or "see also collection Y"
— the site renders this from collection relationships.

# Card titles and source locators

A card title names the mathematics on the card. A textbook section number, exam
problem number, or other source locator is not a title. Source locators belong to
the collection entry that lists the problem, because one problem may occur at
different locations in different sources.

Use mathematical notation in a title when prose would merely spell out a standard
formula or object. Write `$\ZZ^3$`, `$x^8+1$`, `$L^2$`, `$\pi_3$`,
`$\ZZ\times\ZZ$`, or `$\frac{\cos x}{(1+x^2)^2}$`, not "Z cubed",
"x to the eighth plus one", "L2", "pi_3", "Z x Z", or "cos x over the
square of one plus x squared". Prose should name the mathematical phenomenon;
notation should carry routine formulas. Do not make the opposite mistake of
turning an ordinary conceptual title such as "Product of compact spaces" into
unreadable symbol soup merely because symbols are available.

```yaml
- id: P-EXAMPLE
  comment: Hungerford 4.1.7
```

The card itself keeps only its mathematical name. The rendered Source Collections
panel combines the collection name with that appearance comment. Do not add a
card-level `subtitle:` for provenance; that field was retired once collection
appearances became the canonical home for locators.

# Review prompts

Any card may carry `prompts:`, the questions that front it when it is used for
review.

```yaml
title: Normal Family
prompts:
- What is a normal family?
- Give the Montel criterion.
```

A prompt is a question, and the card is its answer. One card may have several,
because one statement can be asked for in more than one way; the list keeps them
all rather than choosing between them. There is no separate flashcard kind: a
prompt hangs on the definition or theorem it tests, so the mathematics is
written once.

The list is free text and empty by default. Empty means the card has no review
question yet, and nothing derives one. A title names the card; it is not a
question, and it is never used as one.

# Solution status

Solution status is derived from content, not declared. A problem card is solved
when it carries a `solution` section. There is no standalone solution card and
no `solves` relation: the solution is content of the problem it answers. There
is no `solved` field; a solutions commit writes
the body and the status follows from it.

Missing solutions are authored mathematical content, not corpus defects, so
they do not appear in `BACKLOG.md`. The outstanding missing-solution queue
lives in two surfaces:

- `queues/C-unsolved-cards.md` — the measurement. It lists every problem card
  with no `solution` section.
  Regenerated by `just unsolved` and by the commit gate whenever a commit
  touches the corpus. A card leaves the list only by gaining a solution; the
  boxes are a measurement, not a ledger.
- `queues/09-author-solutions.md` — the authored disposition (Queue 9,
  `TODO.md` §7 "Author solutions"). It is a repeating one-card-at-a-time loop:
  select an unsolved card, read the problem and its source, write a
  Lamport-style structured proof, add a `solution` section, and commit before
  selecting the next card.

`just sample-unsolved` draws n random unsolved cards (default 5) by querying
the catalog for problem cards with no solution section. The solution
authoring workflow is recorded in `TODO.md`
under [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2), and the
solution-sheet integration ledgers live in
`sources/qual-review-and-solutions-ledgers/`.

## Audit history

A problem card may carry `audit:`, a list of dated events recording who did
what to it. Three events exist:

- `solution-written` — someone wrote the solution on the card.
- `source-checked` — someone compared the statement against the original source.
- `solution-reviewed` — someone checked the solution for correctness.

```yaml
audit:
- event: solution-written
  by: dzackgarza
  date: 2026-08-16
- event: solution-reviewed
  by: neil
  date: 2026-08-27
  note: optional free text
```

`by` is a handle or a name, whatever identifies the person; there is no registry.
`date` is an ISO calendar date. The field is `date` and not `on` because YAML
reads a bare `on` as the boolean `true`. `note` is optional. The entries stay in
the order they were written, and repeated rounds of one event are normal: a
solution reviewed twice records two `solution-reviewed` entries.

This list is a record, not a status. Nothing is derived from it, and it does not
replace the rule above: a card is solved because it carries a solution, not
because someone wrote it down here. Record only events you can substantiate.
Backfilling the list for cards whose history nobody knows is fabricating content.

* * *

> Source: `PR_GUIDANCE.md` in `ai`.

# Review Guidelines

These are additional requirements for reviewing agent work.
They do not replace the reviewer’s normal role, repo-specific standards, or technical
judgment. They provide the failure model that should shape the review.

The task is not merely to review a PR. The task is to decide whether a completion claim
is true under the original objective.
The standard is full, correct, provable completion against the original requirements and
repo guidelines. Anything less is incomplete work that must not be treated as a win.

## Failure Model

Agents systematically produce impressive non-completion.
Common patterns are: polished summaries that imply finished work, caveats that quietly
narrow the goal, reclassification without proof, delegated discovery presented as
resolution, process language that substitutes for evidence, merged PRs treated as
completion, passing checks treated as semantic proof, and artifacts that look
substantial while leaving required work unowned.

Treat the agent’s summary, PR description, closing comment, issue closure, “goal
completed” statement, and self-reported validations as untrusted.
They may be diagnostic pointers, but they are not evidence that the work is complete.
The evidence is the original issue or task, the code diff, tests, source/runtime facts,
review comments, and produced artifacts.

## Decisive Invariants

Preserve the original success condition.
Read the original issue or task before accepting any restatement of it.
Keep its quantifiers intact: “all,” “complete,” "full subset," “zero remaining,” and
similar terms cannot be quietly narrowed to examples, partial coverage, known blockers,
or whatever the PR happened to touch.

Nothing required may disappear silently.
A required work family must be implemented, explicitly falsified, or validly
reclassified with evidence that satisfies the issue’s own standard.
Partial implementation is not completion.
Future work is not completion.
Count reduction is not completion.
Resolved review threads are not completion.
Passing checks are not completion.
Substantial-looking work is not completion.
“Better than before” is not completion.

Goal substitution is the main thing to detect.
Ask whether the submitted work solves the original problem or merely produces a narrower
artifact: cleaner metadata, a partial subset, a better explanation, a new issue, a
renamed scope, a local workaround, or proof that someone should investigate later.

Technically correct administrative artifacts can be goal substitution.
A well-written issue, comment, audit note, scope statement, or enumeration of remaining
work may be required, but it does not complete implementation, testing, proof, or
downstream cleanup. If the original task requires execution, the artifact is only useful
insofar as it drives that execution; it must not become the stopping point.

Treat self-scoped remaining-work lists as a severe completion-laundering pattern.
When an agent is asked to enumerate remaining work, the domain is the original full
completion requirement, not the agent’s intended subset, the PR’s current shape, a
closeability criterion, or the work left after deferral and reclassification.
A valid enumeration subtracts only artifact-proven completed work from the original
contract. Deferrals, routed follow-ups, owner changes, and truthful incompletion notes
remain unresolved work unless the original task explicitly made that administrative
routing the whole deliverable.

If an agent repeats a narrowed enumeration after being corrected, treat that as a hard
misalignment signal, not as an innocent wording issue.
The reviewer should identify the original full requirement, the scope the agent
substituted, and the required work hidden by that substitution.

Silent reclassification is not resolution.
If the PR says remaining work is out-of-scope, research-owned, stub-owned, plugin-owned,
downstream-owned, or future-owned, require evidence from the relevant source/runtime
behavior, repo boundary, or original acceptance criteria.
A sentence in the PR description is not enough.

Ownership boundaries matter.
The submitting repo must prove its own claimed behavior and do the blocker forensics
required by its own issue.
Do not require a receiving or downstream repo to classify another project’s internal
uncertainty unless the original issue explicitly made that part of acceptance.
When an external issue is created, it should be written for that receiving repo, not for
a reader who already knows the submitting repo’s context.

## Evidence Expectations

Review tests as evidence, not as decoration.
Valid tests exercise the real production path or semantic requirement.
Be skeptical of helper-only tests, tautologies, assertions of the implementation’s own
output, bypasses around the runtime/plugin/stub path, example-only coverage where the
issue required full coverage, weakened assertions, and missing invalid-nearby cases
where the fix could overgeneralize.

For plugin work, the evidence should usually distinguish valid generic behavior from
invalid nearby ordinary Python and should not hard-code a downstream consumer.
For stubs work, the evidence should be source-backed: the upstream surface exists, the
stub matches public behavior, no fake API is added, no Any/object opacity escape is
introduced, and inherited-method inflation is not used unless source exposes that
surface.

Watch for code-level laundering: hard-coded consumer names, support for local research
abstractions as if they were external API, fake stubs, broad Any/object escapes, line
suppressions, diagnostic filtering, deletion of required data, broad type widening, and
any move that makes checks pass by weakening the problem instead of solving it.

## When Acting on Review Feedback

A positive disposition requires a commit.

Do not resolve an accepted review comment until the code/proof remediation is committed and the reply cites the commit.

Never reply “accepted,” “aligned,” “fixed,” “addressed,” or “will address” to a review thread unless the remediation is already committed. A thread cannot be resolved on intent or future work.

Rejected and modified feedback must be collected in a top-level PR comment titled `Review feedback disposition ledger` so resolved threads do not hide the audit trail.

Review comments are not implementation specs. The worker must translate accepted feedback into first-principles remediation requirements before assigning implementation.

For each comment:
- Identify the concern.
- Identify the proposed fix.
- Decide whether the concern is true under global + repo policy.
- Decide whether the proposed fix preserves those policies.
- If the concern is true but the fix is wrong, apply a policy-compatible remediation.

## Writing the Review

Write nuanced feedback for an intelligent reader.
Do not force a machine-readable template, a mandatory table, or a simplistic pass/fail
label when prose communicates the situation better.
Do make the completion judgment clear: whether the original task can be considered
complete, what evidence supports that judgment, and which unresolved requirements block
completion if any remain.

Do not foreground effort, progress, good intentions, volume of work, or “substantial”
partial implementation when required work remains.
Mention completed pieces only when they are necessary to identify the exact remaining
blockers or to prevent redoing already-correct work.
Do not compare incomplete work to “no work done” or “completely fake work”; compare it
to the expected standard: the task done correctly, completely, and provably.

When required work remains, lead with the incompleteness and the concrete blockers.
Do not make the reader excavate the missing work from beneath praise, context-setting,
or a narrative of what did get done.

Nuance belongs in the evidence and blocker analysis, not in softening the completion
standard. The review should make it easy to finish the work, not easy to feel satisfied
with less than the original contract required.
