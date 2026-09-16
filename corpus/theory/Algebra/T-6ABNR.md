---
schema: qual/card@1
id: T-6ABNR
kind: theorem
title: Diagonalizability via the minimal polynomial
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.theorem}
Let $F$ be a field and $M\in M_n(F)$ with [[D-GK5SF|minimal polynomial]] $m_M\in F[x]$.
Then $M$ is [[FD-K6FVX|diagonalizable]] over $F$ if and only if $m_M$ splits over $F$ into distinct linear factors.
:::

::: {.proof}
If $M=PDP^{-1}$ with $D$ diagonal whose distinct diagonal entries are $\lambda_1,\ldots,\lambda_r$, then $\prod_i(x-\lambda_i)$ annihilates $D$ and hence $M$, so $m_M$ divides a product of distinct linear factors.

Conversely, suppose $m_M=\prod_{i=1}^r(x-\lambda_i)$ with the $\lambda_i\in F$ distinct.
The factors are pairwise coprime, so by the kernel decomposition $F^n=\ker m_M(M)=\bigoplus_{i=1}^r\ker(M-\lambda_i I)$.
Choosing a basis of each eigenspace $\ker(M-\lambda_i I)$ gives a basis of $F^n$ of eigenvectors of $M$.
:::

::: {.example}
A minimal polynomial that splits with a repeated factor does not suffice.
Over any field $F$, $M=\begin{bmatrix} 1 & 1 \\ 0 & 1\end{bmatrix}$ has $m_M = (x-1)^2$, which splits over $F$, but $\ker(M-I)$ is one-dimensional, so $M$ is not diagonalizable.
:::
