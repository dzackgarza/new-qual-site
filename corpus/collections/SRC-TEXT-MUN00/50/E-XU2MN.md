---
schema: qual/card@1
id: E-XU2MN
kind: problem
title: Hausdorff equals completely regular for locally euclidean spaces
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Separation Axioms
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
    Checked against Munkres, Topology (2000), supplementary Exercise 7 of §50, printed p. 318, with the definition
    of complete regularity in §33 and Theorem 29.1 for the one-point compactification. A completely regular space
    is T1 and separates points from closed sets, hence Hausdorff. Conversely a Hausdorff locally euclidean space
    is locally compact, being covered by the interiors of compact coordinate balls, so it imbeds in its
    compact Hausdorff one-point compactification, which is normal and hence completely regular by Theorem 33.1,
    and complete regularity passes to subspaces. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves supplementary Exercise 7 of §50 (printed
    p. 318). Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of
    Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8
    | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost.
    The Stack Exchange queries of this pass, listed in the COMPLAINTS.md entry for §43--§50, returned no
    question on the equivalence. The card's two steps are its own: complete regularity gives Hausdorff because
    it includes $T_1$ and separates a point from a singleton, and conversely a locally $m$-euclidean Hausdorff
    space is locally compact by a closed ball inside a chart, hence completely regular through its one-point
    compactification. Nothing needed correction.
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that $X$ is Hausdorff if and only if $X$ is completely regular.
:::

::: {.solution}
If $X$ is completely regular, then by definition it is $T_1$, and complete regularity separates points from closed sets; in particular distinct points have disjoint neighborhoods. Thus $X$ is Hausdorff.

Conversely, suppose $X$ is Hausdorff and locally $m$-euclidean. Every point has a neighborhood homeomorphic to an open subset of $\RR^m$; shrinking inside such a chart gives a neighborhood whose closure in the chart is compact. Hence $X$ is locally compact. Every locally compact Hausdorff space is completely regular, being a subspace of its compact Hausdorff one-point compactification. Therefore
$$
X\text{ is Hausdorff}\quad\Longleftrightarrow\quad X\text{ is completely regular}.
$$
:::
