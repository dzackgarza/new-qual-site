---
schema: qual/card@1
id: P-TWN5M
kind: problem
title: Circles, lines and half-planes in $\CC$ defined by moduli and real parts
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Geometrically describe the following subsets of $\CC$:

(a) $\abs{z-1} = 1$

(b) $\abs{z-1} = 2\abs{z-2}$

(c) $1/z = \bar z$

(d) $\Re(z) = 3$

(e) $\Im(z) = a$ with $a\in \RR$.

(f) $\Re(z) > a$ with $a\in \RR$.

(g) $\abs{z-1} < 2\abs{z-2}$
:::

::: {.solution}
Write $z = x + iy$ with $x, y \in \RR$.

::: pf

::: pf-step

(a) The set is the circle of radius $1$ centered at $1$.

::: pf-proof

$\abs{z-1}$ is the distance from $z$ to $1$.

:::

:::

::: {.pf-step #apollonius}

(b) The set is the circle of radius $\frac23$ centered at $\frac73$.

::: pf-proof

Squaring, $\abs{z-1} = 2\abs{z-2}$ is equivalent to
$$
\begin{aligned}
(x-1)^2 + y^2 - 4\qty((x-2)^2 + y^2) &= 0, \\
-3x^2 + 14x - 3y^2 - 15 &= 0, \\
x^2 - \tfrac{14}{3}x + y^2 + 5 &= 0, \\
\qty(x - \tfrac73)^2 + y^2 &= \tfrac{49}{9} - 5 = \qty(\tfrac23)^2.
\end{aligned}
$$

:::

:::

::: pf-step

(c) The set is the unit circle $\abs{z} = 1$.

::: pf-proof

For $z \neq 0$, multiplying $1/z = \bar z$ by $z$ gives the equivalent equation $1 = z\bar z = \abs{z}^2$.

:::

:::

::: pf-step

(d) The set is the vertical line through $3$.

::: pf-proof

The condition is $x = 3$ with $y$ arbitrary.

:::

:::

::: pf-step

(e) The set is the horizontal line through $ia$.

::: pf-proof

The condition is $y = a$ with $x$ arbitrary.

:::

:::

::: pf-step

(f) The set is the open half-plane to the right of the vertical line through $a$.

::: pf-proof

The condition is $x > a$ with $y$ arbitrary.

:::

:::

::: pf-step

(g) The set is the exterior of the circle of radius $\frac23$ centered at $\frac73$.

::: pf-proof

The computation of step [](#apollonius){.pf-ref} with $<$ in place of $=$ gives $-3x^2 + 14x - 3y^2 - 15 < 0$. Dividing by $-3$ reverses the inequality, so the condition is $\qty(x - \frac73)^2 + y^2 > \qty(\frac23)^2$.

:::

:::

:::

:::
