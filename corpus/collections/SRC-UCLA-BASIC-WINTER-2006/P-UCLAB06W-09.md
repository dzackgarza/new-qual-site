---
schema: qual/card@1
id: P-UCLAB06W-09
kind: problem
title: Eigenvalue claim for a symmetric determinant-one matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Qual Winter 2006 PDF; the source asks for the eigenvalue $1$ conclusion exactly as stated here.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The printed assertion is false; the solution gives an explicit symmetric positive-definite determinant-one counterexample.
---

::: {.problem}
Let $A\in\mathbb M_3(\mathbb R)$ be invertible and satisfy $A=A^t$ and $\det A=1$.
Prove that $A$ has $1$ as an eigenvalue.
:::

::: {.solution}
The assertion is false as printed.
For example,
\[
A=\begin{pmatrix}
2&0&0\\
0&2&0\\
0&0&1/4
\end{pmatrix}
\]
is real, symmetric, and invertible, and
\[
\det A=2\cdot2\cdot\frac14=1.
\]
Its eigenvalues are $2,2,1/4$, so $1$ is not an eigenvalue.
:::
