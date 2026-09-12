---
schema: qual/card@1
id: E-G74LH
kind: problem
title: Connected open sets in locally path connected spaces
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

Let $X$ be locally path connected.
Show that every connected open set in $X$ is path connected.
:::

::: {.solution}
Let $U\subseteq X$ be open and connected. Since $X$ is locally path connected, the subspace $U$ is locally path connected: if $x\in U$, choose a path-connected open neighborhood $V$ of $x$ contained in $U$.

In a locally path-connected space, path components are open. Indeed, if $P$ is a path component and $x\in P$, choose a path-connected open neighborhood $V$ of $x$; then every point of $V$ is path connected to $x$, so $V\subseteq P$. Thus each path component of $U$ is open in $U$.

Distinct path components are disjoint, and their union is $U$. If there were more than one, one path component and the union of all the others would give a separation of connected $U$. Hence $U$ has only one path component and is path connected.
:::
