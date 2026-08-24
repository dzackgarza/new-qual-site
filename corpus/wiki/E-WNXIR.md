---
schema: qual/card@1
id: E-WNXIR
kind: exercise
title: Holomorphic functions have discrete zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Identity Theorem
  - Power Series
relations: []
review: draft
---

:::{.exercise title="Holomorphic functions have discrete zeros"}
If $f$ is holomorphic on $\Omega$ and not identically zero, then $f\inv(0) \intersect \Omega$ is discrete.

:::

:::{.solution}
It suffices to show that if $f(a) = 0$ then $f$ is nonzero on some $\DD_\eps^*(a)$.
Without loss of generality, suppose $a=0$ and expand $f(z) = \sum_{k\geq 0}c_k z^k = \sum_{k\geq m}c_k z^k$ where $m\geq 0$ is minimal such that $c_m\neq 0$.
This exists since $f$ is not identically zero, by uniqueness of power series.
Then write
\[
f(z) = \sum_{k\geq m} c_k z^k = z^m \sum_{k\geq m} c_k z^{k-m} = z^m (c_m + c_{m+1}z + \cdots) \da z^m g(z)
,\]
where $g(a) = c_m \neq 0$.
Being nonzero is an open condition, so $g$ is nonzero in some punctured neighborhood of $a$, making $f$ nonzero there.
:::
