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

::: {.problem}
Recall that for any $p \geq 2$, the 3-dimensional lens space $L^3(p,1)$ has integral homology groups $\ZZ, \ZZ_p, 0, \ZZ$ in dimensions 0, 1, 2, 3. Calculate the integral homology of the product $L(p,1) \times L(q,1)$.
:::

::: {.solution}

::: pf

::: pf-step
Put $d=\gcd(p,q)$. Then
$$
\ZZ/p\otimes\ZZ/q\cong\ZZ/d,
\qquad
\operatorname{Tor}_1^{\ZZ}(\ZZ/p,\ZZ/q)\cong\ZZ/d.
$$

::: pf-proof
Both statements follow from the standard free resolution
$$
0\to\ZZ\xrightarrow{p}\ZZ\to\ZZ/p\to0
$$
and the fact that the kernel and cokernel of multiplication by $p$ on $\ZZ/q$ are cyclic of order $d$.
:::

:::

::: pf-step
The Künneth theorem gives
$$
H_n(L(p,1)\times L(q,1);\ZZ)\cong
\begin{cases}
\ZZ,&n=0,6,\\
\ZZ/p\oplus\ZZ/q,&n=1,4,\\
\ZZ/d,&n=2,\\
\ZZ^2\oplus\ZZ/d,&n=3,\\
0,&n=5\text{ or }n>6.
\end{cases}
$$

::: pf-proof
For $L(p,1)$ the only nonzero homology groups are $H_0=\ZZ$, $H_1=\ZZ/p$, and $H_3=\ZZ$, and similarly for $L(q,1)$. The tensor terms give
$$
H_1:\ \ZZ/p\oplus\ZZ/q,\qquad
H_2:\ \ZZ/d,\qquad
H_3:\ \ZZ^2,\qquad
H_4:\ \ZZ/p\oplus\ZZ/q,\qquad
H_6:\ \ZZ.
$$
The only nonzero Tor term occurs from $H_1\otimes H_1$ one degree later, contributing $\ZZ/d$ to $H_3$. Over $\ZZ$ the Künneth short exact sequence splits noncanonically, yielding the displayed groups.
:::

:::

:::

:::

