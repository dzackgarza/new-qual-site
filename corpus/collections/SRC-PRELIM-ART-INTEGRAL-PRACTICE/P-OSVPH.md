---
schema: qual/card@1
id: P-OSVPH
kind: problem
title: Evaluate $\int\frac{\sin^3 x}{\cos x-\cos^3 x}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Evaluate the indefinite integral:
$$
\int \frac{\sin^3(x)}{\cos(x) - \cos^3(x)} \, dx.
$$
:::

::: solution
**Goal:** Compute the antiderivative $\int \frac{\sin^3(x)}{\cos(x) - \cos^3(x)} \, dx$.

<1>1. Algebraic simplification of the integrand:
    *Proof:*
    <2>1. Factor $\cos(x)$ out of the denominator:
    $$\cos(x) - \cos^3(x) = \cos(x)(1 - \cos^2(x)).$$
    <2>2. Apply the Pythagorean identity $1 - \cos^2(x) = \sin^2(x)$:
    $$\cos(x) - \cos^3(x) = \cos(x) \sin^2(x).$$
    <2>3. Substitute into the integrand on its domain $\{x \in \mathbb{R} : \sin(x) \neq 0, \cos(x) \neq 0\}$:
    $$\frac{\sin^3(x)}{\cos(x) - \cos^3(x)} = \frac{\sin^3(x)}{\cos(x) \sin^2(x)} = \frac{\sin(x)}{\cos(x)} = \tan(x).$$

<1>2. Integration via $u$-substitution:
    *Proof:*
    <2>1. Substitute $u = \cos(x)$, so $du = -\sin(x) \, dx$:
    $$\int \frac{\sin(x)}{\cos(x)} \, dx = -\int \frac{du}{u} = -\ln|u| + C = -\ln|\cos(x)| + C.$$
    <2>2. Equivalently, using logarithmic properties, $-\ln|\cos(x)| = \ln|\sec(x)|$.

<1>3. Conclusion:
    *Proof:*
    $$\int \frac{\sin^3(x)}{\cos(x) - \cos^3(x)} \, dx = -\ln|\cos(x)| + C = \ln|\sec(x)| + C.$$
:::
