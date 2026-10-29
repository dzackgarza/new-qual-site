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
Consider the quadratic form $f ( \vec { x } ) = 2 x _ { 1 } ^ { 2 } + 4 x _ { 1 } x _ { 2 } + 3 x _ { 2 } ^ { 2 } + 4 x _ { 2 } x _ { 3 } + 5 x _ { 3 } ^ { 2 }$ ,where $x _ { i } , i = 1 , 2 , 3$ are components of x in $\RR ^ { 3 }$

(a) Reduce $f ( \vec { x } )$ to the canonical form.
Calculate its rang and signature.

(b) Write the transition matrix to the basis where f (x) has the canonical form.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

Hence
$$
f
=
2(x_1+x_2)^2
+
x_2^2+4x_2x_3+5x_3^2.
$$


::: pf-proof

Substitute the identity from step [](#s1-1){.pf-ref} into the original quadratic form.

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

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

Combine steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

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

Substitute the definitions of the $u_i$ into step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The rank is
$$
\boxed{3}.
$$


::: pf-proof

The canonical form in step [](#s1-5){.pf-ref} has three nonzero square terms.

:::

:::

::: {.pf-step #s1-7}

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

::: {.pf-step #s1-8}

Part (a) follows.


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} give the canonical form, rank, and signature.

:::

:::

::: {.pf-step #s1-9}

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

This matrix encodes exactly the three equations in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

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

From step [](#s1-5){.pf-ref},
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

::: {.pf-step #s1-12}

Part (b) follows.


::: pf-proof

Step [](#s1-10){.pf-ref} gives the transition matrix from canonical coordinates to the
original basis, while step [](#s1-9){.pf-ref} gives the inverse coordinate transformation.

:::

:::

::: pf-qed

Steps [](#s1-8){.pf-ref} and [](#s1-12){.pf-ref} establish parts (a) and (b).

:::

:::

:::
