---
schema: qual/card@1
id: P-UCLAB16S-09
kind: problem
title: Linear independence over the reals and rationals
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let
\[
v_1=(0,1,x),\qquad v_2=(1,x,1),\qquad v_3=(x,1,0).
\]
Find all $x\in\mathbb R$ for which $\{v_1,v_2,v_3\}$ is linearly independent over $\mathbb R$.
Similarly, find all $x\in\mathbb R$ for which $\{v_1,v_2,v_3\}$ is linearly independent over $\mathbb Q$.
:::

::: pf

::: pf-step

Put the vectors as the columns of
\[
M(x)
=
\begin{pmatrix}
0&1&x\\
1&x&1\\
x&1&0
\end{pmatrix}.
\]
Then
\[
\boxed{
\det M(x)
=
x(2-x^2).
}
\]


::: pf-proof

Expanding along the first row,
\[
\begin{aligned}
\det M(x)
&=
-
\det
\begin{pmatrix}
1&1\\
x&0
\end{pmatrix}
+
x
\det
\begin{pmatrix}
1&x\\
x&1
\end{pmatrix}\\
&=
-(-x)
+
x(1-x^2)\\
&=
2x-x^3\\
&=
x(2-x^2).
\end{aligned}
\]

:::

:::

::: pf-step

The vectors are linearly independent over $\mathbb R$ exactly when
\[
\boxed{
x\notin\{0,\sqrt2,-\sqrt2\}.
}
\]


::: pf-proof

Three vectors in $\mathbb R^3$ are linearly independent over $\mathbb R$ exactly when the determinant of the matrix having them as columns is nonzero.
By step <1>1,
\[
\det M(x)=0
\]
exactly when
\[
x=0
\quad\text{or}\quad
x^2=2.
\]
This proves the real case.

:::

:::

::: pf-step

If
\[
x\notin\{0,\sqrt2,-\sqrt2\},
\]
then the vectors are also linearly independent over $\mathbb Q$.


::: pf-proof

A rational linear relation is in particular a real linear relation.
Thus real linear independence implies rational linear independence.
Apply step <1>2.

:::

:::

::: pf-step

At
\[
x=0,
\]
the vectors are linearly dependent over $\mathbb Q$.


::: pf-proof

When
\[
x=0,
\]
\[
v_1=(0,1,0)
\]
and
\[
v_3=(0,1,0).
\]
Thus
\[
v_1-v_3=0
\]
is a nontrivial rational linear relation.

:::

:::

::: pf-step

Suppose
\[
x=\pm\sqrt2
\]
and
\[
q_1v_1+q_2v_2+q_3v_3=0
\]
with
\[
q_1,q_2,q_3\in\mathbb Q.
\]
Then
\[
q_1=q_2=q_3=0.
\]


::: pf-proof

Comparing coordinates gives
\[
q_2+xq_3=0,
\]
\[
q_1+xq_2+q_3=0,
\]
and
\[
xq_1+q_2=0.
\]

From the third equation,
\[
q_2=-xq_1.
\]
If
\[
q_1\ne0,
\]
then
\[
x=-\frac{q_2}{q_1}
\in\mathbb Q,
\]
contradicting
\[
x=\pm\sqrt2\notin\mathbb Q.
\]
Therefore
\[
q_1=0,
\]
and hence
\[
q_2=0.
\]
The first equation then gives
\[
xq_3=0.
\]
Since
\[
x\ne0,
\]
one gets
\[
q_3=0.
\]

:::

:::

::: pf-step

Therefore the vectors are linearly independent over $\mathbb Q$ exactly when
\[
\boxed{x\ne0}.
\]


::: pf-proof

Step <1>3 handles all values except
\[
0,\pm\sqrt2.
\]
Step <1>4 shows dependence at $0$, while step <1>5 proves rational independence at
\[
\pm\sqrt2.
\]
Thus $0$ is the only excluded value.

:::

:::

::: pf-qed

Step <1>2 gives the answer over $\mathbb R$, and step <1>6 gives the answer over $\mathbb Q$.

:::

:::
