---
schema: qual/card@1
id: P-TRIV-LA44
kind: problem
title: Canonical form, rank and signature of a ternary quadratic form
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 44, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the quadratic form $f ( \vec { x } ) = 2 x _ { 1 } ^ { 2 } + 4 x _ { 1 } x _ { 2 } + 3 x _ { 2 } ^ { 2 } + 4 x _ { 2 } x _ { 3 } + 5 x _ { 3 } ^ { 2 }$ ,where $x _ { i } , i = 1 , 2 , 3$ are components of x in $\mathbb { R } ^ { 3 }$

(a) Reduce $f ( \vec { x } )$ to the canonical form.
Calculate its rang and signature.

(b) Write the transition matrix to the basis where f (x) has the canonical form.
:::

::: pf

::: pf-step

Complete the square in $x_1$:
$$
2x_1^2+4x_1x_2+3x_2^2
=
2(x_1+x_2)^2+x_2^2.
$$


::: pf-proof

Expand
$$
2(x_1+x_2)^2
=
2x_1^2+4x_1x_2+2x_2^2.
$$
Adding the remaining $x_2^2$ gives the original three terms.

:::

:::

::: pf-step

Hence
$$
f
=
2(x_1+x_2)^2
+
x_2^2+4x_2x_3+5x_3^2.
$$


::: pf-proof

Substitute the identity from step <1>1 into the original quadratic form.

:::

:::

::: pf-step

Complete the square in the remaining two variables:
$$
x_2^2+4x_2x_3+5x_3^2
=
(x_2+2x_3)^2+x_3^2.
$$


::: pf-proof

Expand
$$
(x_2+2x_3)^2
=
x_2^2+4x_2x_3+4x_3^2,
$$
then add $x_3^2$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
f
=
2(x_1+x_2)^2
+
(x_2+2x_3)^2
+
x_3^2.
}
$$


::: pf-proof

Combine steps <1>2--<1>3.

:::

:::

::: pf-step

Define new coordinates
$$
u_1=\sqrt2(x_1+x_2),
\qquad
u_2=x_2+2x_3,
\qquad
u_3=x_3.
$$
Then
$$
\boxed{f=u_1^2+u_2^2+u_3^2}.
$$


::: pf-proof

Substitute the definitions of the $u_i$ into step <1>4.

:::

:::

::: pf-step

The rank is
$$
\boxed{3}.
$$


::: pf-proof

The canonical form in step <1>5 has three nonzero square terms.

:::

:::

::: pf-step

The inertia is
$$
\boxed{(3,0)},
$$
so the signature $p-q$ is
$$
\boxed{3}.
$$


::: pf-proof

All three coefficients in the canonical form are positive and none are
negative.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

Steps <1>5--<1>7 give the canonical form, rank, and signature.

:::

:::

::: pf-step

The coordinate change from old coordinates $x$ to canonical coordinates
$u$ is
$$
u=Cx,
$$
with
$$
\boxed{
C=
\begin{pmatrix}
\sqrt2&\sqrt2&0\\
0&1&2\\
0&0&1
\end{pmatrix}.
}
$$


::: pf-proof

This matrix encodes exactly the three equations in step <1>5.

:::

:::

::: pf-step

Equivalently,
$$
x=P u,
$$
where
$$
\boxed{
P=C^{-1}
=
\begin{pmatrix}
1/\sqrt2&-1&2\\
0&1&-2\\
0&0&1
\end{pmatrix}.
}
$$


::: pf-proof

From step <1>5,
$$
x_3=u_3,
$$
$$
x_2=u_2-2u_3,
$$
and
$$
x_1=\frac{u_1}{\sqrt2}-x_2
=
\frac{u_1}{\sqrt2}-u_2+2u_3.
$$
These relations are the rows of the displayed matrix $P$.

:::

:::

::: pf-step

In matrix form, if
$$
Q=
\begin{pmatrix}
2&2&0\\
2&3&2\\
0&2&5
\end{pmatrix}
$$
is the symmetric matrix of the original quadratic form, then
$$
\boxed{P^TQP=I_3}.
$$


::: pf-proof

The identity
$$
f(x)=x^TQx=u^Tu
$$
with $x=Pu$ implies
$$
u^TP^TQPu=u^Tu
$$
for every $u$. Hence
$$
P^TQP=I_3.
$$

:::

:::

::: pf-step

Part (b) follows.


::: pf-proof

Step <1>10 gives the transition matrix from canonical coordinates to the
original basis, while step <1>9 gives the inverse coordinate transformation.

:::

:::

::: pf-qed

Steps <1>8 and <1>12 establish parts (a) and (b).

:::

:::
