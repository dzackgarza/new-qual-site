---
schema: qual/card@1
id: S-ILPNY
kind: solution
title: Solution to P-SJPBM
classification:
  areas:
  - real-analysis
  topics:
  - conformal-maps
  - counterexamples
relations:
- kind: solves
  target: P-SJPBM
review: draft
---

:::{.solution}
Suppose $f: Q\to R$ satisfies the given conditions. By continuity, it must preserve the order of the vertices, so by precomposing with rotations and flips if necessary, we may assume that $f$ fixes the vertical line segment $[0,i]$. By the Schwarz reflection principle, applied iteratively and reflecting over the vertical lines, we can extend $f$ to a map from the strip $0\le \text{Im}(z)\le 1$ to itself. We can then reflect over the two horizontal lines to extend $f$ to a map from the strip $-1\le \text{Im}(z)\le 2$ to itself. This strip is simply connected and so is conformally equivalent to $\mathbb{D}$. So $f$ has been extended to a conformal automorphism of a region conformally equivalent to $\mathbb{D}$, and $f$ has two fixed points, which implies $f$ is the identity, a contradiction. $\square$
:::
