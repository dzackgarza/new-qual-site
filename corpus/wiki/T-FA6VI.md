---
schema: qual/card@1
id: T-FA6VI
kind: theorem
title: "Characterizations of continuous maps, Munkres 18.1"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.theorem title="Characterizations of continuous maps, Munkres 18.1"}
For $f:X\to Y$, TFAE:

- $f$ is continuous

- $A\subset X \implies f(\cl_X(A)) \subset \cl_X(f(A))$

- $B$ closed in $Y \implies f\inv(B)$ closed in $X$.

- For each $x\in X$ and each neighborhood $V \ni f(x)$, there is a neighborhood $U\ni x$ such that $f(U) \subset V$.
:::
