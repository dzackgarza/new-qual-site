---
schema: qual/card@1
id: P-TRIV-DE11
kind: problem
title: Integrating factor for $(xy^2-y)\,dx+x\,dy=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve

$$
( x y ^ { 2 } - y ) \mathrm { d } x + x \mathrm { d } y = 0
$$
:::

Write
$$
M(x,y)=xy^2-y,
\qquad
N(x,y)=x.
$$

::: pf

::: pf-step

The differential form
$$
M\,dx+N\,dy
$$
is not exact.


::: pf-proof

One has
$$
M_y=2xy-1,
$$
while
$$
N_x=1.
$$
These are not equal in general.

:::

:::

::: pf-step

For $y\neq0$,
$$
\frac{N_x-M_y}{M}
=
-\frac2y.
$$


::: pf-proof

Compute
$$
N_x-M_y
=
1-(2xy-1)
=
2(1-xy),
$$
while
$$
M
=
y(xy-1).
$$
Therefore
$$
\frac{N_x-M_y}{M}
=
\frac{2(1-xy)}{y(xy-1)}
=
-\frac2y.
$$

:::

:::

::: pf-step

Hence an integrating factor depending only on $y$ is
$$
\mu(y)
=
\exp\left(
\int -\frac2y\,dy
\right)
=
y^{-2}.
$$


::: pf-proof

For a differential form $Mdx+Ndy$, if $(N_x-M_y)/M$ depends only on $y$, then
$$
\mu(y)
=
\exp\int\frac{N_x-M_y}{M},dy
$$
is an integrating factor.
Apply step <1>2.

:::

:::

::: pf-step

Multiplying by $y^{-2}$ gives
$$
\left(
x-\frac1y
\right)dx
+
\frac{x}{y^2},dy
=0.
$$


::: pf-proof

Multiply each coefficient of the original form by $y^{-2}$.

:::

:::

::: pf-step

The form in step <1>4 is exact.


::: pf-proof

One has
$$
\frac{\partial}{\partial y}
\left(
x-\frac1y
\right)
=
\frac1{y^2},
$$
and
$$
\frac{\partial}{\partial x}
\left(
\frac{x}{y^2}
\right)
=
\frac1{y^2}.
$$

:::

:::

::: pf-step

A potential function is
$$
F(x,y)
=
\frac{x^2}{2}
-
\frac{x}{y}.
$$


::: pf-proof

Integrate the $dx$-coefficient from step <1>4 with respect to $x$:
$$
\int
\left(
x-\frac1y
\right)dx
=
\frac{x^2}{2}
-
\frac{x}{y}
+
h(y).
$$
Differentiating with respect to $y$ gives
$$
\frac{x}{y^2}+h'(y).
$$
Matching the $dy$-coefficient in step <1>4 forces $h'(y)=0$.

:::

:::

::: pf-step

Therefore every nonzero solution satisfies
$$
\boxed{
\frac{x^2}{2}
-
\frac{x}{y}
=
C.
}
$$


::: pf-proof

For an exact differential equation $dF=0$, the potential $F$ is constant along solutions.

:::

:::

::: pf-step

Solving for $y$ gives
$$
\boxed{
y(x)
=
\frac{2x}{x^2+C_1},
}
$$
on intervals where the denominator is nonzero.


::: pf-proof

From step <1>7,
$$
\frac{x}{y}
=
\frac{x^2}{2}-C.
$$
Thus
$$
y
=
\frac{x}{x^2/2-C}
=
\frac{2x}{x^2-2C}.
$$
Rename the arbitrary constant $-2C$ as $C_1$.

:::

:::

::: pf-step

The function
$$
\boxed{y\equiv0}
$$
is also a solution.


::: pf-proof

Substitution into the original differential form gives
$$
(x\cdot0^2-0)dx+x\,d(0)=0.
$$
This solution was excluded from steps <1>2--<1>8 because the integrating factor $y^{-2}$ is undefined at $y=0$.

:::

:::

::: pf-qed

Steps <1>8--<1>9 give the complete solution family.

:::

:::
