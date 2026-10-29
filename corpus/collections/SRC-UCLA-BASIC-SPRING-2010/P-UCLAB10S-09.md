---
schema: qual/card@1
id: P-UCLAB10S-09
kind: problem
title: A regular level set is locally a parametrized surface
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 9. Let $f(x,y,z)$ be a real-valued continuously differentiable function such that
$$
f(x_0,y_0,z_0)=0,
\qquad
\nabla f(x_0,y_0,z_0)\ne0.
$$
Show that there is a differentiable parametrized surface
$$
(x(s,t),y(s,t),z(s,t))
$$
through $(x_0,y_0,z_0)$ on which $f=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since
$$
\nabla f(x_0,y_0,z_0)\ne0,
$$
at least one of
$$
f_x(x_0,y_0,z_0),
\qquad
f_y(x_0,y_0,z_0),
\qquad
f_z(x_0,y_0,z_0)
$$
is nonzero.


::: pf-proof

The gradient is the vector of these three partial derivatives.
A vector is nonzero exactly when at least one of its coordinates is nonzero.

:::

:::

::: {.pf-step #s1-2}

After relabeling the coordinate variables if necessary, assume
$$
\boxed{
f_z(x_0,y_0,z_0)\ne0.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives a nonzero partial derivative.
If the nonzero derivative is $f_x$ or $f_y$ instead, interchange the names of the coordinates so that the corresponding variable is called $z$.
The argument below is unchanged under such a relabeling.

:::

:::

::: {.pf-step #s1-3}

There exist neighborhoods
$$
U\subseteq\RR^2
$$
of
$$
(x_0,y_0)
$$
and
$$
J\subseteq\RR
$$
of $z_0$, together with a continuously differentiable function
$$
\phi:U\to J
$$
such that
$$
\phi(x_0,y_0)=z_0
$$
and
$$
\boxed{
f(x,y,\phi(x,y))=0
}
$$
for all
$$
(x,y)\in U.
$$


::: pf-proof

Apply the implicit function theorem to the equation
$$
f(x,y,z)=0
$$
at the point
$$
(x_0,y_0,z_0).
$$
The hypotheses are satisfied:
$$
f(x_0,y_0,z_0)=0
$$
by assumption,
$f$ is continuously differentiable, and
$$
f_z(x_0,y_0,z_0)\ne0
$$
by step [](#s1-2){.pf-ref}.
Therefore the theorem solves uniquely for $z$ as a $C^1$ function of $(x,y)$ near $(x_0,y_0)$.

:::

:::

::: {.pf-step #s1-4}

Choose $\varepsilon>0$ so small that
$$
(x_0+s,y_0+t)\in U
$$
whenever
$$
|s|<\varepsilon,
\qquad
|t|<\varepsilon.
$$


::: pf-proof

The set $U$ is an open neighborhood of $(x_0,y_0)$.
Hence it contains an open rectangle centered at that point.
Choose $\varepsilon$ so that the displayed square lies inside that rectangle.

:::

:::

::: {.pf-step #s1-5}

Define
$$
x(s,t)=x_0+s,
$$
$$
y(s,t)=y_0+t,
$$
and
$$
z(s,t)
=
\phi(x_0+s,y_0+t)
$$
for
$$
|s|,|t|<\varepsilon.
$$


::: pf-proof

The first two component functions are affine, and the third is the composition of the $C^1$ function $\phi$ with an affine map.
Thus all three component functions are continuously differentiable.

:::

:::

::: {.pf-step #s1-6}

The parametrization passes through the prescribed point:
$$
\boxed{
(x(0,0),y(0,0),z(0,0))
=(x_0,y_0,z_0).
}
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
x(0,0)=x_0,
\qquad
y(0,0)=y_0.
$$
By step [](#s1-3){.pf-ref},
$$
z(0,0)
=
\phi(x_0,y_0)
=
z_0.
$$

:::

:::

::: {.pf-step #s1-7}

The entire parametrized surface lies in the zero level set of $f$:
$$
\boxed{
f(x(s,t),y(s,t),z(s,t))=0
}
$$
for all sufficiently small $s,t$.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
(x_0+s,y_0+t)\in U.
$$
Using step [](#s1-5){.pf-ref} and the identity from step [](#s1-3){.pf-ref},
$$
\begin{aligned}
f(x(s,t),y(s,t),z(s,t))
&=
f\bigl(
x_0+s,
y_0+t,
\phi(x_0+s,y_0+t)
\bigr)\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

The map
$$
\Psi(s,t)
=
\bigl(
x(s,t),
y(s,t),
z(s,t)
\bigr)
$$
is a differentiable parametrized surface near $(0,0)$.


::: pf-proof

By step [](#s1-5){.pf-ref}, $\Psi$ is $C^1$.
Its partial derivatives are
$$
\Psi_s
=
\bigl(
1,0,\phi_x(x_0+s,y_0+t)
\bigr)
$$
and
$$
\Psi_t
=
\bigl(
0,1,\phi_y(x_0+s,y_0+t)
\bigr).
$$
These two vectors are linearly independent because their first two coordinates are
$$
(1,0)
\quad\text{and}\quad
(0,1).
$$
Thus the parametrization has rank $2$ and defines a regular differentiable surface.

:::

:::

::: {.pf-step #s1-9}

Therefore there exists a differentiable parametrized surface through $(x_0,y_0,z_0)$ on which
$$
\boxed{f=0}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives passage through the required point, step [](#s1-7){.pf-ref} places the image in the level set, and step [](#s1-8){.pf-ref} proves regularity of the parametrization.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
