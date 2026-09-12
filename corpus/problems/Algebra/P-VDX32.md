---
schema: qual/card@1
id: P-VDX32
kind: problem
title: Matrix algebra
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Matrices
relations: []
review: draft
---

::: problem
What is a matrix algebra?
:::

::: solution
Let $k$ be a commutative ring, usually a field. The set
\[
M_n(k)
\]
of $n\times n$ matrices with entries in $k$ is an associative unital $k$-algebra:

- addition and scalar multiplication are entrywise;
- multiplication is matrix multiplication;
- the multiplicative identity is $I_n$.

As a $k$-module it is free of rank $n^2$, with basis given by the matrix units
\[
E_{ij},\qquad 1\le i,j\le n,
\]
where $E_{ij}$ has a single $1$ in position $(i,j)$. Their multiplication is
\[
E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell}.
\]

More generally, a **matrix algebra** over $k$ can mean a $k$-subalgebra of some $M_n(k)$, or specifically the full matrix algebra $M_n(k)$ when the context is clear.
:::
