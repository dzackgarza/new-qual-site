---
schema: qual/card@1
id: P-UDBZP
kind: problem
title: Every nondegenerate real matrix factors as $UT$ with $U$ orthogonal and $T$
  upper triangular
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Inner Product Spaces
  - Bases
relations: []
review: draft
---

::: problem
Prove that any nondegenerate matrix $X\in M_n(\RR)$ can be written as $X = UT$ where $U$ is orthogonal and $T$ is upper triangular.
:::

::: solution
Write the columns of $X$ as
\[
X=(x_1\ \cdots\ x_n).
\]
Since $X$ is nondegenerate, the vectors $x_1,\ldots,x_n$ are linearly
independent. Apply the Gram--Schmidt process to them. This produces an
orthonormal basis $u_1,\ldots,u_n$ such that for every $j$,
\[
\operatorname{span}(u_1,\ldots,u_j)
=\operatorname{span}(x_1,\ldots,x_j).
\]
Hence each $x_j$ has a unique expansion
\[
x_j=\sum_{i=1}^j t_{ij}u_i.
\]

Let $U$ be the matrix whose columns are $u_1,\ldots,u_n$, and let
$T=(t_{ij})$, where $t_{ij}=0$ for $i>j$. Then $T$ is upper triangular, and
the $j$-th column of $UT$ is exactly $x_j$. Therefore
\[
X=UT.
\]
Since the columns of $U$ form an orthonormal basis,
\[
U^{\mathsf T}U=I_n,
\]
so $U$ is orthogonal. Thus every nondegenerate real matrix admits the desired
factorization.
:::
