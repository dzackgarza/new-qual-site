# The wiki is a textbook

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
external oracle is `SOURCE-02` in [CONTRIBUTING.md](../../CONTRIBUTING.md); how localization
prerequisites are phrased is `DEF-35`.

## Where agents get this wrong

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

## What good work looks like

Read the mathematics. Decide what a student needs. Write the page. Group,
split, collect, and drill down as the exposition requires, and justify each
move by what it does for a reader.

## Two concerns, and the test that separates them

The wiki has an engineering side and an authoring side. Both are real work and
neither substitutes for the other.

The engineering side measures the file. Does the page parse; does its
mathematics typeset; do its links resolve; does it carry a title and an integer
`order`; does its directory carry an `index.md`; is Obsidian syntax reaching
the reader as literal text; do two pages in one folder render the same text
twice in the sidebar. These are mechanical, they have exact answers, and a
checker should be strict about them. `just doctor` is that checker and it earns
its place. The rules in "[What a tool may do](../../AGENTS.md#what-a-tool-may-do)" apply to it unchanged: it reports
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
