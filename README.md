# Qual corpus — proof of concept

A compiler pipeline, not a website with a database bolted on:

```
corpus/*.md  ──►  qualc  ──►  build/catalog.sqlite  ──►  build/quarto  ──►  _site
 (authored)      (compile)      (derived index)         (renderer input)
```

Markdown cards in git are the only authored source.
The SQLite catalog is a disposable projection, rebuilt from scratch on every build.
Quarto is a last-mile renderer that never sees the corpus.

## Try it

```
just check     # validate every card against the schema and the registries
just build     # catalog.sqlite + generated Quarto project
just site      # render to build/quarto/_site
just preview   # live-reload server
just test      # prove the invariants below still hold
```

Quarto runs through `uvx --from quarto-cli quarto`; nothing is installed system-wide.

## The three structures, kept apart

| Structure | Lives in | Changing it affects |
| --- | --- | --- |
| Source layout | `corpus/` | source paths and edit links, nothing else |
| Semantic graph | card front matter + relations | the catalog and every view |
| Publication structure | `publications/*.yaml` | one guide page |

`corpus/` is semantically inert.
Directory names assign nothing; filenames determine nothing; moving a card between contributor subtrees changes no identity, no URL, and no catalog row.
`tests/test_invariants.py` flattens the whole corpus into one directory of numbered files and asserts the catalog comes out byte-identical.

## Cards

One required envelope, `kind` selecting an exact payload — a closed discriminated union, not one record with forty optional fields.
Unknown fields are rejected, so a typo fails the build rather than being silently ignored.

```yaml
---
schema: qual/card@1
id: P-P2UAH
kind: problem
title: Let $G$ be a finite group whose order is divisible by a prime number...
classification:
  areas: [algebra]
  topics: [groups]
relations:
- kind: uses
  target: D-7TQ2M
review: draft
---

::: problem
Let $G$ be a finite group ...
:::
```

Kinds: `problem`, `occurrence`, `source`, `solution`, `hint`, `definition`. Relation kinds: `instance-of`, `solves`, `hints-at`, `uses`, `related-to`. Review states: `draft`, `reviewed`, `verified`.

Closed enums are for genuinely closed concepts (card kind, relation kind, review state, date kind).
Open-ended sets are registries in `vocabularies/`: adding a university or a topic is a data change, never a schema change.

Unknown information is a case, not a sentinel:

```yaml
date: {kind: academic-term, year: 2018, term: fall}
date: {kind: year, year: 2018}
date: {kind: unknown}
```

### Problem ≠ occurrence

A canonical problem is not "from UGA". It may have appeared at several institutions in several wordings.
`problem` holds the normalized statement; `occurrence` holds the verbatim wording as it appeared, and points at a `source` and a locator.
Queries by university or year join through occurrences.
Deduplicating means repointing occurrences; nothing historical is deleted.

### Prose stays in markdown

Front matter carries only what must be queried, validated, or used for identity.
Statements, hints, and solutions are markdown with the fenced-div schema already used in `qual-wiki` (`::: problem`, `::: solution`, `::: hint`, `::: definition`, `::: remark`).

## No markdown by hand, anywhere

Every stage that reads or writes markdown goes through the pandoc AST via panflute — sections are found as `Div` nodes, pages are composed as block trees, and pandoc's own writer emits them.
Nothing string-concatenates markdown or regexes LaTeX.

The one deliberate exception is front matter, which is written as YAML directly.
Routing it through the markdown writer escapes it as if it were prose: `contents: tag/P-*.qmd` comes back as `tag/P-\*.qmd`, and the listing silently matches nothing.
Machine config is not prose.

## Semantics in the corpus, presentation in the renderer

Cards say what a block *is*. `site/filters/reveal.lua` decides what that means on screen — hints, solutions, and verbatim occurrences collapse behind a summary so the page does not spoil the problem.
A print or exam target would make a different choice with no card changing.

The emitter renames the classes it renders itself to `qual-*`, because Quarto claims `.solution`, `.remark`, and the theorem environments for its own processing before user filters run.

## Publication manifests

A guide is not a directory.
It is an ordered composition of stable IDs and queries (`publications/algebra-guide.yaml`): explicit `ref:` entries for exposition, `query:` panels for problems.
The problem browser never consults it, so reorganizing a guide cannot affect the catalog.

## What this slice contains

39 records from `make-me-a-qual`, imported by `tools/import_mmaq.py`: UGA Algebra 2018, UGA Real Analysis 2018, UW Algebra 2018, and the duplicate groups from the undated UGA Complex Analysis pile.
They compile to 34 canonical problems, 34 occurrences, and 9 sources, plus one hand-authored definition, hint, and solution.

Two inferences the importer makes, because the source data cannot support them directly:

* The source has no `season` field.
  Where a year's numbering restarts, the records are treated as separate sittings, since a locator reset means a new exam document.
  Terms stay unknown.

* `year: 0` and `year: Extra` become `date: {kind: unknown}`.

Problem titles are generated from the first prose in each statement, with math preserved.
They are placeholders; editorial titles are a curation task.

## Deliberately not built

* **`/curate`.** Duplicate detection ran once during import (exact normalized statements).
  Scanning the full 508 records for cross-institution recurrences at a 0.6 Jaccard threshold surfaced four candidates, all false positives on short statements — this slice contains no genuine cross-sitting recurrence, so no problem here has more than one occurrence.
  The structure supports it; the data does not yet exhibit it.

* **Alias/merge records.** No merge of pre-existing IDs has happened yet, so there is nothing for an alias table to hold.

* **MakeMeAQual export.** The catalog is the query surface it would need; the export target is not written.

* **Crossref numbering** for definitions and theorems.
  Quarto can do it, but it needs `#def-…` ids derived from card ids.

* **Full-text search UI.** The `search` FTS5 table is populated and Quarto's own site search is on; they are not yet connected.
