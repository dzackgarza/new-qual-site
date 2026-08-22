---
schema: qual/card@1
id: P-APAF22C
kind: problem
title: Approximate rank-nullity for a nearly vanishing unit vector
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Norms
relations: []
review: draft
solved: false
---

::: problem
Let $V$ and $W$ be two finite-dimensional real inner product spaces, $\dim V = \dim W = n$, and let $\phi \colon V \to W$ be a linear map.

Suppose there exists a vector $v_0 \in V$, $\|v_0\| = 1$, such that $\|\phi(v_0)\| \leq 10^{-10}$.

Prove the following “approximate rank–nullity” statement: there exists a subspace $W' \subseteq W$ with $\dim W' \leq n - 1$, with the property that
\[
\forall v \in V,\ \|v\| \leq 1:\ \exists w \in W':\ \|\phi(v) - w\| \leq 10^{-10}.
\]

[Hint: you can use the singular value decomposition, or argue directly.]
:::
