---
schema: qual/card@1
id: P-OSVPH
kind: problem
title: $\int\frac{\sin^3 x}{\cos x-\cos^3 x}\,dx$
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

::: {.problem}
Evaluate the indefinite integral:
$$
\int \frac{\sin^3(x)}{\cos(x) - \cos^3(x)} \, dx.
$$
:::

::: {.solution}
<1>1. On the domain $\{x \in \mathbb{R} : \sin(x) \neq 0, \cos(x) \neq 0\}$ of the integrand, $\frac{\sin^3(x)}{\cos(x) - \cos^3(x)} = \tan(x)$.

::: {.proof}
Factoring and the Pythagorean identity $1 - \cos^2(x) = \sin^2(x)$ give
$$\cos(x) - \cos^3(x) = \cos(x)(1 - \cos^2(x)) = \cos(x) \sin^2(x),$$
so
$$\frac{\sin^3(x)}{\cos(x) - \cos^3(x)} = \frac{\sin^3(x)}{\cos(x) \sin^2(x)} = \frac{\sin(x)}{\cos(x)} = \tan(x).$$
:::

<1>2. $\int \tan(x) \, dx = -\ln|\cos(x)| + C$.

::: {.proof}
Substitute $u = \cos(x)$, so $du = -\sin(x) \, dx$:
$$\int \frac{\sin(x)}{\cos(x)} \, dx = -\int \frac{du}{u} = -\ln|u| + C = -\ln|\cos(x)| + C.$$
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2,
$$\int \frac{\sin^3(x)}{\cos(x) - \cos^3(x)} \, dx = \boxed{-\ln|\cos(x)| + C} = \ln|\sec(x)| + C.$$
:::
:::
