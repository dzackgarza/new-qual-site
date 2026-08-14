---
schema: qual/card@1
id: L-CD6QT
kind: lemma
title: "JCF from Minimal and Characteristic Polynomials"
classification:
  areas:
  - algebra
  topics:
  - jordan-canonical-form
  - minimal-and-characteristic-polynomials
  - eigenvalues-and-eigenvectors
relations: []
review: draft
---

::: {.lemma title="JCF from Minimal and Characteristic Polynomials"}
Writing $\spec(A) = \theset{(\lambda_i, m_i)}$,
\[
\min_A(x) &= \prod_i (x- \lambda_i)^{\ell_i} \\
\chi_A(x) &= \prod (x- \lambda_i)^{m_i} \\
E_{\lambda_i} &= \dim(A - \lambda_i I)
\]

- The roots both polynomials are precisely the eigenvalues $\lambda_i$ of $A$.

  - $m_i$ are the *algebraic multiplicities*.

  - $\dim E_{\lambda_i}$ are the *geometric multiplicities*.

- $\ell_i \leq m_i$ by Cayley-Hamilton.

- $\ell_i$ is

  - The size of the **largest** Jordan block associated to $\lambda_i$[^why_largest_block], and

  - The "stabilizing constant".

- $m_i$, associated to the characteristic polynomial, is

  - The **sum of sizes** of all Jordan blocks associated to $\lambda_i$,

  - The number of times $\lambda_i$ appears on the diagonal of $JCF(A)$,

  - The dimension of the *generalized* eigenspace $V^{\lambda_i}$.

- $\dim E_{\lambda_i}$ is

  - The **number of Jordan blocks** associated to $\lambda_i$

  - The number of (usual) eigenvector associated to $\lambda_i$, i.e. the dimension of their span.

- $A$ is diagonalizable iff $\dim E_{\lambda_i} = m_i$ for all $i$.

- Eigenvectors for distinct Jordan blocks are linearly independent.
  This is because $(x-\lambda_i)^{\ell_i}$ annihilates a Jordan block of size $\ell_i$, along with any blocks of size $k\leq \ell_i$.
:::

[^why_largest_block]:
