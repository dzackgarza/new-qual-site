---
schema: qual/card@1
id: P-UCLAB02S-06
kind: problem
title: Completing a regular scalar function to local coordinates
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
Suppose $f:\RR^3\to\RR$ is continuously differentiable and
$$
\nabla f(0,0,0)\ne0.
$$
Show that there exist continuously differentiable functions
$$
g,h:\RR^3\to\RR
$$
such that
$$
(x,y,z)\longmapsto
\bigl(f(x,y,z),g(x,y,z),h(x,y,z)\bigr)
$$
is one-to-one on some neighborhood of $(0,0,0)$.
:::

::: {.solution}

Since
$$
\nabla f(0,0,0)\ne0,
$$
at least one first partial derivative of $f$ at the origin is nonzero.

::: pf

::: {.pf-step #s1-1}

After permuting the coordinates if necessary, assume
$$
f_x(0,0,0)\ne0.
$$


::: pf-proof

The gradient is
$$
\nabla f(0,0,0)
=
\bigl(
f_x(0,0,0),
f_y(0,0,0),
f_z(0,0,0)
\bigr).
$$
Since this vector is nonzero, at least one coordinate is nonzero.
Relabel the coordinate axes so that it is the first.

:::

:::

::: {.pf-step #s1-2}

Define
$$
g(x,y,z)=y
\qquad\text{and}\qquad
h(x,y,z)=z.
$$
Then the map
$$
\Phi:\RR^3\to\RR^3,
\qquad
\Phi(x,y,z)
=
\bigl(
f(x,y,z),y,z
\bigr)
$$
is continuously differentiable.


::: pf-proof

The function $f$ is $C^1$ by hypothesis, while the coordinate functions $y$ and $z$ are smooth.
Therefore $\Phi$ is $C^1$.

:::

:::

::: {.pf-step #s1-3}

The derivative matrix of $\Phi$ at the origin is
$$
D\Phi(0)
=
\begin{pmatrix}
f_x(0)&f_y(0)&f_z(0)\\
0&1&0\\
0&0&1
\end{pmatrix}.
$$


::: pf-proof

Differentiate the three component functions
$$
f,\quad y,\quad z
$$
with respect to the variables $x,y,z$.

:::

:::

::: {.pf-step #s1-4}

The determinant of $D\Phi(0)$ is
$$
\det D\Phi(0)
=
f_x(0,0,0)
\ne0.
$$


::: pf-proof

The matrix in step [](#s1-3){.pf-ref} is upper triangular.
Its determinant is the product of its diagonal entries:
$$
f_x(0,0,0)\cdot1\cdot1.
$$
This is nonzero by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

There exists an open neighborhood
$$
U
$$
of $(0,0,0)$ such that
$$
\Phi\restrict_U
$$
is one-to-one.


::: pf-proof

The inverse function theorem applies to the $C^1$ map $\Phi$ because
$$
\det D\Phi(0)\ne0
$$
by step [](#s1-4){.pf-ref}.
Hence there exist open neighborhoods
$$
U
\ni
(0,0,0)
$$
and
$$
V
\ni
\Phi(0,0,0)
$$
such that
$$
\Phi\restrict_U:U\to V
$$
is a $C^1$ diffeomorphism.
In particular, it is one-to-one.

:::

:::

::: {.pf-step #s1-6}

Therefore the functions
$$
\boxed{g(x,y,z)=y,\qquad h(x,y,z)=z}
$$
have the required property.


::: pf-proof

For these choices, the map in the problem is exactly $\Phi$ from step [](#s1-2){.pf-ref}.
Step [](#s1-5){.pf-ref} proves that it is one-to-one on some neighborhood of the origin.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required construction.

:::

:::

:::
