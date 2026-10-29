---
schema: qual/card@1
id: P-UCLAB18S-05
kind: problem
title: Positive definiteness under sums and symmetrized products
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $A,B$ be positive definite $2\times2$ real matrices.
Prove or disprove each assertion:

1. $A+B$ is positive definite.

2. $AB+BA$ is positive definite.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assertion 1 is true.


::: pf-proof

Let
\[
x\in\RR^2
\]
be nonzero.
Since $A$ and $B$ are positive definite,
\[
x^TAx>0
\qquad\text{and}\qquad
x^TBx>0.
\]
Therefore
\[
\begin{aligned}
x^T(A+B)x
&=
x^TAx+x^TBx\\
&>
0.
\end{aligned}
\]
Also $A+B$ is symmetric because both $A$ and $B$ are symmetric.
Hence
\[
\boxed{A+B\text{ is positive definite}.}
\]

:::

:::

::: {.pf-step #s1-2}

Assertion 2 is false.


::: pf-proof

Consider
\[
A=
\begin{pmatrix}
4&0\\
0&1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&\frac45\\
\frac45&1
\end{pmatrix}.
\]
The following steps verify that $A$ and $B$ are positive definite while $AB+BA$ is not.

:::

:::

::: {.pf-step #s1-3}

The matrix $A$ is positive definite.


::: pf-proof

For
\[
x=
\begin{pmatrix}
u\\v
\end{pmatrix}
\ne0,
\]
one has
\[
x^TAx
=
4u^2+v^2
>
0.
\]

:::

:::

::: {.pf-step #s1-4}

The matrix $B$ is positive definite.


::: pf-proof

The matrix is symmetric.
Its leading principal minors are
\[
1>0
\]
and
\[
\det B
=
1-\frac{16}{25}
=
\frac9{25}
>
0.
\]
By Sylvester's criterion, $B$ is positive definite.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{
AB+BA
=
\begin{pmatrix}
8&4\\
4&2
\end{pmatrix}.
}
\]


::: pf-proof

Direct multiplication gives
\[
AB
=
\begin{pmatrix}
4&\frac{16}{5}\\
\frac45&1
\end{pmatrix}
\]
and
\[
BA
=
\begin{pmatrix}
4&\frac45\\
\frac{16}{5}&1
\end{pmatrix}.
\]
Adding yields the displayed matrix.

:::

:::

::: {.pf-step #s1-6}

The nonzero vector
\[
v=
\begin{pmatrix}
1\\
-2
\end{pmatrix}
\]
satisfies
\[
(AB+BA)v=0.
\]


::: pf-proof

Using step [](#s1-5){.pf-ref},
\[
\begin{pmatrix}
8&4\\
4&2
\end{pmatrix}
\begin{pmatrix}
1\\
-2
\end{pmatrix}
=
\begin{pmatrix}
8-8\\
4-4
\end{pmatrix}
=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
\]

:::

:::

::: {.pf-step #s1-7}

Therefore $AB+BA$ is not positive definite.


::: pf-proof

Positive definiteness would require
\[
v^T(AB+BA)v>0
\]
for every nonzero $v$.
But step [](#s1-6){.pf-ref} gives
\[
v^T(AB+BA)v=0
\]
for a nonzero vector.
Thus
\[
\boxed{AB+BA\text{ need not be positive definite}.}
\]

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves assertion 1, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} disprove assertion 2.

:::

:::

:::
