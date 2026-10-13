---
schema: qual/card@1
id: P-UCLAB03S-09
kind: problem
title: A determinant-one orthogonal matrix in dimension three has eigenvalue one
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Examination, May 2003 PDF.
---

::: {.problem}
Let $A\in M_3(\mathbb R)$ satisfy
\[
\det A=1
\qquad\text{and}\qquad
A^tA=I=AA^t.
\]
Prove that the characteristic polynomial of $A$ has $1$ as a root.
:::

::: {.solution}
<1>1. One has
\[
\det(A-I)=\det(I-A).
\]

::: {.proof}
Since $A^tA=I$, the matrix $A$ is invertible and $A^{-1}=A^t$. Hence
\[
A-I=A(I-A^{-1}),
\]
so, using $\det A=1$,
\[
\det(A-I)
=
\det(A)\det(I-A^{-1})
=
\det(I-A^t).
\]
Because determinant is invariant under transpose,
\[
\det(I-A^t)
=
\det\bigl((I-A)^t\bigr)
=
\det(I-A).
\]
:::

<1>2. One has
\[
\det(A-I)=-\det(I-A).
\]

::: {.proof}
Since
\[
A-I=-(I-A)
\]
and the matrices are $3\times3$,
\[
\det(A-I)
=
\det\bigl(-(I-A)\bigr)
=
(-1)^3\det(I-A)
=
-\det(I-A).
\]
:::

<1>3. The matrix $I-A$ is singular.

::: {.proof}
Combining steps <1>1 and <1>2 gives
\[
\det(I-A)=-\det(I-A).
\]
Over $\mathbb R$, this implies
\[
\det(I-A)=0.
\]
Thus $I-A$ is singular.
:::

<1>4. The characteristic polynomial of $A$ has $1$ as a root.

::: {.proof}
If
\[
\chi_A(t)=\det(tI-A),
\]
then step <1>3 gives
\[
\boxed{\chi_A(1)=\det(I-A)=0}.
\]
Therefore $1$ is a root of $\chi_A$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
