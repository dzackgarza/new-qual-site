---
schema: qual/card@1
id: E-DUQHF
kind: problem
title: Closed subspaces of normal spaces are normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that a closed subspace of a normal space is normal.
:::

::: {.solution}
Let $X$ be normal and let $Y \subseteq X$ be closed.

::: pf

::: pf-step
$Y$ is $T_1$.

::: pf-proof
Each singleton is closed in $X$, so its intersection with $Y$ is closed in $Y$.
:::

:::

::: pf-step
Any two disjoint closed subsets $A, B$ of $Y$ have disjoint open neighborhoods in $Y$, so $Y$ is normal.

::: pf-proof

::: pf-step
$A$ and $B$ are closed in $X$.

::: pf-proof
$A$ is closed in $Y$ and $Y$ is closed in $X$, so $A$ is closed in $X$; the same holds for $B$.
:::

:::

::: pf-step
There are disjoint open sets $U, V \subseteq X$ with $A \subseteq U$ and $B \subseteq V$.

::: pf-proof
$A$ and $B$ are disjoint closed sets in the normal space $X$.
:::

:::

::: pf-step
$U \cap Y$ and $V \cap Y$ are disjoint open sets in $Y$ that contain $A$ and $B$.

::: pf-proof
They are open in the subspace topology, disjoint because $U \cap V = \varnothing$, and contain $A$ and $B$ because $A, B \subseteq Y$.
:::

:::

:::

:::

:::

:::
