# Qual Corpus

Qual Corpus collects qualifying-exam problems and study material for graduate mathematics.
It covers prelims, algebra, real analysis, complex analysis, topology, and workshop problems.

**[Open Qual Corpus](https://dzackgarza.github.io/new-qual-site/)**

No installation is required.

## Study

- [Browse problems](https://dzackgarza.github.io/new-qual-site/problems.html).

- [Browse past exams](https://dzackgarza.github.io/new-qual-site/exams.html).

- [Browse, filter, sample, and print problems](https://dzackgarza.github.io/new-qual-site/problems.html).

- Press `/` on any page to search titles, statements, proofs, and topics.

Problem pages show where and when each problem appeared, when that information is known.
They also show available definitions, theorems, hints, solutions, and related problems.

## Subject guides

- [Prelim](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-PRELIM.html)

- [Algebra](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-ALGEBRA.html)

- [Real Analysis](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-REAL-ANALYSIS.html)

- [Complex Analysis](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-COMPLEX-ANALYSIS.html)

- [Topology](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-TOPOLOGY.html)

- [Workshops](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-WORKSHOPS.html)

Each guide follows a subject path from core definitions and theorems to exam problems.

## Author

Work through a collection in one session, reading, writing, reviewing, and committing each card separately.
Run these recipes from the repository root:

| Command | Use |
| --- | --- |
| `just list-cards SRC-UCSD-ALG-SPRING-2015` | List all authored problem appearances in source order, including cards stored elsewhere and nested collections. |
| `just unsolved-in SRC-UCSD-ALG-SPRING-2015` | List the appearances whose cards currently have no solution section. |
| `just read-card P-ALGS15F` | Read the complete card with its collection appearances, section/page locators, source links, and existing Markdown extraction links. |
| `just path-card P-ALGS15F` | Obtain the current file path for editing. |
| `just diff-card P-ALGS15F` | Review the card's changes against HEAD, including staged changes. |
| `just check-card P-ALGS15F` | Optionally check that one card's schema and Markdown parse. |
| `just commit-card P-ALGS15F "sol(algebra): explain the result and proof"` | Commit exactly that reviewed, tracked card using the prose-only exemption; leave unrelated staged work intact. |

Card recipes accept an ID or a corpus Markdown path.
Collection recipes accept a collection ID, its index path, or its directory containing `index.md`. To work on one exam inside a packet, append its exact authored section name:

```sh
just list-cards SRC-JHU-ANALYSIS-EXAMS 'ANALYSIS QUALIFYING EXAM, SEPTEMBER 2005 (pp. 42–43)'
```

Listings retain each authored appearance, its section, list position, and comment; the position is not an inferred exam problem number.
Nested entries retain their containing section and the referenced collection's own source identity.
`just sample-unsolved COLLECTION 5` samples up to five distinct unsolved IDs and lists their appearances in source order; an exact section name may follow the count.
All listings read current authored files without building a catalog or refreshing a queue.

Use `read-card` to locate and read the recorded source material, then retain that context across the collection.
Its context block is terminal output; the authored card follows unchanged.
Extraction links use the site's existing PDF-to-Markdown resource mapping; no extraction or source attribution is generated.
Repeat discovery when you need fresh candidates, not after every card.

The authoring recipes do not rebuild the site or refresh global queues.
Keep code and renderer changes on the normal verification path.
Mathematical review remains the author's responsibility, including when the single-card check passes.
