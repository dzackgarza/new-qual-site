# Contributing

Contributions can improve mathematical content, source records, study guides, or the website.

## Named policies

Use these stable identifiers in contributions and review. [AGENTS.md](AGENTS.md)
retains the detailed authoring rules; [REVIEW_POLICY.md](REVIEW_POLICY.md) retains
the existing named advisory defect patterns.

| ID | Name | Required action |
| --- | --- | --- |
| `QUAL-01` | Source-faithful mathematics | Read the complete card and relevant source before changing a statement, title, classification, relation, or proof. Preserve hypotheses and every requested part. |
| `QUAL-02` | Semantic authorship | Decide mathematical meaning by reading. Measurements and matching names identify candidates; they do not decide equivalence, correctness, or deletion. |
| `QUAL-03` | One card, one proof owner | Author and review one card at a time. Solutions and hints belong in their problem card; commit the reviewed card before continuing. |
| `QUAL-04` | Dependency-directed work | Use [the TODO DAG](TODO.md#execution-dag). Give each concrete task a stable ID, immediate prerequisites and an observable result. Preserve the scope of unfinished work and reject cycles or unresolved prerequisite IDs. |
| `QUAL-05` | Capture issues when encountered | Record mathematical errors, source ambiguities, and actual papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries. Supply evidence, affected card or owner, expected result, uncertainty, and a repair link. Extend an existing entry for the same issue. Logging is not repair. |
| `QUAL-06` | Match verification to the artifact | Read mathematical proofs for correctness; a parser cannot certify them. For renderer or styling changes, render and inspect the actual affected pages. Use existing just recipes and the prose-only commit exemption where applicable. |
| `QUAL-07` | Preserve concurrent authorship | Reread target files before editing, preserve others' changes and staged files, and commit only the intended paths. Keep complaint and TODO edits confined to the selected entry. |
| `QUAL-08` | Keep process off public cards | Store issue capture here and in COMPLAINTS/TODO, not in rendered remarks. Mathematical errata may explain a false statement and its corrected hypotheses on the card. |

## Requirements

- Python 3.14

- [uv](https://docs.astral.sh/uv/)

- [just](https://just.systems/)

- [Pandoc](https://pandoc.org/) with the `pandoc server` command

## Setup

```sh
git clone https://github.com/dzackgarza/new-qual-site.git
cd new-qual-site
uv sync --group dev
```

## Repository structure

- `corpus/` contains problems, sources, definitions, theorems, proofs, hints, and solutions.

- `publications/` orders cards into subject guides and reading paths.

- `vocabularies/` contains shared topics, institutions, textbooks, citations, and MathJax macros.

- `tools/qualc/` contains the corpus compiler and static-site generator.

- `site/` contains browser code and styles.

- `build/` contains generated files. Do not edit them.

## Mathematical content

Read the relevant cards before changing their titles, classifications, relations, or content.
Make semantic decisions from the mathematics, not from filenames or text similarity.
In card titles, use ordinary mathematical notation instead of spelling simple
formulas out in words (`$L^2$`, `$\ZZ^3/N$`, `$x^8-1$`, not “L2”, “Z cubed
mod N”, or “x to the eighth minus one”). Keep conceptual prose as prose.

A canonical problem states one mathematical problem.
An exam or textbook collection lists those problems in the order they appeared.
Appearances on a problem page are generated from that list.

Use an existing card of the same kind as the format example.
The compiler rejects unknown fields, unknown card kinds, invalid relations, and unregistered vocabulary.

## Build the site

Check the corpus:

```sh
just check
```

Build the catalog and website:

```sh
just build
```

Preview the website:

```sh
just preview
```

Open <http://localhost:8000> after the preview server starts.

Run `just --list` for the current development commands.
