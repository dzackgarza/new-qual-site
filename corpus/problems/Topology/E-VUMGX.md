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
---

::: exercise
Prove that $X, Y$ are Hausdorff iff $X\cross Y$ is Hausdorff.
:::

::: {.solution}
<1>1. If $X$ and $Y$ are Hausdorff, then $X\times Y$ is Hausdorff.
::: {.proof}
For distinct $(x_1,y_1),(x_2,y_2)$, at least one coordinate differs. Separate that coordinate by disjoint open neighborhoods and take the product with the whole other factor.
:::

<1>2. Conversely, if $X\times Y$ is Hausdorff and both factors are nonempty, then $X$ and $Y$ are Hausdorff.
::: {.proof}
Choose $y_0\in Y$. The slice $X\times\{y_0\}$ is a subspace of the Hausdorff product and is homeomorphic to $X$, hence $X$ is Hausdorff. Similarly $Y$ is Hausdorff using a point of $X$.
:::

<1>3. Thus, for nonempty factors,
$$\boxed{X\times Y\text{ is Hausdorff}\iff X\text{ and }Y\text{ are Hausdorff}.}$$
::: {.proof}
Combine <1>1--<1>2. If an empty factor is allowed, the converse needs the stated nonemptiness qualification because the empty product space is Hausdorff regardless of the other factor.
:::
:::
