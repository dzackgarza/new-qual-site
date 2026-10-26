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

::: pf

::: {.pf-step #s1-1}

Consider the diagonal matrix
$$
A=
\begin{pmatrix}
2&0&0\\
0&2&0\\
0&0&1/4
\end{pmatrix}.
$$
Then $A$ satisfies all hypotheses of the problem.


::: pf-proof

The matrix is real and diagonal, hence
$$
A^t=A.
$$
Its diagonal entries are all nonzero, so it is invertible. Moreover,
$$
\det A
=2\cdot2\cdot\frac14
=1.
$$
Thus every stated hypothesis is satisfied.

:::

:::

::: {.pf-step #s1-2}

The matrix $A$ does not have $1$ as an eigenvalue.


::: pf-proof

For a diagonal matrix, the eigenvalues are its diagonal entries. Hence the eigenvalues of $A$ are
$$
2,
\qquad
2,
\qquad
\frac14.
$$
None is equal to $1$.

:::

:::

::: {.pf-step #s1-3}

Therefore the assertion in the problem is false as printed.


::: pf-proof

Step [](#s1-1){.pf-ref} gives a matrix satisfying all hypotheses, while step [](#s1-2){.pf-ref} shows that it fails the claimed conclusion. This is a counterexample.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} completely resolves the printed claim by disproving it.

:::

:::
