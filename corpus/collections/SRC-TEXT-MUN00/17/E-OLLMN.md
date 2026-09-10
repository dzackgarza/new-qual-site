---
schema: qual/card@1
id: E-OLLMN
kind: problem
title: Closed subsets of closed subspaces are closed
classification:
  areas:
  - topology
  topics:
  - Closed Sets
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

Show that if $A$ is closed in $Y$ and $Y$ is closed in $X$, then $A$ is closed in $X$.
:::

::: {.solution}
Since $A$ is closed in the subspace $Y$, there is a closed set $C$ of $X$ with
\[
A=Y\cap C.
\]
Because $Y$ is closed in $X$, both $Y$ and $C$ are closed in $X$, hence so is their intersection $A$.
:::
