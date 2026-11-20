---
schema: qual/card@1
id: T-GELFND
kind: theorem
title: Gelfand's formula for the spectral radius
slogan: '$\rho(A)=\lim_k\norm{A^k}^{1/k}$'
classification:
  areas:
  - algebra
  topics:
  - Spectral Radius
  - Matrix Norms
relations: []
review: draft
---

::: {.theorem}
Let $A\in M_n(\CC)$ with spectral radius $\rho(A)$, and let $\norm{\cdot}$ be a norm on $M_n(\CC)$.
Then
$$
\rho(A) = \lim_{k\to\infty}\norm{A^k}^{1/k},
$$
and if the norm is submultiplicative then also $\rho(A) = \inf_{k\geq1}\norm{A^k}^{1/k}$ and $\rho(A)\leq\norm A$.

The submultiplicative clauses are Rudin, *Functional Analysis*, Theorem 10.13(b); the limit for an arbitrary norm on the finite-dimensional space $M_n(\CC)$ follows from the equivalence of norms.
:::
