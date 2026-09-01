---
schema: qual/card@1
id: P-SJPBM
kind: problem
title: No corner-to-corner conformal homeomorphism from a square onto a $2\times 1$
  rectangle
classification:
  areas:
  - real-analysis
  topics:
  - Conformal Maps
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Let $Q$ be the closed unit square in $\mathbb{C}$ and let $R$ be the closed rectangle in $\mathbb{C}$ with vertices $\{0,2,i,2+i\}$.
Prove there does not exist a surjective homeomorphism $f: Q\to R$ that is conformal on the interior of $Q$ and maps corners to corners.
:::

:::{.solution}
Suppose $f: Q\to R$ satisfies the given conditions. By continuity, it must preserve the order of the vertices, so by precomposing with rotations and flips if necessary, we may assume that $f$ fixes the vertical line segment $[0,i]$. By the Schwarz reflection principle, applied iteratively and reflecting over the vertical lines, we can extend $f$ to a map from the strip $0\le \text{Im}(z)\le 1$ to itself. We can then reflect over the two horizontal lines to extend $f$ to a map from the strip $-1\le \text{Im}(z)\le 2$ to itself. This strip is simply connected and so is conformally equivalent to $\mathbb{D}$. So $f$ has been extended to a conformal automorphism of a region conformally equivalent to $\mathbb{D}$, and $f$ has two fixed points, which implies $f$ is the identity, a contradiction. $\square$
:::
