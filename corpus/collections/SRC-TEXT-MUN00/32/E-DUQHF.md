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
**Goal.** Show a closed subspace of a normal space is normal.

::: pf

::: pf-step
Let $X$ be normal and $Y \subseteq X$ closed.

::: pf-proof
setup.
:::

:::

::: pf-step
$Y$ is $T_1$.

::: pf-proof
a subspace of a $T_1$ space is $T_1$ (singletons are closed in $X$, hence in $Y$).
:::

:::

::: {.pf-step #y-is-normal}
$Y$ is normal.

::: pf-proof

::: pf-step
Let $A, B \subseteq Y$ be disjoint closed subsets of $Y$.

::: pf-proof
take arbitrary disjoint closed sets in $Y$.
:::

:::

::: pf-step
$A$ and $B$ are closed in $X$.

::: pf-proof
$A$ is closed in $Y$ and $Y$ is closed in $X$, so $A$ is closed in $X$; same for $B$.
:::

:::

::: pf-step
By normality of $X$, there are disjoint open $U, V \subseteq X$ with $A \subseteq U$ and $B \subseteq V$.

::: pf-proof
$A, B$ are disjoint closed sets in the normal space $X$.
:::

:::

::: pf-step
Then $U \cap Y$ and $V \cap Y$ are disjoint open sets in $Y$ separating $A$ and $B$.

::: pf-proof
restrict the open sets to $Y$.
:::

:::

:::

:::

::: pf-qed
Step [](#y-is-normal){.pf-ref} shows $Y$ is normal.
:::

:::

:::
