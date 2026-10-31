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
