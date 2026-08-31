---
schema: qual/card@1
id: P-5UMRG
kind: problem
title: $\int\frac{\sqrt{x^2-a^2}}{x}\,dx$
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

::: problem
5. $\displaystyle \int \frac {\sqrt {x^2-a^2}}{x} ~dx = \tan (\sec ^{-1} (\frac {x}{a})) - a \sec ^{-1} (\frac {x}{a}) = \color {blue} {\sqrt {x^2-a^2} - a \sec ^{-1} (\frac {x}{a})} = \color {blue} {\sqrt {x^2-a^2} - a \tan ^{-1} (\frac {\sqrt {x^2 - a^2}}{a})}​$

- **Solution:** $\sec (u) = \frac {1}{a} x$, $\tan (u) \sec (u) ~du = \frac {1}{a} ~dx$

- **Solution:** $\frac {\sqrt {x^2-a^2}}{x} ~dx = \frac {a \tan (u)}{a \sec (u)} \cdot a \tan (u) \sec (u) ~du = a \tan ^2 (u) ~du = a (\sec ^2 (u) - 1) ~du$

  1. $\displaystyle \int \frac {\sqrt {x^2-1}}{x} ~dx = \color {blue} {\sqrt {x^2-1} - \sec ^{-1} (x)} = \color {blue} {\sqrt {x^2-1} - \tan ^{-1} (\sqrt {x^2-1})}$

  2. $\displaystyle \int \frac {\sqrt {x^2-9}}{x} ~dx = \color {blue} {\sqrt {x^2-9} - 3 \sec ^{-1} (\frac {x}{3})} = \color {blue} {\sqrt {x^2-9} - 3 \tan ^{-1} (\frac {\sqrt {x^2-9}}{3})}$

  - **Used 2019**, *Unsolved*
:::

::: {.solution}
**Goal:** Evaluate the indefinite integral $\int \frac{\sqrt{x^2-a^2}}{x} \, dx$ for $a > 0$ and $x > a$.

<1>1. Substitute $x = a \sec(\theta)$ with $\theta \in (0, \pi/2)$.
::: {.proof}
<2>1. Then $dx = a \sec(\theta)\tan(\theta) \, d\theta$.
<2>2. Since $x > a > 0$, $\sqrt{x^2 - a^2} = \sqrt{a^2(\sec^2(\theta) - 1)} = \sqrt{a^2 \tan^2(\theta)} = a \tan(\theta)$.
:::

<1>2. Transform and integrate: $$\int \frac{\sqrt{x^2-a^2}}{x} \, dx = \int \frac{a \tan(\theta)}{a \sec(\theta)} \cdot a \sec(\theta)\tan(\theta) \, d\theta = a \int \tan^2(\theta) \, d\theta.$$
::: {.proof}
<2>1. From <1>1, $x = a\sec(\theta)$, $dx = a\sec(\theta)\tan(\theta)\,d\theta$, and $\sqrt{x^2-a^2} = a\tan(\theta)$.
<2>2. Substituting these into the integrand gives $\frac{a\tan(\theta)}{a\sec(\theta)}\cdot a\sec(\theta)\tan(\theta)\,d\theta$.
<2>3. The factors $a\sec(\theta)$ cancel, leaving $a\tan^2(\theta)\,d\theta$.
:::

<1>3. Evaluate $a \int \tan^2(\theta) \, d\theta = a (\tan(\theta) - \theta) + C$.
::: {.proof}
Using the Pythagorean identity $\tan^2(\theta) = \sec^2(\theta) - 1$: $$a \int (\sec^2(\theta) - 1) \, d\theta = a (\tan(\theta) - \theta) + C.$$
:::

<1>4. Express the antiderivative in terms of $x$: $$\int \frac{\sqrt{x^2-a^2}}{x} \, dx = \sqrt{x^2-a^2} - a \operatorname{arcsec}\left(\frac{x}{a}\right) + C = \sqrt{x^2-a^2} - a \arctan\left(\frac{\sqrt{x^2-a^2}}{a}\right) + C.$$
::: {.proof}
<2>1. Since $\sec(\theta) = \frac{x}{a}$, we have $\theta = \operatorname{arcsec}\left(\frac{x}{a}\right)$.
<2>2. Since $\tan(\theta) = \frac{\sqrt{x^2-a^2}}{a}$, we have $a\tan(\theta) = \sqrt{x^2-a^2}$ and $\theta = \arctan\left(\frac{\sqrt{x^2-a^2}}{a}\right)$.
<2>3. Substituting these expressions into the antiderivative $a(\tan(\theta) - \theta) + C$ from <1>3 gives the result.
:::
:::
