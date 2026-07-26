# Qual corpus

A compiler pipeline for qualifying-exam mathematics:

```text
corpus/*.md ──► qualc ──► build/catalog.sqlite
                    ├──► build/quarto/_site   (production HTML)
                    └──► build/quarto/*.qmd   (inspectable secondary projection)
```

Markdown cards in git are the authored source.
The SQLite catalog and both site projections are disposable build outputs.

`qualc` parses independent Markdown documents through one build-scoped Pandoc server in bounded batches.
The emitter projects production HTML directly from the resulting ASTs; it does not launch Pandoc or a site renderer once per card.

## Build and inspect

```sh
just check          # validate cards, relations, and registries
just build          # rebuild the catalog, QMD, and production HTML
just preview        # build and serve build/quarto/_site
just test           # prove the repository-owned invariants
just query 'select id, kind, title from cards limit 5'
```

Commit, push, and CI gates are available as `just test-commit`, `just test-push`, and `just test-ci`.

## Three independent structures

| Structure | Authoritative source | Changing it affects |
| --- | --- | --- |
| Source layout | `corpus/` paths | edit location only |
| Semantic graph | card front matter, body, and relations | catalog content and projections |
| Publication hierarchy | `publications/*.yaml` | reading paths and card appearances |

Directory names and filenames assign no semantic identity.
Moving every card to a flat directory leaves the catalog byte-identical.
Moving a card appearance between publication pages leaves its `tag/<ID>.html` route unchanged.

## Cards

Every card has one required envelope.
Its `kind` selects a closed Pydantic variant; unknown fields and kinds fail the build.

```yaml
---
schema: qual/card@1
id: S-4WQ1R
kind: solution
title: Normal p-subgroups lie in every Sylow — part (a)
classification:
  areas:
  - algebra
  topics:
  - groups
relations:
- kind: solves
  target: P-P2UAH
- kind: uses
  target: D-7TQ2M
review: draft
---
```

Kinds include problems, occurrences, sources, hints, solutions, definitions, theorems, proofs, examples, exercises, and other measured prose environments.
Relation kinds include `instance-of`, `solves`, `hints-at`, `uses`, `related-to`, `cites`, `variant-of`, and `extracted-from`.

Closed concepts live in the schema.
Open sets—areas, topics, institutions, textbooks, and MathJax macros—live in `vocabularies/`.

### Canonical problems and occurrences

A `problem` owns the canonical statement.
An `occurrence` preserves one historical wording, source, and locator and points to the canonical problem.
Queries by institution or year join through occurrences.
Deduplication repoints occurrences; it does not delete history.

### Semantic prose

Front matter carries identity and queryable facts.
Mathematical prose remains Pandoc Markdown with semantic fenced divs such as `::: theorem`, `::: problem`, `::: hint`, and `::: solution`, nested to any depth.

Pandoc owns every Markdown read and write.
The emitter composes AST blocks, not Markdown strings.
YAML front matter is the deliberate exception because it is machine configuration, not prose.

## Publication manifests

`qual/publication@2` manifests own:

- the subject hierarchy and dependency order;

- connective prose between cards;

- explicit stable-card appearances;

- bounded catalog-query panels.

They do not own card content or routes.
The compiler validates parent order, references, query review scope, and nonempty query results.

Publication pages render:

- a subject sidebar, breadcrumbs, and previous/next reading order;

- independently addressable card appearances;

- authored dependencies, derived appearances, and backlinks as separate groups;

- problem statements before collapsed hints and solutions.

Search emits three reader-facing result types: `Page`, `Card`, and `Problem`. The problem browser, publication query panels, and exam generator read the same SQLite card catalog.

## Finite-groups vertical slice

The first complete subject path is:

```text
Algebra
└── Finite Groups
    └── Actions and Counting
        └── Sylow Theory
            └── Applications and Problems
```

It composes Lagrange and Cauchy, actions, orbit-stabilizer, fixed-point counting, the class equation, finite p-groups, Sylow I/II/III, the six algebra workshop problems, linked UGA questions, and the `P-P2UAH` / `D-7TQ2M` / `H-2JK8Q` / `S-4WQ1R` chain.

This slice does not claim a publication hierarchy for every subject or redesign the existing exam generator.
