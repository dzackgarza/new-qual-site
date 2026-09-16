---
schema: qual/card@1
id: FT-BC6S2
kind: theorem
title: Characterizations of diagonalizability
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
Let $F$ be a field and let $M\in\Mat_n(F)$.
The following are equivalent:

1. $M$ is [[FD-K6FVX|diagonalizable]] over $F$.

2. The [[D-GK5SF|minimal polynomial]] $\min_M(x)$ is a product of distinct monic linear factors in $F[x]$.

3. There is a basis of $F^n$ consisting of eigenvectors of $M$.

4. Every elementary divisor of $M$ has degree $1$.

In particular, if $M$ has $n$ distinct eigenvalues in $F$, equivalently if $\min_M(x)$ has $n$ distinct roots in $F$, then $M$ is diagonalizable over $F$.
:::

::: {.example}
A minimal polynomial that splits over $F$ with a repeated root does not satisfy condition 2.
For $M=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ over any field $F$, $\min_M(x)=(x-1)^2$ splits over $F$, and $M$ is not diagonalizable, because its only eigenvalue is $1$ and $M\ne I$.
:::
