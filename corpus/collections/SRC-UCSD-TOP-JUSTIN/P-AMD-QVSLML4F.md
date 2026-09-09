---
schema: qual/card@1
id: P-AMD-QVSLML4F
kind: problem
title: Homology of $X\times S^n$ in terms of $H_*(X)$, and of $T^n$
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
Compute $H_*(X\cross S^n)$ in terms of $H_*(X)$

1. Compute $H_*(T^n)$
:::

::: {.solution}
<1>1. For every $k$,
$$
\boxed{H_k(X\times S^n;\mathbb Z)\cong H_k(X;\mathbb Z)\oplus H_{k-n}(X;\mathbb Z),}
$$
where $H_j(X)=0$ for $j<0$.
::: {.proof}
The homology of $S^n$ is free and nonzero only in degrees $0$ and $n$, where it is $\mathbb Z$. Hence the Künneth theorem has no Tor terms and gives
$$
H_k(X\times S^n)
\cong H_k(X)\otimes H_0(S^n)
\oplus H_{k-n}(X)\otimes H_n(S^n),
$$
which is the displayed direct sum.
:::

<1>2. For the $n$-torus $T^n=(S^1)^n$,
$$
\boxed{H_k(T^n;\mathbb Z)\cong\mathbb Z^{\binom nk}}
$$
for $0\le k\le n$, and $H_k(T^n)=0$ otherwise.
::: {.proof}
Proceed by induction using $T^n=T^{n-1}\times S^1$ and <1>1:
$$
H_k(T^n)\cong H_k(T^{n-1})\oplus H_{k-1}(T^{n-1}).
$$
If the ranks are $\binom{n-1}{k}$ and $\binom{n-1}{k-1}$, Pascal's identity gives
$$
\binom{n-1}{k}+\binom{n-1}{k-1}=\binom nk.
$$
The base case $T^1=S^1$ is immediate.
:::
:::
