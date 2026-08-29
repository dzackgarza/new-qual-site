---
schema: qual/card@1
id: FT-BC6S2
kind: theorem
title: Characterizations of Diagonalizability of a Square Matrix $M$
prompts:
- What conditions each characterise diagonalizability of a square matrix?
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
---

::: {.theorem}
- $\min_M(x)/\FF$ splits into distinct linear factors over $\FF$ (i.e. is separable)

- There exists a basis of $\FF^n$ consisting of eigenvectors of $M$

- All elementary divisors are linear

- (Sufficient) $M$ has $n$ distinct eigenvalues

- (Sufficient) $\min_M(x)/\FF$ has $n$ distinct roots.

**Not** equivalent: "$\FF$ contains all the roots of $\min_M(x)$". That is necessary but not sufficient, since $(x-1)^2$ splits over any $\FF$ and $\begin{bmatrix} 1 & 1 \\ 0 & 1\end{bmatrix}$ is not diagonalizable.
:::
