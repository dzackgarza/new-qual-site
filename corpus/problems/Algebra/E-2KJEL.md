---
schema: qual/card@1
id: E-2KJEL
kind: problem
title: "The Jordan canonical form of a matrix"
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Determine $\operatorname{JCF}(B)$ for
\[
B :=
\begin{pmatrix}
5 & -1 & 0 & 0 \\
9 & -1 & 0 & 0 \\
0 & 0 & 7 & -2 \\
0 & 0 & 12 & -3
\end{pmatrix}
.\]

:::

::: {.solution}
Write
\[
B=B_1\oplus B_2,
\qquad
B_1=\begin{pmatrix}5&-1\\9&-1\end{pmatrix},
\quad
B_2=\begin{pmatrix}7&-2\\12&-3\end{pmatrix}.
\]

For $B_1$,
\[
\chi_{B_1}(t)=(t-5)(t+1)+9=(t-2)^2.
\]
Moreover
\[
B_1-2I=\begin{pmatrix}3&-1\\9&-3\end{pmatrix}
\]
has rank $1$, so the eigenspace for $2$ is one-dimensional. Hence $B_1$ contributes one Jordan block $J_2(2)$.

For $B_2$,
\[
\chi_{B_2}(t)=(t-7)(t+3)+24=t^2-4t+3=(t-1)(t-3),
\]
so $B_2$ has two distinct eigenvalues and is diagonalizable.

Therefore, up to ordering of Jordan blocks,
\[
\boxed{
\operatorname{JCF}(B)=
\begin{pmatrix}
2&1&0&0\\
0&2&0&0\\
0&0&1&0\\
0&0&0&3
\end{pmatrix}.}
\]
:::
