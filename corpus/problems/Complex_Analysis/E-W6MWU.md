---
schema: qual/card@1
id: E-W6MWU
kind: problem
title: The Cayley map $\HH\to\DD$ from a cross-ratio
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

::: {.exercise}
Find a conformal map $\HH \to \DD$ using cross-ratios.
:::

::: {.hint}
Send $i$, a point of $\HH$, to $0$ and its reflection $-i$ across $\RR$ to $\infty$; symmetry of points is preserved by Möbius maps.
:::

::: {.solution}
::: pf

::: {.pf-step #def}
The Möbius map with $\infty\mapsto1$, $i\mapsto0$, $-i\mapsto\infty$ is $F(z) = \frac{z-i}{z+i}$.

::: pf-proof
The cross-ratio sending $(\infty, i, -i)$ to $(1, 0, \infty)$ is
$$
F(z) = \frac{z-i}{z+i}\cdot\frac{\infty+i}{\infty-i} = \frac{z-i}{z+i}.
$$
:::

:::

::: pf-step
$F$ maps $\HH$ conformally onto $\DD$.

::: pf-proof
$\abs{F(z)} < 1$ if and only if $z$ is closer to $i$ than to $-i$, that is, $\Im z > 0$.
So the Möbius map $F$ sends $\HH$ into $\DD$ and $\CC\setminus\overline{\HH}$ into $\CC\setminus\overline{\DD}$, and $\RR\cup\theset{\infty}$ onto $\partial\DD$.
Since $F$ is a bijection of the Riemann sphere, $F(\HH) = \DD$.
:::

:::

:::

:::
