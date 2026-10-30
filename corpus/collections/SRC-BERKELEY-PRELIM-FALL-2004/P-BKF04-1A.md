---
schema: qual/card@1
id: P-BKF04-1A
kind: problem
title: The delay integral equation $y(x)=\int_0^\infty e^{-2s}y(x-s)\,ds$ with $y=e^x$ on $x\le0$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Show that there is a unique piecewise continuous function $y(x)$ on $\RR$ satisfying the two conditions
$$
\begin{aligned}
y(x) &= \int_{0}^{\infty} e^{-2s}\, y(x-s)\, ds && \text{for } x > 0, \text{ and} \\
y(x) &= e^{x} && \text{for } x \le 0,
\end{aligned}
$$
and find an explicit formula for $y(x)$ for $x > 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A function $y$ with $y(x)=e^x$ for $x\le0$ satisfies the integral equation for $x>0$ if and only if
$$
e^{2x}y(x)=\int_{-\infty}^{x}e^{2t}y(t)\,dt\qquad(x>0).
$$

::: pf-proof

The substitution $t=x-s$ gives $\int_0^\infty e^{-2s}y(x-s)\,ds=\int_{-\infty}^x e^{-2(x-t)}y(t)\,dt$. Multiply by $e^{2x}$.

:::

:::

::: {.pf-step #s2}

A solution satisfies $y(x)=ce^{-x}$ for $x>0$, for some $c\in\RR$.

::: pf-proof

The right side of step [](#s1){.pf-ref} is continuous in $x$, so $y$ is continuous on $(0,\infty)$. Then the right side is differentiable with derivative $e^{2x}y(x)$, so $y$ is differentiable on $(0,\infty)$. Differentiation gives $e^{2x}(y'+2y)=e^{2x}y$, so $y'=-y$ on $(0,\infty)$.

:::

:::

::: {.pf-step #s3}

$c=\frac13$.

::: pf-proof

Substitute step [](#s2){.pf-ref} into step [](#s1){.pf-ref}: for $x>0$,
$$
ce^{x}=\int_{-\infty}^0e^{3t}\,dt+\int_0^x ce^{t}\,dt=\frac13+c(e^x-1),
$$
so $c=\frac13$.

:::

:::

::: {.pf-step #s4}

The function with $y(x)=\frac13e^{-x}$ for $x>0$ and $y(x)=e^x$ for $x\le0$ is a solution.

::: pf-proof

It is piecewise continuous. The computation of step [](#s3){.pf-ref} with $c=\frac13$ shows that it satisfies the identity of step [](#s1){.pf-ref}, which is equivalent to the integral equation.

:::

:::

::: pf-qed

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref} any solution equals the function of step [](#s4){.pf-ref}, which is a solution. So the solution is unique, and $y(x)=\frac13e^{-x}$ for $x>0$.

:::

:::

:::
