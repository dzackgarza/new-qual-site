---
schema: qual/card@1
id: E-PBT3I
kind: problem
title: Products of closed sets are closed
classification:
  areas:
  - topology
  topics:
  - Closed Sets
  - Product Topology
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

Show that if $A$ is closed in $X$ and $B$ is closed in $Y$, then $A \times B$ is closed in $X \times Y$.
:::

::: {.solution}
Since $A$ and $B$ are closed, $X-A$ and $Y-B$ are open. The complement of $A\times B$ is
\[
(X\times Y)-(A\times B)
=((X-A)\times Y)\cup(X\times(Y-B)),
\]
a union of product-open sets. Therefore $A\times B$ is closed in $X\times Y$.
:::
