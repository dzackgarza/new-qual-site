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
1. $\displaystyle \int \frac {\sin^3(x)}{\cos(x) - \cos^3(x)} ~dx = \color {blue} {- \ln (\cos(x))}$

- **Solution:** $\frac {\sin^3(x)}{\cos(x) - \cos^3(x)} = \frac {\sin^3(x)}{\cos(x) \sin ^2 (x)} = \tan (x)$

- **Used 2019**
:::

::: solution
**Goal:** Integrate
$$\int \frac{\sin^3 x}{\cos x-\cos^3 x}\,dx.$$

<1> Simplify the integrand.
    *Proof:*
    <2>1. Factor the denominator:
        $$\cos x-\cos^3 x=\cos x(1-\cos^2 x)=\cos x\sin^2 x.$$
    <2>2. For points where $\sin x\neq0$ and $\cos x\neq0$,
        $$\frac{\sin^3 x}{\cos x-\cos^3 x}=\frac{\sin x}{\cos x}=\tan x.$$

<1> Integrate.
    *Proof:*
    <2>1. An antiderivative of $\tan x$ is $-\ln|\cos x|$.
    <2>2. Therefore
        $$\int \frac{\sin^3 x}{\cos x-\cos^3 x}\,dx = -\ln|\cos x|+C.$$

Authored by **Codex 5.3 Spark Extra High**.
:::
