---
schema: qual/card@1
id: P-CZ3R7
kind: problem
title: $|z-z_1|/|z-z_2|=c$ is a circle
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
(a) Prove that if $c>0$,
$$
\abs{w_1} = c\abs{w_2} \implies \abs{w_1 - c^2 w_2} = c\abs{w_1 - w_2}
.$$

(b) Prove that if $c>0$ and $c\neq 1$, with $z_1\neq z_2$, then the following equation represents a circle:
$$
\abs{z-z_1 \over z-z_2} = c
.$$
Find its center and radius.

> Hint: use part (a)

:::

::: {.solution}
::: pf

::: {.pf-step #expand}
For all $w_1, w_2\in\CC$ and $c>0$,
$$
\abs{w_1 - c^2 w_2}^2 - c^2\abs{w_1 - w_2}^2 = (1-c^2)\left(\abs{w_1}^2 - c^2\abs{w_2}^2\right).
$$

::: pf-proof
Expanding $\abs{u-v}^2 = \abs u^2 + \abs v^2 - 2\Re(u\bar v)$,
$$
\abs{w_1 - c^2 w_2}^2 = \abs{w_1}^2 + c^4\abs{w_2}^2 - 2c^2\Re(w_1\bar w_2),
\qquad
c^2\abs{w_1 - w_2}^2 = c^2\abs{w_1}^2 + c^2\abs{w_2}^2 - 2c^2\Re(w_1\bar w_2).
$$
The difference is $(1-c^2)\abs{w_1}^2 - c^2(1-c^2)\abs{w_2}^2$.
:::

:::

::: {.pf-step #part-a}
(a) If $\abs{w_1} = c\abs{w_2}$, then $\abs{w_1 - c^2 w_2} = c\abs{w_1 - w_2}$.

::: pf-proof
The right side of step [](#expand){.pf-ref} vanishes, so $\abs{w_1 - c^2 w_2}^2 = c^2\abs{w_1-w_2}^2$; both moduli are nonnegative and $c>0$, so taking square roots gives the claim.
:::

:::

::: pf-step
(b) The set $\theset{z\neq z_2 \st \abs{z-z_1} = c\abs{z-z_2}}$ is the circle with
$$
\boxed{\text{center } z_0 = \frac{z_1 - c^2 z_2}{1-c^2}, \qquad \text{radius } r = \frac{c\abs{z_1 - z_2}}{\abs{1-c^2}}.}
$$

::: pf-proof
Put $w_1 \coloneqq z - z_1$ and $w_2 \coloneqq z - z_2$, so that $w_1 - w_2 = z_2 - z_1$ and $w_1 - c^2 w_2 = (1-c^2)(z - z_0)$.
Since $c\neq 1$, step [](#expand){.pf-ref} shows that $\abs{w_1} = c\abs{w_2}$ holds if and only if $\abs{w_1 - c^2w_2} = c\abs{w_1 - w_2}$; the forward direction is part (a).
The second equation reads $\abs{1-c^2}\abs{z-z_0} = c\abs{z_1-z_2}$, that is, $\abs{z - z_0} = r$, and $r>0$ because $z_1\neq z_2$.
The point $z_2$ is not on this circle: $z_2 - z_0 = (z_2 - z_1)/(1-c^2)$ has modulus $\abs{z_1 - z_2}/\abs{1-c^2}\neq r$, because $c\neq 1$.
Hence the equation $\abs{(z-z_1)/(z-z_2)} = c$ holds exactly on the circle $\abs{z-z_0} = r$.
:::

:::

:::

:::
