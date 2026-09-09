---
schema: qual/card@1
id: P-KDJFP
kind: problem
title: Existence and uniqueness of $AX=b$ by rank
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Linear Algebra
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $A\in M_{m\times n}(F)$ and $b\in F^m$. Let $[A\mid b]$ be the augmented matrix.

1. Show that $Ax=b$ has a solution if and only if
   \[
   \operatorname{rank}A=\operatorname{rank}[A\mid b].
   \]
2. Assuming the system is consistent, show that the solution is unique if and only if
   \[
   \operatorname{rank}A=n.
   \]
:::

::: {.solution}
<1>1. The system is consistent iff $b$ lies in the column space of $A$.
::: {.proof}
Writing the columns of $A$ as $a_1,\ldots,a_n$, the equation
\[
Ax=b
\]
means exactly that
\[
b=x_1a_1+\cdots+x_na_n.
\]
Thus a solution exists iff $b\in\operatorname{col}(A)$. This is equivalent to adjoining $b$ as an extra column without increasing the column-space dimension, namely
\[
\operatorname{rank}[A\mid b]=\operatorname{rank}A.
\]
:::

<1>2. A consistent system has a unique solution iff $\ker A=0$.
::: {.proof}
Fix one solution $x_0$. Then every solution is of the form
\[
x_0+v,
\qquad v\in\ker A,
\]
because
\[
A(x_0+v)=b
\iff Av=0.
\]
Hence the solution is unique iff $\ker A=0$. By rank-nullity,
\[
n=\operatorname{rank}A+\dim\ker A,
\]
so $\ker A=0$ iff $\operatorname{rank}A=n$.
:::
:::
