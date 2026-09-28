---
schema: qual/card@1
id: P-TOPQ17D
kind: problem
title: "Integer homology of RP^2 x X where H_k(X) = Z/kZ"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Künneth Formula
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Let $X$ be a path-connected space whose homology groups in positive dimensions are $H_k(X; \mathbb{Z}) = \mathbb{Z}/k\mathbb{Z}$.
Compute the integer homology $H_*(\mathbb{RP}^2 \times X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. The integral homology of $\mathbb{RP}^2$ is $H_0=\mathbb Z$, $H_1=\mathbb Z/2$, and zero otherwise.
::: {.proof}
This is the standard cellular computation.
:::

<1>2. For $n\ge1$, the Künneth exact sequence gives
$$H_n(\mathbb{RP}^2\times X)\cong H_n(X)\oplus(H_{n-1}(X)\otimes\mathbb Z/2)\oplus\operatorname{Tor}(H_{n-2}(X),\mathbb Z/2),$$
with the convention that negative-index groups vanish.
::: {.proof}
Only $H_0$ and $H_1$ of $\mathbb{RP}^2$ contribute. The Künneth sequence splits (noncanonically) over $\mathbb Z$.
:::

<1>3. Since $H_k(X)=\mathbb Z/k$ for $k>0$ and $H_0(X)=\mathbb Z$, one has
$$\mathbb Z/m\otimes\mathbb Z/2\cong\operatorname{Tor}(\mathbb Z/m,\mathbb Z/2)\cong\begin{cases}\mathbb Z/2,&m\text{ even},\\0,&m\text{ odd}.
\end{cases}$$
::: {.proof}
Both groups are isomorphic to $\mathbb Z/\gcd(m,2)$.
:::

<1>4. Therefore $H_0\cong\mathbb Z$, $H_1\cong\mathbb Z/2$, and for $n\ge2$,
$$\boxed{H_n(\mathbb{RP}^2\times X)\cong \mathbb Z/n\oplus E_{n-1}\oplus E_{n-2},}$$
where $E_j=\mathbb Z/2$ if $j>0$ is even and $E_j=0$ otherwise.
::: {.proof}
Substitute <1>3 into <1>2>. For $n=1$, the $H_0(X)\otimes H_1(\mathbb{RP}^2)$ term gives $\mathbb Z/2$ while $H_1(X)=\mathbb Z/1=0$.
:::
:::
