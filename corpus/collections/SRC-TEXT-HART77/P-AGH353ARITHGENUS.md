---
schema: qual/card@1
id: P-AGH353ARITHGENUS
kind: problem
title: Arithmetic genus as a birational invariant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Arithmetic Genus
  - Euler Characteristic
  - Birational Invariants
relations: []
review: draft
---

::: problem
Let $X$ be a projective scheme of dimension $r$ over a field $k$.
We define the arithmetic genus $p_a$ of $X$ by
\[
p_a(X)=(-1)^r(\chi(\mco_X)-1).
\]
Note that it depends only on $X$, not on any projective embedding.

a. If $X$ is integral, and $k$ algebraically closed, show that $H^0(X, \mco_X) \cong k$, so that
\[
p_a(X)=\sum_{i=0}^{r-1}(-1)^i \dim_k H^{r-i}(X, \mco_X).
\]
In particular, if $X$ is a curve, we have
\[
p_a(X)=\dim_k H^1(X, \mco_X).
\]
Hint: Use (I, 3.4).

b. If $X$ is a closed subvariety of $\PP_k^r$, show that this $p_a(X)$ coincides with the one defined in (I, Ex.
7.2), which apparently depended on the projective embedding.

c. If $X$ is a nonsingular projective curve over an algebraically closed field $k$, show that $p_a(X)$ is in fact a birational invariant.
Conclude that a nonsingular plane curve of degree $d \geq 3$ is not rational.
:::
