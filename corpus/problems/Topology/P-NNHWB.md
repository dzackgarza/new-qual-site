---
schema: qual/card@1
id: P-NNHWB
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.problem}
Show that a closed subset $A$ of a compact space $X$ is compact.
:::

::: {.solution}

Let $\mathcal U$ be a cover of $A$ by open subsets of $X$.

::: pf

::: pf-step

Since $A$ is closed, $X\setminus A$ is open, and
$$\mathcal U\cup\{X\setminus A\}$$
is an open cover of $X$.

::: pf-proof

The members of $\mathcal U$ cover $A$, while $X\setminus A$ covers every point outside $A$.

:::

:::

::: pf-step

Compactness of $X$ gives a finite subcover of this enlarged cover.

::: pf-proof

This is the definition of compactness.

:::

:::

::: pf-step

Removing $X\setminus A$ if it occurs leaves finitely many members of $\mathcal U$ that cover $A$. Hence $A$ is compact.

::: pf-proof

The removed set contains no point of $A$.

:::

:::

:::

:::
