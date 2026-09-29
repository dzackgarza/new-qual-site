---
schema: qual/card@1
id: P-7NXQ7
kind: problem
title: $\int_1^2\frac{dx}{x\sqrt{x^2-1}}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometric Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
1. $\displaystyle \int_{1}^{2} \frac {1}{x\sqrt {x^2 -1}} dx = \color {blue} {\frac {\pi}{3}}$

- **Solution:** $\sec ^{-1} (x) |_{1}^{2}$
:::

::: {.solution}

::: pf

::: pf-step

The antiderivative of $\frac{1}{x\sqrt{x^2-1}}$ for $x > 1$ is $\operatorname{arcsec}(x) + C = \arccos(1/x) + C$.

::: pf-proof

::: pf-step

Make the trigonometric substitution $x = \sec(\theta)$ for $\theta \in (0, \pi/2)$.

:::

::: pf-step

Then $dx = \sec(\theta)\tan(\theta) \, d\theta$, and $\sqrt{x^2 - 1} = \sqrt{\sec^2(\theta) - 1} = \tan(\theta)$.

:::

::: pf-step

Substituting: $$\int \frac{1}{x\sqrt{x^2 - 1}} \, dx = \int \frac{\sec(\theta)\tan(\theta)}{\sec(\theta)\tan(\theta)} \, d\theta = \int 1 \, d\theta = \theta + C = \operatorname{arcsec}(x) + C.$$

:::

:::

:::

::: pf-step

The definite integral is an improper integral at the lower limit $x=1$, defined by $\lim_{t \to 1^+} \int_t^2 \frac{1}{x\sqrt{x^2-1}} \, dx$.

::: pf-proof

The integrand has an infinite discontinuity at $x=1$.

:::

:::

::: pf-step

$$\int_1^2 \frac{1}{x\sqrt{x^2-1}} \, dx = \lim_{t \to 1^+} [\operatorname{arcsec}(x)]_t^2 = \operatorname{arcsec}(2) - \lim_{t \to 1^+} \operatorname{arcsec}(t) = \frac{\pi}{3} - 0 = \boxed{\frac{\pi}{3}}.$$

::: pf-proof

$\sec(\pi/3) = 2$, so $\operatorname{arcsec}(2) = \pi/3$; $\sec(0) = 1$, so $\operatorname{arcsec}(1) = 0$, and $\operatorname{arcsec}$ is continuous at $1$.

:::

:::

:::

:::
