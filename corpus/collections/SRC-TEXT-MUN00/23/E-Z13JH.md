---
schema: qual/card@1
id: E-Z13JH
kind: problem
title: Infinite sets are connected in the finite complement topology
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that if $X$ is an infinite set, it is connected in the finite complement topology.
:::

::: {.solution}
In the finite-complement topology on an infinite set $X$, every nonempty open set has finite complement.

Suppose $U,V$ were disjoint nonempty open sets. Then
\[
U\subseteq X-V,
\]
so $U$ is finite because $X-V$ is finite. But $U$ is nonempty open, so $X-U$ is also finite. Therefore
\[
X=U\cup(X-U)
\]
would be finite, a contradiction. Thus no separation exists, and $X$ is connected.
:::
