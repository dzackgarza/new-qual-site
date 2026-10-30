---
schema: qual/card@1
id: P-TRIV-DE39
kind: problem
title: First-order PDE $f_x+af_y+(x-2y)f=0$ by characteristics
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 39, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the most general solution of $\frac{\partial f}{\partial x} + a\frac{\partial f}{\partial y} + (x - 2y)f = 0$.
:::

::: {.solution}

::: pf

::: pf-step

The characteristic curves satisfy
$$
\frac{dy}{dx}=a,
$$
so
$$
\eta=y-ax
$$
is constant along each characteristic.


::: pf-proof

The transport part of the PDE is $f_x+af_y$, whose characteristic equations are $dx/ds=1$ and $dy/ds=a$. Dividing gives $dy/dx=a$, hence $y-ax$ is constant.

:::

:::

::: {.pf-step #s1-2}

Along a characteristic $y=ax+\eta$, the function $F(x)=f(x,ax+\eta)$ satisfies
$$
F'(x)+\bigl((1-2a)x-2\eta\bigr)F(x)=0.
$$


::: pf-proof

By the chain rule,
$$
F'(x)=f_x(x,ax+\eta)+a f_y(x,ax+\eta).
$$
Substitute $y=ax+\eta$ into $x-2y$ in the PDE to obtain
$$
x-2(ax+\eta)=(1-2a)x-2\eta.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
F(x)=C(\eta)\exp\left(-\frac{1-2a}{2}x^2+2\eta x\right),
$$
where $C$ is an arbitrary function.


::: pf-proof

Step [](#s1-2){.pf-ref} is separable:
$$
\frac{F'}F=-((1-2a)x-2\eta).
$$
Integrating in $x$ gives
$$
\log F=-\frac{1-2a}{2}x^2+2\eta x+\log C(\eta).
$$

:::

:::

::: {.pf-step #s1-4}

Substituting $\eta=y-ax$ into step [](#s1-3){.pf-ref} gives
$$
F(x)=C(y-ax)\exp\left(2xy-\left(a+\frac12\right)x^2\right).
$$


::: pf-proof

The exponent in step [](#s1-3){.pf-ref} becomes
$$
-\frac{1-2a}{2}x^2+2x(y-ax)
\;=
-\frac{x^2}{2}-ax^2+2xy.
$$

:::

:::

::: {.pf-step #s1-5}

Hence, after simplification,
$$
\boxed{
f(x,y)=\Phi(y-ax)
\exp\left(2xy-\left(a+\frac12\right)x^2\right)}.
$$


::: pf-proof

Rename the arbitrary function $C$ in step [](#s1-4){.pf-ref} as $\Phi$. Every characteristic is labeled by $y-ax$, and $\Phi$ assigns its integration constant, so the family contains the general characteristic solution.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the most general solution.

:::

:::

:::
