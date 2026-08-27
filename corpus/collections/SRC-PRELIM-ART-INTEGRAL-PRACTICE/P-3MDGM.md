---
schema: qual/card@1
id: P-3MDGM
kind: problem
title: Antiderivatives of $(\sec^3 x+e^{\sin x})/\sec x$ and $1/(\tan x+\cot x)$
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
3. $\displaystyle \int \frac {\sec^3(x) + e^{\sin(x)}}{\sec(x)} ~dx = \color {blue} {\tan(x) + e^{\sin(x)}}$

- **Solution:** $\frac {\sec ^3 (x) + e^{\sin(x)}}{\sec(x)} = \sec ^2 (x) + \cos (x) \cdot e^{\sin(x)}$

- **Used 2018**

4. $\displaystyle \int \frac {1}{\tan (x) + \cot (x)} ~dx = \color {blue} {\frac {1}{2}\sin ^2 (x)} = \color {blue} {- \frac {1}{2}\cos ^2 (x)}$

- **Solution:** $\frac {1}{\tan (x) + \cot (x)} = \frac {1}{\frac {\sin (x)}{\cos (x)} + \frac {\cos (x)}{\sin (x)}} = \frac {\sin (x) \cos (x)}{\sin ^2 (x) + \cos ^2 (x)} = \sin (x) \cos (x)$
:::

::: {.solution}
**Goal:** Evaluate the indefinite integrals: (a) $\int \frac{\sec^3(x) + e^{\sin(x)}}{\sec(x)} \, dx$ (b) $\int \frac{1}{\tan(x) + \cot(x)} \, dx$

<1>1. $\int \frac{\sec^3(x) + e^{\sin(x)}}{\sec(x)} \, dx = \tan(x) + e^{\sin(x)} + C$.
Proof: <2>1. Simplify the integrand algebraically using $\frac{1}{\sec(x)} = \cos(x)$: $$\frac{\sec^3(x) + e^{\sin(x)}}{\sec(x)} = \sec^2(x) + \cos(x) e^{\sin(x)}.$$ <2>2. Integrate term-by-term: $$\int \sec^2(x) \, dx = \tan(x) + C_1.$$ <2>3. For $\int \cos(x) e^{\sin(x)} \, dx$, substitute $u = \sin(x) \implies du = \cos(x) \, dx$: $$\int \cos(x) e^{\sin(x)} \, dx = \int e^u \, du = e^u + C_2 = e^{\sin(x)} + C_2.$$ <2>4. Combining yields $\tan(x) + e^{\sin(x)} + C$.

<1>2. $\int \frac{1}{\tan(x) + \cot(x)} \, dx = \frac{1}{2}\sin^2(x) + C = -\frac{1}{2}\cos^2(x) + C'$.
Proof: <2>1. Rewrite trigonometric functions in terms of $\sin(x)$ and $\cos(x)$: $$\tan(x) + \cot(x) = \frac{\sin(x)}{\cos(x)} + \frac{\cos(x)}{\sin(x)} = \frac{\sin^2(x) + \cos^2(x)}{\sin(x)\cos(x)} = \frac{1}{\sin(x)\cos(x)}.$$ <2>2. Thus the integrand is $\frac{1}{\tan(x) + \cot(x)} = \sin(x)\cos(x)$.
<2>3. Using the substitution $u = \sin(x) \implies du = \cos(x) \, dx$: $$\int \sin(x)\cos(x) \, dx = \int u \, du = \frac{1}{2} u^2 + C = \frac{1}{2}\sin^2(x) + C.$$ <2>4. Alternatively, using $\sin^2(x) = 1 - \cos^2(x)$, this equals $-\frac{1}{2}\cos^2(x) + C'$.
Q.E.D.
:::
