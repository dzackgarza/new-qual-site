---
schema: qual/card@1
id: P-UCTOP-SU12-6
kind: problem
title: Degree 1 map from T^3 to S^3 but not vice versa
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
---

Show that there exists a degree 1 map from $T^3 = S^1 \times S^1 \times S^1$ to $S^3$, but not vice versa.

::: {.solution}
<1>1. Choose an embedded closed $3$-ball $B^3\subset T^3$ and collapse its complement to a point:
$$
q:T^3\longrightarrow T^3/(T^3\setminus\operatorname{int}B^3).
$$
::: {.proof}
The quotient is well-defined because the complement is closed.
:::

<1>2. The quotient space is homeomorphic to $S^3$.
::: {.proof}
After collapsing the complement, the boundary $\partial B^3$ is collapsed to the same point, so the quotient is
$$
B^3/\partial B^3\cong S^3.
$$
:::

<1>3. With compatible orientations, the quotient map has degree $+1$.
::: {.proof}
A regular value in the interior of the image of $B^3$ has exactly one preimage, lying in $\operatorname{int}B^3$, and the quotient map is locally orientation-preserving there. Hence its local degree, and therefore its global degree, is $+1$.
:::

<1>4. Conversely, every map $f:S^3\to T^3$ lifts to the universal cover $\mathbb R^3\to T^3$.
::: {.proof}
Since $S^3$ is simply connected, the covering-space lifting criterion applies to every map $f$.
:::

<1>5. Every such map has degree $0$.
::: {.proof}
Write $f=p\circ\widetilde f$ with $\widetilde f:S^3\to\mathbb R^3$. Since $H_3(\mathbb R^3;\mathbb Z)=0$, the induced map
$$
\widetilde f_*:H_3(S^3)\to H_3(\mathbb R^3)
$$
is zero, hence so is $f_*=p_*\widetilde f_*$. Therefore $\deg f=0$.
:::

<1>6. Thus there is a degree-$1$ map $T^3\to S^3$, but no degree-$1$ map $S^3\to T^3$.
::: {.proof}
Combine <1>1--<1>5.
:::
:::
