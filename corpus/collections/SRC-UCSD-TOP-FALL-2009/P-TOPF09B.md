---
schema: qual/card@1
id: P-TOPF09B
kind: problem
title: "Fundamental group and homology of a space from gluing a hexagon and triangle"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
A solid hexagon and a solid triangle are glued together along their edges, according to the following scheme.
Calculate the fundamental group and the homology of the resulting space $X$.
:::

::: {.solution}

::: pf

::: pf-step

From the source diagram, all vertices are identified to one vertex and there are three $1$-cells $a,b,c$. With compatible boundary orientations, the hexagon attaches by
$$(abc)^2$$
and the triangle by
$$(abc)^{-1}.$$

::: pf-proof

The hexagon reads $a,b,c,a,b,c$ around its boundary. The triangle has the same three labelled arrows with the opposite cyclic orientation, so its attaching word is the inverse of $abc$.

:::

:::

::: pf-step

Hence
$$\pi_1(X)\cong\langle a,b,c\mid (abc)^2,(abc)^{-1}\rangle\cong F_2.$$

::: pf-proof

The triangle relation gives $abc=1$, making the hexagon relation redundant; eliminate $c=(ab)^{-1}$.

:::

:::

::: pf-step

The cellular boundary $\partial_2:\mathbb Z^2\to\mathbb Z^3$ has columns $(2,2,2)^T$ and $(-1,-1,-1)^T$, so its image has rank $1$ and its kernel has rank $1$.

::: pf-proof

Again cellular boundaries are exponent-sum vectors of the attaching words; the two columns are integer multiples of the primitive vector $(1,1,1)^T$.

:::

:::

::: pf-step

Therefore
$$\boxed{H_k(X;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,2,\\\mathbb Z^2,&k=1,\\0,&k>2.\end{cases}}$$

::: pf-proof

$H_2=\ker\partial_2\cong\mathbb Z$, while $H_1=\mathbb Z^3/\langle(1,1,1)\rangle\cong\mathbb Z^2$.

:::

:::

:::

:::
