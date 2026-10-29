---
schema: qual/card@1
id: P-UCLAB14F-07
kind: problem
title: Minimum-norm solution of an underdetermined linear system
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
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 7. Among all solutions to the system
\[
\begin{pmatrix}
1&1&1&1\\
2&3&5&7\\
-2&-1&1&3
\end{pmatrix}x
=
\begin{pmatrix}2\\7\\-1\end{pmatrix},
\]
find the solution with minimal length.
:::

::: {.solution}

Let
\[
A=
\begin{pmatrix}
1&1&1&1\\
2&3&5&7\\
-2&-1&1&3
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
2\\
7\\
-1
\end{pmatrix}.
\]

::: pf

::: pf-step

The third row equation is the difference between the second row equation and four times the first.


::: pf-proof

For the coefficient rows,
\[
(2,3,5,7)-4(1,1,1,1)
=
(-2,-1,1,3),
\]
and for the right-hand side,
\[
7-4\cdot2=-1.
\]
Thus the third equation is redundant.

:::

:::

::: {.pf-step #s1-2}

Every solution has the form
\[
x(s,t)
=
\begin{pmatrix}
2s+4t-1\\
-3s-5t+3\\
s\\
t
\end{pmatrix},
\qquad
s,t\in\RR.
\]


::: pf-proof

Set
\[
x_3=s,
\qquad
x_4=t.
\]
The first two independent equations are
\[
x_1+x_2=2-s-t
\]
and
\[
2x_1+3x_2=7-5s-7t.
\]
Subtracting twice the first from the second gives
\[
x_2=3-3s-5t.
\]
Substituting into the first gives
\[
x_1
=
2-s-t-(3-3s-5t)
=
2s+4t-1.
\]

:::

:::

::: {.pf-step #s1-3}

The squared Euclidean norm of $x(s,t)$ is
\[
\|x(s,t)\|^2
=
2\bigl(
7s^2+23st-11s+21t^2-19t+5
\bigr).
\]


::: pf-proof

Substitute the coordinates from step [](#s1-2){.pf-ref}:
\[
\begin{aligned}
\|x(s,t)\|^2
&=
(2s+4t-1)^2
+
(-3s-5t+3)^2
+
s^2+t^2.
\end{aligned}
\]
Expanding and collecting terms gives the displayed quadratic polynomial.

:::

:::

::: {.pf-step #s1-4}

A minimizer of the squared norm must satisfy
\[
14s+23t=11
\]
and
\[
23s+42t=19.
\]


::: pf-proof

Differentiate the quadratic polynomial from step [](#s1-3){.pf-ref}:
\[
\frac{\partial}{\partial s}\|x(s,t)\|^2
=
2(14s+23t-11),
\]
\[
\frac{\partial}{\partial t}\|x(s,t)\|^2
=
2(23s+42t-19).
\]
At an interior minimum in $\RR^2$, both partial derivatives vanish.

:::

:::

::: {.pf-step #s1-5}

The system in step [](#s1-4){.pf-ref} has the unique solution
\[
\boxed{
s=\frac{25}{59},
\qquad
t=\frac{13}{59}
}.
\]


::: pf-proof

The determinant of the coefficient matrix is
\[
14\cdot42-23^2
=
588-529
=59\ne0.
\]
Cramer's rule gives
\[
s
=
\frac{11\cdot42-23\cdot19}{59}
=
\frac{462-437}{59}
=
\frac{25}{59},
\]
and
\[
t
=
\frac{14\cdot19-23\cdot11}{59}
=
\frac{266-253}{59}
=
\frac{13}{59}.
\]

:::

:::

::: {.pf-step #s1-6}

The critical point in step [](#s1-5){.pf-ref} is the unique global minimum of the squared norm.


::: pf-proof

The Hessian of
\[
\frac12\|x(s,t)\|^2
\]
is
\[
\begin{pmatrix}
14&23\\
23&42
\end{pmatrix}.
\]
Its first leading principal minor is
\[
14>0,
\]
and its determinant is
\[
59>0.
\]
Hence the Hessian is positive definite.
Therefore the quadratic function is strictly convex and its unique critical point is its unique global minimizer.

:::

:::

::: {.pf-step #s1-7}

Substituting the minimizing parameters gives
\[
\boxed{
x_{\min}
=
\frac1{59}
\begin{pmatrix}
43\\
37\\
25\\
13
\end{pmatrix}
}.
\]


::: pf-proof

Using step [](#s1-2){.pf-ref} and
\[
s=\frac{25}{59},
\qquad
t=\frac{13}{59},
\]
one gets
\[
x_1
=
\frac{50+52-59}{59}
=
\frac{43}{59},
\]
\[
x_2
=
\frac{-75-65+177}{59}
=
\frac{37}{59},
\]
while
\[
x_3=\frac{25}{59},
\qquad
x_4=\frac{13}{59}.
\]

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} prove that the displayed solution is the unique solution of minimal Euclidean length.

:::

:::

:::
