---
schema: qual/card@1
id: FT-BC6S2
kind: theorem
title: Characterizations of diagonalizability
slogan: 'Diagonalizable means an eigenbasis, equivalently a squarefree split minimal polynomial.'
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

::: {.proof}
(1)$\Rightarrow$(2): if $M=PDP^{-1}$ with $D$ diagonal whose distinct diagonal entries are $\lambda_1,\ldots,\lambda_r$, then $\prod_i(x-\lambda_i)$ annihilates $D$ and hence $M$, so $\min_M$ divides a product of distinct linear factors.

(2)$\Rightarrow$(3): suppose $\min_M=\prod_{i=1}^r(x-\lambda_i)$ with the $\lambda_i\in F$ distinct.
The factors are pairwise coprime, so by the kernel decomposition $F^n=\ker\min_M(M)=\bigoplus_{i=1}^r\ker(M-\lambda_i I)$, and a basis of each eigenspace gives a basis of $F^n$ of eigenvectors of $M$.
:::

::: {.example}
A matrix whose minimal polynomial splits over $F$ need not be diagonalizable over $F$.
For $M=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ over any field $F$, $\min_M(x)=(x-1)^2$ splits over $F$, and $M$ is not diagonalizable, because its only eigenvalue is $1$ and $M\ne I$.
:::
