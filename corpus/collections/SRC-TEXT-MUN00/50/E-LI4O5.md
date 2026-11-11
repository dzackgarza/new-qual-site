---
schema: qual/card@1
id: E-LI4O5
kind: problem
title: Components of metrizable locally euclidean spaces are manifolds
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
    Checked against Munkres, Topology (2000), supplementary Exercise 9 of §50, printed p. 318, with Theorem 25.4
    (the components of a locally path connected space are open), Theorem 30.2, Theorem 42.1 and the card of §41
    Exercise 10, which shows that a connected, locally compact, paracompact space is a countable union of compact
    subspaces. Points checked: a locally euclidean space is locally path connected, so components are open; the
    component is then locally m-euclidean and metrizable, hence Hausdorff, locally compact and paracompact; the
    countable cover by compact pieces yields a countable cover by second countable coordinate neighbourhoods,
    whose union of countable bases is a countable basis. Nothing needed correction.
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that if $X$ is metrizable, then each component of $X$ is an $m$-manifold.
:::

::: {.solution}
Let $C$ be a component of the metrizable locally $m$-euclidean space $X$.

A locally euclidean space is locally path connected, so its components are open. Hence $C$ is itself locally $m$-euclidean and metrizable (therefore Hausdorff).

It remains to prove that $C$ has a countable basis. The space $C$ is locally compact, since every point has a Euclidean coordinate neighborhood, and it is Hausdorff. It is metrizable, hence paracompact by Stone's theorem. By [[E-GZX7B]], the connected space $C$ is a countable union of compact subsets $K_n$. Cover each $K_n$ by finitely many open coordinate neighborhoods. These neighborhoods are second-countable, and together they form a countable open cover of $C$. The union of their countable bases is a countable basis for $C$. Hence $C$ is Hausdorff, second-countable, and locally $m$-euclidean: it is an $m$-manifold.
:::
