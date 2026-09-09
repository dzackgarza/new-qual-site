---
schema: qual/card@1
id: P-AMD-IJD6LW4S
kind: problem
title: $S_m \vee S_n$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
---

::: {.problem}
Use cellular chain complexes to compute the homology of $S^m \vee S^n$ and $S^m \times S^n$.
:::

::: {.solution}
<1>1. Give each sphere its CW structure with one $0$-cell and one top-dimensional cell. Then $S^m\vee S^n$ has one $0$-cell, one $m$-cell and one $n$-cell, with all cellular differentials zero.
::: {.proof}
Each positive-dimensional cell is attached to the common basepoint, so its cellular boundary is zero. If $m=n$, there are two cells in that common dimension.
:::

<1>2. Hence, for $m,n>0$,
$$
\boxed{\widetilde H_k(S^m\vee S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=m\ne n\text{ or }k=n\ne m,\\
\mathbb Z^2,&k=m=n,\\
0,&\text{otherwise.}
\end{cases}}
$$
::: {.proof}
This is the homology of the cellular chain complex in <1>1.
:::

<1>3. The product CW structure on $S^m\times S^n$ has one cell in dimensions $0,m,n,m+n$, with two cells in dimension $m=n$ when the middle dimensions coincide, and all cellular differentials zero.
::: {.proof}
The cells are products of the $0$- and top cells of the two sphere factors. Cellular boundaries obey the product boundary formula, and the differentials in each sphere factor are zero.
:::

<1>4. Therefore, for $m,n>0$,
$$
\boxed{H_k(S^m\times S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,m,n,m+n\text{ when these are distinct},\\
\mathbb Z^2,&k=m=n,\\
0,&\text{otherwise,}
\end{cases}}
$$
with $H_{2m}\cong\mathbb Z$ in the case $m=n$.
::: {.proof}
Read the homology from the zero-differential cellular chain complex of <1>3.
:::
:::
