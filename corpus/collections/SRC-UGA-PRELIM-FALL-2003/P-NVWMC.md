---
schema: qual/card@1
id: P-NVWMC
kind: problem
title: Line integral of $2xy\,dx+(x^2+y^2)\,dy$ from $(1,0)$ to $(0,1)$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
a) Let $\gamma$ be a path in the plane $\mathbb{R}^2$.
Define what is meant by $$\int_\gamma f(x,y)\,dx + g(x,y)\,dy.$$

b) Compute this line integral in the case where $f(x,y) = 2xy, g(x,y) = x^2 + y^2$ and $\gamma$ is the straight-line path from $P = (1,0)$ to $Q = (0,1)$.

c) Is there another path $\beta$ from $P$ to $Q$ such that the corresponding line integral takes a different value?
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
If $\gamma: [a,b] \to \RR^2$ is a piecewise-smooth path with $\gamma(t) = (x(t), y(t))$, then
$$\int_\gamma f\,dx + g\,dy = \int_a^b \left[ f(x(t), y(t))\, x'(t) + g(x(t), y(t))\, y'(t) \right] dt.$$

::: pf-proof
definition of the line integral of the differential form $f\,dx + g\,dy$ along $\gamma$.
:::

:::

:::

**Part (b).**

::: pf

::: pf-step
Parametrize $\gamma(t) = (1-t, t)$ for $t \in [0,1]$.

::: pf-proof
this is the straight line from $(1,0)$ to $(0,1)$.
:::

:::

::: pf-step
$x'(t) = -1$ and $y'(t) = 1$.

::: pf-proof
differentiate.
:::

:::

::: pf-step
The integrand is $f\,x' + g\,y' = 2xy(-1) + (x^2 + y^2)(1) = -2(1-t)t + (1-t)^2 + t^2$.

::: pf-proof
substitute $x = 1-t$, $y = t$.
:::

:::

::: pf-step
$\int_\gamma f\,dx + g\,dy = \int_0^1 \left[ -2t(1-t) + (1-t)^2 + t^2 \right] dt = \int_0^1 (1 - 4t + 4t^2)\, dt$.

::: pf-proof
expand $-2t + 2t^2 + 1 - 2t + t^2 + t^2 = 1 - 4t + 4t^2$.
:::

:::

::: {.pf-step #p2-5}
$\int_0^1 (1 - 4t + 4t^2)\, dt = \left[ t - 2t^2 + \tfrac{4}{3}t^3 \right]_0^1 = 1 - 2 + \tfrac{4}{3} = \tfrac{1}{3}$.

::: pf-proof
evaluate the antiderivative.
:::

:::

::: pf-step
Hence $\int_\gamma f\,dx + g\,dy = \tfrac{1}{3}$.

::: pf-proof
Step [](#p2-5){.pf-ref}.
:::

:::

:::

**Part (c).**

::: pf

::: {.pf-step #p3-1}
No such path $\beta$ exists.

::: pf-proof

::: {.pf-step #p3-1-1}
The form $f\,dx + g\,dy$ is exact.

::: pf-proof
$\frac{\partial f}{\partial y} = 2x = \frac{\partial g}{\partial x}$, so the form is closed; on the simply connected domain $\RR^2$ every closed form is exact.
:::

:::

::: {.pf-step #p3-1-2}
The line integral of an exact form depends only on the endpoints.

::: pf-proof
if $f\,dx + g\,dy = dF$, then $\int_\gamma f\,dx + g\,dy = F(Q) - F(P)$ by the fundamental theorem of line integrals.
:::

:::

::: pf-step
Hence every path from $P$ to $Q$ gives the same value $\tfrac{1}{3}$.

::: pf-proof
Steps [](#p3-1-1){.pf-ref} and [](#p3-1-2){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Step [](#p3-1){.pf-ref}.
:::

:::
:::
