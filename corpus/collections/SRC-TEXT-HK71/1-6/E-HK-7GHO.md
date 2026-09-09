---
schema: qual/card@1
id: E-HK-7GHO
kind: problem
title: Simultaneous row and column reduction to diagonal form
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
  note: Checked against Hoffman--Kunze Exercise 1.6.11.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Let A be an $m \times n$ matrix.
Show that by means of a finite number of elementary row and/or column operations one can pass from A to a matrix R which is both ‘row-reduced echelon’ and ‘column-reduced echelon,’ i.e., $R_{ij} = 0$ if $i \neq j$, $R_{ii} = 1$, $1 \leq i \leq r$, $R_{ii} = 0$ if i > r. Show that R = PAQ, where P is an invertible $m \times m$ matrix and Q is an invertible $n \times n$ matrix.
:::


::: solution
Let $r=\operatorname{rank}A$. Elementary row operations preserve rank and correspond to multiplication on the left by invertible elementary matrices; elementary column operations correspond to multiplication on the right by invertible elementary matrices.

Row-reduce $A$. After finitely many row operations, obtain a row-reduced echelon matrix with $r$ pivot columns. Using column interchanges, move those pivot columns to the first $r$ positions. The first $r$ columns are then the first $r$ standard basis vectors of $F^m$.

For every remaining column $j>r$, use column operations
\[
C_j\leftarrow C_j-\sum_{i=1}^r R_{ij}C_i.
\]
Because the first $r$ columns are standard basis columns, this clears every entry of column $j$. Thus the resulting matrix is
\[
D_r=
\begin{bmatrix}
I_r&0\\
0&0
\end{bmatrix},
\]
which is both row-reduced echelon and column-reduced echelon.

If $P$ is the product of the elementary row matrices used and $Q$ the product of the elementary column matrices used, then
\[
D_r=PAQ.
\]
Every elementary matrix is invertible, so both $P\in GL_m$ and $Q\in GL_n$ are invertible.
:::
