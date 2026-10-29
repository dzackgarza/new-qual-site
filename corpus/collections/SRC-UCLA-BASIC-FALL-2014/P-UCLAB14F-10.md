---
schema: qual/card@1
id: P-UCLAB14F-10
kind: problem
title: Maximum number of ones in an invertible zero-one matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 10. What is the largest number of $1$'s an invertible $0$-$1$ matrix of size $n\times n$ can have? You must show both that this number is possible and that no larger number is possible.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Any invertible $n\times n$ zero-one matrix must contain at least
$$
n-1
$$
zero entries.


::: pf-proof

Suppose a zero-one matrix contained at most
$$
n-2
$$
zeros.
There are $n$ rows.
If every row except possibly one contained at least one zero, there would be at least $n-1$ zeros.
Therefore at least two rows contain no zero entries at all.

A zero-one row containing no zeros is
$$
(1,1,\ldots,1).
$$
Thus those two rows are identical, so the matrix is singular.
Hence an invertible zero-one matrix must contain at least $n-1$ zeros.

:::

:::

::: {.pf-step #s1-2}

Consequently an invertible zero-one matrix has at most
$$
\boxed{n^2-n+1}
$$
entries equal to $1$.


::: pf-proof

An $n\times n$ matrix has $n^2$ entries.
By step [](#s1-1){.pf-ref}, at least $n-1$ of them must be zero.
Therefore the number of ones is at most
$$
n^2-(n-1)
=
n^2-n+1.
$$

:::

:::

::: {.pf-step #s1-3}

Let $M_n$ be the zero-one matrix obtained from the all-ones matrix by changing the first $n-1$ diagonal entries to zero:
$$
M_n=
\begin{pmatrix}
0&1&1&\cdots&1\\
1&0&1&\cdots&1\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
1&1&\cdots&0&1\\
1&1&\cdots&1&1
\end{pmatrix}.
$$
Then $M_n$ contains exactly
$$
n^2-n+1
$$
ones.


::: pf-proof

Exactly the first $n-1$ diagonal entries are zero.
All remaining
$$
n^2-(n-1)
$$
entries are one.

:::

:::

::: {.pf-step #s1-4}

The matrix $M_n$ is invertible.


::: pf-proof

For each
$$
i=1,\ldots,n-1,
$$
replace row $i$ by
$$
R_i-R_n.
$$
These row operations do not change the determinant.

The resulting matrix has first $n-1$ rows
$$
-e_1^t,\ldots,-e_{n-1}^t
$$
and final row
$$
(1,1,\ldots,1).
$$
Thus it has the form
$$
\begin{pmatrix}
-I_{n-1}&0\\
\ast&1
\end{pmatrix}.
$$
Its determinant is
$$
(-1)^{n-1}\ne0.
$$
Therefore
$$
\det M_n\ne0,
$$
so $M_n$ is invertible.

:::

:::

::: {.pf-step #s1-5}

Hence the largest possible number of ones is
$$
\boxed{n^2-n+1}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} proves that no invertible zero-one matrix can have more than this many ones.
Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} exhibit an invertible zero-one matrix attaining the bound.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves both optimality and attainability.

:::

:::

:::
