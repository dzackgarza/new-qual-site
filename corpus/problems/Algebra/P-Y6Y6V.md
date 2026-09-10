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

::: problem
Does diagonalizable imply invertible? Does invertible imply diagonalizable?
:::

::: solution
Neither implication holds.

A diagonalizable matrix need not be invertible. For example,
\[
A=\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]
is already diagonal, but
\[
\det A=0,
\]
so it is not invertible.

An invertible matrix need not be diagonalizable. For example,
\[
B=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]
has determinant $1$, so it is invertible. But its only eigenvalue is $1$, and
\[
\ker(B-I)
\]
is one-dimensional, so $B$ does not have a basis of eigenvectors and is not diagonalizable.
:::
