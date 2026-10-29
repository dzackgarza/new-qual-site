---
schema: qual/card@1
id: P-UCLAB15F-05
kind: problem
title: Cyclic derivative identity from the implicit function theorem
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
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $F(x,y,z)$ be continuously differentiable with all three partial derivatives nonzero at $(0,0,0)$.
Define functions
$$
x=x(y,z),\qquad y=y(x,z),\qquad z=z(x,y)
$$
locally as the solutions of
$$
F(x,y,z)=F(0,0,0)
$$
near $(0,0)$ in the corresponding pairs of variables.
Prove that
$$
\frac{\partial x}{\partial y}
\frac{\partial y}{\partial z}
\frac{\partial z}{\partial x}=-1,
$$
where all three derivatives are evaluated at $(0,0)$ in their corresponding variable pairs.
:::

::: {.solution}

Write
$$
F_x,F_y,F_z
$$
for the three partial derivatives of $F$, evaluated at $(0,0,0)$ when no arguments are displayed.

::: pf

::: pf-step

The implicit function theorem defines each of the three local functions in the statement.


::: pf-proof

Since
$$
F_x(0,0,0)\ne0,
$$
the implicit function theorem solves
$$
F(x,y,z)=F(0,0,0)
$$
locally for
$$
x=x(y,z).
$$
Similarly,
$$
F_y(0,0,0)\ne0
$$
gives
$$
y=y(x,z),
$$
and
$$
F_z(0,0,0)\ne0
$$
gives
$$
z=z(x,y).
$$
All three functions are continuously differentiable near the origin.

:::

:::

::: {.pf-step #s1-2}

Differentiating
$$
F(x(y,z),y,z)=F(0,0,0)
$$
with respect to $y$ gives
$$
F_x\,\frac{\partial x}{\partial y}
+
F_y
=0
$$
at the origin.


::: pf-proof

Apply the chain rule while holding $z$ fixed:
$$
\frac{\partial}{\partial y}
F(x(y,z),y,z)
=
F_x(x(y,z),y,z)x_y
+
F_y(x(y,z),y,z).
$$
The right side of the level equation is constant, so its derivative is zero.
Evaluating at $(y,z)=(0,0)$ gives the displayed identity.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\frac{\partial x}{\partial y}
=
-\frac{F_y}{F_x}
}
$$
at the origin.


::: pf-proof

Solve the identity in step [](#s1-2){.pf-ref} for $x_y$.
The denominator is nonzero by hypothesis.

:::

:::

::: {.pf-step #s1-4}

Differentiating
$$
F(x,y(x,z),z)=F(0,0,0)
$$
with respect to $z$ gives
$$
\boxed{
\frac{\partial y}{\partial z}
=
-\frac{F_z}{F_y}
}
$$
at the origin.


::: pf-proof

Holding $x$ fixed and applying the chain rule gives
$$
F_y\,y_z+F_z=0.
$$
Since $F_y\ne0$, solve for $y_z$.

:::

:::

::: {.pf-step #s1-5}

Differentiating
$$
F(x,y,z(x,y))=F(0,0,0)
$$
with respect to $x$ gives
$$
\boxed{
\frac{\partial z}{\partial x}
=
-\frac{F_x}{F_z}
}
$$
at the origin.


::: pf-proof

Holding $y$ fixed and applying the chain rule gives
$$
F_x+F_z\,z_x=0.
$$
Since $F_z\ne0$, solve for $z_x$.

:::

:::

::: {.pf-step #s1-6}

Multiplying the three identities gives
$$
\boxed{
\frac{\partial x}{\partial y}
\frac{\partial y}{\partial z}
\frac{\partial z}{\partial x}
=
-1
}.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref},
$$
\begin{aligned}
x_y\,y_z\,z_x
&=
\left(-\frac{F_y}{F_x}\right)
\left(-\frac{F_z}{F_y}\right)
\left(-\frac{F_x}{F_z}\right)\\
&=
-1.
\end{aligned}
$$
All factors cancel because each of $F_x,F_y,F_z$ is nonzero.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required cyclic derivative identity.

:::

:::

:::
