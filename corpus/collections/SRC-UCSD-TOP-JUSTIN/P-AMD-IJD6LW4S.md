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

::: pf

::: {.pf-step #s1}

Give each sphere its CW structure with one $0$-cell and one top-dimensional cell. Then $S^m\vee S^n$ has one $0$-cell, one $m$-cell and one $n$-cell, with all cellular differentials zero.

::: pf-proof

Each positive-dimensional cell is attached to the common basepoint, so its cellular boundary is zero. If $m=n$, there are two cells in that common dimension.

:::

:::

::: pf-step

Hence, for $m,n>0$,
$$
\boxed{\widetilde H_k(S^m\vee S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=m\ne n\text{ or }k=n\ne m,\\
\mathbb Z^2,&k=m=n,\\
0,&\text{otherwise.}
\end{cases}}
$$

::: pf-proof

This is the homology of the cellular chain complex in step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

The product CW structure on $S^m\times S^n$ has one cell in dimensions $0,m,n,m+n$, with two cells in dimension $m=n$ when the middle dimensions coincide, and all cellular differentials zero.

::: pf-proof

The cells are products of the $0$- and top cells of the two sphere factors. Cellular boundaries obey the product boundary formula, and the differentials in each sphere factor are zero.

:::

:::

::: pf-step

Therefore, for $m,n>0$,
$$
\boxed{H_k(S^m\times S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,m,n,m+n\text{ when these are distinct},\\
\mathbb Z^2,&k=m=n,\\
0,&\text{otherwise,}
\end{cases}}
$$
with $H_{2m}\cong\mathbb Z$ in the case $m=n$.

::: pf-proof

Read the homology from the zero-differential cellular chain complex of step [](#s3){.pf-ref}.

:::

:::

:::

:::
