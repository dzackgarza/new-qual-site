---
schema: qual/card@1
id: P-TRIV-LA47
kind: problem
title: Simultaneous diagonalization of two binary quadratic forms
classification:
  areas: [prelim]
  topics:
  - Quadratic Forms
  - Simultaneous Diagonalization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 47, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the quadratic forms $f(\vec{x}) = x_1^2 + 2x_1x_2 + 3x_2^2$ and $g(\vec{x}) = 4x_1^2 + 16x_1x_2 + 6x_2^2$ in $\RR^2$.

(a) Check if at least one of these forms is sign definite.

(b) Find the change of coordinates that reduces $f(\vec{x})$ and $g(\vec{x})$ to the diagonal form.
:::

::: {.solution}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

Hence $f$ is positive definite.


::: pf-proof

Both leading principal minors in step [](#s1-2){.pf-ref} are positive. Sylvester's criterion
therefore gives positive definiteness.

:::

:::

::: {.pf-step #s1-4}

Part (a) follows.


::: pf-proof

Step [](#s1-3){.pf-ref} shows that at least one form is sign definite.

:::

:::

::: {.pf-step #s1-5}

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

::: {.pf-step #s1-6}

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

Substitute the definitions into step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

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

From step [](#s1-6){.pf-ref},
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

The coefficient of $y_1y_2$ in step [](#s1-7){.pf-ref} is $4\sqrt2$, so the off-diagonal
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

::: {.pf-step #s1-10}

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

::: {.pf-step #s1-11}

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

The columns of $R$ are the orthonormal eigenvectors from step [](#s1-10){.pf-ref}, so $R$
is orthogonal.

:::

:::

::: {.pf-step #s1-12}

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
so the form $f$ from step [](#s1-6){.pf-ref} stays diagonal with identity matrix.

Also,
$$
R^TG_yR=
\begin{pmatrix}
5&0\\
0&-4
\end{pmatrix}
$$
by step [](#s1-10){.pf-ref}, giving the stated form of $g$.

:::

:::

::: {.pf-step #s1-13}

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

By step [](#s1-6){.pf-ref},
$$
\begin{pmatrix}y_1\\y_2\end{pmatrix}
=
\begin{pmatrix}
1&1\\
0&\sqrt2
\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}.
$$
Apply $R^T=R$ from step [](#s1-11){.pf-ref} and simplify.

:::

:::

::: {.pf-step #s1-14}

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

Solve the two linear equations in step [](#s1-13){.pf-ref} for $x_1,x_2$.

:::

:::

::: {.pf-step #s1-15}

Part (b) follows.


::: pf-proof

Steps [](#s1-12){.pf-ref} through [](#s1-14){.pf-ref} give the simultaneous diagonalization and the explicit
change of coordinates.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-15){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
