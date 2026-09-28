---
schema: qual/card@1
id: P-AGH412POLESATFINITESET
kind: problem
title: A rational function with poles at a prescribed finite set of points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Linear Systems
  - Divisors
relations: []
review: draft
---

::: {.problem}
Again let $X$ be a curve, and let $P_1, \ldots, P_r \in X$ be points. Then there is a rational function $f \in K(X)$ having poles (of some order) at each of the $P_i$, and regular elsewhere.
:::

::: {.solution}
Let $D= P_1 + \cdots + P_r$, we then want $f\in \globsec{X; \mcl(nD)}$ for $n\gg 0$. By RR,
$$
\chi(\mcl(nD)) = \deg D + 1-g \implies h^0(\mcl(nD)) = rn + 1 - g
,$$
which is non-negative for $n\gg 0$.
:::
