---
schema: qual/card@1
id: E-D1NXY
kind: problem
title: The line is a manifold that is not compact
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 3 of §50, printed p. 317, together with the
    card of supplementary Exercise 2 for the labels of the conditions: R is locally 1-euclidean, Hausdorff and
    second countable (the intervals with rational endpoints), so it satisfies (ii); the cover by the intervals
    (-n,n) has no finite subcover, so it fails (i). Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located treats supplementary Exercise 3 of §50 (printed
    p. 316); the example is a two-line matter of the countable basis of intervals with rational endpoints and
    the cover by $(-n,n)$, and the card gives it. Murayama's selection has no Chapter 8, dbFin has no
    chapter-8 page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop before §36,
    and the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The Stack
    Exchange queries of this pass are listed in the COMPLAINTS.md entry for §43--§50. Nothing needed
    correction.
---

::: {.exercise}

Show that $\RR$ is locally 1-euclidean and satisfies (ii) but not (i) of Exercise 2.
:::

::: {.solution}
The usual line $\RR$ is locally $1$-euclidean since every point has an open interval neighborhood homeomorphic to an open interval of $\RR$. It is Hausdorff and has the countable basis of intervals with rational endpoints, so it is a $1$-manifold; thus it satisfies condition (ii) of [[E-OYPV7]].

It is not compact: the open cover
$$
\{(-n,n):n\in\ZZ_+\}
$$
has no finite subcover. Hence condition (i) fails. Therefore $\RR$ is locally $1$-euclidean and satisfies (ii) but not (i).
:::
