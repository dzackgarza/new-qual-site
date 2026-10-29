---
schema: qual/card@1
id: P-UCLAB15F-12
kind: problem
title: Positive definiteness of a structured dense matrix
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
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Prove that the $n\times n$ matrix
\[
M=\begin{pmatrix}
2&1&1&\cdots&1\\
1&3&1&\cdots&1\\
1&1&4&\cdots&1\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&1&1&\cdots&n+1
\end{pmatrix}
\]
is positive definite.
:::

::: {.solution}

Let
\[
\mathbf1=
\begin{pmatrix}
1\\
\vdots\\
1
\end{pmatrix}
\in\RR^n
\]
and let
\[
D=\operatorname{diag}(1,2,\ldots,n).
\]

::: pf

::: {.pf-step #s1-1}

One has
\[
\boxed{M=D+\mathbf1\mathbf1^t}.
\]


::: pf-proof

The matrix
\[
\mathbf1\mathbf1^t
\]
has every entry equal to $1$.
Adding
\[
D=\operatorname{diag}(1,2,\ldots,n)
\]
changes the diagonal entries to
\[
2,3,\ldots,n+1
\]
while leaving every off-diagonal entry equal to $1$.
This is exactly $M$.

:::

:::

::: {.pf-step #s1-2}

For every vector
\[
x=(x_1,\ldots,x_n)^t\in\RR^n,
\]
one has
\[
x^tMx
=
\sum_{j=1}^n jx_j^2
+
\left(\sum_{j=1}^n x_j\right)^2.
\]


::: pf-proof

Using step [](#s1-1){.pf-ref},
\[
\begin{aligned}
x^tMx
&=
x^tDx
+
x^t\mathbf1\mathbf1^tx\\
&=
\sum_{j=1}^n jx_j^2
+
(\mathbf1^tx)^2\\
&=
\sum_{j=1}^n jx_j^2
+
\left(\sum_{j=1}^n x_j\right)^2.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-3}

If $x\ne0$, then
\[
\sum_{j=1}^n jx_j^2>0.
\]


::: pf-proof

All coefficients
\[
j
\]
are positive.
If $x\ne0$, at least one coordinate $x_j$ is nonzero, so the corresponding term
\[
jx_j^2
\]
is strictly positive, while every other term is nonnegative.

:::

:::

::: {.pf-step #s1-4}

Hence for every nonzero $x$,
\[
\boxed{x^tMx>0}.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
x^tMx
=
\sum_{j=1}^n jx_j^2
+
\left(\sum_{j=1}^n x_j\right)^2.
\]
The first term is strictly positive by step [](#s1-3){.pf-ref}, and the second is nonnegative.
Thus their sum is positive.

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
\boxed{M\text{ is positive definite}.}
\]


::: pf-proof

A real symmetric matrix is positive definite precisely when
\[
x^tMx>0
\]
for every nonzero real vector $x$.
Step [](#s1-4){.pf-ref} verifies this condition.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
