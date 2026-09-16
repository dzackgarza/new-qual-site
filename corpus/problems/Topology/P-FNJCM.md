---
schema: qual/card@1
id: P-FNJCM
kind: problem
title: Products of Hausdorff spaces; $\RR$ versus $[0,\infty)$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
  - Homeomorphisms
relations: []
review: draft
---

::: {.problem}
- Is every product (finite or infinite) of Hausdorff spaces Hausdorff?

- Is $\RR$ homeomorphic to $[0, \infty)$?
:::

::: {.solution}
<1>1. Every product, finite or infinite, of Hausdorff spaces is Hausdorff.
::: {.proof}
If two points $x=(x_i)$ and $y=(y_i)$ differ, choose a coordinate $j$ with $x_j\ne y_j$. Separate $x_j,y_j$ by disjoint open sets $U,V$ in the Hausdorff factor $X_j$. Their inverse images under the projection $\prod_iX_i\to X_j$ are disjoint open neighborhoods of $x,y$.
:::

<1>2. The spaces $\mathbb R$ and $[0,\infty)$ are not homeomorphic.
::: {.proof}
Removing any point from $\mathbb R$ disconnects it into two components. But removing the endpoint $0$ from $[0,\infty)$ leaves $(0,\infty)$, which is connected. A homeomorphism would preserve this point-deletion property.
:::
:::
