# Repository work documents

Use the [shared math container](https://github.com/dzackgarza/ai-review-ci/blob/main/SAGE-CONTAINER.md#use-the-image)
(`ghcr.io/dzackgarza/sage:develop`) for Lean/elan, Sage with mypy, GAP,
Julia/Oscar, Macaulay2, and Singular. The guide covers image pull/run commands,
CI use, and the host launchers.

Read the [issue tree](https://github.com/dzackgarza/new-qual-site/issues/83) for the open work (`itree next dzackgarza/new-qual-site` selects the next work unit),
[CONTRIBUTING.md](CONTRIBUTING.md#named-policies) for named contribution policies,
and [COMPLAINTS.md](COMPLAINTS.md) for mathematical issues and workflow papercuts.
Apply `QUAL-05` when a problem is encountered, including outside the selected card.
Record the evidence before leaving that work; logging does not complete a repair.
These documents apply to every stream working in the clone.

Lean formalization lives only in [lean-categories](https://github.com/dzackgarza/lean-categories).
This repository holds no Lean declaration. A Lean certificate of a card is a declaration on
lean-categories main, written there by a lean-categories issue under its rules (its LC-09
search of Mathlib and the formalization corpus first), and the card links it.
A Lean certificate settles a contested proof: when agents dispute a card's proof, the
dispute stops and one solution is formalized there instead of argued in prose. An
uncontested proof is not formalized.

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
separate citation rules.

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
a finding that the two cards are the same statement. Do not wire it
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
CI runs it with `--with-queues`, which also writes the generated queues `just
unsolved` (`queues/C-unsolved-cards.md`) and `just prose-only`
(`queues/D-prose-only-solutions.md`) write standalone, and publishes all three
as the `corpus-reports` workflow artifact.

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
appearance. Existing `E-*` ids are not renamed to another prefix; the prefix does not
declare a card kind. One statement has one card and one id; a proven duplicate is merged
and its id deleted under `CARD-04` in [CONTRIBUTING.md](CONTRIBUTING.md). An authored `::: exercise` fence likewise records how the
source presented the item and parses as a problem section.

Good work on this corpus is reading mathematics, understanding what a statement
says, and making curation decisions: writing a title that names the problem,
classifying a card under the right topics, writing a solution, relating two
cards that depend on each other. A gap in a field is curation work, not a
tooling problem.

## The wiki is a textbook

Before you write, split, merge, move, or retitle a page under `wiki/`, read [docs/agents/wiki.md](docs/agents/wiki.md).

## Work one item at a time

Create and edit authored data one item at a time, not in batches. This rule applies especially to
problem cards. It also applies to titles, statements, classifications,
relations, solutions, hints, and remarks.

First, write a straightforward checklist that names each item. Then process the
checklist in order, one item at a time. Read the source mathematics and the
relevant existing cards before each change. Make an independent curation
decision for that item. Verify the completed item before starting the next one.

Do not use scripts, loops, templates, bulk edits, or generators to produce
authored data. Do not derive a title, create a card, fill a field, or change
mathematical content automatically. Each result must come from intelligent
reading and mathematical judgment.

Notation is the exception. Rewriting a raw LaTeX command to the vocabulary macro that
has exactly one meaning for it (`\mathbb{R}` to `\RR`) changes no mathematics, so it
is one codemod over the whole corpus plus a commit check that rejects the raw form,
never a card-by-card agent sweep. A letter with several meanings (`\mathbb{P}`:
projective space, a probability, the irrationals) gets one semantic macro per meaning
in the preamble; each occurrence is classified once by meaning, and the same codemod
applies the classification.

## Do not end a turn without the next source started

A turn that ends with the work banked and nothing in flight still stops this repository until
somebody notices and pushes it. On 2026-09-12 that happened nine times, costing between eleven
and fifty-five minutes each — more total time than every blocked commit, stale lock and failed
hook that day combined.

Ending a turn is a decision to stop, so make it deliberately. When a unit of work is committed,
take the next one in the same turn from the first open work unit of the
[issue tree](https://github.com/dzackgarza/new-qual-site/issues/83) (`itree next dzackgarza/new-qual-site`): open it,
read it, begin. If work genuinely must pause — a run you are waiting on, a decision you cannot
make — say what you are waiting for and what you will do when it returns, so the next turn begins
with an instruction rather than a question.

Selecting the next item is your work, not the steward's.

## Sources and gaps

Where something came from is not tracked. There are no ledgers, dispositions, migration or import
records, provenance blocks, audit or event logs, `variant-of` relations, or queues of sources to
process. To find what is missing, open the old source, compare it with the corpus, and add or
correct what the corpus lacks, in an ordinary commit of the cards themselves.

The same goes for duplicates: one notion has one card. Two cards that state the same mathematics
are folded into one, keeping every distinct hypothesis, example and review prompt on the survivor
and pointing every link at it. Two cards that look alike but state different mathematics are
both kept, with no relation asserting otherwise. A problem that several collections list is one
card listed by each of them, as described under
[Problems may appear in multiple collections](#problems-may-appear-in-multiple-collections).

## Review your own session for drift

Before starting a new source, look back at the one you just finished and ask what it produced:

- **Authored content, or paperwork and normalisations?** Cards, solutions, corrected
  statements and rewritten copy are the product. A session whose output is decisions about
  sources has left the corpus unchanged.
- **Did authored content change?** If commits landed but no card, statement, solution or page
  copy changed, the commits were not authoring.
- **Is something making every source cost more than it should?** An extraction step you redo by
  hand each time, a check that reformats files you did not touch, a count you have learned not
  to trust. That is an obstruction, and working around it silently is how it survives to cost
  the next worker the same.

Fix the obstruction where it lives, with its regression.

## Repair the tooling that wastes your turns

When the same friction appears twice, stop and fix it at its owner rather than working around
it. The formatter that reflowed seventy-six sibling cards on every pathspec commit was not a
quirk to route around — it made `git status` unreadable, which is the condition under which
authored work goes missing unnoticed, and this repository has already lost 962 authored lines
that way. It was a four-line defect in a shared formatter that had been costing every commit
for days.

The same applies to an OCR count that is routinely wrong, an extraction path that silently
truncates, a check that cannot distinguish a solved card from an unsolved one. Fix it where it
lives, and commit the fix with its regression. A workaround you carry in
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
algebra, differential geometry / manifolds, representation theory, combinatorics and graph theory (filed in
algebra), and number theory.

Do not add numerical analysis, statistics, or probability. Those are out of
scope for now. A department posting an exam in those subjects is not a reason
to create a collection card. Applied Algebra is not numerical analysis.

## Screenshots of notes

Before you store, match, or delete a screenshot of the author's typeset notes (the QualBot PNGs or a similar crop), read [Screenshots of notes](docs/agents/collection-provenance.md#screenshots-of-notes).

## Migration archives are history, not assets

Before you keep, add, or remove a migration snapshot or a file under `assets/` that a card points into, read [Migration archives are history, not assets](docs/agents/collection-provenance.md#migration-archives-are-history-not-assets).

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

Before you extract, re-extract, or transcribe a PDF or a retained raster source for intake, read [docs/agents/pdf-extraction.md](docs/agents/pdf-extraction.md).

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
for a human to read. Do not wire it to anything that acts on it.

The build reads authored content and renders it. It does not derive fields. A
build that derives titles, classifications, relations, or any other field is
fabricating content, not rendering it.

# Collection provenance

The corpus has two tiers: collections and problems. A collection is the only
card that carries `provenance:`. A problem carries no provenance; where a
problem comes from follows from backlinks — every collection whose
`source.problems` lists it. Collection cards live in `corpus/collections/`.

Before you edit a collection card, its `provenance:` list or `source.problems` list, a collection page, or the problem browser (`problems.html`), read [docs/agents/collection-provenance.md](docs/agents/collection-provenance.md).

## Problems may appear in multiple collections

It is common and expected for a problem to appear in multiple collections. An
exam may reuse a question from a textbook, the same problem may appear on
different exams, or a compilation may contain overlapping problem sets. Each
collection independently lists the problems it contains; the same problem card
may be referenced by many collections. One card listed in several collections
is correct, not redundancy; do not suppress an appearance. Two cards for one
statement are the opposite case: that is a duplicate, merged under `CARD-04`. What a rendered remark may say about a card's sources is `SEC-7`.

# Data issues

The order of work across copy, intake, mathematical repair, proof writing and
publication is the sibling order of the
[issue tree](https://github.com/dzackgarza/new-qual-site/issues/83): complete
source-faithful proofs come first, their certification second, and reader-facing
publication after both. A solution is not deferred to publication; it is the
content publication renders.

Within data issues, in order of urgency:
1. Incorrect data — problem statements, titles, or classifications that are
   simply wrong. This is the most urgent.
2. Problem cards not appearing in any collection (orphaned problems)
3. Collections containing no problems or an incomplete list of problems
4. Missing or invalid provenance that prevents auditing

Missing solutions, empty solution fields, and unsolved cards are authoring
concerns, not data integrity problems.

# Finding work

The [issue tree](https://github.com/dzackgarza/new-qual-site/issues/83) holds the open work units in execution order. Unsolved problems are the problem cards with no `solution`
section; `just unsolved` lists them. A solve that is prose is a solution by that list and
still not what issue #2 asks for, so a problem card whose solution holds no numbered step
is listed separately by `just prose-only`. Before taking a card, read it: a sibling may have solved it
since the list was produced. Never author the same card as a sibling.

# One checkout, one branch

Streams work directly on `main` in the single clone, without worktrees or
branches.

The project cc-safety-net rulebook `one-checkout` (`.cc-safety-net/rules/one-checkout/`) blocks `git worktree add`, `git checkout -b`/`-B`, and `git switch -c`/`-C`.

This repository is authored content. A stream writes solutions, hints and wiki prose
into card files it selected off a queue, and two streams never hold the same card —
so there is nothing for a branch to isolate and nothing for a merge to resolve. The
isolation apparatus was not protecting the work; it was protecting against a fear.

The fear is `git commit -a` sweeping in a sibling stream's concurrent edit. That is
not a conflict and not lost work: the other stream's change is already on disk and
already correct, and the only thing wrong is the message describing it. When your
commit swept in a sibling's card, fix the message:

```bash
git commit --amend
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

Before you remove a worktree that `git worktree list` reports beside the main checkout, read [docs/agents/retiring-worktrees.md](docs/agents/retiring-worktrees.md).

## Merge and reconciliation snapshots

A merge, reconciliation, or duplicate-adjudication snapshot is temporary working state,
not an archive. Delete the snapshot in the same turn that finishes its last use. If the
work that depends on it is still active, leave it in place and state the specific live
dependency; do not retain a completed snapshot merely as insurance.

# Running checks

The same changed-card validation obligation holds at each supported content route:

- **Ordinary commit with staged card edits.** Commit hooks validate the staged card blobs in Git's
  index and run the shared syntax checks. A valid working-tree edit must not conceal an invalid staged
  blob; what commits is what is staged.

- **`just commit-card` on one reviewed card.** This is the sanctioned card-authoring route. It first
  validates the selected card's YAML and schema from the working tree, then commits that single card
  with `git commit --only --no-verify`. Use it when you are committing exactly one card and want the
  card validated before the hook-free content commit.

- **Explicit `git commit --no-verify` for authored content.** This is the repository owner's sanctioned
  commit route for prose-only, documentation-only, and authored-content commits (copy, prose,
  mathematics, solutions, statement corrections, new cards): it is the documented workflow, not an
  evasion of any gate. Mathematical content is verified by reading the diff. Cards committed through
  this route are still validated by the push hook below, because that hook validates committed blobs,
  not how they were committed.

- **Push.** The push hook validates the committed card blobs in the outgoing range, including cards
  committed without hooks, and runs the shared syntax checks. Its `test-push` recipe runs `qualc.authoring check-changes --mode push` on
  the exact blob identities, so content commits made through the hook-free authoring route are still
  checked before upload. At the outgoing tip it also rejects any collection member, relation target,
  guide `ref`, or card-id link in a card or wiki page that names an id no card carries, so a
  `CARD-04` merge that deletes a card must repoint every reference in the same push.

- **Local diagnosis before a push.** `just test-push` is the explicit project diagnostic command: it
  runs the shared tier and then adds the extraction-residue check, the macro-mirror check, and the focused
  parser and Git-boundary tests. It is not how cards are normally committed; it is the command to run when
  you want the fast local checks plus their focused tests in one place.

Before you change a commit or push recipe, set `QUALC_PARALLEL_WORKERS`, or download CI reports or a built site, read [docs/agents/running-checks.md](docs/agents/running-checks.md).

Checks follow `QUAL-06` in [CONTRIBUTING.md](CONTRIBUTING.md#named-policies). Content work — copy,
prose, mathematics, solutions, statement corrections, and new cards or ingested collections — is
verified by reading its diff and reviewing the mathematics, and is committed as soon as the item is
done. Do not run or wait on builds, test suites, renders, screenshots, broad formatters, or queue
regeneration for content work. The cheap validation that guards outgoing content is the changed-card
YAML and schema check plus the shared syntax checks; it runs on staged or committed blobs, not on a
whole-corpus load, and it is independent of Pandoc, site emission, and broad audits.

Code, renderer, schema, executable configuration, and mixed code/content changes use the normal
commit and push gates. Use focused checks while investigating a specific defect; CI runs
the full acceptance checks.

## A red gate is the current task

When a gate you run — a code commit gate, or the push gate — goes red, stop and diagnose it:
root-cause and fix the gate, or report it as a blocker with a reproducer. Do not accumulate
unpushed work around a red gate. A gate that is red on two consecutive
attempts is a defect to diagnose, not an environment condition to wait out.

## Every run leaves a duration record

Before you read or change a run's duration record (stored in `$XDG_STATE_HOME/new-qual-site/run-records`, or `~/.local/state/new-qual-site/run-records` when that variable is unset), read [Every run leaves a duration record](docs/agents/running-checks.md#every-run-leaves-a-duration-record).

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

To write solutions, follow the per-card execution rule of [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2):
select one unsolved card, read the problem and its source, independently verify any source
solution, write a complete Lamport-style structured proof in a `solution` section on that problem
card in the layout `STYLE-08` fixes, and commit it before selecting the next card.
`just sample-unsolved COLLECTION [n] [section]` samples unsolved card IDs from one collection in
source order.

# Proof status: the three words a problem page states

Before you add a certificate row to `proofs/README.md`, change a card's `review:` field, or add or correct an `audit:` event or a dated `COMPLAINTS.md` record (`QUAL-11`), read [docs/agents/proof-status.md](docs/agents/proof-status.md).
