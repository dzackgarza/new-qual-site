---
schema: qual/card@1
id: P-SGXRZ
kind: problem
title: Normal subgroups
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Homomorphisms
  - Geometry
relations: []
review: draft
---

::: problem
What is a normal subgroup? What natural map does it determine? How does this relate to covering spaces?
:::

::: solution
A subgroup $N\le G$ is **normal**, written $N\normal G$, if
\[
gNg^{-1}=N\qquad\text{for every }g\in G.
\]
Equivalently, the left and right cosets of $N$ coincide.

Normality is exactly the condition that makes the quotient set $G/N$ into a group. The natural quotient homomorphism is
\[
\pi:G\twoheadrightarrow G/N,
\qquad g\longmapsto gN,
\]
and
\[
\ker\pi=N.
\]
Conversely, kernels of group homomorphisms are normal, so normal subgroups are precisely kernels.

There is also a covering-space interpretation. Let $X$ be path connected, locally path connected, and semilocally simply connected, and identify
\[
G=\pi_1(X,x_0).
\]
Subgroups $H\le G$ correspond to connected covering spaces of $X$ up to equivalence. The covering corresponding to $H$ is regular (Galois) exactly when $H\normal G$. In that case its deck transformation group is naturally
\[
G/H.
\]
Thus the algebraic triple
\[
H\normal G\twoheadrightarrow G/H
\]
models the fundamental group of the covering, the fundamental group of the base, and the deck group of a regular covering.
:::
