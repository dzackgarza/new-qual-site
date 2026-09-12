---
schema: qual/card@1
id: E-JZMX6
kind: problem
title: Restrictions of open maps to open subspaces are open
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
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

Let $p: X \to Y$ be an open map.
Show that if $A$ is open in $X$, then the map $q: A \to p(A)$ obtained by restricting $p$ is an open map.
:::

::: {.solution}
Let $U\subseteq A$ be open in the subspace $A$. Since $A$ itself is open in $X$, every subspace-open set $U$ is actually open in $X$. Because $p$ is an open map, $p(U)$ is open in $Y$. Therefore
\[
p(U)\cap p(A)=p(U)
\]
is open in the subspace $p(A)$. Hence the restriction
\[
q=p|_A:A\to p(A)
\]
is open.
:::
