---
schema: qual/card@1
id: P-TOPS10H
kind: problem
title: "Homology of a solid lens with top and bottom identified via a 120-degree twist"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Lens Spaces
relations: []
review: draft
---

::: problem
Let $L$ be a solid $3$-dimensional lens (a flattened ball).
Identify the top and bottom surfaces via vertical translation and a twist of $120$ degrees, as shown in the picture.
Calculate the integral homology of the resulting space.
:::

::: {.solution}
<1>1. The quotient shown in the source is the lens space $L(3,1)$.
::: {.proof}
The solid lens is a $3$-ball whose boundary is decomposed into the top and bottom discs. Identifying those discs after a rotation through $2\pi/3$ is the standard fundamental-domain construction of the lens space $L(3,1)$: three copies of the lens assemble cyclically to the universal cover $S^3$.
:::

<1>2. The standard CW structure on $L(3,1)$ has one cell in each dimension $0,1,2,3$, with cellular chain complex
$$
0\to\mathbb Z\xrightarrow{0}\mathbb Z\xrightarrow{\times3}\mathbb Z\xrightarrow{0}\mathbb Z\to0.
$$
::: {.proof}
The $1$-skeleton is a circle representing the generator of $\pi_1(L(3,1))\cong\mathbb Z/3$. The $2$-cell attaches by the degree-$3$ map on that circle, so $\partial_2$ is multiplication by $3$. The top cell supplies the orientation class of the closed orientable $3$-manifold, hence $\partial_3=0$.
:::

<1>3. Therefore
$$
\boxed{H_k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,3,\\
\mathbb Z/3,&k=1,\\
0,&k=2\text{ or }k>3.
\end{cases}}
$$
::: {.proof}
Take kernels modulo images in the cellular chain complex of <1>2.
:::
:::
