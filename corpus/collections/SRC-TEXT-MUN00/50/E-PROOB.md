---
schema: qual/card@1
id: E-PROOB
kind: problem
title: Manifolds have dimension at most m
classification:
  areas:
  - topology
  topics:
  - Dimension
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
    Checked against Munkres, Topology (2000), §50 Exercise 9, printed p. 317, with Theorem 50.6 (compact
    subspaces of R^N have dimension at most N), Theorem 50.1 and Corollary 50.3 for the finite union of the
    pieces of a compact set, and the preceding exercise (the card of Exercise 50.8) for the passage from the
    compact subspaces to the manifold, which is sigma-compact because it is locally compact and second
    countable. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 9 (printed p. 318).
    Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of Munkres
    solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day
    18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The
    card reduces the manifold to the sigma-compact theorem [[E-MVB8P]] through the dimension bound on its
    compact subspaces, and that bound is the step the exercise is for: a compact set is covered by finitely
    many coordinate patches, each piece is a closed subspace of $\RR^m$ under its chart, and the finite union
    of closed pieces keeps the dimension. Nothing needed correction.
---

::: {.exercise}

Corollary.
Every $m$-manifold has topological dimension at most $m$.
:::

::: {.solution}
Let $M$ be an $m$-manifold. Its local Euclidean charts make it locally compact. Since it is also Hausdorff and second-countable, it is $\sigma$-compact.

Let $K\subset M$ be compact. Cover $K$ by finitely many coordinate neighborhoods and shrink them so that there are compact sets
$$
K=K_1\cup\cdots\cup K_r
$$
with each $K_i$ contained in one coordinate chart. Under that chart, $K_i$ is homeomorphic to a compact, hence closed, subspace of $\RR^m$. Since $\dim\RR^m\le m$ and dimension does not increase on closed subspaces,
$$
\dim K_i\le m.
$$
The finite closed-union theorem for dimension then gives $\dim K\le m$.

Thus every compact subspace of $M$ has dimension at most $m$. Applying the $\sigma$-compact theorem [[E-MVB8P]] yields
$$
\boxed{\dim M\le m}.
$$
:::
