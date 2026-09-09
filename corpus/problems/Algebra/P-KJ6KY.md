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

::: problem
Let $J=J_n(\lambda)$ be a single $n\times n$ Jordan block over a field $F$. Determine all matrices $X\in M_n(F)$ satisfying
\[
XJ=JX.
\]
:::

::: {.solution}
Write
\[
J=\lambda I+N,
\]
where
\[
N=J_n(0)
\]
is the nilpotent Jordan block with $1$s on the superdiagonal. Since $\lambda I$ commutes with every matrix,
\[
XJ=JX
\iff XN=NX.
\]

Let $X=(x_{ij})$. Comparing entries in $XN=NX$ gives
\[
x_{i,j-1}=x_{i+1,j}
\]
whenever both sides are defined, together with zeros below the main diagonal. Hence $X$ is upper triangular and constant along each superdiagonal:
\[
X=
\begin{pmatrix}
a_0&a_1&a_2&\cdots&a_{n-1}\\
0&a_0&a_1&\cdots&a_{n-2}\\
0&0&a_0&\cdots&a_{n-3}\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
0&0&\cdots&0&a_0
\end{pmatrix}.
\]
Such a matrix is exactly
\[
a_0I+a_1N+\cdots+a_{n-1}N^{n-1}.
\]
Therefore
\[
C_{M_n(F)}(J)
=F[J]
=\{f(J):f\in F[x],\ \deg f<n\}.
\]
In particular, the centralizer is an $n$-dimensional commutative $F$-algebra.
:::
