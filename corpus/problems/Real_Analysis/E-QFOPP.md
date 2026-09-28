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

<1>1. For measurable $E$, $\int \tau_h \chi_E = m(E)$.

::: {.proof}
$\tau_h\chi_E(x) = \chi_E(x + h) = \chi_{E - h}(x)$, and $m(E - h) = m(E)$ by translation invariance of Lebesgue measure.
:::

<1>2. The claim holds for nonnegative simple $s = \sum_i a_i\chi_{E_i}$.

::: {.proof}
By linearity and step <1>1, $\int \tau_h s = \sum_i a_i m(E_i) = \int s$.
:::

<1>3. The claim holds for measurable $f \geq 0$.

::: {.proof}
Choose simple functions $0 \leq s_k \nearrow f$ pointwise. Then $\tau_h s_k \nearrow \tau_h f$ pointwise, and the monotone convergence theorem with step <1>2 gives $\int \tau_h f = \lim_k \int \tau_h s_k = \lim_k \int s_k = \int f$.
:::

<1>4. Q.E.D.

::: {.proof}
For $f \in L^1$, $(\tau_h f)^\pm = \tau_h(f^\pm)$; apply step <1>3 to $f^+$ and $f^-$ and subtract.
:::
:::
