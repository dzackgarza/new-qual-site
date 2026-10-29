---
schema: qual/card@1
id: P-PSTM-05
kind: problem
title: Connected base and connected fibers imply connected total space
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $p \colon X \to Y$ be a quotient map.
Suppose $Y$ is connected, and, for each $y \in Y$, the subspace $p^{-1}(\{y\})$ is connected.
Show that $X$ is connected.
:::

::: {.solution}
Suppose that $X = U \sqcup V$ with $U$ and $V$ disjoint, open and nonempty.
We derive a contradiction.

::: pf

::: {.pf-step #saturated}
$U = p^{-1}(p(U))$ and $V = p^{-1}(p(V))$.

::: pf-proof
For $y \in Y$, the sets $p^{-1}(y) \cap U$ and $p^{-1}(y) \cap V$ are disjoint, relatively open, and cover the connected fiber $p^{-1}(y)$.
So one of them is empty, and every fiber lies in $U$ or in $V$.
A point of $p^{-1}(p(U))$ shares its fiber with a point of $U$, so it lies in $U$; the same holds for $V$.
:::

:::

::: pf-step
$Y = p(U) \sqcup p(V)$ with $p(U)$ and $p(V)$ disjoint, open and nonempty, which contradicts the connectedness of $Y$.

::: pf-proof
Since $p$ is a quotient map, a set $W \subseteq Y$ is open when $p^{-1}(W)$ is open.
By step [](#saturated){.pf-ref}, $p^{-1}(p(U)) = U$ and $p^{-1}(p(V)) = V$ are open, so $p(U)$ and $p(V)$ are open.
They are nonempty because $U$ and $V$ are.
They are disjoint, because a common point would have its fiber in both $U$ and $V$ by step [](#saturated){.pf-ref}.
They cover $Y$ because $p$ is surjective.
:::

:::

:::
:::
