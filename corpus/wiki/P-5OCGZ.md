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
solved: true
---

::: problem
3. $\displaystyle \int \frac {x+1}{\sqrt {4-x^2}} ~dx = \color {blue} {-\sqrt {4-x^2}+\sin ^{-1} (\frac {x}{2})}$

- **Solution:** $\frac {x+1}{\sqrt {4-x^2}} ~dx = - \frac {1}{2} \frac {-2x}{\sqrt {4-x^2}} ~dx + \frac {1}{\sqrt {4-x^2}} ~dx​$

- **Solution:** $\sin (u) = \frac {1}{2} x$, $\cos (u) ~du = \frac {1}{2} ~dx$

- **Solution:** $\frac {1}{\sqrt {4-x^2}} ~dx =  \frac {1}{2 \cos (u)} 2 \cdot \cos (u) ~du = du$

- **Used 2019**
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the indefinite integral $\int \frac{x+1}{\sqrt{4-x^2}} \, dx$ for $|x| < 2$.

<1>1. Split the integral into two parts: $$\int \frac{x+1}{\sqrt{4-x^2}} \, dx = \int \frac{x}{\sqrt{4-x^2}} \, dx + \int \frac{1}{\sqrt{4-x^2}} \, dx.$$ Proof: By linearity of the indefinite integral.

<1>2. $\int \frac{x}{\sqrt{4-x^2}} \, dx = -\sqrt{4-x^2} + C_1$.
Proof: <2>1. Substitute $u = 4 - x^2 \implies du = -2x \, dx \implies x \, dx = -\frac{1}{2} \, du$.
<2>2. $\int \frac{x}{\sqrt{4-x^2}} \, dx = -\frac{1}{2} \int u^{-1/2} \, du = -\frac{1}{2} (2 u^{1/2}) + C_1 = -\sqrt{4-x^2} + C_1$.

<1>3. $\int \frac{1}{\sqrt{4-x^2}} \, dx = \arcsin\left(\frac{x}{2}\right) + C_2$.
Proof: <2>1. Substitute $x = 2\sin(\theta)$ for $\theta \in (-\pi/2, \pi/2)$.
Then $dx = 2\cos(\theta) \, d\theta$ and $\sqrt{4-x^2} = 2\cos(\theta)$.
<2>2. $\int \frac{1}{\sqrt{4-x^2}} \, dx = \int \frac{2\cos(\theta)}{2\cos(\theta)} \, d\theta = \int 1 \, d\theta = \theta + C_2 = \arcsin\left(\frac{x}{2}\right) + C_2$.

<1>4. Combining results: $$\int \frac{x+1}{\sqrt{4-x^2}} \, dx = -\sqrt{4-x^2} + \arcsin\left(\frac{x}{2}\right) + C.$$ Proof: By adding <1>2 and <1>3. Q.E.D.
:::
