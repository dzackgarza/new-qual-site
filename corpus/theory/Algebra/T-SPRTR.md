---
schema: qual/card@1
id: T-SPRTR
kind: theorem
title: Orthogonal and unitary diagonalizability characterize symmetric and normal matrices
slogan: 'A real matrix is symmetric exactly when an orthogonal change of basis diagonalizes it; a complex matrix is normal exactly when a unitary one does.'
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Spectral Theorem
  - Inner Product Spaces
relations: []
review: draft
---

::: {.theorem}
Let $A\in\Mat_n(\RR)$.
Then $A$ is symmetric if and only if there is an orthogonal $Q$ with $Q^tAQ$ diagonal [@HK71, Theorem 18 and its Corollary].

Let $A\in\Mat_n(\CC)$.
Then $A$ is normal if and only if there is a unitary $U$ with $U^{\dagger}AU$ diagonal [@HK71, Theorem 22 and its Corollary].
:::
