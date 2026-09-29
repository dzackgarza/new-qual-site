---
schema: qual/card@1
id: P-5OCGZ
kind: problem
title: $\int\frac{x+1}{\sqrt{4-x^2}}\,dx$
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
3. $\displaystyle \int \frac {x+1}{\sqrt {4-x^2}} ~dx = \color {blue} {-\sqrt {4-x^2}+\sin ^{-1} (\frac {x}{2})}$

- **Solution:** $\frac {x+1}{\sqrt {4-x^2}} ~dx = - \frac {1}{2} \frac {-2x}{\sqrt {4-x^2}} ~dx + \frac {1}{\sqrt {4-x^2}} ~dx​$

- **Solution:** $\sin (u) = \frac {1}{2} x$, $\cos (u) ~du = \frac {1}{2} ~dx$

- **Solution:** $\frac {1}{\sqrt {4-x^2}} ~dx =  \frac {1}{2 \cos (u)} 2 \cdot \cos (u) ~du = du$

- **Used 2019**
:::

::: {.solution}
Take $|x| < 2$.

::: pf

::: pf-step

Split the integral into two parts: $$\int \frac{x+1}{\sqrt{4-x^2}} \, dx = \int \frac{x}{\sqrt{4-x^2}} \, dx + \int \frac{1}{\sqrt{4-x^2}} \, dx.$$

::: pf-proof

The integrand satisfies $\frac{x+1}{\sqrt{4-x^2}} = \frac{x}{\sqrt{4-x^2}} + \frac{1}{\sqrt{4-x^2}}$, and the integral of a sum is the sum of the integrals.

:::

:::

::: {.pf-step #s2}

$\int \frac{x}{\sqrt{4-x^2}} \, dx = -\sqrt{4-x^2} + C_1$.

::: pf-proof

::: pf-step

Substitute $u = 4 - x^2 \implies du = -2x \, dx \implies x \, dx = -\frac{1}{2} \, du$.

:::

::: pf-step

$\int \frac{x}{\sqrt{4-x^2}} \, dx = -\frac{1}{2} \int u^{-1/2} \, du = -\frac{1}{2} (2 u^{1/2}) + C_1 = -\sqrt{4-x^2} + C_1$.

:::

:::

:::

::: {.pf-step #s3}

$\int \frac{1}{\sqrt{4-x^2}} \, dx = \arcsin\left(\frac{x}{2}\right) + C_2$.

::: pf-proof

::: pf-step

Substitute $x = 2\sin(\theta)$ for $\theta \in (-\pi/2, \pi/2)$, so $dx = 2\cos(\theta) \, d\theta$ and $\sqrt{4-x^2} = \sqrt{4 - 4\sin^2(\theta)} = 2\cos(\theta)$.

:::

::: pf-step

$\int \frac{1}{\sqrt{4-x^2}} \, dx = \int \frac{2\cos(\theta)}{2\cos(\theta)} \, d\theta = \int 1 \, d\theta = \theta + C_2 = \arcsin\left(\frac{x}{2}\right) + C_2$.

:::

:::

:::

::: pf-step

Combining results: $$\int \frac{x+1}{\sqrt{4-x^2}} \, dx = -\sqrt{4-x^2} + \arcsin\left(\frac{x}{2}\right) + C.$$

::: pf-proof

Adding the two antiderivatives from steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, and absorbing the constants $C_1 + C_2$ into a single constant $C$, gives the stated result.

:::

:::

:::

:::
