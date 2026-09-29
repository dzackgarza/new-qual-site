---
schema: qual/card@1
id: E-QFOPP
kind: problem
title: Translation invariance of the Lebesgue integral
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- $\star$: Prove that the Lebesgue integral is translation invariant, i.e. if $\tau_h(x) = x+h$ then $\int \tau_h f = \int f$.
:::

::: {.solution}
Write $\tau_h f \coloneqq f \circ \tau_h$, so $\tau_h f(x) = f(x+h)$, and let $m$ be Lebesgue measure on $\RR^n$.

::: pf

::: {.pf-step #s1}

For measurable $E$, $\int \tau_h \chi_E = m(E)$.

::: pf-proof

$\tau_h\chi_E(x) = \chi_E(x + h) = \chi_{E - h}(x)$, and $m(E - h) = m(E)$ by translation invariance of Lebesgue measure.

:::

:::

::: {.pf-step #s2}

The claim holds for nonnegative simple $s = \sum_i a_i\chi_{E_i}$.

::: pf-proof

By linearity and step [](#s1){.pf-ref}, $\int \tau_h s = \sum_i a_i m(E_i) = \int s$.

:::

:::

::: {.pf-step #s3}

The claim holds for measurable $f \geq 0$.

::: pf-proof

Choose simple functions $0 \leq s_k \nearrow f$ pointwise. Then $\tau_h s_k \nearrow \tau_h f$ pointwise, and the monotone convergence theorem with step [](#s2){.pf-ref} gives $\int \tau_h f = \lim_k \int \tau_h s_k = \lim_k \int s_k = \int f$.

:::

:::

::: pf-qed

For $f \in L^1$, $(\tau_h f)^\pm = \tau_h(f^\pm)$; apply step [](#s3){.pf-ref} to $f^+$ and $f^-$ and subtract.

:::

:::

:::
