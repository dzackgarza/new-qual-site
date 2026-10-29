---
schema: qual/card@1
id: D-DVLK5
kind: definition
title: Adjoint, symmetric, Hermitian, orthogonal, and unitary matrices
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Inner Product Spaces
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$.
For a matrix $A$, let $A^t$ be its transpose and $A^{\dagger}\coloneqq \bar A^t$ its conjugate transpose, and let $\inner{\cdot}{\cdot}$ be the standard inner product on $\RR^n$ or $\CC^n$.

- The \dfn{adjoint} of $A\in\Mat_{n\times n}(\CC)$ is $A^{\dagger}$; it is the unique matrix with $\inner{A\vector x}{\vector y} = \inner{\vector x}{A^{\dagger}\vector y}$ for all $\vector x,\vector y\in\CC^n$. The matrix $A$ is \dfn{self-adjoint} if $A = A^{\dagger}$.

- A matrix $A\in\Mat_{n\times n}(\RR)$ is \dfn{symmetric} if $A = A^t$, and \dfn{orthogonal} if $A^tA = AA^t = I_n$.

- A matrix $A\in\Mat_{n\times n}(\CC)$ is \dfn{Hermitian} if $A^{\dagger} = A$, and \dfn{unitary} if $A^{\dagger}A = AA^{\dagger} = I_n$.
:::
