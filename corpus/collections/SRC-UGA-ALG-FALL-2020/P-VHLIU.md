---
schema: qual/card@1
id: P-VHLIU
kind: problem
title: Minimal polynomial and Jordan form of $\begin{pmatrix}1&3&3\\2&2&3\\-1&-2&-2\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Consider the following matrix:
\[
B \da 
\begin{bmatrix}
1 & 3 & 3
\\
2 & 2 & 3
\\
-1 & -2 & -2
\end{bmatrix}
.\]

a. Find the minimal polynomial of $B$.

b. Find a $3\times 3$ matrix $J$ in Jordan canonical form and an invertible matrix $P$ such that $B = PJP\inv$.
:::

::: {.solution}
The characteristic polynomial is
\[
\chi_B(x)=\det(xI-B)=(x+1)(x-1)^2.
\]
By Cayley--Hamilton, the minimal polynomial divides this polynomial. Since both $1$ and $-1$ are eigenvalues, the minimal polynomial is divisible by $(x-1)(x+1)$. Moreover
\[
B^2-I=
\begin{bmatrix}
3&3&6\\
3&3&6\\
-3&-3&-6
\end{bmatrix}\ne0,
\]
so $(B-I)(B+I)\ne0$. Therefore the factor $(x-1)$ must occur with exponent $2$, and
\[
m_B(x)=(x+1)(x-1)^2.
\]

A Jordan form is
\[
J=
\begin{bmatrix}
-1&0&0\\
0&1&1\\
0&0&1
\end{bmatrix}.
\]
Take
\[
P=
\begin{bmatrix}
-3&3&1\\
1&3&1\\
1&-3&0
\end{bmatrix}.
\]
Its determinant is $-12$, so $P$ is invertible. Direct multiplication gives
\[
PJP^{-1}=
\begin{bmatrix}
1&3&3\\
2&2&3\\
-1&-2&-2
\end{bmatrix}=B.
\]
Thus $B$ is similar to the displayed Jordan matrix.
:::
