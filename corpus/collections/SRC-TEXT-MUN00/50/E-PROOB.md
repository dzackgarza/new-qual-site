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
