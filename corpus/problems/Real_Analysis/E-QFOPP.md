---
schema: qual/card@1
id: E-QFOPP
kind: exercise
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

::: exercise
- $\star$: Prove that the Lebesgue integral is translation invariant, i.e. if $\tau_h(x) = x+h$ then $\int \tau_h f = \int f$.
:::

::: {.solution}
<1>1. It suffices to prove the claim for non-negative measurable $f$: the general $f \in L^1$ case follows by linearity on positive and negative parts.
::: {.proof}
$\int \tau_h f = \int \tau_h f^+ - \int \tau_h f^-$, and $\tau_h(f^\pm) = (\tau_h f)^\pm$.
:::

<1>2. The claim holds for indicators: $\int \tau_h \chi_E = m(E - h) = m(E)$.
::: {.proof}
$\tau_h\chi_E(x) = \chi_E(x + h)$, which equals $1$ iff $x \in E - h$; so $\tau_h\chi_E = \chi_{E - h}$ and $m(E - h) = m(E)$ by translation invariance of Lebesgue measure.
:::

<1>3. The claim holds for non-negative simple functions $s = \sum_i a_i\chi_{E_i}$.
::: {.proof}
$\int \tau_h s = \sum_i a_i\int \tau_h\chi_{E_i} = \sum_i a_i m(E_i) = \int s$ by <1>2 and linearity.
:::

<1>4. The claim holds for all non-negative measurable $f$.
<2>1. Choose simple functions $s_k \nearrow f$ pointwise.
::: {.proof}
standard approximation of a non-negative measurable function by simple functions.
:::
<2>2. $\tau_h s_k \nearrow \tau_h f$ pointwise.
::: {.proof}
translation is a bijection of $\RR^n$ and $s_k \nearrow f$.
:::
<2>3. $\int \tau_h f = \lim_k \int \tau_h s_k = \lim_k \int s_k = \int f$.
::: {.proof}
monotone convergence applied to <2>2, then <1>3, then monotone convergence applied to <2>1. <2>4. Q.E.D. Proof: <2>3.
:::

<1>5. The claim holds for all $f \in L^1$.
::: {.proof}
by <1>1, apply <1>4 to $f^+$ and $f^-$, both non-negative and integrable.
:::

<1>6. Q.E.D.
::: {.proof}
<1>4 covers non-negative measurable $f$ and <1>5 covers signed integrable $f$.
:::
:::
