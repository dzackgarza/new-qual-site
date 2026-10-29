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
$$
v_1=(0,1,x),\qquad v_2=(1,x,1),\qquad v_3=(x,1,0).
$$
Find all $x\in\RR$ for which $\{v_1,v_2,v_3\}$ is linearly independent over $\RR$.
Similarly, find all $x\in\RR$ for which $\{v_1,v_2,v_3\}$ is linearly independent over $\QQ$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Put the vectors as the columns of
$$
M(x)
=
\begin{pmatrix}
0&1&x\\
1&x&1\\
x&1&0
\end{pmatrix}.
$$
Then
$$
\boxed{
\det M(x)
=
x(2-x^2).
}
$$


::: pf-proof

Expanding along the first row,
$$
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
$$

:::

:::

::: {.pf-step #s1-2}

The vectors are linearly independent over $\RR$ exactly when
$$
\boxed{
x\notin\{0,\sqrt2,-\sqrt2\}.
}
$$


::: pf-proof

Three vectors in $\RR^3$ are linearly independent over $\RR$ exactly when the determinant of the matrix having them as columns is nonzero.
By step [](#s1-1){.pf-ref},
$$
\det M(x)=0
$$
exactly when
$$
x=0
\quad\text{or}\quad
x^2=2.
$$
This proves the real case.

:::

:::

::: {.pf-step #s1-3}

If
$$
x\notin\{0,\sqrt2,-\sqrt2\},
$$
then the vectors are also linearly independent over $\QQ$.


::: pf-proof

A rational linear relation is in particular a real linear relation.
Thus real linear independence implies rational linear independence.
Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

At
$$
x=0,
$$
the vectors are linearly dependent over $\QQ$.


::: pf-proof

When
$$
x=0,
$$
$$
v_1=(0,1,0)
$$
and
$$
v_3=(0,1,0).
$$
Thus
$$
v_1-v_3=0
$$
is a nontrivial rational linear relation.

:::

:::

::: {.pf-step #s1-5}

Suppose
$$
x=\pm\sqrt2
$$
and
$$
q_1v_1+q_2v_2+q_3v_3=0
$$
with
$$
q_1,q_2,q_3\in\QQ.
$$
Then
$$
q_1=q_2=q_3=0.
$$


::: pf-proof

Comparing coordinates gives
$$
q_2+xq_3=0,
$$
$$
q_1+xq_2+q_3=0,
$$
and
$$
xq_1+q_2=0.
$$

From the third equation,
$$
q_2=-xq_1.
$$
If
$$
q_1\ne0,
$$
then
$$
x=-\frac{q_2}{q_1}
\in\QQ,
$$
contradicting
$$
x=\pm\sqrt2\notin\QQ.
$$
Therefore
$$
q_1=0,
$$
and hence
$$
q_2=0.
$$
The first equation then gives
$$
xq_3=0.
$$
Since
$$
x\ne0,
$$
one gets
$$
q_3=0.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore the vectors are linearly independent over $\QQ$ exactly when
$$
\boxed{x\ne0}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} handles all values except
$$
0,\pm\sqrt2.
$$
Step [](#s1-4){.pf-ref} shows dependence at $0$, while step [](#s1-5){.pf-ref} proves rational independence at
$$
\pm\sqrt2.
$$
Thus $0$ is the only excluded value.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the answer over $\RR$, and step [](#s1-6){.pf-ref} gives the answer over $\QQ$.

:::

:::

:::
