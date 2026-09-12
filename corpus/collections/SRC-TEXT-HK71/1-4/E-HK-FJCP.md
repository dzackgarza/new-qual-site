---
schema: qual/card@1
id: E-HK-FJCP
kind: problem
title: Classification of $2 \times 2$ row-reduced echelon matrices
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
  note: Checked against Hoffman--Kunze, Section 1.4, Exercise 3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Describe explicitly all $2 \times 2$ row-reduced echelon matrices.
:::

::: solution
All $2\times2$ row-reduced echelon matrices are exactly
\[
\begin{bmatrix}0&0\\0&0\end{bmatrix},
\qquad
\begin{bmatrix}1&a\\0&0\end{bmatrix}\quad(a\in F),
\qquad
\begin{bmatrix}0&1\\0&0\end{bmatrix},
\qquad
\begin{bmatrix}1&0\\0&1\end{bmatrix}.
\]

<1>1. These matrices are all row-reduced echelon matrices.
::: proof
Each has zero rows below nonzero rows, each leading nonzero entry is $1$, pivot
columns have no other nonzero entries, and successive pivots move strictly to
the right.
:::

<1>2. No other $2\times2$ row-reduced echelon matrix exists.
::: proof
Classify by rank. Rank $0$ gives the zero matrix. Rank $2$ forces pivots in both
columns and hence gives $I_2$. For rank $1$, there is one nonzero row. If its
pivot is in column $1$, the row is $(1,a)$ with arbitrary $a\in F$. If its pivot
is in column $2$, its first entry must be zero, giving $(0,1)$. These exhaust
all possibilities.
:::
:::
