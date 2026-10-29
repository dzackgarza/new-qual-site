---
schema: qual/card@1
id: E-JN4QP
kind: problem
title: Continuous bijections from compact spaces to Hausdorff spaces are homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
---

::: {.problem}
Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
:::

::: {.solution}
Let $f\colon X\to Y$ be a continuous bijection with $X$ compact and $Y$ Hausdorff.

::: pf

::: {.pf-step #closed}

For every closed $C\subseteq X$, the image $f(C)$ is closed in $Y$.

::: pf-proof

A closed subset of a compact space is compact, so $C$ is compact. The continuous image of a compact set is compact, so $f(C)$ is compact. A compact subset of a Hausdorff space is closed, so $f(C)$ is closed.

:::

:::

::: pf-step

$f$ is a homeomorphism.

::: pf-proof

Since $f$ is bijective, $f^{-1}\colon Y\to X$ exists and $(f^{-1})^{-1}(C) = f(C)$ for every $C\subseteq X$. By step [](#closed){.pf-ref}, preimages of closed sets under $f^{-1}$ are closed, so $f^{-1}$ is continuous.

:::

:::

:::

:::
