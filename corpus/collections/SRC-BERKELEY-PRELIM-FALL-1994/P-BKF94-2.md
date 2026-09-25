---
schema: qual/card@1
id: P-BKF94-2
kind: problem
title: Signs of the eigenvalues of a nearly rank-one matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used equality of the first and third rows to bound the rank by two, then
    exhibited vectors on which the symmetric quadratic form is positive and
    negative.
---

::: {.problem}
Prove that
\[
\begin{pmatrix}
1&1.00001&1\\
1.00001&1&1.00001\\
1&1.00001&1
\end{pmatrix}
\]
has one positive eigenvalue and one negative eigenvalue.
:::

::: {.solution}
Let
$$
A\coloneqq
\begin{pmatrix}
1&1.00001&1\\
1.00001&1&1.00001\\
1&1.00001&1
\end{pmatrix}.
$$

<1>1. The matrix $A$ has rank at most $2$.

::: {.proof}
Its first and third rows are equal. Therefore the three rows are linearly
dependent, so
$$
\operatorname{rank}A\leq2.
$$
:::

<1>2. The quadratic form of $A$ takes a positive value.

::: {.proof}
For
$$
u=
\begin{pmatrix}
1\\
0\\
0
\end{pmatrix},
$$
one has
$$
u^tAu=1>0.
$$
:::

<1>3. The quadratic form of $A$ takes a negative value.

::: {.proof}
Take
$$
v=
\begin{pmatrix}
1\\
-2\\
1
\end{pmatrix}.
$$
Direct multiplication gives
$$
Av=
\begin{pmatrix}
-0.00002\\
0.00002\\
-0.00002
\end{pmatrix},
$$
and therefore
$$
v^tAv
=
-0.00002
-2(0.00002)
-0.00002
=
-0.00008
<0.
$$
:::

<1>4. The matrix $A$ has at least one positive eigenvalue and at least one
negative eigenvalue.

::: {.proof}
The matrix $A$ is real symmetric, so the spectral theorem gives an
orthonormal eigenbasis and expresses its quadratic form as
$$
x^tAx
=
\sum_j\lambda_jc_j^2
$$
in eigenbasis coordinates. If every eigenvalue were nonnegative, the
quadratic form could not take the negative value in step <1>3. Hence some
eigenvalue is negative. If every eigenvalue were nonpositive, the quadratic
form could not take the positive value in step <1>2. Hence some eigenvalue
is positive.
:::

<1>5. The matrix $A$ has exactly one positive and exactly one negative
eigenvalue.

::: {.proof}
By step <1>1, at most two eigenvalues are nonzero, counted with
multiplicity. Step <1>4 already supplies one positive and one negative
eigenvalue, so these are exactly the two nonzero eigenvalues.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
