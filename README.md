# Qual Corpus

Qual Corpus collects qualifying-exam problems and study material for graduate mathematics.
It covers prelims, algebra, applied algebra, algebraic geometry, real analysis, complex analysis, topology, and workshop problems.

**[Open Qual Corpus](https://dzackgarza.github.io/new-qual-site/)**

No installation is required.

## Study

- [Browse, filter, sample, and print problems](https://dzackgarza.github.io/new-qual-site/problems.html).

- [Browse sources](https://dzackgarza.github.io/new-qual-site/exams.html): past exams, textbooks, homework sets, and compilations.

- Press `/` on any page to search titles, statements, proofs, and topics.

Problem pages show where and when each problem appeared, when that information is known.
They also show available definitions, theorems, hints, solutions, and related problems.

## Subject guides

- [Prelim](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-PRELIM.html)

- [Algebra](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-ALGEBRA.html)

- [Applied Algebra](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-APPLIED-ALGEBRA.html)

- [Real Analysis](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-REAL-ANALYSIS.html)

- [Complex Analysis](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-COMPLEX-ANALYSIS.html)

- [Topology](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-TOPOLOGY.html)

- [Workshops](https://dzackgarza.github.io/new-qual-site/guide/GUIDE-WORKSHOPS.html)

Each guide orders one subject's definitions, theorems, and exam problems.

## Local preview

Run `just preview` from the repository root, then open <http://new-qual-site-preview.localhost/>. This is the single canonical local preview URL. The recipe rebuilds and republishes the current working tree, including uncommitted edits; do not use a separate `localhost:PORT` preview.

## Author

Cards in a collection are read, written, reviewed, and committed one at a time.
The recipes below run from the repository root:

| Command | Use |
| --- | --- |
| `just list-cards SRC-UCSD-ALG-SPRING-2015` | List all authored problem appearances in source order, including cards stored elsewhere and nested collections. |
| `just unsolved-in SRC-UCSD-ALG-SPRING-2015` | List the appearances whose cards currently have no solution section. |
| `just read-card P-ALGS15F` | Read the complete card with its collection appearances, section/page locators, source links, and existing Markdown extraction links. |
| `just path-card P-ALGS15F` | Print the current file path. |
| `just diff-card P-ALGS15F` | Review the card's changes against HEAD, including staged changes. |
| `just check-card P-ALGS15F` | Check that one card's schema and Markdown parse. |
| `just commit-card P-ALGS15F "sol(algebra): explain the result and proof"` | Commit exactly that reviewed, tracked card through the content commit route (`QUAL-06`), leaving unrelated staged work intact. |

Card recipes accept an ID or a corpus Markdown path.
Collection recipes accept a collection ID, its index path, or its directory containing `index.md`. To work on one exam inside a packet, append its exact authored section name:

```sh
just list-cards SRC-JHU-ANALYSIS-EXAMS 'ANALYSIS QUALIFYING EXAM, SEPTEMBER 2005 (pp. 42–43)'
```

Listings retain each authored appearance, its section, list position, and comment; the position is not an inferred exam problem number.
Nested entries retain their containing section and the referenced collection's own source identity.
`just sample-unsolved COLLECTION 5` samples up to five distinct unsolved IDs and lists their appearances in source order; an exact section name may follow the count.
All listings read current authored files without building a catalog or refreshing a queue.

`read-card` locates the recorded source material for a card through its source and extraction links.
Its context block is terminal output; the authored card follows unchanged.
Extraction links use the site's existing PDF-to-Markdown resource mapping; no extraction or source attribution is generated.
Discovery is repeated when fresh candidates are needed, not after every card.

The authoring recipes do not rebuild the site or refresh global queues.
Keep code and renderer changes on the normal verification path.
Mathematical review remains the author's responsibility, including when the single-card check passes.
