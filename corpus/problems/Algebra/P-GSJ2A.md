---
schema: qual/card@1
id: P-GSJ2A
kind: problem
title: Eigenvalues of a symmetric matrix
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Matrices
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}

What can you say about the eigenvalues of a real symmetric matrix?

:::

::: {.solution}

Let $A\in M_n(\RR)$ satisfy $A^t=A$, and let $\inner{v}{w}=\sum_k v_k\overline{w_k}$ be the standard Hermitian inner product on $\CC^n$.

::: pf

::: pf-step

Every eigenvalue of $A$ is real.

::: pf-proof

Let $Av=\lambda v$ with $\lambda\in\CC$ and $0\ne v\in\CC^n$. Since $A$ is real and symmetric, $\inner{Av}{v}=\inner{v}{Av}$, so
$$
\lambda\inner{v}{v}
=\inner{Av}{v}
=\inner{v}{Av}
=\overline\lambda\inner{v}{v}.
$$
Since $\inner{v}{v}>0$, $\lambda=\overline\lambda$.

:::

:::

::: pf-step

There are an orthogonal matrix $Q$ and real numbers $\lambda_1,\ldots,\lambda_n$ such that
$$
Q^tAQ=\diag(\lambda_1,\ldots,\lambda_n).
$$
In particular, $A$ is diagonalizable over $\RR$, $\RR^n$ has an orthonormal basis of eigenvectors of $A$, and eigenspaces belonging to distinct eigenvalues are orthogonal.

::: pf-proof

This is the real spectral theorem.

:::

:::

:::

:::
