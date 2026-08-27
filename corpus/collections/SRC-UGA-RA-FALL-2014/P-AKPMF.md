---
schema: qual/card@1
id: P-AKPMF
kind: problem
title: $\|f\|_p=\sup_{\|g\|_q=1}|\int fg|$ for $f\in L^p(\RR^n)$ and conjugate exponents
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $1 \leq p,q \leq \infty$ be conjugate exponents, and show that
\[
f \in L^p(\RR^n) \implies \|f\|_{p} = \sup _{\|g\|_{q}=1}\left|\int f(x) g(x) d x\right|
\]
:::
::: {.solution}
**Setup.** $1 \le p, q \le \infty$ are conjugate: $1/p + 1/q = 1$ (with the usual convention for $p = 1, \infty$). All functions are on $\RR^n$ with Lebesgue measure.

<1>1. For every $g$ with $\|g\|_q = 1$: $\left|\int f g\right| \le \|f\|_p$.
Proof: Hölder's inequality gives $\left|\int fg\right| \le \|f\|_p\|g\|_q = \|f\|_p$.
<2>1. Hence $\|f\|_p \ge \sup_{\|g\|_q = 1}\left|\int fg\right|$.
Proof: <1>1 holds for all admissible $g$.

<1>2. Case $1 < p < \infty$: define $g(x) = \dfrac{\mathrm{sgn}(f(x))\,|f(x)|^{p-1}}{\|f\|_p^{p/q}}$ (and $g = 0$ where $f = 0$). <2>1. $\|g\|_q^q = \dfrac{\int |f|^{q(p-1)}}{\|f\|_p^{pq/q}} = \dfrac{\int |f|^p}{\|f\|_p^{p}} = 1$, since $q(p-1) = p$.
Proof: $1/p + 1/q = 1$ implies $q(p-1) = p$; the numerator is $\|f\|_p^p$ by definition.
<2>2. $\left|\int f g\right| = \dfrac{\int |f|^p}{\|f\|_p^{p/q}} = \|f\|_p^{p - p/q} = \|f\|_p$.
Proof: $f\,\mathrm{sgn}(f)\,|f|^{p-1} = |f|^p$; and $p - p/q = p(1 - 1/q) = p \cdot (1/p) = 1$.
<2>3. Q.E.D. for $1 < p < \infty$.
Proof: <2>1 and <2>2 exhibit an admissible $g$ attaining $\|f\|_p$, so the sup equals $\|f\|_p$ by <1>1.

<1>3. Case $p = 1$ (so $q = \infty$): take $g = \mathrm{sgn}(f)$.
Proof: $\|g\|_\infty = 1$ and $\int fg = \int |f| = \|f\|_1$; combined with <1>1 the sup equals $\|f\|_1$.

<1>4. Case $p = \infty$ (so $q = 1$). <2>1. For $0 < \eps < \|f\|_\infty$, the set $\{x : |f(x)| \ge \|f\|_\infty - \eps\}$ has positive measure and contains a measurable subset $E$ with $0 < m(E) < \infty$ (intersect with a large ball).
Proof: definition of the essential supremum; $\RR^n$ is $\sigma$-finite.
<2>2. Define $g = \dfrac{\mathrm{sgn}(f)\,\chi_E}{m(E)}$; then $\|g\|_1 = 1$ and $\left|\int f g\right| = \dfrac{1}{m(E)}\int_E |f| \ge \|f\|_\infty - \eps$.
Proof: normalization by $m(E)$; the bound uses <2>1. <2>3. Q.E.D. for $p = \infty$.
Proof: <2>2 gives $\sup_{\|g\|_1 = 1}\left|\int fg\right| \ge \|f\|_\infty - \eps$ for every $\eps > 0$; with <1>1 the sup equals $\|f\|_\infty$.

<1>5. Q.E.D. Proof: <1>2, <1>3, and <1>4 cover all conjugate pairs $1 \le p \le \infty$.
:::
