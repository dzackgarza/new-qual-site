---
schema: qual/card@1
id: P-TOPF03G
kind: problem
title: "A map from S^2 to CP^2 disjoint from CP^1 is null-homotopic"
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Consider the standard embedding $\CP^1 \hookrightarrow \CP^2$.
Show that any map $f : S^2 \to \CP^2$ whose image $f(S^2)$ is disjoint from $\CP^1$ must be null-homotopic.
:::

::: {.solution}

::: pf

::: pf-step

The complement of the standard hyperplane $\CP^1\subset\CP^2$ is homeomorphic to $\CC^2$.

::: pf-proof

Take homogeneous coordinates $[z_0:z_1:z_2]$ with
$$
\CP^1=\{z_0=0\}.
$$
On the complement $z_0\ne0$, normalize to $z_0=1$. This identifies the complement with the affine chart
$$
[1:z_1:z_2]\longleftrightarrow (z_1,z_2)\in\CC^2.
$$

:::

:::

::: pf-step

Since $f(S^2)$ is disjoint from $\CP^1$, the map factors through this complement:
$$
S^2\xrightarrow{\tilde f}\CC^2\hookrightarrow\CP^2.
$$

::: pf-proof

The image condition says exactly that the codomain of $f$ may be restricted to $\CP^2\setminus\CP^1$.

:::

:::

::: pf-step

The map $\tilde f:S^2\to\CC^2$ is null-homotopic.

::: pf-proof

The space $\CC^2$ is contractible by the straight-line homotopy to the origin.

:::

:::

::: pf-step

Therefore $f$ is null-homotopic as a map into $\CP^2$.

::: pf-proof

Compose the null-homotopy in $\CC^2$ with the inclusion into $\CP^2$.

:::

:::

:::

:::
