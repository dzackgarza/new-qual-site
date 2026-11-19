---
schema: qual/card@1
id: T-WQHMA
kind: theorem
title: Spectral theorem for Hermitian and real symmetric matrices
slogan: 'Hermitian matrices are unitarily diagonalizable with real eigenvalues; real symmetric matrices are orthogonally diagonalizable.'
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Inner Product Spaces
  - Matrices
relations: []
review: draft
---

::: {.theorem}
1. If $A\in\Mat_n(\CC)$ is Hermitian, that is, $A^{\dagger} = A$, then $A$ is diagonalizable over $\CC$; more precisely, there is a unitary matrix $U$ such that $U^{\dagger}AU$ is diagonal with real entries.

2. If $A\in\Mat_n(\RR)$ is symmetric, that is, $A^t = A$, then $A$ is diagonalizable over $\RR$; more precisely, there is an orthogonal matrix $Q$ such that $Q^tAQ$ is diagonal.
:::

::: {.proof}
Both statements are proved by induction on $n=\dim V$, for a self-adjoint operator on a finite-dimensional inner product space.

Let $A$ be Hermitian and let $\lambda$ be an eigenvalue with unit eigenvector $v$, which exists over $\CC$. Then
$$
\lambda = \lambda\inner{v}{v} = \inner{Av}{v} = \inner{v}{Av} = \overline{\lambda},
$$
so $\lambda\in\RR$.

Let $W = \theset{v}^\perp$. For $w\in W$,
$$
\inner{v}{Aw} = \inner{Av}{w} = \lambda\inner{v}{w} = 0,
$$
so $Aw\in W$; the restriction of $A$ to $W$ is again self-adjoint, so by induction $W$ has an orthonormal basis of eigenvectors of $A$, and adjoining $v$ gives an orthonormal basis of eigenvectors for $V$.

The matrix of $A$ in that basis is diagonal, so the change of basis is unitary; for real symmetric $A$ the eigenvalues are real and the eigenvectors may be taken real, so the same induction runs over $\RR$ and the change of basis is orthogonal.
:::
