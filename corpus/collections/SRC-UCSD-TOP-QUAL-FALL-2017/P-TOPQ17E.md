---
schema: qual/card@1
id: P-TOPQ17E
kind: problem
title: "Degree 1 map from T^3 to S^3 exists but not vice versa"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Manifolds
  - Homology
relations: []
review: draft
---

::: {.problem}
Show that there exists a degree $1$ map from $T^3 = S^1 \times S^1 \times S^1$ to $S^3$, but not vice versa.
:::

::: {.solution}
<1>1. There is a degree-$1$ map $T^3\to S^3$.
::: {.proof}
Choose an embedded closed $3$-ball $B\subset T^3$ and collapse $T^3\setminus\operatorname{int}B$ to a point. The quotient is $B/\partial B\cong S^3$, and the quotient map carries the fundamental class of $T^3$ to the fundamental class of $S^3$, hence has degree $1$ after choosing compatible orientations.
:::

<1>2. There is no degree-$1$ map $S^3\to T^3$.
::: {.proof}
If $f:M^n\to N^n$ has degree $\pm1$ between closed oriented manifolds, then $f^*:H^*(N;\mathbb Z)\to H^*(M;\mathbb Z)$ is injective: Poincaré duality pairs any nonzero class with a complementary class, and evaluation after pullback is multiplied by the degree. But $H^1(T^3;\mathbb Z)\cong\mathbb Z^3$ whereas $H^1(S^3;\mathbb Z)=0$, so such an injection is impossible.
:::
:::
