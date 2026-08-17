---
schema: qual/card@1
id: P-7NXQ7
kind: problem
title: "$\\displaystyle \\int_{1}^{2} \\frac {1}{x\\sqrt {x^2 -1}} dx = \\color {blue} {\\frac {\\pi}{3}}$ Solution: $\\sec ^{-1} (x) |_{1}^{2}$"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - trigonometric-substitution
relations: []
review: draft
solved: true
---

::: problem
1. $\displaystyle \int_{1}^{2} \frac {1}{x\sqrt {x^2 -1}} dx = \color {blue} {\frac {\pi}{3}}$

- **Solution:** $\sec ^{-1} (x) |_{1}^{2}$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the definite integral $\int_{1}^{2} \frac{1}{x\sqrt{x^2 -1}} \, dx$.

<1>1. The antiderivative of $\frac{1}{x\sqrt{x^2-1}}$ for $x > 1$ is $\operatorname{arcsec}(x) + C = \arccos(1/x) + C$.
Proof: <2>1. Make the trigonometric substitution $x = \sec(\theta)$ for $\theta \in (0, \pi/2)$.
<2>2. Then $dx = \sec(\theta)\tan(\theta) \, d\theta$, and $\sqrt{x^2 - 1} = \sqrt{\sec^2(\theta) - 1} = \tan(\theta)$.
<2>3. Substituting: $$\int \frac{1}{x\sqrt{x^2 - 1}} \, dx = \int \frac{\sec(\theta)\tan(\theta)}{\sec(\theta)\tan(\theta)} \, d\theta = \int 1 \, d\theta = \theta + C = \operatorname{arcsec}(x) + C.$$

<1>2. The definite integral is an improper integral at the lower limit $x=1$, defined by $\lim_{t \to 1^+} \int_t^2 \frac{1}{x\sqrt{x^2-1}} \, dx$.
Proof: The integrand has an infinite discontinuity at $x=1$.

<1>3. Evaluation: $$\int_1^2 \frac{1}{x\sqrt{x^2-1}} \, dx = \lim_{t \to 1^+} [\operatorname{arcsec}(x)]_t^2 = \operatorname{arcsec}(2) - \lim_{t \to 1^+} \operatorname{arcsec}(t) = \frac{\pi}{3} - 0 = \frac{\pi}{3}.$$ Proof: $\sec(\pi/3) = 2 \implies \operatorname{arcsec}(2) = \pi/3$, and $\sec(0) = 1 \implies \operatorname{arcsec}(1) = 0$.
Q.E.D.
:::
