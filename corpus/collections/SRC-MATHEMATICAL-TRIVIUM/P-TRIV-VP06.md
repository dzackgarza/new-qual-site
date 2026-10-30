---
schema: qual/card@1
id: P-TRIV-VP06
kind: problem
title: Euler--Lagrange equations for a particle in a potential
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the functional $S[x, y, z] = \int_{t_1}^{t_2} dt\, L(x, y, z, x', y', z')$, where
$$
L = \frac{m}{2}(x'^2 + y'^2 + z'^2) - U(x, y, z), \tag{14}
$$
and $U$ is a $C^1$ function of $x, y, z$. Write the system of equations on $x(t), y(t), z(t)$ whose solution is an extremum of $S[x, y, z]$ in a class of $C^2([t_1, t_2])$ functions with fixed boundary conditions.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For the coordinate $x$, the Euler--Lagrange equation is
$$
\frac d{dt}
\frac{\partial L}{\partial x'}
-
\frac{\partial L}{\partial x}
=0.
$$


::: pf-proof

The endpoint values are fixed, so admissible variations vanish at
$t_1,t_2$. The usual first-variation argument for the coordinate $x$ gives
the Euler--Lagrange equation.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\frac{\partial L}{\partial x'}=mx'
$$
and
$$
\frac{\partial L}{\partial x}=-U_x.
$$


::: pf-proof

Differentiate
$$
L
=
\frac m2
\left(
(x')^2+(y')^2+(z')^2
\right)
-
U(x,y,z)
$$
with respect to $x'$ and $x$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{mx''=-U_x(x,y,z)}.
$$


::: pf-proof

Substitute step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref}:
$$
\frac d{dt}(mx')+U_x=0.
$$

:::

:::

::: {.pf-step #s1-4}

The same argument for the coordinate $y$ gives
$$
\boxed{my''=-U_y(x,y,z)}.
$$


::: pf-proof

Now
$$
\frac{\partial L}{\partial y'}=my',
\qquad
\frac{\partial L}{\partial y}=-U_y.
$$
Substitute into the Euler--Lagrange equation for $y$.

:::

:::

::: {.pf-step #s1-5}

The same argument for the coordinate $z$ gives
$$
\boxed{mz''=-U_z(x,y,z)}.
$$


::: pf-proof

Use
$$
\frac{\partial L}{\partial z'}=mz',
\qquad
\frac{\partial L}{\partial z}=-U_z.
$$

:::

:::

::: {.pf-step #s1-6}

Hence the extremals satisfy
$$
\boxed{
m
\begin{pmatrix}
x''\\
y''\\
z''
\end{pmatrix}
=
-\nabla U(x,y,z).
}
$$


::: pf-proof

Collect the three scalar equations from steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} into vector form.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required Euler--Lagrange system.

:::

:::

:::
