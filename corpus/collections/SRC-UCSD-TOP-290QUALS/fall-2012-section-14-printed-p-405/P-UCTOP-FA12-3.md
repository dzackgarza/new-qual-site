---
schema: qual/card@1
id: P-UCTOP-FA12-3
kind: problem
title: Homology and cohomology of RP^2 × Y with H_2(Y) = Z_4
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $Y$ be a space whose homology groups vanish except for $H_0(Y; \ZZ) = \ZZ$ and $H_2(Y; \ZZ) = \ZZ_4$.
Compute the homology $H_*(\RP^2 \times Y; \ZZ)$ and cohomology $H^*(\RP^2 \times Y; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step
The only nonzero integral homology groups of the factors are
$$
H_0(\RP^2)=\ZZ,\quad H_1(\RP^2)=\ZZ/2,
$$
and
$$
H_0(Y)=\ZZ,\quad H_2(Y)=\ZZ/4.
$$

::: pf-proof
These are the standard homology groups of $\RP^2$ and the groups assumed for $Y$.
:::

:::

::: {.pf-step #kunneth-homology}
The Künneth theorem gives
$$
H_n(\RP^2\times Y;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ/2,&n=1,\\
\ZZ/4,&n=2,\\
\ZZ/2,&n=3,4,\\
0,&n\ge5.
\end{cases}
$$

::: pf-proof
The tensor terms contribute $\ZZ/2$ in degree $1$, $\ZZ/4$ in degree $2$, and
$$
(\ZZ/2)\otimes(\ZZ/4)\cong\ZZ/2
$$
in degree $3$. The only nonzero Tor term is
$$
\operatorname{Tor}(\ZZ/2,\ZZ/4)\cong\ZZ/2,
$$
which appears one degree later, in degree $4$.
:::

:::

::: pf-step
The cohomological universal coefficient theorem gives
$$
H^n(\RP^2\times Y;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
0,&n=1,\\
\ZZ/2,&n=2,\\
\ZZ/4,&n=3,\\
\ZZ/2,&n=4,5,\\
0,&n\ge6.
\end{cases}
$$

::: pf-proof
For each $n$ there is a short exact sequence
$$
0\to\operatorname{Ext}(H_{n-1},\ZZ)\to H^n\to\operatorname{Hom}(H_n,\ZZ)\to0.
$$
All positive-degree homology groups in step [](#kunneth-homology){.pf-ref} are finite, so their Hom into $\ZZ$ vanishes, while
$$
\operatorname{Ext}(\ZZ/m,\ZZ)\cong\ZZ/m.
$$
Thus $H^n$ for $n\ge2$ is the torsion group $H_{n-1}$ from step [](#kunneth-homology){.pf-ref}, giving the displayed list.
:::

:::

:::

:::
