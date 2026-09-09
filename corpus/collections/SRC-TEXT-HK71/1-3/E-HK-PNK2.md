---
schema: qual/card@1
id: E-HK-PNK2
kind: problem
title: Non-row-equivalent matrices
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze, Section 1.3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Prove that the following two matrices are not row-equivalent:

$$
\left[ \begin{array}{c c c} 2 & 0 & 0 \\ a & - 1 & 0 \\ b & c & 3 \end{array} \right], \qquad \left[ \begin{array}{c c c} 1 & 1 & 2 \\ - 2 & 0 & - 1 \\ 1 & 3 & 5 \end{array} \right].
$$
:::

::: solution
Let
\[
A=\begin{bmatrix}2&0&0\\a&-1&0\\b&c&3\end{bmatrix},
\qquad
B=\begin{bmatrix}1&1&2\\-2&0&-1\\1&3&5\end{bmatrix}.
\]

<1>1. The matrix $A$ has rank $3$.
::: proof
$A$ is lower triangular and
\[
\det A=2(-1)3=-6\ne0.
\]
Hence $A$ is invertible and has rank $3$.
:::

<1>2. The matrix $B$ has rank $2$.
::: proof
Its determinant is
\[
\det B=0,
\]
so its rank is at most $2$. The minor formed by the first two rows and first two
columns is
\[
\det\begin{bmatrix}1&1\\-2&0\end{bmatrix}=2\ne0,
\]
so its rank is at least $2$.
:::

<1>3. Therefore $A$ and $B$ are not row-equivalent.
::: proof
Elementary row operations preserve rank, whereas <1>1 and <1>2 give different
ranks.
:::
:::
