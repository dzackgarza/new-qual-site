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

::: exercise
- $\star$: Prove that the Lebesgue integral is dilation invariant, i.e. if $f_\delta(x) = {f({x\over \delta}) \over \delta^n}$ then $\int f_\delta = \int f$.
:::

::: {.solution}
<1>1. It suffices to prove the claim for non-negative measurable $f$: the general $f \in L^1$ case then follows by linearity on the positive and negative parts.
::: {.proof}
$\int f_\delta = \int (f^+)_\delta - \int (f^-)_\delta$, and $(f^\pm)_\delta = (f_\delta)^\pm$; if the claim holds for non-negative functions it holds for $f^+$ and $f^-$ separately.
:::

<1>2. The claim holds for non-negative simple functions.
<2>1. Write $f = \sum_{i=1}^{m} a_i \chi_{E_i}$ with $a_i \ge 0$ and the $E_i$ pairwise disjoint measurable sets of finite measure.
::: {.proof}
definition of a simple function.
:::
<2>2. $\int (\chi_E)_\delta = m(E)$ for every measurable set $E$ of finite measure.
::: {.proof}
$(\chi_E)_\delta(x) = \delta^{-n}\chi_E(x/\delta) = \delta^{-n}\chi_{\delta E}(x)$, so $\int (\chi_E)_\delta = \delta^{-n} m(\delta E)$; Lebesgue measure scales under dilation, $m(\delta E) = \delta^n m(E)$.
:::
<2>3. $\int f_\delta = \sum_i a_i \int (\chi_{E_i})_\delta = \sum_i a_i m(E_i) = \int f$.
::: {.proof}
linearity of the integral and <2>2. <2>4. Q.E.D. Proof: <2>3.
:::

<1>3. The claim holds for all non-negative measurable $f$.
<2>1. There exist simple functions $s_k \nearrow f$ pointwise.
::: {.proof}
standard approximation of a non-negative measurable function by simple functions.
:::
<2>2. $(s_k)_\delta \nearrow f_\delta$ pointwise.
::: {.proof}
$x \mapsto x/\delta$ is a bijection of $\RR^n$ and $t \mapsto t/\delta^n$ is increasing on $[0,\infty)$.
:::
<2>3. $\int f_\delta = \lim_k \int (s_k)_\delta = \lim_k \int s_k = \int f$.
::: {.proof}
monotone convergence applied to <2>2, then <1>2 for each $s_k$, then monotone convergence applied to <2>1. <2>4. Q.E.D. Proof: <2>3.
:::

<1>4. The claim holds for all $f \in L^1$.
::: {.proof}
by <1>1 it suffices to apply <1>3 to $f^+$ and $f^-$, both non-negative and integrable.
:::

<1>5. Q.E.D.
::: {.proof}
<1>3 covers non-negative measurable $f$ and <1>4 covers signed integrable $f$; the identity is exactly the change of variables $y = x/\delta$, $dx = \delta^n\,dy$.
:::
:::
