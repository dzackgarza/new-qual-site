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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked by differentiation: with u = sin x, du = cos x dx,
    the integral is int u^{-2} du = -1/u + C = -csc x + C, and d/dx(-csc x) = csc x cot x =
    cos x/sin^2 x, so the answer is right. The card also checks it by differentiating, which is the
    right way to close an indefinite integral. Not claimed: any definite-integral variant, or the
    behaviour at the zeros of sin x, where the antiderivative has poles.
---

::: {.problem}
Evaluate
$$
\int\frac{\cos x}{\sin^2 x}\,dx.
$$
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
