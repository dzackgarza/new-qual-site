---
schema: qual/card@1
id: P-TOPF18B
kind: problem
title: "Fundamental group and homology of a hexagon-triangle gluing"
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

::: problem
Let $X$ be the space made by gluing the edges of a solid hexagon $H$ and a solid triangle $T$ according to the scheme pictured.
Calculate $\pi_1(X)$ and $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Reading the source diagram, all vertices are identified to one vertex. There are four $1$-cells $a,b,c,d$, and the triangle and hexagon attach by the words
$$abc,\qquad adbdcd,$$
up to cyclic permutation and simultaneous inversion.
::: {.proof}
Following the displayed arrows around the triangle gives one occurrence each of $a,b,c$. Following them around the hexagon gives $a,d,b,d,c,d$. The repeated $d$-edge identifications, together with the $a,b,c$ identifications to the triangle, collapse all boundary vertices to one class.
:::

<1>2. Thus
$$\boxed{\pi_1(X)\cong\langle a,b,c,d\mid abc,\ adbdcd\rangle.}$$
::: {.proof}
This is the standard CW presentation from one $0$-cell, four $1$-cells, and the two polygonal $2$-cells.
:::

<1>3. The cellular boundary $\partial_2:\mathbb Z^2\to\mathbb Z^4$ has columns
$$(1,1,1,0)^T,\qquad(1,1,1,3)^T.$$
::: {.proof}
These are the exponent-sum vectors of the two attaching words in the basis $(a,b,c,d)$.
:::

<1>4. Its two columns are independent, so $H_2(X)=0$, and its cokernel is
$$\mathbb Z^4/\langle(1,1,1,0),(1,1,1,3)\rangle\cong\mathbb Z^2\oplus\mathbb Z/3.$$
::: {.proof}
Subtracting the first column from the second gives $(0,0,0,3)$. The first vector is primitive, so Smith normal form is $\operatorname{diag}(1,3)$.
:::

<1>5. Hence
$$\boxed{H_k(X;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,\\\mathbb Z^2\oplus\mathbb Z/3,&k=1,\\0,&k\ge2.\end{cases}}$$
::: {.proof}
There are no cells above dimension $2$.
:::
:::
