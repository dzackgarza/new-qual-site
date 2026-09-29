---
schema: qual/card@1
id: P-5YTY5
kind: problem
title: The line integral $\int_\Delta y\,dx+2x\,dy$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $\Delta$ be the triangular boundary in $\mathbb{R}^2$ with vertices $(0,1)$, $(2,0)$, and $(2,1)$, traversed counterclockwise.
Evaluate the line integral:
$$I = \oint_{\Delta} y \, dx + 2x \, dy.$$
:::

::: {.solution}
**Goal:** Evaluate the closed line integral $\oint_\Delta y\,dx + 2x\,dy$ around the oriented triangle using Green's Theorem.

::: pf

::: pf-step
Setting up Green's Theorem:

::: pf-proof

::: pf-step
Let $D \subset \mathbb{R}^2$ be the filled triangular region enclosed by the positively oriented (counterclockwise) boundary curve $\partial D = \Delta$.
:::

::: pf-step
The vector field components are:
$$P(x, y) = y, \qquad Q(x, y) = 2x.$$
:::

::: pf-step
Both $P$ and $Q$ have continuous partial derivatives on $\mathbb{R}^2$:
$$\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}(2x) = 2, \qquad \frac{\partial P}{\partial y} = \frac{\partial}{\partial y}(y) = 1.$$
:::

::: pf-step
By **Green's Theorem**:
$$\oint_{\Delta} P \, dx + Q \, dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx \, dy = \iint_D (2 - 1) \, dA = \iint_D 1 \, dA = \operatorname{Area}(D).$$
:::

:::

:::

::: pf-step
Computation of the Area of the Triangular Region $D$:

::: pf-proof

::: pf-step
The vertices of the triangle are $A = (0, 1)$, $B = (2, 0)$, and $C = (2, 1)$.
:::

::: pf-step
Notice that the side $AC$ is the horizontal line segment from $(0, 1)$ to $(2, 1)$ of length $2$.
:::

::: pf-step
The side $BC$ is the vertical line segment from $(2, 0)$ to $(2, 1)$ of height $1$.
:::

::: pf-step
Since $AC$ is horizontal and $BC$ is vertical, the angle at vertex $C = (2, 1)$ is a **right angle** ($90^\circ$).
:::

::: pf-step
Thus $D$ is a right-angled triangle with base $b = 2$ and height $h = 1$.
:::

::: pf-step
The area of $D$ is:
$$\operatorname{Area}(D) = \frac{1}{2} \cdot \text{base} \cdot \text{height} = \frac{1}{2} \cdot 2 \cdot 1 = 1.$$
:::

:::

:::

::: pf-step
Alternative Direct Line Integral Computation:

::: pf-proof

::: pf-step
**Path 1 ($A(0,1) \to B(2,0)$):** Parameterize $r_1(t) = (2t, 1 - t)$ for $t \in [0, 1]$.

- $dx = 2\,dt$, $dy = -dt$.
- $\int_{C_1} y\,dx + 2x\,dy = \int_0^1 (1 - t)(2) + 2(2t)(-1) \, dt = \int_0^1 (2 - 2t - 4t) \, dt = \int_0^1 (2 - 6t) \, dt = 2 - 3 = -1$.
:::

::: pf-step
**Path 2 ($B(2,0) \to C(2,1)$):** Parameterize $r_2(t) = (2, t)$ for $t \in [0, 1]$.

- $dx = 0$, $dy = dt$.
- $\int_{C_2} y\,dx + 2x\,dy = \int_0^1 2(2) \, dt = 4$.
:::

::: pf-step
**Path 3 ($C(2,1) \to A(0,1)$):** Parameterize $r_3(t) = (2 - 2t, 1)$ for $t \in [0, 1]$.

- $dx = -2\,dt$, $dy = 0$.
- $\int_{C_3} y\,dx + 2x\,dy = \int_0^1 (1)(-2) \, dt = -2$.
:::

::: pf-step
Summing all three edges:
$$I = (-1) + 4 + (-2) = 1.$$
:::

:::

:::

::: pf-step
Conclusion:
The value of the line integral is $1$.
:::

:::
:::
