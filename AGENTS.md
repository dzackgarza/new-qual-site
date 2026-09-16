# Repository work documents

Read [TODO.md](TODO.md) for the task DAG,
[CONTRIBUTING.md](CONTRIBUTING.md#named-policies) for named contribution policies,
and [COMPLAINTS.md](COMPLAINTS.md) for mathematical issues and workflow papercuts.
Apply `QUAL-05` when a problem is encountered, including outside the selected card.
Record the evidence before leaving that work; logging does not complete a repair.
These documents apply to every stream working in the clone.

## Owner pause — 2026-09-16

The repository owner has paused this workstream. Do not start, select, continue,
revive, wake, route, or push new work while this pause stands. If a turn was already
mid-unit when the pause arrived, bank only that coherent unit and stop before selecting
another. Preserve the existing dirty/shared tree. Only a later explicit owner instruction
resumes this repository; recurrence of an older scheduled continuation does not supersede
the pause.

<!-- agent-memory:start -->
# Agent memory

This repository uses the central agent memory vault at `/home/dzack/.agent-memory-vault`.

Project memory key: `projects/new-qual-site/index`.

Repository `.agents` and `.hermes` paths are symlinks to the same vault-owned project directory.

Before changing architecture, search both project and global memory:

```bash
agent-memory search --scope both "<task or subsystem>"
```

Record durable repo-specific lessons with:

```bash
agent-memory add --scope project --type decision --title <title> --content <content>
agent-memory add --scope project --type trap --title <title> --content <content>
agent-memory add --scope project --type advice --title <title> --content <content>
agent-memory add --scope project --type context --title <title> --content <content>
agent-memory add --scope project --type reference --title <title> --content <content>
```

Plan work is card-backed. Create and update plan cards with `agent-memory plan add` and `agent-memory plan update`, not `agent-memory add --type plan`.

Use `agent-memory retrieve <key>`, `agent-memory update <key>`, and `agent-memory delete <key>` for memory CRUD.

The vault should be committed at all times. Treat staged or unstaged vault changes as an ephemeral error state. Before normal memory work resumes, load the bundled vault-maintenance skill with `agent-memory maintain skill vault-maintenance` and follow its referenced check, repair, and commit workflows.

Move reusable lessons during maintenance with:

```bash
agent-memory maintain move <key> --to global/advice
```
<!-- agent-memory:end -->


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

Semantic recurring review is advisory, not a check. The
[corpus review patterns](CONTRIBUTING.md#corpus-review-patterns) name previously observed
defect patterns and the reading tasks that can surface new candidates. The scheduled corpus-review crawler runs an agent only in an isolated,
disposable copy of a bounded slice and copies back only its report. It must stop at
candidate reporting: no candidate is a finding until a human reads it, no agent
finding triggers an edit, and a run with no candidates is not evidence that the corpus
is clean.

`just backlog` (and `uv run python tools/backlog.py`) regenerates `BACKLOG.md`;
`just test-push` runs it before every push. Never run it manually — it is redundant.

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

Whether a standard definition or theorem keeps a local statement card or resolves to an
external oracle is `SOURCE-02` in [CONTRIBUTING.md](CONTRIBUTING.md); how localization
prerequisites are phrased is `DEF-35`.

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

**Do not remove a thin or empty section.** It is a chapter not yet written, not
a folder to tidy away. Write the chapter.

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

## Do not end a turn without the next source started

A turn that ends with the work banked and nothing in flight still stops this repository until
somebody notices and pushes it. On 2026-09-12 that happened nine times, costing between eleven
and fifty-five minutes each — more total time than every blocked commit, stale lock and failed
hook that day combined.

Ending a turn is a decision to stop, so make it deliberately. When a unit of work is committed,
take the next one in the same turn from the highest-priority node with ready work in the
[TODO.md milestone](TODO.md#milestone-publish-with-every-remedial-obligation-cleared): open it,
read it, begin. If work genuinely must pause — a run you are waiting on, a decision you cannot
make — say what you are waiting for and what you will do when it returns, so the next turn begins
with an instruction rather than a question.

Selecting the next item is your work, not the steward's. A Queue E entry recorded as blocked on
MinerU Flash is not ready work; take the next ready item instead.

## A disposition is not a unit of work

Deciding that a source is reference-only, ticking a queue entry, closing a defect record,
normalising whitespace across a collection: none of this is authored content, and none of it is
a unit of work. The unit of work in this repository is a card, a solution, a source properly
carded, a statement corrected against its source, or a page or card's copy rewritten to the
[CONTRIBUTING.md](CONTRIBUTING.md) policies. A session whose output is dispositions has produced a tidier queue and no mathematics.

This matters here more than elsewhere because the queue is long and dispositioning is easy. It
is always possible to spend a session deciding about sources rather than carding them, and the
queue counts will move the whole time. On 2026-09-12 a worker described folding a queue
disposition into a commit as its next unit of work, and separately produced commits titled
"bank" that moved the dirty count by one file.

So: fold the queue disposition into the commit carrying the cards it describes, never commit it
alone, and never let a turn end with dispositions as its only product. If a source genuinely
needs no cards, say so in the commit that finishes the source before it, and move to one that
does.

## Your queues are a product, and a wrong one costs cards

The files under `queues/` and the output of `just unsolved` are what say which source is next
and which card is still unsolved. They are instruments, not notes: a queue whose counts are
wrong sends the next worker to the wrong source, and an unsolved-card list that cannot tell a
solved card from an unsolved one means nobody can see what the corpus still owes.

They are also routinely wrong in a specific way — OCR-derived problem counts. A queue entry
saying a PDF holds four problems when it holds fourteen is not a small error; it decides how
many cards get authored. Count from the source document, never from the inventory, and when
they disagree, correct the queue in the commit that cards the source.

Treat a queue defect as work, not as noise to steer around. If the regeneration is wrong, fix
the regenerator; if an entry is unreadable, resolve it rather than skipping past it; if the
list disagrees with the corpus, find out which is lying before authoring against either.

## Review your own session for drift

Before starting a new source, look back at the one you just finished and ask what it produced:

- **Authored content, or dispositions and normalisations?** Cards, solutions, corrected
  statements and rewritten copy are the product. A session whose output is decisions about
  sources has left the corpus unchanged.
- **Did authored content change?** If commits landed but no card, statement, solution or page
  copy changed, the commits were not authoring.
- **Is something making every source cost more than it should?** An extraction step you redo by
  hand each time, a check that reformats files you did not touch, a count you have learned not
  to trust. That is an obstruction, and working around it silently is how it survives to cost
  the next worker the same.

Fix the obstruction where it lives, with its regression, and note it in the queue.

## Repair the tooling that wastes your turns

When the same friction appears twice, stop and fix it at its owner rather than working around
it. The formatter that reflowed seventy-six sibling cards on every pathspec commit was not a
quirk to route around — it made `git status` unreadable, which is the condition under which
authored work goes missing unnoticed, and this repository has already lost 962 authored lines
that way. It was a four-line defect in a shared formatter that had been costing every commit
for days.

The same applies to an OCR count that is routinely wrong, an extraction path that silently
truncates, a check that cannot distinguish a solved card from an unsolved one. Fix it where it
lives, commit the fix with its regression, and note it in the queue. A workaround you carry in
your head is a defect the next worker meets fresh.

## Public audience and remarks

The audience, the public surface of a card, and what a rendered remark may carry are defined in
[CONTRIBUTING.md](CONTRIBUTING.md#audience-and-scope): `PROSE-01`, `PROSE-11`, `SEC-7`, and
`QUAL-08`. Deciding whether a sentence is filler or review content is editorial and is made by
reading the mathematics, never by a phrase-matching rewrite.

## Areas

The corpus stores four core qualifying-exam areas: algebra, real analysis,
complex analysis, and topology. Two additional exam tracks are registered as
areas because they are whole exams, not topics inside a core area: `prelim`
(UGA) and `applied-algebra` (UCSD Math 202). Exam identity is institution +
area + date; Applied Algebra and Algebra share institution and term, so they
cannot share `area: algebra`.

`algebraic-geometry` is a seventh registered area. It is a qualifying exam in
its own right at Harvard and Berkeley, with its own examiners and its own
question bank, so it is not a topic inside algebra.

The remaining extensions do live inside those areas as topics: commutative
algebra, differential geometry / manifolds, representation theory (filed in
algebra), and number theory.

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

PDF intake has one epistemic baseline: a **high-quality machine extraction** checked into the repository.
Two methods are valid. Use MinerU Flash first:

```bash
mineru-open-api flash-extract myfile.pdf --language en
```

When MinerU Flash fails on a source (timeouts, parse failures, or garbled output at an
identified location), extract it with the Mistral OCR API, which writes the extraction and its
provenance file:

```bash
just ocr-pdf assets/attachments/myfile.pdf assets/attachments/myfile_extracted.md
```

Do not use `pdftotext`, `pdftoppm`, Tesseract, PyMuPDF/`fitz`, PDFium/`pypdfium2`,
`mutool`, screenshots, page renders, model vision, or any other mechanism as an extraction
or validation substitute. A model looking at a rendered PDF page provides no reproducible
evidence that an extraction is correct; visual agreement must never be used to certify a
statement, problem count, formula, label, or source transcription.

Every problem-bearing PDF consumed by intake must therefore have a checked-in MinerU Flash or
Mistral OCR Markdown extraction. The extraction is the auditable transcription baseline from which cards
are produced. An existing `*_extracted.md` or `assets/attachments/extracted/*.md` file may be
reused only when repository evidence establishes that it came from one of these two paths.
**Unknown extraction provenance is not acceptable evidence:** regenerate the extraction before
using it for intake.

Model work begins only *after* the machine extraction exists. Its role
is limited to transcription cleanup and resolving concrete extractor errors or ambiguities. If a
specific extraction defect must be resolved against the original PDF, inspect only that disputed
location and record the correction as such; do not turn source inspection into an independent
second transcription pass or a claim that the rest of the extraction has been verified. If
neither extractor can run, intake of that PDF is blocked rather than falling back to another
extraction path.

A genuine source that exists only as a retained raster image is not a separate extraction case.
Preserve the original image as provenance, wrap it losslessly and deterministically into a PDF
container, record the image hash and derived-PDF hash, and run the same extraction on
that PDF. The conversion step must not OCR, resample, enhance, redraw, or otherwise interpret the
image. Model vision is still not evidence. If the image itself is missing (for example the lost Anki
`collection.media` figures), there is nothing to convert or extract; that remains missing-source
recovery work.

Never extract PDFs to `/tmp`, `.tmp`, or any other temp directory. Temp
files are not tracked by git and vanish between sessions. Always extract
into the repository so the output is versioned and persistent.

Source PDFs live under `assets/attachments/`. Their checked-in extractions live
under `assets/attachments/` as `<stem>_extracted.md` beside the PDF or as
`assets/attachments/extracted/<stem>.md`. Example:

```bash
mineru-open-api flash-extract assets/attachments/exam.pdf > assets/attachments/exam_extracted.md
```

Commit the final extraction with the intake work. If you need intermediate files while resolving
a specific extraction defect, stage them in the repo — for example
`assets/attachments/intermediate/` — and delete them when the final extraction/correction is
committed. Generic page-render review directories are not an intake artifact and must not be
created merely to "verify" a PDF visually.

### Extraction output is an input, not a card

What comes out of an extractor is a transcription source. It becomes a card when its
mathematics has been written as LaTeX and reads as the source reads — not when it has been
pasted between `::: {.problem}` fences. A statement carrying unicode mathematics outside any
`$`-delimiter has not been transcribed: `∂u ∂x (0, 0)` is a lost derivative, a bare `Z` where
an integral belongs is a lost integral, and a nested radical flattened to `v u s r Z 9u √ q t`
is a lost problem. The card looks finished, `just unsolved` offers it, and a worker writes a
proof of something nobody asked.

Never run a whitespace or line normalizer over unconverted extraction output. The column
layout in a raw extraction is the last surviving record of the fraction bar, the integral
bound, and the superscript; joining the lines is not a cleanup, it is the step that makes the
card unrecoverable without going back to the PDF. On 2026-09-13 a normalization pass did
exactly this to three freshly ingested collections, one commit after ingesting them.

Two consequences for a turn. An ingest that needs a follow-up normalization commit did not
land cards, it landed extraction residue — fix the pipeline rather than paying it by hand on
every source. And where the source cannot settle what a statement said, mark the card as
unrecovered and say so; an invented plausible problem is the one outcome worse than a gap,
because nothing downstream can tell it from the real thing.

## Bank before you wait

Work that is written but uncommitted lives only in this chat's working tree, and a turn that
ends, a chat that is replaced, or a host that runs out of memory takes it with it. On
2026-09-13 this repository sat idle holding 91 tracked paths of finished repairs, none of them
banked, while the thing they were waiting on was a gate run over the whole batch.

So order the work the other way. When a piece is written and you believe it correct, commit it
*before* starting whatever comes next — the validating run, the next collection, the rest of
the batch. A commit is not a claim that everything is finished; the message can say what is
still pending. What it buys is that a stall, a kill or an ended turn costs a wait and nothing
else, rather than taking the work with it.

Commit in coherent groups as you go, not in one batch at the end. One collection transcribed is a commit; there is no reason for the second collection's work to ride on the first one's gate.

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

## Problems may appear in multiple collections

It is common and expected for a problem to appear in multiple collections. An
exam may reuse a question from a textbook, the same problem may appear on
different exams, or a compilation may contain overlapping problem sets. Each
collection independently lists the problems it contains; the same problem card
may be referenced by many collections. Do not merge, deduplicate, or suppress
a problem card because it appears in multiple places — that is correct behavior,
not redundancy. What a rendered remark may say about a card's sources is `SEC-7`.

# Data issues

Completion of all solutions is a very low priority concern and is NOT a data
issue. Solutions are authored content that will be filled in over time, after
`publication-milestone`. The order of work across copy, intake, mathematical
repair and proof adjudication is the
[TODO.md milestone](TODO.md#milestone-publish-with-every-remedial-obligation-cleared).

Within data issues, in order of urgency:
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

## Reconcile queues before claiming

Every stream solves on `main`, and the queues are regenerated at push, so a queue can be stale
the moment a sibling commits. Before claiming a card from `queues/C-unsolved-cards.md` or a
sibling queue, read the card itself: a listed card may already carry a solution. Never author
the same card as a sibling; batch-committing cards authored off-queue is prohibited.

# One checkout, one branch

**Streams work directly on `main` in the single clone. Do not create worktrees and
do not create branches.**

This repository is authored content. A stream writes solutions, hints and wiki prose
into card files it selected off a queue, and two streams never hold the same card —
so there is nothing for a branch to isolate and nothing for a merge to resolve. The
isolation apparatus was not protecting the work; it was protecting against a fear.

The fear is `git commit -a` sweeping in a sibling stream's concurrent edit. That is
not a conflict and not lost work: the other stream's change is already on disk and
already correct, and the only thing wrong is the message describing it. Fix the
message:

```bash
git commit --amend        # your commit swept in a sibling's card
```

Or commit the paths you meant in the first place, which `QUAL-07` already requires:

```bash
git commit -- corpus/problems/Algebra/P-XXXXX.md
```

Neither costs anything. A worktree per stream costs a second checkout of the whole
corpus — 353 MB of tracked assets each — to carry a handful of edited markdown files.
Twenty-seven of them filled the volume on 2026-09-10 while holding forty-four changed
files between them, and a full volume presents as killed processes and dying exec
sessions rather than as a disk error, so it reads as worker misbehaviour for hours
before anyone runs `df`.

There is one environment, the main checkout's `.venv`, created with
`uv sync --group dev` and used directly. No `UV_PROJECT_ENVIRONMENT`, no
`UV_NO_SYNC`, no `PYTHONPATH` override — those existed solely to stop worktrees
fighting over one editable install, and with one checkout there is nothing to point
anywhere.

## Worktrees from before this rule

`git worktree list` reports only the main checkout, and `test-commit` runs `_no-worktrees`.
If a worktree from before this rule is found, it is not debris and must not be removed on
sight: another stream's authoring is live until three readings say otherwise, taken
immediately before the removal and never carried over from an earlier survey.

```bash
git -C PATH --no-optional-locks status --short                     # 1. clean
git merge-base --is-ancestor "$(git -C PATH rev-parse HEAD)" HEAD  # 2. reachable
pgrep -a -f PATH                                                   # 3. no process
```

Reading 1 fails on any output at all — staged or unstaged, tracked or untracked. An
uncommitted card is somebody's unbanked authoring, and a `.orig` file beside it is the
evidence of a merge they are still resolving. Reading 2 asks whether every commit on
that worktree's branch is already in `main`; run it from the main checkout, whose
`HEAD` is the reference. Reading 3 discards the checking shell's own PID, and
`pgrep -f` matches on substring, so a probe for `sp19` also matches `sp19-audit2` —
read the command lines it prints rather than counting them.

When all three pass:

```bash
git worktree remove .worktrees/<name>
git worktree prune
```

When any one fails, leave it in place and report it. Re-take all three for each
worktree at the point of removal rather than acting on a list. Worktrees outside the
repository are outside this rule; report them and do not remove them.


## Merge and reconciliation snapshots

A merge, reconciliation, or duplicate-adjudication snapshot is temporary working state,
not an archive. Delete the snapshot in the same turn that finishes its last use. If the
work that depends on it is still active, leave it in place and state the specific live
dependency; do not retain a completed snapshot merely as insurance.

# Running checks

**Commit content with `git commit --no-verify`.** This is the repository owner's sanctioned commit
route for prose-only, documentation-only, and authored-content commits (copy, prose, mathematics,
solutions, statement corrections, new cards): it is the documented workflow, not an evasion of any
gate. Those commits are verified by reading the diff, and every gate runs at push. `just
commit-card` takes the same route. Code, renderer, schema, and executable-configuration commits use
normal hooks.

Checks follow `QUAL-06` in [CONTRIBUTING.md](CONTRIBUTING.md#named-policies). Content work — copy,
prose, mathematics, solutions, statement corrections, and new cards or ingested collections — is
verified by reading its diff and reviewing the mathematics, and is committed as soon as the item is
done. Do not run or wait on builds, test suites, renders, screenshots, broad formatters, or queue
regeneration for content work: repairs to copy, prose, mathematics, and solutions are checked by
eye until they are pushed. The content-specific gates — the extraction detector, which rejects
untranscribed extractor output in a problem block, and the regeneration of
`queues/C-unsolved-cards.md` — run at push, together with the build, crawl, and test suite.
Builds, renders, and rendered-page inspection belong to the push and deployment phase.

Code, renderer, schema, executable configuration, and mixed code/content changes use the normal
commit and push gates. Use focused checks while investigating a specific defect; let those gates
run the broader checks.

## A red gate is the current task

When a gate you run — a code commit gate, or the push gate — goes red, stop and diagnose it:
root-cause and fix the gate, or report it as a blocker with a reproducer. Do not push behind a red
gate, and do not accumulate unpushed work around one. A gate that is red on two consecutive
attempts is a defect to diagnose, not an environment condition to wait out.

# Citations, collection references, and titles

Citations follow `CITE-1` and `CITE-2`; a card does not list the collections it appears in
(`SOURCE-03`); and a card title names the mathematics, with source locators on the collection
appearance (`CARD-01`, `CARD-02`, `CARD-06`). All are in [CONTRIBUTING.md](CONTRIBUTING.md).

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
they do not appear in `BACKLOG.md`. The generated measurement and the authored
workflow are deliberately separate:

- `queues/C-unsolved-cards.md` — the measurement. It lists every problem card
  with no `solution` section.
  Regenerated by `just unsolved` and at push; between pushes it can lag the
  corpus, so read the candidate card before selecting it. A card leaves the list only by gaining
  a solution; the boxes are a measurement, not a ledger.
- `TODO.md` §7, "Author solutions", together with issue #2 — the authored
  repeating loop, which begins after `publication-milestone`. Select one unsolved card, read the problem and its source,
  independently verify any retained source solution, write a complete
  Lamport-style structured proof in a `solution` section on that same problem
  card in the layout `STYLE-08` fixes, and commit it before selecting the next
  card, verified by reading as [Running checks](#running-checks) describes.

`just sample-unsolved COLLECTION [n] [section]` samples up to n distinct
unsolved card IDs (default 5) from one collection's authored appearances and
lists them in source order. The solution
authoring workflow is recorded in `TODO.md` under
[issue #2](https://github.com/dzackgarza/new-qual-site/issues/2), and the
solution-sheet routing ledgers live in
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
