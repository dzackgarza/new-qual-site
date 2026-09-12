---
schema: qual/card@1
id: E-HK-2OUI
kind: problem
title: Invertibility and the kernel of a matrix
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
  note: Checked against Hoffman--Kunze Exercise 1.6.7.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Let $A$ be an $n \times n$ (square) matrix.
Prove the following two statements:

(a) If $A$ is invertible and $AB = 0$ for some $n \times n$ matrix $B$, then $B = 0$ .

(b) If $A$ is not invertible, then there exists an $n \times n$ matrix $B$ such that $AB = 0$ but $B \neq 0$ .
:::


::: solution
<1>1. If $A$ is invertible and $AB=0$, then $B=0$.
::: proof
Multiply on the left by $A^{-1}$:
\[
B=A^{-1}AB=A^{-1}0=0.
\]
:::

<1>2. If $A$ is not invertible, there is a nonzero matrix $B$ with $AB=0$.
::: proof
Since $A$ is singular, its nullspace contains some nonzero column vector $v$ with $Av=0$. Let $B$ be the matrix whose first column is $v$ and whose remaining columns are zero. Then $B\ne0$, while every column of $AB$ is zero; hence $AB=0$.
:::
:::
