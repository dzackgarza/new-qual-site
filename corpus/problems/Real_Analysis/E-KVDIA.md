---
schema: qual/card@1
id: E-KVDIA
kind: problem
title: Dilation invariance of the Lebesgue integral
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
- $\star$: Prove that the Lebesgue integral is dilation invariant, i.e. if $f_\delta(x) = {f({x\over \delta}) \over \delta^n}$ then $\int f_\delta = \int f$.
:::

::: {.solution}
Fix $\delta > 0$ and let $m$ be Lebesgue measure on $\RR^n$.

<1>1. For every measurable $E \subseteq \RR^n$, $\int (\chi_E)_\delta = m(E)$.

::: {.proof}
$(\chi_E)_\delta(x) = \delta^{-n}\chi_E(x/\delta) = \delta^{-n}\chi_{\delta E}(x)$, so $\int (\chi_E)_\delta = \delta^{-n} m(\delta E) = m(E)$ by the scaling law $m(\delta E) = \delta^n m(E)$.
:::

<1>2. The claim holds for nonnegative simple $f = \sum_{i=1}^{m} a_i \chi_{E_i}$.

::: {.proof}
$f_\delta = \sum_i a_i (\chi_{E_i})_\delta$, so by linearity of the integral and step <1>1, $\int f_\delta = \sum_i a_i m(E_i) = \int f$.
:::

<1>3. The claim holds for nonnegative measurable $f$.

::: {.proof}
Choose nonnegative simple functions $s_k \nearrow f$ pointwise. Then $(s_k)_\delta \nearrow f_\delta$ pointwise, since $(s_k)_\delta(x) = \delta^{-n}s_k(x/\delta)$. By the monotone convergence theorem and step <1>2, $\int f_\delta = \lim_k \int (s_k)_\delta = \lim_k \int s_k = \int f$.
:::

<1>4. Q.E.D.

::: {.proof}
For $f \in L^1$, $(f_\delta)^\pm = (f^\pm)_\delta$, and step <1>3 applies to $f^+$ and $f^-$; subtracting gives $\int f_\delta = \int f$.
:::
:::
