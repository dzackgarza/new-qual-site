---
schema: qual/card@1
id: P-AMD-JXFC4L6D
kind: problem
title: $H_*(\RP^2 \times \RP^3; \ZZ)$
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
Compute $H_*(\RP^2\cross \RP^3; \ZZ)$
:::

::: {.solution}

::: pf

::: pf-step

The integral homology of the factors is
$$
H_i(\mathbb{RP}^2)=
\begin{cases}
\ZZ,&i=0,\\
\ZZ/2,&i=1,\\
0,&\text{otherwise},
\end{cases}
$$
and
$$
H_i(\mathbb{RP}^3)=
\begin{cases}
\ZZ,&i=0,3,\\
\ZZ/2,&i=1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

These are the standard cellular homology groups of real projective spaces.

:::

:::

::: pf-step

The Künneth theorem gives
$$
\boxed{H_n(\mathbb{RP}^2\times\mathbb{RP}^3;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
(\ZZ/2)^2,&n=1,\\
\ZZ/2,&n=2,\\
\ZZ\oplus\ZZ/2,&n=3,\\
\ZZ/2,&n=4,\\
0,&n\ge5.
\end{cases}}
$$

::: pf-proof

The tensor terms give
$$
\begin{array}{c|ccccc}
n&0&1&2&3&4\\ \hline
\bigoplus_{i+j=n}H_i(\mathbb{RP}^2)\otimes H_j(\mathbb{RP}^3)
&\ZZ&(\ZZ/2)^2&\ZZ/2&\ZZ&\ZZ/2.
\end{array}
$$
The only nonzero Tor contribution is
$$
\operatorname{Tor}(H_1(\mathbb{RP}^2),H_1(\mathbb{RP}^3))
\cong\operatorname{Tor}(\ZZ/2,\ZZ/2)
\cong\ZZ/2,
$$
which appears in degree $3$. The Künneth short exact sequence splits noncanonically, giving the displayed groups.

:::

:::

:::

:::
