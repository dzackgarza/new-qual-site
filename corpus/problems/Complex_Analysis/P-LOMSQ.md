---
schema: qual/card@1
id: P-LOMSQ
kind: problem
title: Cayley map $\HH\to\DD$ and the image of the first quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Find a fractional linear transformation $T$ which maps $\HH$ to $\DD$, and explicitly describe the image of the first quadrant under $T$.
:::

::: {.solution}
Let $Q = \theset{x + iy \suchthat x > 0, y > 0}$ be the first quadrant.

::: pf

::: {.pf-step #cayley-map}
$\boxed{T(z) = \frac{z - i}{z + i}}$ is a Möbius transformation mapping $\HH$ conformally onto $\DD$.

::: pf-proof
For real $z$, $\abs{z - i} = \abs{z + i}$, so $T$ sends the boundary $\RR \cup \theset{\infty}$ of $\HH$ onto the unit circle. A Möbius map is a bijection of the Riemann sphere, so it sends each component of the complement of $\RR\cup\theset{\infty}$ onto a component of the complement of the unit circle. Since $T(i) = 0$, it sends $\HH$ onto $\DD$.
:::

:::

::: {.pf-step #positive-real-axis-image}
$T$ maps the positive real axis onto the open lower semicircle $\theset{e^{i\theta} \suchthat -\pi < \theta < 0}$.

::: pf-proof
For $x > 0$, $\abs{T(x)} = 1$. As $x$ runs from $0$ to $\infty$, $T(x)$ moves continuously and injectively on the unit circle from $T(0) = -1$ to $T(\infty) = 1$, passing through $T(1) = \frac{1-i}{1+i} = -i$; so it traces the lower semicircle.
:::

:::

::: {.pf-step #positive-imaginary-axis-image}
$T$ maps the positive imaginary axis onto the interval $(-1, 1)$.

::: pf-proof
For $y > 0$, $T(iy) = \frac{y-1}{y+1}$, which increases from $-1$ to $1$ as $y$ runs from $0$ to $\infty$.
:::

:::

::: pf-step
$T(Q)$ is the lower half-disk $\boxed{\theset{w \in \DD \suchthat \Im w < 0}}$.

::: pf-proof
The boundary of $Q$ in the Riemann sphere is the positive real axis, the positive imaginary axis, $0$ and $\infty$. By steps [](#positive-real-axis-image){.pf-ref} and [](#positive-imaginary-axis-image){.pf-ref}, $T$ maps it onto the boundary of the lower half-disk: the lower semicircle, the diameter $(-1,1)$, and the points $-1=T(0)$ and $1=T(\infty)$. Since $T$ is a homeomorphism of the sphere, $T(Q)$ is a component of the complement of that closed curve, contained in $\DD$ by step [](#cayley-map){.pf-ref}. The sample point $1+i\in Q$ maps to $T(1+i) = \frac{1}{2+i} = \frac{2 - i}{5}$, which has negative imaginary part, so $T(Q)$ is the lower half-disk.
:::

:::

:::
:::
