---
schema: qual/card@1
id: P-UCTOP-SU09-3
kind: problem
title: Integral homology of product of lens spaces
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Recall that for any $p \geq 2$, the 3-dimensional lens space $L^3(p,1)$ has integral homology groups $\mathbb{Z}, \mathbb{Z}_p, 0, \mathbb{Z}$ in dimensions 0, 1, 2, 3. Calculate the integral homology of the product $L(p,1) \times L(q,1)$.

::: {.solution}
<1>1. Put $d=\gcd(p,q)$. Then
$$
\mathbb Z/p\otimes\mathbb Z/q\cong\mathbb Z/d,
\qquad
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/p,\mathbb Z/q)\cong\mathbb Z/d.
$$
:::
::: {.proof}
Both statements follow from the standard free resolution
$$
0\to\mathbb Z\xrightarrow{p}\mathbb Z\to\mathbb Z/p\to0
$$
and the fact that the kernel and cokernel of multiplication by $p$ on $\mathbb Z/q$ are cyclic of order $d$.
:::

<1>2. The Künneth theorem gives
$$
H_n(L(p,1)\times L(q,1);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,6,\\
\mathbb Z/p\oplus\mathbb Z/q,&n=1,4,\\
\mathbb Z/d,&n=2,\\
\mathbb Z^2\oplus\mathbb Z/d,&n=3,\\
0,&n=5\text{ or }n>6.
\end{cases}
$$
:::
::: {.proof}
For $L(p,1)$ the only nonzero homology groups are $H_0=\mathbb Z$, $H_1=\mathbb Z/p$, and $H_3=\mathbb Z$, and similarly for $L(q,1)$. The tensor terms give
$$
H_1:\ \mathbb Z/p\oplus\mathbb Z/q,\qquad
H_2:\ \mathbb Z/d,\qquad
H_3:\ \mathbb Z^2,\qquad
H_4:\ \mathbb Z/p\oplus\mathbb Z/q,\qquad
H_6:\ \mathbb Z.
$$
The only nonzero Tor term occurs from $H_1\otimes H_1$ one degree later, contributing $\mathbb Z/d$ to $H_3$. Over $\mathbb Z$ the Künneth short exact sequence splits noncanonically, yielding the displayed groups.
:::
:::

