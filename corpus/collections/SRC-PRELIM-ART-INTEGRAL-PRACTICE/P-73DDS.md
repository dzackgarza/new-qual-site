---
schema: qual/card@1
id: P-73DDS
kind: problem
title: $\int\frac{\cos x}{\sin^2 x}\,dx$
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

::: {.problem}
1. $\displaystyle \int \frac {\cos(x)}{\sin ^2 (x)} ~dx = \color {blue} {- \csc (x)}$

- **Solution:** $\frac {\cos (x)}{\sin ^2 (x)} = \cot (x) \csc (x)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The substitution $u = \sin(x)$ gives $\int \frac{\cos(x)}{\sin^2(x)} \, dx = -\csc(x) + C$.

::: pf-proof

With $u = \sin(x)$, $du = \cos(x) \, dx$, so
$$\int \frac{\cos(x)}{\sin^2(x)} \, dx = \int u^{-2} \, du = -\frac{1}{u} + C = -\frac{1}{\sin(x)} + C = -\csc(x) + C.$$

:::

:::

::: {.pf-step #s2}

The identity $\frac{\cos(x)}{\sin^2(x)} = \cot(x)\csc(x)$ gives the same antiderivative.

::: pf-proof

$\frac{\cos(x)}{\sin^2(x)} = \frac{\cos(x)}{\sin(x)} \cdot \frac{1}{\sin(x)} = \cot(x)\csc(x)$, and since $\frac{d}{dx}(\csc(x)) = -\csc(x)\cot(x)$,
$$\int \csc(x)\cot(x) \, dx = -\csc(x) + C.$$

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $\int \frac{\cos(x)}{\sin^2(x)} \, dx = \boxed{-\csc(x) + C}$; step [](#s2){.pf-ref} checks it.

:::

:::

:::
