---
schema: qual/card@1
id: P-F06DT
kind: problem
title: Determinant of a $4\times 4$ integer matrix
classification:
  areas:
  - prelim
  topics:
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Compute the determinant of the matrix $$B = \begin{bmatrix} 1 & 0 & -1 & 2 \\ 3 & 1 & 0 & 1 \\ 4 & -1 & 1 & 1 \\ -1 & 2 & 1 & 2 \end{bmatrix}.$$
:::

::: solution
Expand along the first row:
\[
\det B
=\det\begin{bmatrix}1&0&1\\-1&1&1\\2&1&2\end{bmatrix}
-\det\begin{bmatrix}3&1&1\\4&-1&1\\-1&2&2\end{bmatrix}
-2\det\begin{bmatrix}3&1&0\\4&-1&1\\-1&2&1\end{bmatrix}.
\]
The three $3\times3$ determinants are respectively
\[
-1,\qquad -21,\qquad -10.
\]
Therefore
\[
\det B=-1-(-21)-2(-10)=40.
\]
:::
