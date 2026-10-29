---
schema: qual/card@1
id: P-Y6Y6V
kind: problem
title: Neither diagonalizable nor invertible implies the other
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Matrices
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Does diagonalizable imply invertible? Does invertible imply diagonalizable?
:::

::: {.solution}

::: pf

::: pf-step
A diagonalizable matrix need not be invertible.

::: pf-proof
$A=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ is diagonal, and $\det A=0$.
:::

:::

::: pf-step
An invertible matrix need not be diagonalizable.

::: pf-proof
$B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has $\det B=1$.
Its only eigenvalue is $1$, and $\ker(B-I)$ is one-dimensional, so $B$ has no basis of eigenvectors.
:::

:::

::: pf-qed
$\boxed{\text{Neither implication holds.}}$
:::

:::

:::
