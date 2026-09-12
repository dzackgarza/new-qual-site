---
schema: qual/card@1
id: P-AMD-VP43HDJY
kind: problem
title: CW structure, $\pi_1$, and homology of the lens space $L(p,1)$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
  - Fundamental Group
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Describe a CW complex structure for the lens space $L(p, 1)$ and compute $\pi_1, H_*$ for it.
:::

::: {.solution}
<1>1. The lens space $L(p,1)$ admits a CW structure with one cell in each dimension $0,1,2,3$.
::: {.proof}
View $L(p,1)$ as the quotient of $S^3$ by the free action of the cyclic group of order $p$. Equivalently, use the standard lens-space fundamental domain: the quotient has one vertex, one edge generating the cyclic fundamental group, one $2$-cell whose attaching map winds $p$ times around that edge, and one top-dimensional $3$-cell.
:::

<1>2. Its fundamental group is
$$
\boxed{\pi_1(L(p,1))\cong\mathbb Z/p}.
$$
::: {.proof}
The $1$-skeleton is a circle with generator $a$, and the $2$-cell is attached by the degree-$p$ map, imposing the single relation $a^p=1$. The $3$-cell does not change $\pi_1$.
:::

<1>3. The cellular chain complex is
$$
0\longrightarrow\mathbb Z\xrightarrow{0}\mathbb Z\xrightarrow{p}\mathbb Z\xrightarrow{0}\mathbb Z\longrightarrow0.
$$
::: {.proof}
There is one cell in each dimension. The $2$-cell attaching map has degree $p$ on the $1$-cell, so $\partial_2$ is multiplication by $p$. The top boundary is zero because $L(p,1)$ is a closed orientable $3$-manifold, so its top homology is $\mathbb Z$.
:::

<1>4. Therefore
$$
\boxed{H_k(L(p,1);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,3,\\
\mathbb Z/p,&k=1,\\
0,&\text{otherwise}.
\end{cases}}
$$
::: {.proof}
Take homology of the chain complex in <1>3.
:::
:::
