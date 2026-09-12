---
schema: qual/card@1
id: P-4GMLL
kind: problem
title: Jordan form of $\begin{pmatrix}-3&3&-2\\-7&6&-3\\1&-1&2\end{pmatrix}$ and a
  conjugating matrix
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let
\[
A=\left(\begin{array}{ccc}
-3 & 3 & -2 \\
-7 & 6 & -3 \\
1 & -1 & 2
\end{array}\right) \in M_{3}(\mathrm{C})
.\]

a.
Find the Jordan canonical form $J$ of $A$.

b.
Find an invertible matrix $P$ such that $P\inv A P = J$.
You do not need to compute $P\inv$.
:::

::: solution
The characteristic polynomial is
\[
\chi_A(x)=(x-1)(x-2)^2.
\]
For the eigenvalue $2$, the eigenspace is one-dimensional, so there is a single Jordan block of size $2$. Thus
\[
J=\begin{bmatrix}
1&0&0\\
0&2&1\\
0&0&2
\end{bmatrix}.
\]

Take
\[
P=\begin{bmatrix}
1&\tfrac12&\tfrac12\\
2&\tfrac12&1\\
1&-\tfrac12&0
\end{bmatrix}.
\]
Its determinant is $1/4$, so $P$ is invertible. Its first column is an eigenvector for eigenvalue $1$; if $v_2,v_3$ are the second and third columns, then
\[
(A-2I)v_2=0,
\qquad
(A-2I)v_3=v_2.
\]
Therefore the columns of $P$ form a Jordan basis and
\[
P^{-1}AP=J.
\]
:::
