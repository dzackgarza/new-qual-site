---
schema: qual/card@1
id: P-PRACT20-W4-25
kind: problem
title: Maximum number of ones in an invertible $0$--$1$ matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Determinants
relations: []
review: draft
---

::: {.problem}
Consider an $n \times n$ matrix in which each entry is either zero or one.
If the matrix is invertible, what is the maximum amount of ones in the matrix?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

An invertible $0$--$1$ matrix has at most $n^2-n+1$ entries equal to $1$.

::: pf-proof

Suppose the matrix had more than $n^2-n+1$ ones. Then it would contain fewer than $n-1$ zeros.

A column fails to be the all-ones column only if it contains at least one zero. With fewer than $n-1$ zeros, at most $n-2$ columns can contain a zero. Hence at least two columns are both equal to
$$
\begin{pmatrix}1\\ \vdots\\1\end{pmatrix}.
$$
Those two columns are equal, so the matrix is singular. Therefore an invertible matrix can contain at most $n^2-n+1$ ones.

:::

:::

::: {.pf-step #s2}

The upper bound $n^2-n+1$ is attained.

::: pf-proof

Let $A=(a_{ij})$ be the $n\times n$ matrix with
$$
a_{ij}=
\begin{cases}
0,&i=j+1,\\
1,&\text{otherwise}.
\end{cases}
$$
Thus the only zeros are the $n-1$ entries immediately below the diagonal, so $A$ has
$$
n^2-(n-1)=n^2-n+1
$$
ones.

To prove invertibility, suppose $Ax=0$ for $x=(x_1,\dots,x_n)^T$. The first row gives
$$
x_1+\cdots+x_n=0.
$$
For each $i=2,\dots,n$, the $i$th row gives the same sum with $x_{i-1}$ omitted. Subtracting that equation from the first-row equation yields
$$
x_{i-1}=0.
$$
Hence $x_1=\cdots=x_{n-1}=0$, and the first-row equation then gives $x_n=0$. Thus $\ker A=0$, so $A$ is invertible.

:::

:::

::: {.pf-step #s3}

The maximum number of ones is
$$
\boxed{n^2-n+1}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the upper bound and step [](#s2){.pf-ref} gives an invertible matrix attaining it.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the requested maximum.

:::

:::

:::
