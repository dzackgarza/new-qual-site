---
schema: qual/card@1
id: E-HK-J2K6
kind: problem
title: Row-reduction and factorization over $\CC$
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
  note: Checked against Hoffman--Kunze Exercise 1.6.2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Do Exercise 1, but with

$$
A = \left[ \begin{array}{c c c} 2 & 0 & i \\ 1 & - 3 & - i \\ i & 1 & 1 \end{array} \right].
$$
:::


::: solution
The matrix is invertible, so its reduced row echelon form is $R=I_3$. One may take $P=A^{-1}$, namely
\[
P=
\begin{bmatrix}
\frac13&\frac1{30}-\frac{i}{10}&\frac1{10}-\frac{3i}{10}\\
0&-\frac3{10}-\frac{i}{10}&\frac1{10}-\frac{3i}{10}\\
-\frac{i}{3}&\frac15+\frac{i}{15}&\frac35+\frac{i}{5}
\end{bmatrix}.
\]
Direct multiplication gives $PA=I_3$, hence $R=PA$. Since $P$ has inverse $A$, it is invertible as required.
:::
