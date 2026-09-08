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

Work through a collection in one session, reading, writing, reviewing, and
committing each card separately. Run these recipes from the repository root:

| Command | Use |
| --- | --- |
| `just unsolved-in corpus/collections/SRC-UCSD-ALG-SPRING-2015` | List current cards without solution sections in that directory, with IDs, paths, and titles. |
| `just read-card PATH` | Read a complete card or collection index, including source links and authored problem order. |
| `just diff-card PATH` | Review the card's changes against HEAD, including staged changes. |
| `just check-card PATH` | Optionally check that one card's schema and Markdown parse. |
| `just commit-card PATH "sol(algebra): explain the result and proof"` | Commit exactly that reviewed, tracked card using the prose-only exemption; leave unrelated staged work intact. |

Read the collection index and relevant source material, retain that context, and
proceed through its authored problem order. The live directory scan reports a measurement;
it does not decide whether a solution is correct, whether a review is complete,
or which problem to work on. Repeat it when you need fresh candidates, not after
every card.

`just sample-unsolved DIRECTORY 5` samples up to five current candidates from
that corpus directory. Both selection recipes read authored files directly;
they need no compiled catalog or generated queue. A directory scan is not a
collection-membership audit: the collection index owns its source order and
may also reference cards stored elsewhere.

The authoring recipes do not rebuild the site or refresh global queues. Keep
code and renderer changes on the normal verification path. Mathematical review
remains the author's responsibility, including when the single-card check passes.
