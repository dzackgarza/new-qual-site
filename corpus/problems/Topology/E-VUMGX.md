---
schema: qual/card@1
id: E-VUMGX
kind: problem
title: $X\times Y$ is Hausdorff if and only if $X$ and $Y$ are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source omits nonemptiness; X x {} is Hausdorff for every X, so the converse is false without it. The statement now assumes X and Y nonempty."
---

::: {.exercise}
Let $X$ and $Y$ be nonempty topological spaces. Prove that $X, Y$ are Hausdorff iff $X\cross Y$ is Hausdorff.
:::

::: {.solution}

::: pf

::: pf-step

If $X$ and $Y$ are Hausdorff, then $X\times Y$ is Hausdorff.

::: pf-proof

Distinct points $(x_1,y_1),(x_2,y_2)$ differ in at least one coordinate, say $x_1\neq x_2$. Choose disjoint open $U_1\ni x_1$ and $U_2\ni x_2$ in $X$. Then $U_1\times Y$ and $U_2\times Y$ are disjoint open neighborhoods of the two points. The case $y_1\neq y_2$ is symmetric.

:::

:::

::: pf-step

If $X\times Y$ is Hausdorff, then $X$ and $Y$ are Hausdorff.

::: pf-proof

Choose $y_0\in Y$. The map $x\mapsto(x,y_0)$ is a homeomorphism of $X$ onto the subspace $X\times\{y_0\}$, and a subspace of a Hausdorff space is Hausdorff, so $X$ is Hausdorff. Choosing $x_0\in X$ shows the same for $Y$.

:::

:::

:::

:::
