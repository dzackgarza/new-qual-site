---
schema: qual/card@1
id: E-SMI-8000E-ED5
kind: problem
title: Matrices over a Euclidean domain are diagonalizable by invertible row and column operations
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Modules
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Assume $R$ is a Euclidean domain.
Prove every $m \times n$ matrix over $R$ can be diagonalized by invertible row and column operations.

[Hint: use induction on the size of the upper left entry of the matrix instead of on the number of prime factors.]
:::

::: {.solution}
Let $N\colon R\setminus\{0\}\to\mathbb Z_{\ge0}$ be the Euclidean size function. The operations used are: interchanging two rows or two columns, and adding an $R$-multiple of one row (column) to another; each is invertible. Call two matrices equivalent if one is obtained from the other by such operations. We induct on $m+n$.

::: pf

::: {.pf-step #s1}

Every nonzero matrix $A$ is equivalent to a matrix $B$ with $b_{11}\ne0$ and $b_{1j}=b_{i1}=0$ for all $i,j>1$.

::: pf-proof

Among all matrices equivalent to $A$, all of which are nonzero, choose $B$ and a nonzero entry of $B$ of least size; after interchanging rows and columns, that entry is $b_{11}$. Suppose $b_{11}\nmid b_{1j}$ for some $j$. Division gives $b_{1j}=qb_{11}+r$ with $r\ne0$ and $N(r)<N(b_{11})$; subtracting $q$ times column $1$ from column $j$ produces an equivalent matrix with the nonzero entry $r$, contradicting the choice of $b_{11}$. Hence $b_{11}$ divides every $b_{1j}$, and by the same argument with rows, every $b_{i1}$. Subtracting $b_{1j}/b_{11}$ times column $1$ from column $j$ and $b_{i1}/b_{11}$ times row $1$ from row $i$ clears the first row and column except $b_{11}$.

:::

:::

::: {.pf-step #s2}

If every matrix with fewer than $m+n$ rows plus columns is equivalent to a diagonal matrix, so is every $m\times n$ matrix $A$.

::: pf-proof

If $A=0$, it is diagonal. Otherwise, by step [](#s1){.pf-ref}, $A$ is equivalent to $\begin{pmatrix}b_{11}&0\\0&A'\end{pmatrix}$ with $A'$ of size $(m-1)\times(n-1)$. If $m=1$ or $n=1$, this matrix is already diagonal. Otherwise, by hypothesis $A'$ is equivalent to a diagonal matrix, and each operation on the rows or columns of $A'$ is an operation on rows or columns $2,\ldots$ of the block matrix that leaves its first row and column unchanged.

:::

:::

::: pf-qed

A $1\times1$ matrix is diagonal, and step [](#s2){.pf-ref} is the induction step on $m+n$.

:::

:::

:::
