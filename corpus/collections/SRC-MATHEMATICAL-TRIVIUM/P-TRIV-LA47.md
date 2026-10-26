---
schema: qual/card@1
id: P-TRIV-LA47
kind: problem
title: Simultaneous diagonalization of two binary quadratic forms
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 47, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the quadratic forms $f ( { \vec { x } } ) = x _ { 1 } ^ { 2 } + 2 x _ { 1 } x _ { 2 } + 3 x _ { 2 } ^ { 2 }$ and $g ( \vec { x } ) = { 4 x _ { 1 } ^ { 2 } + 1 6 x _ { 1 } x _ { 2 } + }$ $6 x _ { 2 } ^ { 2 }$ in $\mathbb { R } ^ { 2 }$

(a) Check if at least one of these forms is sign definite.
(b) Find the change of coordinates that reduces f (x) and g(x) to the diagonal form.
:::

::: pf

::: pf-step

The symmetric matrix of $f$ is
$$
F=
\begin{pmatrix}
1&1\\
1&3
\end{pmatrix}.
$$


::: pf-proof

The cross term $2x_1x_2$ corresponds to off-diagonal entries $1$.

:::

:::

::: pf-step

The leading principal minors of $F$ are
$$
1
\qquad\text{and}\qquad
\det F=2.
$$


::: pf-proof

Directly,
$$
\det F=1\cdot3-1\cdot1=2.
$$

:::

:::

::: pf-step

Hence $f$ is positive definite.


::: pf-proof

Both leading principal minors in step <1>2 are positive. Sylvester's criterion
therefore gives positive definiteness.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

Step <1>3 shows that at least one form is sign definite.

:::

:::

::: pf-step

Complete the square in $f$:
$$
f
=
(x_1+x_2)^2
+
2x_2^2.
$$


::: pf-proof

Expand the right-hand side:
$$
x_1^2+2x_1x_2+x_2^2+2x_2^2
=
x_1^2+2x_1x_2+3x_2^2.
$$

:::

:::

::: pf-step

Define
$$
y_1=x_1+x_2,
\qquad
y_2=\sqrt2,x_2.
$$
Then
$$
f=y_1^2+y_2^2.
$$


::: pf-proof

Substitute the definitions into step <1>5.

:::

:::

::: pf-step

In the $y$-coordinates,
$$
g
=
4y_1^2
+
4\sqrt2,y_1y_2
-
3y_2^2.
$$


::: pf-proof

From step <1>6,
$$
x_2=\frac{y_2}{\sqrt2},
\qquad
x_1=y_1-\frac{y_2}{\sqrt2}.
$$
Substitute these expressions into
$$
g=4x_1^2+16x_1x_2+6x_2^2
$$
and simplify.

:::

:::

::: pf-step

The symmetric matrix of $g$ in the $y$-coordinates is
$$
G_y=
\begin{pmatrix}
4&2\sqrt2\\
2\sqrt2&-3
\end{pmatrix}.
$$


::: pf-proof

The coefficient of $y_1y_2$ in step <1>7 is $4\sqrt2$, so the off-diagonal
matrix entries are $2\sqrt2$.

:::

:::

::: pf-step

The eigenvalues of $G_y$ are
$$
5
\qquad\text{and}\qquad
-4.
$$


::: pf-proof

The characteristic polynomial is
$$
\begin{aligned}
\det(G_y-\lambda I)
&=
(4-\lambda)(-3-\lambda)-8\\
&=
\lambda^2-\lambda-20\\
&=
(\lambda-5)(\lambda+4).
\end{aligned}
$$

:::

:::

::: pf-step

Corresponding orthonormal eigenvectors are
$$
e_+=
\frac13
\begin{pmatrix}
2\sqrt2\\
1
\end{pmatrix}
$$
for eigenvalue $5$, and
$$
e_-=
\frac13
\begin{pmatrix}
1\\
-2\sqrt2
\end{pmatrix}
$$
for eigenvalue $-4$.


::: pf-proof

Direct substitution shows
$$
G_y e_+=5e_+,
\qquad
G_y e_-=-4e_-.
$$
Their norms equal $1$, and their inner product is $0$.

:::

:::

::: pf-step

Define new coordinates $z_1,z_2$ by
$$
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix}
=
R^T
\begin{pmatrix}
y_1\\
y_2
\end{pmatrix},
$$
where
$$
R=
\frac13
\begin{pmatrix}
2\sqrt2&1\\
1&-2\sqrt2
\end{pmatrix}.
$$


::: pf-proof

The columns of $R$ are the orthonormal eigenvectors from step <1>10, so $R$
is orthogonal.

:::

:::

::: pf-step

In the $z$-coordinates,
$$
\boxed{f=z_1^2+z_2^2}
$$
and
$$
\boxed{g=5z_1^2-4z_2^2}.
$$


::: pf-proof

Because $R$ is orthogonal,
$$
y_1^2+y_2^2=z_1^2+z_2^2,
$$
so the form $f$ from step <1>6 stays diagonal with identity matrix.

Also,
$$
R^TG_yR=
\begin{pmatrix}
5&0\\
0&-4
\end{pmatrix}
$$
by step <1>10, giving the stated form of $g$.

:::

:::

::: pf-step

Explicitly, the simultaneous coordinate change from $x$ to $z$ is
$$
\boxed{
z_1
=
\frac{\sqrt2}{3}(2x_1+3x_2),
\qquad
z_2
=
\frac13(x_1-3x_2).
}
$$


::: pf-proof

By step <1>6,
$$
\begin{pmatrix}y_1\\y_2\end{pmatrix}
=
\begin{pmatrix}
1&1\\
0&\sqrt2
\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}.
$$
Apply $R^T=R$ from step <1>11 and simplify.

:::

:::

::: pf-step

Equivalently,
$$
\boxed{
x_1
=
\frac{z_1}{\sqrt2}+z_2,
\qquad
x_2
=
\frac{z_1}{3\sqrt2}-\frac23z_2.
}
$$


::: pf-proof

Solve the two linear equations in step <1>13 for $x_1,x_2$.

:::

:::

::: pf-step

Part (b) follows.


::: pf-proof

Steps <1>12--<1>14 give the simultaneous diagonalization and the explicit
change of coordinates.

:::

:::

::: pf-qed

Steps <1>4 and <1>15 establish parts (a) and (b), respectively.

:::

:::
