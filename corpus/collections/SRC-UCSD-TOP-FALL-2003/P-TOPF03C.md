---
schema: qual/card@1
id: P-TOPF03C
kind: problem
title: "Homology of a space obtained by identifying edges of a solid hexagon"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $X$ be the space obtained by identifying the edges of a solid hexagon as shown.
Compute $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Reading the arrows in the source diagram, all six vertices are identified to one vertex, the three $a$-edges form one oriented edge $a$, the three $b$-edges form one oriented edge $b$, and the hexagonal $2$-cell has attaching word
$$a^3b^3.$$
::: {.proof}
The three consecutive $a$-arrows and three consecutive $b$-arrows form one directed cycle around the boundary. Because consecutive occurrences of each label share endpoints, the edge identifications collapse all polygon vertices to a single class.
:::

<1>2. Thus the cellular chain complex in positive degrees is
$$0\to\mathbb Z\xrightarrow{\partial_2}\mathbb Z^2\to0,\qquad \partial_2(1)=(3,3).$$
::: {.proof}
The cellular boundary records the exponent sums of $a$ and $b$ in the attaching word.
:::

<1>3. Therefore
$$\boxed{H_k(X;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,\\\mathbb Z\oplus\mathbb Z/3,&k=1,\\0,&k\ge2.\end{cases}}$$
::: {.proof}
The map $\partial_2$ is injective, so $H_2=0$, and $\operatorname{coker}(3,3)\cong\mathbb Z\oplus\mathbb Z/3$ by Smith normal form.
:::
:::
