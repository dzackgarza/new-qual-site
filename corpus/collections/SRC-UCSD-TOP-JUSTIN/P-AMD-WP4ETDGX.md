---
schema: qual/card@1
id: P-AMD-WP4ETDGX
kind: problem
title: Reduced homology of a union of $n$ sets with nested contractible intersections
  vanishes in degrees $\geq n-1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
---

::: {.problem}
Suppose $X$ is a space which can be written as a union of non-empty open sets $A_1,\dots,A_n$ so that for each $1\le k\le n$, the intersection of any $k$ of the sets is either empty or contractible. Show that $\widetilde H_i(X)=0$ for $i\ge n-1$, and give an example showing that this inequality is sharp.
:::

::: {.solution}
<1>1. For the finite open cover $\{A_1,\dots,A_n\}$ there is a Mayer--Vietoris spectral sequence
$$
E^1_{p,q}=\bigoplus_{i_0<\cdots<i_p}H_q(A_{i_0}\cap\cdots\cap A_{i_p})\Longrightarrow H_{p+q}(X).
$$
::: {.proof}
This is the standard iterated Mayer--Vietoris (Čech-to-homology) spectral sequence of a finite open cover, obtained from the double complex whose horizontal direction is the alternating Čech differential and whose vertical direction is the singular boundary.
:::

<1>2. By hypothesis every nonempty intersection is contractible, so after passing to reduced homology the spectral sequence is concentrated in row $q=0$ and identifies $\widetilde H_*(X)$ with the reduced simplicial homology of the nerve $N$ of the cover.
::: {.proof}
A nonempty contractible intersection has $H_q=0$ for $q>0$ and $H_0\cong\mathbb Z$. The horizontal $q=0$ complex is precisely the simplicial chain complex of the nerve. Empty intersections contribute no summand.
:::

<1>3. A simplicial complex on $n$ vertices has no reduced homology in degrees $i\ge n-1$.
::: {.proof}
If the full $(n-1)$-simplex is absent, the nerve has dimension at most $n-2$. If it is present, then every subset of the $n$ vertices is present and the nerve is the full simplex, hence contractible. In either case $\widetilde H_i(N)=0$ for $i\ge n-1$.
:::

<1>4. Consequently
$$
\boxed{\widetilde H_i(X)=0\quad\text{for all }i\ge n-1.}
$$
::: {.proof}
Combine <1>2 and <1>3.
:::

<1>5. The bound is sharp: there are good covers of $S^{n-2}$ by $n$ open sets whose nerve is the boundary of an $(n-1)$-simplex.
::: {.proof}
Take the standard cover obtained from sufficiently small open stars of the vertices in the barycentric subdivision of the boundary of an $(n-1)$-simplex. Every nonempty finite intersection is contractible, the total intersection of all $n$ sets is empty, and the nerve is the boundary sphere $S^{n-2}$. Thus $\widetilde H_{n-2}(X)\cong\mathbb Z\ne0$, so the vanishing threshold cannot be lowered from $n-1$ to $n-2$.
:::
:::
