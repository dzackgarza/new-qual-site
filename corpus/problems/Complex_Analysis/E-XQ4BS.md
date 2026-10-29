---
schema: qual/card@1
id: E-XQ4BS
kind: problem
title: $z+3+2e^z$ has one root in $\{\Re z\le 0\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Show that $h(z) = z + 3 + 2e^z$ has one root in $\theset{ \Re(z) \leq 0}$.
:::

::: {.solution}
Fix $R>5$ and let $\gamma_R$ be the boundary of the half-disc $\{\abs{z}<R,\ \Re z<0\}$: the segment $C_1$ from $-iR$ to $iR$ and the left semicircle $C_R$.

![](../../assets/figures/2021-07-29_20-39-31.png)

::: pf

::: {.pf-step #dominate}
If $\Re z\le0$ and either $\Re z = 0$ or $\abs{z}\ge R$, then $\abs{2e^z} < \abs{z+3}$.

::: pf-proof
For $\Re z\le0$, $\abs{2e^z} = 2e^{\Re z}\le 2$.
If $z = iy$, then $\abs{z+3} = \sqrt{9+y^2}\ge3>2$.
If $\abs{z}\ge R$, then $\abs{z+3}\ge R-3>2$.
:::

:::

::: {.pf-step #inside}
$h$ has exactly one zero in $\{\abs{z}<R,\ \Re z<0\}$.

::: pf-proof
By step [](#dominate){.pf-ref}, $\abs{2e^z}<\abs{z+3}$ on $\gamma_R$.
By Rouché's theorem, $h = (z+3) + 2e^z$ has as many zeros inside $\gamma_R$ as $z+3$, whose only zero $-3$ lies inside.
:::

:::

::: pf-step
$h$ has exactly one zero in $\{\Re z\le0\}$.

::: pf-proof
By step [](#dominate){.pf-ref}, $\abs{h(z)} \ge \abs{z+3} - \abs{2e^z} > 0$ on the imaginary axis and on $\{\Re z\le0,\ \abs{z}\ge R\}$, so every zero of $h$ in $\{\Re z\le 0\}$ lies in the open half-disc, where step [](#inside){.pf-ref} counts exactly one.
:::

:::

:::

:::
