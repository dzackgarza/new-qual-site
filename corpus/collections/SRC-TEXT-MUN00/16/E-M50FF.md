---
schema: qual/card@1
id: E-M50FF
kind: problem
title: Transitivity of the subspace topology
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
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

Show that if $Y$ is a subspace of $X$, and $A$ is a subset of $Y$, then the topology $A$ inherits as a subspace of $Y$ is the same as the topology it inherits as a subspace of $X$.
:::

::: {.solution}
Let $\mathcal T_X$ be the topology of $X$. The topology that $A$ inherits directly from $X$ is
\[
\{A\cap U:U\in\mathcal T_X\}.
\]
The topology that $Y$ inherits from $X$ is $\{Y\cap U:U\in\mathcal T_X\}$. Hence the topology that $A$ inherits from $Y$ consists of
\[
A\cap(Y\cap U)=(A\cap Y)\cap U=A\cap U
\]
with $U\in\mathcal T_X$, since $A\subseteq Y$. Thus the two subspace topologies coincide.
:::
