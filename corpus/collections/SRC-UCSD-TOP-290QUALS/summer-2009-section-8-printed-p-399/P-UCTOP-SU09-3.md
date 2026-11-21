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
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. Recomputed the Kunneth sum: tensor terms give Z in degrees 0 and 6,
    Z/p + Z/q in 1 and 4, Z/p tensor Z/q = Z/d in degree 2, and Z + Z in degree 3; the only nonzero
    Tor term is Tor(Z/p, Z/q) = Z/d, landing in degree 3, so H_3 = Z^2 + Z/d and all other degrees
    vanish. The card's table matches, including that degree 2 carries the tensor term and not a Tor
    term, which is the easy slip in this computation. Checked Z/d = Z/gcd(p,q) for both the tensor and
    the Tor term via the resolution 0 -> Z -p-> Z -> Z/p -> 0. Not checked: the printed exam, which
    was not re-read in this pass.
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

