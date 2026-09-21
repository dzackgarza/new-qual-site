---
schema: qual/card@1
id: P-BERK79S-01
kind: problem
title: Inertia of a symmetric four-by-four matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used symmetry to make all four eigenvalues real. The determinant is
    625, so none is zero and an even number are negative. The trace is zero,
    which rules out all four eigenvalues having the same sign; hence exactly
    two are positive and two are negative.
---

::: {.problem}
Prove that
\[
\begin{pmatrix}
0&5&1&0\\
5&0&5&0\\
1&5&0&5\\
0&0&5&0
\end{pmatrix}
\]
has two positive and two negative eigenvalues, counted with multiplicity.
:::

::: {.solution}
Let
$$
A=
\begin{pmatrix}
0&5&1&0\\
5&0&5&0\\
1&5&0&5\\
0&0&5&0
\end{pmatrix}.
$$

<1>1. All four eigenvalues of $A$ are real.

::: {.proof}
The matrix $A$ is real and symmetric:
$$
A^T=A.
$$
By the spectral theorem for real symmetric matrices, $A$ is orthogonally
diagonalizable over $\RR$. Hence all its eigenvalues are real.
:::

<1>2. The determinant of $A$ is
$$
\det A=625>0.
$$

::: {.proof}
Expand along the fourth row. The only nonzero entry is the $5$ in column
$3$, so
$$
\det A
=
-5
\det
\begin{pmatrix}
0&5&0\\
5&0&0\\
1&5&5
\end{pmatrix}.
$$
Expanding the remaining determinant along its third column gives
$$
\det
\begin{pmatrix}
0&5&0\\
5&0&0\\
1&5&5
\end{pmatrix}
=
5
\det
\begin{pmatrix}
0&5\\
5&0
\end{pmatrix}
=
-125.
$$
Therefore
$$
\det A=(-5)(-125)=625.
$$
:::

<1>3. None of the eigenvalues is zero, and the number of negative
eigenvalues is even.

::: {.proof}
Let the four real eigenvalues, counted with multiplicity, be
$$
\lambda_1,\lambda_2,\lambda_3,\lambda_4.
$$
Their product equals the determinant:
$$
\lambda_1\lambda_2\lambda_3\lambda_4
=
\det A
=
625
>
0.
$$
Thus none is zero. A product of nonzero real numbers is positive exactly
when an even number of its factors are negative, so the number of negative
eigenvalues is $0$, $2$, or $4$.
:::

<1>4. The eigenvalues cannot all be positive and cannot all be negative.

::: {.proof}
The trace of $A$ is zero because every diagonal entry is zero:
$$
\operatorname{tr}A=0.
$$
The trace is the sum of the eigenvalues counted with multiplicity, so
$$
\lambda_1+\lambda_2+\lambda_3+\lambda_4=0.
$$
Four positive real numbers cannot have sum zero, and neither can four
negative real numbers.
:::

<1>5. The matrix $A$ has
$$
\boxed{
\text{two positive and two negative eigenvalues}
}
$$
counted with multiplicity.

::: {.proof}
By step <1>3, the number of negative eigenvalues is one of
$$
0,\ 2,\ 4.
$$
Step <1>4 rules out $0$ and $4$. Hence exactly two eigenvalues are
negative. Since none is zero and there are four eigenvalues in total, the
remaining two are positive.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required inertia statement.
:::
:::
