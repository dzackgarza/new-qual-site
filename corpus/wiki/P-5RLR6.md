---
schema: qual/card@1
id: P-5RLR6
kind: problem
title: '$\displaystyle \int e^{\sin ^2 (x)} \sin (2x) ~dx = \color{blue} {e^{\sin^2(x)}}​$
  Solution: $u = \sin ^2 (x)​$, $du = 2 \sin (x) \cos (x) ~dx = \sin (2x) ~dx​$ Used
  2018 Used 2019'
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
  - Trigonometry
relations: []
review: draft
---

::: problem
2. $\displaystyle \int e^{\sin ^2 (x)} \sin (2x) ~dx = \color{blue} {e^{\sin^2(x)}}​$

- **Solution:** $u = \sin ^2 (x)​$, $du = 2 \sin (x) \cos (x) ~dx = \sin (2x) ~dx​$

- **Used 2018**

- **Used 2019**
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the indefinite integral $\int e^{\sin^2(x)} \sin(2x) \, dx$.

<1>1. Make the substitution $u = \sin^2(x)$.
Proof: By the chain rule, $\frac{du}{dx} = 2\sin(x)\cos(x)$.
By the double-angle identity for sine, $2\sin(x)\cos(x) = \sin(2x)$.
Thus $du = \sin(2x) \, dx$.

<1>2. Transform and evaluate the integral in terms of $u$: $$\int e^{\sin^2(x)} \sin(2x) \, dx = \int e^u \, du = e^u + C.$$ Proof: The antiderivative of the natural exponential function $e^u$ is $e^u + C$.

<1>3. Substitute back $u = \sin^2(x)$: $$\int e^{\sin^2(x)} \sin(2x) \, dx = e^{\sin^2(x)} + C.$$ Proof: Follows directly from <1>1 and <1>2. Q.E.D.
:::
