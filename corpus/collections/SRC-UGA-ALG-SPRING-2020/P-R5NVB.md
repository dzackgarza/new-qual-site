---
schema: qual/card@1
id: P-R5NVB
kind: problem
title: Jordan form, conjugating matrix, and minimal polynomial of $\begin{pmatrix}2&0&0\\4&6&1\\-16&-16&-2\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let
\[
A=\left[\begin{array}{ccc}
2 & 0 & 0 \\
4 & 6 & 1 \\
-16 & -16 & -2
\end{array}\right] \in M_{3}(\mathrm{C})
.\]

a.
Find the Jordan canonical form $J$ of $A$.

b.
Find an invertible matrix $P$ such that $P\inv A P = J$. 

c.
Write down the minimal polynomial of $A$.

> You should not need to compute $P\inv$.
:::

::: {.solution}
The characteristic polynomial is
\[
\chi_A(x)=(x-2)^3.
\]
Moreover
\[
A-2I=
\begin{bmatrix}
0&0&0\\
4&4&1\\
-16&-16&-4
\end{bmatrix}
\neq0,
\qquad
(A-2I)^2=0.
\]
Thus the minimal polynomial is
\[
m_A(x)=(x-2)^2.
\]
Consequently the Jordan form has one block of size $2$ and one block of size $1$:
\[
J=
\begin{bmatrix}
2&1&0\\
0&2&0\\
0&0&2
\end{bmatrix}.
\]

One suitable change-of-basis matrix is
\[
P=
\begin{bmatrix}
0&1&-1\\
4&0&1\\
-16&0&0
\end{bmatrix}.
\]
Its determinant is $-16\ne0$, and direct multiplication gives
\[
AP=PJ,
\]
so $P^{-1}AP=J$.
:::
