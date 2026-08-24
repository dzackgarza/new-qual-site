---
schema: qual/card@1
id: P-APA24C
kind: problem
title: Eigenvalue interlacing for a Hermitian matrix plus a rank-$2$ update
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
---

::: problem
Let $A, C \in M_n(\mathbb{C}) = \mathbb{C}^{n \times n}$ be Hermitian and suppose the following:

- The $n$ eigenvalues of $A$ are notated and ordered as follows:
  \[
  \lambda_1(A) \geq \lambda_2(A) \geq \cdots \geq \lambda_n(A);
  \]

- The $n$ eigenvalues of $C$ are notated and ordered as follows:
  \[
  \lambda_1(C) \geq \lambda_2(C) \geq \cdots \geq \lambda_n(C);
  \]

- We have $C = A + B B^H$ for some rank $2$ matrix $B \in M_{n,m}(\mathbb{C}) = \mathbb{C}^{n \times m}$ with $m \geq 2$.
  Note: $B^H = \overline{B}^T$.

Prove, for all $1 \leq k \leq n - 2$, that
\[
\lambda_{k+2}(C) \leq \lambda_k(A).
\]
:::
