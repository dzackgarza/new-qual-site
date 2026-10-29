---
schema: qual/card@1
id: E-WYJ7K
kind: problem
title: Conformal map from the lune between the tangent circles $\abs{z-i}=1$ and $\abs{z-i/2}=1/2$ to $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from the region bounded by $\abs{z - {i\over 2}} = {1\over 2}$ and $\abs{z-i} = 1$ to $\DD$.
:::

::: {.hint}
The two circles are internally tangent at $0$; inversion sends both to parallel lines.
:::

::: {.solution}
Let $\Omega = \theset{\abs{z-i}<1}\setminus\theset{\abs{z-i/2}\le1/2}$, the region between the circles.

::: pf

::: {.pf-step #strip}
$w = 1/z$ maps $\Omega$ conformally onto the strip $S = \theset{-1<\Im w<-\frac12}$.

::: pf-proof
The circle $\abs{z-ia}=a$ is $\abs z^2 = 2a\Im z$, and on it $\Im(1/z) = -\Im z/\abs z^2 = -\frac1{2a}$.
So $\abs{z-i}=1$ maps into $\Im w=-\frac12$ and $\abs{z-i/2}=\frac12$ maps into $\Im w=-1$.
The point $\frac32 i\in\Omega$ maps to $-\frac23 i\in S$, so $1/z$ maps $\Omega$ onto $S$.
:::

:::

::: {.pf-step #half-plane}
$w\mapsto e^{2\pi(w+i)}$ maps $S$ conformally onto $\HH$.

::: pf-proof
$w\mapsto2\pi(w+i)$ maps $S$ onto $\theset{0<\Im\zeta<\pi}$, which $\exp$ maps bijectively onto $\HH$.
:::

:::

::: pf-step
$$
\boxed{F(z) = \frac{\exp\qty(2\pi\qty(z^{-1}+i))-i}{\exp\qty(2\pi\qty(z^{-1}+i))+i}}
$$
maps $\Omega$ conformally onto $\DD$.

::: pf-proof
Compose steps [](#strip){.pf-ref} and [](#half-plane){.pf-ref} with the Cayley map $u\mapsto\frac{u-i}{u+i}$ from $\HH$ onto $\DD$.
:::

:::

:::

:::
