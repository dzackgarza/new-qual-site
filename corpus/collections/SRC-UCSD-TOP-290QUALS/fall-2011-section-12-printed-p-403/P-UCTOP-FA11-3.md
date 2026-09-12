---
schema: qual/card@1
id: P-UCTOP-FA11-3
kind: problem
title: Counting path-connected covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

Assume that $X$ is a path-connected, locally simply-connected space with fundamental group isomorphic to $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_3$.
How many path-connected covering spaces of $X$ are there, up to equivalence?

::: {.solution}
<1>1. Path-connected covering spaces of $X$ up to equivalence correspond to conjugacy classes of subgroups of
$$
G=\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/3.
$$
::: {.proof}
This is the standard classification of connected covering spaces for a path-connected locally simply-connected space.
:::

<1>2. Since $G$ is abelian, conjugacy classes of subgroups are just subgroups.
::: {.proof}
Conjugation is trivial in an abelian group.
:::

<1>3. Every subgroup of $G$ is the product of a subgroup of $(\mathbb Z/2)^2$ and a subgroup of $\mathbb Z/3$.
::: {.proof}
The $2$-primary and $3$-primary components are characteristic and have coprime orders. For any subgroup $H\le G$, its Sylow subgroups are $H\cap(\mathbb Z/2)^2$ and $H\cap\mathbb Z/3$, and $H$ is their direct product.
:::

<1>4. The group $(\mathbb Z/2)^2$ has exactly five subgroups, while $\mathbb Z/3$ has exactly two.
::: {.proof}
The first has the trivial subgroup, its three one-dimensional subspaces, and the whole group. A cyclic group of prime order has only the trivial subgroup and itself.
:::

<1>5. Therefore the number of path-connected covering spaces up to equivalence is
$$
\boxed{5\cdot2=10}.
$$
::: {.proof}
Combine <1>1--<1>4.
:::
:::
