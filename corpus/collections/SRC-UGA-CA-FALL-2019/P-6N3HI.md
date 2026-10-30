---
schema: qual/card@1
id: P-6N3HI
kind: problem
title: "Conformal map from a lune to the unit disk"
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
Find a conformal map from 
$$
D=\theset{ z\in \CC\st \abs{z}<1 \text{ and } \abs{ z-{1\over 2}}>{1\over 2}}
$$
to the unit disk $\Delta=\{z:\abs{z}<1\}$.
:::

::: {.solution}
The boundary circles $\abs{z}=1$ and $\abs{z-1/2}=1/2$ of $D$ are tangent at $z=1$.

::: pf

::: {.pf-step #maps-to-strip}
The Möbius map $w = \frac{1}{1-z}$ sends $D$ biholomorphically onto the strip $\{w : 1/2 < \Re w < 1\}$.

::: pf-proof

::: {.pf-step #circle1-to-line}
The circle $\abs{z} = 1$ maps to the line $\Re w = 1/2$.

::: pf-proof
For $z=e^{i\theta}$ with $\theta\notin2\pi\ZZ$, $\frac{1}{1-e^{i\theta}} = \frac{1}{2} + \frac{i}{2}\cot(\theta/2)$, and $z=1$ goes to $\infty$.
:::

:::

::: {.pf-step #circle2-to-line}
The circle $\abs{z - 1/2} = 1/2$ maps to the line $\Re w = 1$.

::: pf-proof
For $z = 1/2 + (1/2)e^{i\theta}$, $w = \frac{2}{1 - e^{i\theta}} = 1 + i\cot(\theta/2)$.
:::

:::

::: pf-step
$D$ maps onto the strip $\{w : 1/2 < \Re w < 1\}$.

::: pf-proof
By steps [](#circle1-to-line){.pf-ref} and [](#circle2-to-line){.pf-ref}, the Möbius map sends $D$ onto one component of the complement of the lines $\Re w=1/2$ and $\Re w=1$.
The point $z=-1/2\in D$ goes to $w=2/3$, so that component is the strip.
:::

:::

:::

:::

::: {.pf-step #strip-to-disk}
The map $w\mapsto \frac{e^{\pi i(2w-1)} - i}{e^{\pi i(2w-1)} + i}$ sends the strip $\{1/2 < \Re w < 1\}$ biholomorphically onto $\Delta$.

::: pf-proof

::: pf-step
$\zeta = 2w - 1$ maps the strip onto $\{0 < \Re \zeta < 1\}$.

::: pf-proof
It maps $\Re w = 1/2$ to $\Re \zeta = 0$ and $\Re w = 1$ to $\Re \zeta = 1$.
:::

:::

::: pf-step
$\eta = e^{\pi i \zeta}$ maps $\{0 < \Re \zeta < 1\}$ biholomorphically onto the upper half-plane $\HH$.

::: pf-proof
If $\zeta=x+iy$ with $0<x<1$, then $e^{\pi i\zeta}=e^{-\pi y}e^{i\pi x}$ has argument $\pi x\in(0,\pi)$.
Conversely every point of $\HH$ has a unique logarithm with imaginary part in $(0,\pi)$, so this map is a bijection onto $\HH$.
:::

:::

::: pf-step
$\xi = \frac{\eta - i}{\eta + i}$ maps $\HH$ biholomorphically onto $\Delta$.

::: pf-proof
This is the Cayley transform.
:::

:::

:::

:::

::: pf-step
A conformal map $D \to \Delta$ is
$$
\boxed{z \mapsto \frac{e^{\pi i(2/(1-z) - 1)} - i}{e^{\pi i(2/(1-z) - 1)} + i}}.
$$

::: pf-proof
This is the composition of the maps of steps [](#maps-to-strip){.pf-ref} and [](#strip-to-disk){.pf-ref}.
:::

:::

:::

:::
