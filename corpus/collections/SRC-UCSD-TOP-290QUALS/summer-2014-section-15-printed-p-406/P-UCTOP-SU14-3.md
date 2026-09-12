---
schema: qual/card@1
id: P-UCTOP-SU14-3
kind: problem
title: Homology and cohomology of Klein bottle × Klein bottle
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $X = K \times K$ be the product of the Klein bottle $K$ with itself.
Compute the homology $H_*(X; \mathbb{Z})$ and cohomology $H^*(X; \mathbb{Z})$.

::: {.solution}
<1>1. The integral homology of the Klein bottle is
$$
H_0(K)=\mathbb Z,\qquad H_1(K)=\mathbb Z\oplus\mathbb Z/2,\qquad H_i(K)=0\ (i\ge2).
$$
::: {.proof}
This follows from the standard CW structure with one $0$-cell, two $1$-cells, and one $2$-cell attached by $aba^{-1}b$.
:::

<1>2. The Künneth theorem gives
$$
H_n(K\times K;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z^2\oplus(\mathbb Z/2)^2,&n=1,\\
\mathbb Z\oplus(\mathbb Z/2)^3,&n=2,\\
\mathbb Z/2,&n=3,\\
0,&n\ge4.
\end{cases}
$$
::: {.proof}
In degree $2$, the only tensor contribution is
$$
(\mathbb Z\oplus\mathbb Z/2)\otimes(\mathbb Z\oplus\mathbb Z/2)
\cong \mathbb Z\oplus(\mathbb Z/2)^3.
$$
In degree $3$, the only nonzero contribution is
$$
\operatorname{Tor}(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2.
$$
All other terms follow immediately from $H_0(K)=\mathbb Z$ and the vanishing above degree $1$.
:::

<1>3. The universal coefficient theorem for cohomology gives
$$
H^n(K\times K;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z^2,&n=1,\\
\mathbb Z\oplus(\mathbb Z/2)^2,&n=2,\\
(\mathbb Z/2)^3,&n=3,\\
\mathbb Z/2,&n=4,\\
0,&n\ge5.
\end{cases}
$$
::: {.proof}
For each $n$,
$$
0\to\operatorname{Ext}(H_{n-1},\mathbb Z)\to H^n\to\operatorname{Hom}(H_n,\mathbb Z)\to0.
$$
Apply the homology groups from <1>2, using $\operatorname{Ext}(\mathbb Z/2,\mathbb Z)\cong\mathbb Z/2$ and the fact that Hom into $\mathbb Z$ kills torsion. The only extension involving a free quotient splits.
:::
:::
