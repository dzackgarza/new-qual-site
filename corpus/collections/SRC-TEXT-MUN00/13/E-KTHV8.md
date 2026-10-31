---
schema: qual/card@1
id: E-KTHV8
kind: problem
title: Sets containing a neighborhood of each of their points are open
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
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

Let $X$ be a topological space; let $A$ be a subset of $X$.
Suppose that for each $x \in A$ there is an open set $U$ containing $x$ such that $U \subset A$.
Show that $A$ is open in $X$.
:::

::: {.solution}
Let $\mathcal U$ be the collection of all open subsets of $X$ contained in
$A$. The hypothesis says that every $x\in A$ lies in some member of
$\mathcal U$. Therefore
$$
A=\bigcup_{U\in\mathcal U}U.
$$
Since arbitrary unions of open sets are open, $A$ is open.
:::
