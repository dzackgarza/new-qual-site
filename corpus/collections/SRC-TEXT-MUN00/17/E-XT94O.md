---
schema: qual/card@1
id: E-XT94O
kind: problem
title: Equivalents of the T1 axiom
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
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

Show that the $T_1$ axiom is equivalent to the condition that for each pair of points of $X$, each has a neighborhood not containing the other.
:::

::: {.solution}
Assume first that $X$ is $T_1$, so each singleton is closed. Given distinct $x,y\in X$, the set
\[
X-\{y\}
\]
is an open neighborhood of $x$ not containing $y$, and $X-\{x\}$ is an open neighborhood of $y$ not containing $x$.

Conversely, suppose that for every pair $x\ne y$, each has a neighborhood omitting the other. Fix $x\in X$. For every $y\ne x$, choose an open neighborhood $U_y$ of $y$ with $x\notin U_y$. Then
\[
X-\{x\}=\bigcup_{y\ne x}U_y
\]
is open. Thus $\{x\}$ is closed for every $x$, so $X$ is $T_1$.
:::
