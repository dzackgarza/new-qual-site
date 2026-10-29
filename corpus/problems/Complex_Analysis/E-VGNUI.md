---
schema: qual/card@1
id: E-VGNUI
kind: problem
title: $\int_\gamma \frac{f'(z)}{z-a}\,dz = \int_\gamma \frac{f(z)}{(z-a)^2}\,dz$ for holomorphic $f$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source says only that gamma lies in Omega; the identity needs gamma closed and a off gamma, so the statement adds both hypotheses.
---

::: {.exercise}
Suppose $f$ is holomorphic on $\Omega$, a simply connected region, and suppose $\gamma \subseteq \Omega$ is a closed curve and $a\in\Omega$ is a point not on $\gamma$.
Using the Cauchy integral formula, show that
$$
\int_\gamma {f'(z) \over z-a}\dz = \int_\gamma {f(z) \over (z-a)^2 }\dz.
$$
Also prove this when $\Omega$ is *not* simply connected.

:::

::: {.solution}
Let $n = n(\gamma, a)$ be the winding number of $\gamma$ about $a$.

::: pf

::: pf-step
If $\Omega$ is simply connected, both integrals equal $2\pi i\, n\, f'(a)$.

::: pf-proof
On a simply connected region the Cauchy integral formula applies to the holomorphic function $f'$ and gives $\int_\gamma \frac{f'(z)}{z-a}\dz = 2\pi i\, n\, f'(a)$.
The Cauchy integral formula for the first derivative of $f$ gives $\int_\gamma \frac{f(z)}{(z-a)^2}\dz = 2\pi i\, n\, f'(a)$.
:::

:::

::: pf-step
For any region $\Omega$, the two integrals are equal.

::: pf-proof
$G(z) \definedas \frac{f(z)}{z-a}$ is holomorphic on $\Omega\setminus\theset{a}$, which contains $\gamma$, and by the quotient rule
$$
G'(z) = {f'(z)\over z-a} - {f(z) \over (z-a)^2}.
$$
The integral of a derivative over a closed curve is $0$, so
$$
\int_\gamma {f'(z) \over z-a}\dz - \int_\gamma {f(z) \over (z-a)^2}\dz = \int_\gamma G'(z)\dz = G(\gamma(1)) - G(\gamma(0)) = 0.
$$
:::

:::

:::

:::
