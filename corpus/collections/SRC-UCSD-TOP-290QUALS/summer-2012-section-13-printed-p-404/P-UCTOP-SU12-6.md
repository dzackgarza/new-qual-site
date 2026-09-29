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

::: {.problem}
Show that there exists a degree 1 map from $T^3 = S^1 \times S^1 \times S^1$ to $S^3$, but not vice versa.
:::

::: {.solution}

::: pf

::: {.pf-step #collapse-complement}
Choose an embedded closed $3$-ball $B^3\subset T^3$ and collapse its complement to a point:
$$
q:T^3\longrightarrow T^3/(T^3\setminus\operatorname{int}B^3).
$$

::: pf-proof
The quotient is well-defined because the complement is closed.
:::

:::

::: {.pf-step #quotient-is-s3}
The quotient space is homeomorphic to $S^3$.

::: pf-proof
After collapsing the complement, the boundary $\partial B^3$ is collapsed to the same point, so the quotient is
$$
B^3/\partial B^3\cong S^3.
$$
:::

:::

::: {.pf-step #quotient-degree-one}
With compatible orientations, the quotient map has degree $+1$.

::: pf-proof
A regular value in the interior of the image of $B^3$ has exactly one preimage, lying in $\operatorname{int}B^3$, and the quotient map is locally orientation-preserving there. Hence its local degree, and therefore its global degree, is $+1$.
:::

:::

::: {.pf-step #lifts-to-universal-cover}
Conversely, every map $f:S^3\to T^3$ lifts to the universal cover $\mathbb R^3\to T^3$.

::: pf-proof
Since $S^3$ is simply connected, the covering-space lifting criterion applies to every map $f$.
:::

:::

::: {.pf-step #every-map-degree-zero}
Every such map has degree $0$.

::: pf-proof
Write $f=p\circ\widetilde f$ with $\widetilde f:S^3\to\mathbb R^3$. Since $H_3(\mathbb R^3;\mathbb Z)=0$, the induced map
$$
\widetilde f_*:H_3(S^3)\to H_3(\mathbb R^3)
$$
is zero, hence so is $f_*=p_*\widetilde f_*$. Therefore $\deg f=0$.
:::

:::

::: pf-step
Thus there is a degree-$1$ map $T^3\to S^3$, but no degree-$1$ map $S^3\to T^3$.

::: pf-proof
Combine steps [](#collapse-complement){.pf-ref}, [](#quotient-is-s3){.pf-ref}, [](#quotient-degree-one){.pf-ref}, [](#lifts-to-universal-cover){.pf-ref} and [](#every-map-degree-zero){.pf-ref}.
:::

:::

:::

:::
