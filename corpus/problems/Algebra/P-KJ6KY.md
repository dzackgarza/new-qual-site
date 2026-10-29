---
schema: qual/card@1
id: P-KJ6KY
kind: problem
title: Centralizer of a Jordan block
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $J=J_n(\lambda)$ be a single $n\times n$ Jordan block over a field $F$. Determine all matrices $X\in M_n(F)$ satisfying
$$
XJ=JX.
$$
:::

::: {.solution}
Write $J=\lambda I+N$, where $N=J_n(0)$ is the nilpotent Jordan block with $1$s on the superdiagonal, and write $X=(x_{ij})$.

::: pf

::: {.pf-step #reduce}
$XJ=JX$ if and only if $XN=NX$.

::: pf-proof
The scalar matrix $\lambda I$ commutes with every matrix.
:::

:::

::: {.pf-step #toeplitz}
$XN=NX$ if and only if $X$ is upper triangular and constant along each superdiagonal.

::: pf-proof
The $(i,j)$ entry of $XN$ is $x_{i,j-1}$ for $j\ge2$ and $0$ for $j=1$; the $(i,j)$ entry of $NX$ is $x_{i+1,j}$ for $i\le n-1$ and $0$ for $i=n$. Equality of first columns gives $x_{i+1,1}=0$ for $i\le n-1$, equality of last rows gives $x_{n,j-1}=0$ for $j\ge2$, and the remaining entries give $x_{i,j-1}=x_{i+1,j}$. Together these say that every entry below the diagonal vanishes and $x_{ij}$ depends only on $j-i$.
:::

:::

::: pf-step
The matrices commuting with $J$ are exactly
$$
\boxed{a_0I+a_1N+\cdots+a_{n-1}N^{n-1}=f(J),\qquad f\in F[x],\ \deg f<n,}
$$
so the centralizer of $J$ in $M_n(F)$ is $F[J]$, an $n$-dimensional commutative $F$-algebra.

::: pf-proof
By steps [](#reduce){.pf-ref} and [](#toeplitz){.pf-ref}, $X$ commutes with $J$ if and only if
$$
X=
\begin{pmatrix}
a_0&a_1&a_2&\cdots&a_{n-1}\\
0&a_0&a_1&\cdots&a_{n-2}\\
0&0&a_0&\cdots&a_{n-3}\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
0&0&\cdots&0&a_0
\end{pmatrix},
$$
and $N^k$ is the matrix with $1$s on the $k$-th superdiagonal. Polynomials in $N$ are polynomials in $J=\lambda I+N$ and conversely, and $I,N,\ldots,N^{n-1}$ are linearly independent.
:::

:::

:::

:::
