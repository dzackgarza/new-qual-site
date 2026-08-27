---
schema: qual/card@1
id: P-73DDS
kind: problem
title: '$\displaystyle \int \frac {\cos(x)}{\sin ^2 (x)} ~dx = \color {blue} {- \csc
  (x)}$ Solution: $\frac {\cos (x)}{\sin ^2 (x)} = \cot (x) \csc (x)$'
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
1. $\displaystyle \int \frac {\cos(x)}{\sin ^2 (x)} ~dx = \color {blue} {- \csc (x)}$

- **Solution:** $\frac {\cos (x)}{\sin ^2 (x)} = \cot (x) \csc (x)$
:::

::: {.solution}
**Goal:** Evaluate the indefinite integral $\int \frac{\cos(x)}{\sin^2(x)} \, dx$.

<1>1. Method 1 ($u$-substitution): Proof: <2>1. Let $u = \sin(x)$.
Then $du = \cos(x) \, dx$.
<2>2. Transforming the integral: $$\int \frac{\cos(x)}{\sin^2(x)} \, dx = \int u^{-2} \, du = -u^{-1} + C = -\frac{1}{u} + C.$$ <2>3. Substituting back $u = \sin(x)$: $$-\frac{1}{\sin(x)} + C = -\csc(x) + C.$$

<1>2. Method 2 (Trigonometric identity): Proof: <2>1. Rewrite the integrand: $\frac{\cos(x)}{\sin^2(x)} = \frac{\cos(x)}{\sin(x)} \cdot \frac{1}{\sin(x)} = \cot(x)\csc(x)$.
<2>2. Since $\frac{d}{dx}(\csc(x)) = -\csc(x)\cot(x)$, we have: $$\int \csc(x)\cot(x) \, dx = -\csc(x) + C.$$

<1>3. Conclusion: $\int \frac{\cos(x)}{\sin^2(x)} \, dx = -\csc(x) + C$.
Proof: Follows from <1>1 and <1>2. Q.E.D.
:::
