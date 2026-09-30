---
schema: qual/card@1
id: P-64ZUP
kind: problem
title: Conformal map from $\{|z|<1,\ |z-1/2|>1/2\}$ onto the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$ to the unit disk $\Delta=\{z: \ |z|<1\}$.
:::

::: {.solution}
::: pf

::: pf-step
$D$ is the unit disk with the disk $\{|z - 1/2| \le 1/2\}$ removed; it is a simply connected region bounded by two circles tangent at $z = 1$.

::: pf-proof
the two circles $|z| = 1$ and $|z - 1/2| = 1/2$ are tangent at $z = 1$.
:::

:::

::: pf-step
The Möbius map $w = \frac{1}{1-z}$ sends $z = 1$ to $\infty$ and maps the two tangent circles to two parallel lines.

::: pf-proof
a Möbius map sending the tangency point to $\infty$ turns the two tangent circles into parallel lines.
:::

:::

::: {.pf-step #maps-to-strip}
Under $w = \frac{1}{1-z}$, the region $D$ maps to a vertical strip.

::: pf-proof

::: {.pf-step #circle1-to-line}
The circle $|z| = 1$ maps to the line $\operatorname{Re} w = 1/2$.

::: pf-proof
for $|z| = 1$, $w = \frac{1}{1-z}$ satisfies $\operatorname{Re} w = 1/2$ (since $\frac{1}{1-e^{i\theta}} = \frac{1}{2} + \frac{i}{2}\cot(\theta/2)$).
:::

:::

::: {.pf-step #circle2-to-line}
The circle $|z - 1/2| = 1/2$ maps to the line $\operatorname{Re} w = 1$.

::: pf-proof
for $z = 1/2 + (1/2)e^{i\theta}$, $w = \frac{1}{1-z} = \frac{1}{1/2 - (1/2)e^{i\theta}} = \frac{2}{1 - e^{i\theta}}$, whose real part is $1$.
:::

:::

::: pf-step
Hence $D$ maps to the strip $\{w : 1/2 < \operatorname{Re} w < 1\}$.

::: pf-proof
Steps [](#circle1-to-line){.pf-ref} and [](#circle2-to-line){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #strip-to-disk}
Map the strip $\{1/2 < \operatorname{Re} w < 1\}$ to the unit disk.

::: pf-proof

::: pf-step
First translate and scale to the strip $\{0 < \operatorname{Re} \zeta < 1\}$ via $\zeta = 2w - 1$.

::: pf-proof
$\zeta = 2w - 1$ maps $\operatorname{Re} w = 1/2$ to $\operatorname{Re} \zeta = 0$ and $\operatorname{Re} w = 1$ to $\operatorname{Re} \zeta = 1$.
:::

:::

::: pf-step
The map $\eta = e^{\pi i \zeta}$ sends the strip $\{0 < \operatorname{Re} \zeta < 1\}$ to the upper half-plane.

::: pf-proof
If $\zeta=x+iy$ with $0<x<1$, then
\[
e^{\pi i\zeta}=e^{-\pi y}e^{i\pi x},
\]
whose argument lies in $(0,\pi)$.
Conversely every point of $\HH$ has a unique logarithm with argument in $(0,\pi)$, so this is a biholomorphism from the vertical strip onto $\HH$.
:::

:::

::: pf-step
The map $\xi = \frac{\eta - i}{\eta + i}$ sends the upper half-plane to the unit disk.

::: pf-proof
the Cayley transform.
:::

:::

:::

:::

::: {.pf-step #composed-map}
Composing, a conformal map $D \to \Delta$ is $$z \mapsto \frac{e^{\pi i(2/(1-z) - 1)} - i}{e^{\pi i(2/(1-z) - 1)} + i}.$$

::: pf-proof
Steps [](#maps-to-strip){.pf-ref} and [](#strip-to-disk){.pf-ref}.
:::

:::

::: pf-qed
Step [](#composed-map){.pf-ref}.
:::

:::

:::
