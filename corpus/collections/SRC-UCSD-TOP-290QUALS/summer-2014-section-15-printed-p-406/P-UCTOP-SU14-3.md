---
schema: qual/card@1
id: P-UCTOP-SU14-3
kind: problem
title: 'Homology and cohomology of the product of two Klein bottles'
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $X = K \times K$ be the product of the Klein bottle $K$ with itself.
Compute the homology $H_*(X; \ZZ)$ and cohomology $H^*(X; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step
The integral homology of the Klein bottle is
$$
H_0(K)=\ZZ,\qquad H_1(K)=\ZZ\oplus\ZZ/2,\qquad H_i(K)=0\ (i\ge2).
$$

::: pf-proof
This follows from the standard CW structure with one $0$-cell, two $1$-cells, and one $2$-cell attached by $aba^{-1}b$.
:::

:::

::: {.pf-step #kunneth-homology}
The Künneth theorem gives
$$
H_n(K\times K;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ^2\oplus(\ZZ/2)^2,&n=1,\\
\ZZ\oplus(\ZZ/2)^3,&n=2,\\
\ZZ/2,&n=3,\\
0,&n\ge4.
\end{cases}
$$

::: pf-proof
In degree $2$, the only tensor contribution is
$$
(\ZZ\oplus\ZZ/2)\otimes(\ZZ\oplus\ZZ/2)
\cong \ZZ\oplus(\ZZ/2)^3.
$$
In degree $3$, the only nonzero contribution is
$$
\operatorname{Tor}(\ZZ/2,\ZZ/2)\cong\ZZ/2.
$$
All other terms follow immediately from $H_0(K)=\ZZ$ and the vanishing above degree $1$.
:::

:::

::: pf-step
The universal coefficient theorem for cohomology gives
$$
H^n(K\times K;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ^2,&n=1,\\
\ZZ\oplus(\ZZ/2)^2,&n=2,\\
(\ZZ/2)^3,&n=3,\\
\ZZ/2,&n=4,\\
0,&n\ge5.
\end{cases}
$$

::: pf-proof
For each $n$,
$$
0\to\operatorname{Ext}(H_{n-1},\ZZ)\to H^n\to\operatorname{Hom}(H_n,\ZZ)\to0.
$$
Apply the homology groups from step [](#kunneth-homology){.pf-ref}, using $\operatorname{Ext}(\ZZ/2,\ZZ)\cong\ZZ/2$ and the fact that Hom into $\ZZ$ kills torsion. The only extension involving a free quotient splits.
:::

:::

:::

:::
