---
schema: qual/card@1
id: P-APAS23B
kind: problem
title: Real eigenvalues of Hermitian matrices; Courant–Fischer; Rayleigh extrema
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
solved: false
---

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

Consider a Hermitian matrix $A \in M_n$.

(a) Show that the eigenvalues of $A$ are real.

(b) Assume that the eigenvalues of $A$ are ordered so that $\lambda_n \le \lambda_{n-1} \le \cdots \le \lambda_2 \le \lambda_1$. State, but do not prove, the Courant–Fischer theorem.

(c) Prove that
\[
\lambda_n = \min_{x^H x = 1} x^H A x,
\quad\text{and}\quad
\lambda_1 = \max_{x^H x = 1} x^H A x.
\]
:::
