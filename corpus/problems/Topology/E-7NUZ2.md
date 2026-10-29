---
schema: qual/card@1
id: E-7NUZ2
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude-opus-5-5
  date: 2026-10-29
  note: The previous solution proved that a compact subset of a Hausdorff space is closed, the converse direction, with two figures for that argument; it was replaced by a proof of the stated result.
---

::: {.problem}
Let $A\subset X$ with $A$ closed and $X$ compact, and show that $A$ is compact.
:::

::: {.solution}
Let $\mathcal{U}$ be a cover of $A$ by open subsets of $X$.

::: pf

::: {.pf-step #cover}

$\mathcal{U}\cup\{X\setminus A\}$ is an open cover of $X$.

::: pf-proof

$X\setminus A$ is open because $A$ is closed, and every point of $X$ lies either in $A$, hence in a member of $\mathcal{U}$, or in $X\setminus A$.

:::

:::

::: pf-qed

By compactness of $X$, finitely many members $U_1,\ldots,U_n\in\mathcal{U}$, together possibly with $X\setminus A$, cover $X$ by step [](#cover){.pf-ref}. Since $X\setminus A$ contains no point of $A$, the sets $U_1,\ldots,U_n$ cover $A$. So $A$ is compact.

:::

:::

:::
