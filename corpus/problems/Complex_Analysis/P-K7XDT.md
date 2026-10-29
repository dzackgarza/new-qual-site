---
schema: qual/card@1
id: P-K7XDT
kind: problem
title: A conformal map from $\{\Re z>0,\ \abs{z-i}>1\}$ onto $\HH$
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Find a conformal map from $\Omega = \{z\in \CC \mid \abs{z-i} > 1,\, \Re(z) > 0\}$ to $\HH = \{w \in \CC \mid \Im(w) > 0\}$.
:::

::: {.solution}
Let $T(z)=\frac{z}{z-2i}$ and $Q=\{w:\Re w>0,\ \Im w>0\}$.

::: pf

::: {.pf-step #formula}
For $z = x+iy \neq 2i$,
$$
T(z)=\frac{\abs{z-i}^2-1+2ix}{\abs{z-2i}^2}.
$$

::: pf-proof
$T(z) = \frac{z(\bar z + 2i)}{\abs{z-2i}^2} = \frac{\abs{z}^2 - 2y + 2ix}{\abs{z-2i}^2}$, and $\abs{z}^2 - 2y = \abs{z-i}^2 - 1$.
:::

:::

::: {.pf-step #quadrant}
$T$ maps $\Omega$ biholomorphically onto $Q$.

::: pf-proof
$T$ is a Möbius transformation, hence a bijection of $\CC \setminus \{2i\}$ onto $\CC \setminus \{1\}$, and $2i \notin \Omega$, $1 \notin Q$.
By step [](#formula){.pf-ref}, for $z \neq 2i$ we have $T(z) \in Q$ exactly when $\abs{z-i} > 1$ and $x > 0$, that is, when $z \in \Omega$.
:::

:::

::: pf-step
$$
\boxed{F(z)=\left(\frac{z}{z-2i}\right)^2}
$$
maps $\Omega$ conformally onto $\HH$.

::: pf-proof
Squaring maps $Q$ biholomorphically onto $\HH$, since it doubles arguments in $(0, \pi/2)$; compose with step [](#quadrant){.pf-ref}.
:::

:::

:::
:::
