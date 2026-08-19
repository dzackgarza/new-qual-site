# Contributing

Contributions can improve mathematical content, source records, study guides, or the website.

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
