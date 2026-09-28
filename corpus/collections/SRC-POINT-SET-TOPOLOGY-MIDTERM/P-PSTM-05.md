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
Suppose Y is connected, and, for each $y \in Y$ the subspace $p ^ { - 1 } ( \{ y \} )$ is connected.
Show that X is connected.
:::

::: {.solution}
Suppose, toward a contradiction, that $X=U\sqcup V$ is a separation into nonempty open sets.
Because $U$ and $V$ are complementary open sets, both are also closed.

For each $y\in Y$, the connected fiber $p^{-1}(y)$ cannot meet both $U$ and $V$; otherwise
\[
p^{-1}(y)=\bigl(p^{-1}(y)\cap U\bigr)\sqcup\bigl(p^{-1}(y)\cap V\bigr)
\]
would be a separation of that fiber.
Hence every fiber lies entirely in $U$ or entirely in $V$.
Thus $U$ and $V$ are saturated for $p$:
\[
p^{-1}(p(U))=U,
\qquad
p^{-1}(p(V))=V.
\]

Since $p$ is a quotient map and $U,V$ are open saturated subsets of $X$, the sets $p(U)$ and $p(V)$ are open in $Y$.
They are nonempty, disjoint, and cover $Y$ because $p$ is surjective.
This contradicts connectedness of $Y$.
Therefore $X$ is connected.
:::
