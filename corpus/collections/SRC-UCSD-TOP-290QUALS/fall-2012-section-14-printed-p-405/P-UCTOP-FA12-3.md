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

Let $Y$ be a space whose homology groups vanish except for $H_0(Y; \mathbb{Z}) = \mathbb{Z}$ and $H_2(Y; \mathbb{Z}) = \mathbb{Z}_4$.
Compute the homology $H_*(\mathbb{RP}^2 \times Y; \mathbb{Z})$ and cohomology $H^*(\mathbb{RP}^2 \times Y; \mathbb{Z})$.

::: {.solution}
<1>1. The only nonzero integral homology groups of the factors are
$$
H_0(\mathbb{RP}^2)=\mathbb Z,\quad H_1(\mathbb{RP}^2)=\mathbb Z/2,
$$
and
$$
H_0(Y)=\mathbb Z,\quad H_2(Y)=\mathbb Z/4.
$$
::: {.proof}
These are the standard homology groups of $\mathbb{RP}^2$ and the groups assumed for $Y$.
:::

<1>2. The Künneth theorem gives
$$
H_n(\mathbb{RP}^2\times Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z/2,&n=1,\\
\mathbb Z/4,&n=2,\\
\mathbb Z/2,&n=3,4,\\
0,&n\ge5.
\end{cases}
$$
::: {.proof}
The tensor terms contribute $\mathbb Z/2$ in degree $1$, $\mathbb Z/4$ in degree $2$, and
$$
(\mathbb Z/2)\otimes(\mathbb Z/4)\cong\mathbb Z/2
$$
in degree $3$. The only nonzero Tor term is
$$
\operatorname{Tor}(\mathbb Z/2,\mathbb Z/4)\cong\mathbb Z/2,
$$
which appears one degree later, in degree $4$.
:::

<1>3. The cohomological universal coefficient theorem gives
$$
H^n(\mathbb{RP}^2\times Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
0,&n=1,\\
\mathbb Z/2,&n=2,\\
\mathbb Z/4,&n=3,\\
\mathbb Z/2,&n=4,5,\\
0,&n\ge6.
\end{cases}
$$
::: {.proof}
For each $n$ there is a short exact sequence
$$
0\to\operatorname{Ext}(H_{n-1},\mathbb Z)\to H^n\to\operatorname{Hom}(H_n,\mathbb Z)\to0.
$$
All positive-degree homology groups in <1>2 are finite, so their Hom into $\mathbb Z$ vanishes, while
$$
\operatorname{Ext}(\mathbb Z/m,\mathbb Z)\cong\mathbb Z/m.
$$
Thus $H^n$ for $n\ge2$ is the torsion group $H_{n-1}$ from <1>2, giving the displayed list.
:::
:::
