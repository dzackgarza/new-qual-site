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

::: problem
Consider the standard embedding $\mathbb{CP}^1 \hookrightarrow \mathbb{CP}^2$.
Show that any map $f : S^2 \to \mathbb{CP}^2$ whose image $f(S^2)$ is disjoint from $\mathbb{CP}^1$ must be null-homotopic.
:::

::: {.solution}
<1>1. The complement of the standard hyperplane $\mathbb{CP}^1\subset\mathbb{CP}^2$ is homeomorphic to $\mathbb C^2$.
::: {.proof}
Take homogeneous coordinates $[z_0:z_1:z_2]$ with
$$
\mathbb{CP}^1=\{z_0=0\}.
$$
On the complement $z_0\ne0$, normalize to $z_0=1$. This identifies the complement with the affine chart
$$
[1:z_1:z_2]\longleftrightarrow (z_1,z_2)\in\mathbb C^2.
$$
:::

<1>2. Since $f(S^2)$ is disjoint from $\mathbb{CP}^1$, the map factors through this complement:
$$
S^2\xrightarrow{\tilde f}\mathbb C^2\hookrightarrow\mathbb{CP}^2.
$$
::: {.proof}
The image condition says exactly that the codomain of $f$ may be restricted to $\mathbb{CP}^2\setminus\mathbb{CP}^1$.
:::

<1>3. The map $\tilde f:S^2\to\mathbb C^2$ is null-homotopic.
::: {.proof}
The space $\mathbb C^2$ is contractible by the straight-line homotopy to the origin.
:::

<1>4. Therefore $f$ is null-homotopic as a map into $\mathbb{CP}^2$.
::: {.proof}
Compose the null-homotopy in $\mathbb C^2$ with the inclusion into $\mathbb{CP}^2$.
:::
:::
