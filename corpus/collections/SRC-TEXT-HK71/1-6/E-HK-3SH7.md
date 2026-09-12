---
schema: qual/card@1
id: E-HK-3SH7
kind: problem
title: Row-reduction and invertible matrix factorization $R = PA$
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
  note: Checked against Hoffman--Kunze Exercise 1.6.1.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{r r r r} 1 & 2 & 1 & 0 \\ - 1 & 0 & 3 & 5 \\ 1 & - 2 & 1 & 1 \end{array} \right].
$$

Find a row-reduced echelon matrix R which is row-equivalent to A and an invertible $3 \times 3$ matrix P such that R = PA.
:::


::: solution
A row-reduced echelon form of $A$ is
\[
R=
\begin{bmatrix}
1&0&0&-\frac78\\
0&1&0&-\frac14\\
0&0&1&\frac{11}{8}
\end{bmatrix}.
\]
Take
\[
P=
\begin{bmatrix}
\frac38&-\frac14&\frac38\\
\frac14&0&-\frac14\\
\frac18&\frac14&\frac18
\end{bmatrix}.
\]
Direct multiplication gives
\[
PA=
\begin{bmatrix}
1&0&0&-\frac78\\
0&1&0&-\frac14\\
0&0&1&\frac{11}{8}
\end{bmatrix}=R.
\]
Moreover
\[
\det P=\frac1{16}\ne0,
\]
so $P$ is invertible. Hence $R=PA$ with the required properties.
:::
