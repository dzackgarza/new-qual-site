---
schema: qual/card@1
id: E-XHB3F
kind: problem
title: Vanishing of $\int f$, integrability of bounded functions, and density of simple,
  step, and $C_c^\infty$ functions in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - L¹
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source stated f=0 a.e. iff int f=0 for every measurable f, false for chi_[0,1] - chi_[1,2], and bounded iff integrable with no finiteness hypothesis, false for f=1 on R; the statement now assumes f >= 0 and a finite measure space.'
---

::: {.exercise}
(a) Show that if $f \geq 0$ is a measurable function, then $f=0$ a.e. iff $\int f = 0$.

(b) Show that on a measure space of finite measure, a bounded function is Lebesgue integrable iff it is measurable.

(c) Show that simple functions are dense in $L^1$.

(d) Show that step functions are dense in $L^1$.

(e) Show that smooth compactly supported functions are dense in $L^1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For measurable $f \geq 0$, $f = 0$ a.e. if and only if $\int f = 0$.

::: pf-proof

If $f = 0$ a.e., every simple function $0 \leq s \leq f$ vanishes a.e. and has integral $0$, so $\int f = 0$. Conversely, $\theset{f > 0} = \bigcup_{k} \theset{f > 1/k}$, and $\int f \ge \frac{1}{k}\mu\theset{f > 1/k}$ for each $k$; if $\int f = 0$, each $\theset{f > 1/k}$ is null, hence so is $\theset{f > 0}$.

:::

:::

::: {.pf-step #s2}

On a measure space $(X,\mu)$ with $\mu(X) < \infty$, a bounded function is Lebesgue integrable if and only if it is measurable.

::: pf-proof

The Lebesgue integral is defined for measurable functions, so an integrable function is measurable. Conversely, if $f$ is measurable and $\abs{f} \le M$, then $\int\abs{f} \le M\mu(X) < \infty$.

:::

:::

::: {.pf-step #s3}

Simple functions are dense in $L^1$.

::: pf-proof

For $f \geq 0$ in $L^1$, the dyadic simple functions
$$
s_k = \sum_{j=1}^{k 2^k}\frac{j-1}{2^k}\chi_{\theset{\frac{j-1}{2^k} \le f < \frac{j}{2^k}}} + k\chi_{\theset{f \ge k}}
$$
satisfy $0 \le s_k \nearrow f$ pointwise, so $\abs{f - s_k} \le f$ and the dominated convergence theorem gives $\norm{f - s_k}_1 \to 0$. For general $f$, approximate $f^+$ and $f^-$ separately.

:::

:::

::: {.pf-step #s4}

Step functions, finite linear combinations of indicators of bounded intervals, are dense in $L^1(\RR)$.

::: pf-proof

::: {.pf-step #s4-1}

For measurable $E \subseteq \RR$ with $m(E) < \infty$ and $\eps > 0$, there is a finite union $A$ of bounded open intervals with $\norm{\chi_E - \chi_A}_1 < 2\eps$.

::: pf-proof

Outer regularity gives an open $U \supseteq E$ with $m(U \setminus E) < \eps$, so $m(U) < \infty$. $U$ is a countable disjoint union of open intervals $I_i$, each bounded because $m(U) < \infty$, and $\sum_i m(I_i) = m(U)$. Choose $N$ with $\sum_{i > N} m(I_i) < \eps$ and put $A = \bigcup_{i \le N} I_i$. Then $\norm{\chi_E - \chi_A}_1 \le m(U \setminus E) + m(U \setminus A) < 2\eps$.

:::

:::

::: pf-qed

Given $f \in L^1$ and $\eps > 0$, step [](#s3){.pf-ref} gives a simple $s = \sum_{i=1}^m a_i\chi_{E_i}$ with $m(E_i) < \infty$ and $\norm{f - s}_1 < \eps$. Step [](#s4-1){.pf-ref} gives finite unions of intervals $A_i$ with $\norm{\chi_{E_i} - \chi_{A_i}}_1 < \eps/(1 + \sum_i\abs{a_i})$, and $\sum_i a_i\chi_{A_i}$ is a step function within $2\eps$ of $f$.

:::

:::

:::

::: {.pf-step #s5}

$C_c^\infty(\RR^n)$ is dense in $L^1(\RR^n)$.

::: pf-proof

::: {.pf-step #s5-1}

For $f \in L^1$, $f_R = f\chi_{B(0,R)}$ satisfies $\norm{f - f_R}_1 \to 0$ as $R \to \infty$.

::: pf-proof

$\abs{f - f_R} = \abs{f}\chi_{\RR^n \setminus B(0,R)}$ tends to $0$ pointwise and is bounded by $\abs{f} \in L^1$; apply dominated convergence.

:::

:::

::: {.pf-step #s5-2}

Let $\phi \in C_c^\infty(\RR^n)$ with $\phi \ge 0$ and $\int\phi = 1$, and $\phi_\eps(x) = \eps^{-n}\phi(x/\eps)$. Then $f_R \ast \phi_\eps \in C_c^\infty(\RR^n)$ and $\norm{f_R \ast \phi_\eps - f_R}_1 \to 0$ as $\eps \to 0$.

::: pf-proof

Differentiation under the integral gives $D^\alpha(f_R \ast \phi_\eps) = f_R \ast D^\alpha\phi_\eps$, which is continuous, and $\supp(f_R \ast \phi_\eps) \subseteq \overline{B(0,R)} + \supp\phi_\eps$ is compact. The $L^1$ convergence is the $L^1$ convergence of approximations to the identity, which follows from continuity of translation in $L^1$.

:::

:::

::: pf-qed

$\norm{f - f_R \ast \phi_\eps}_1 \le \norm{f - f_R}_1 + \norm{f_R - f_R \ast \phi_\eps}_1$, and steps [](#s5-1){.pf-ref} and [](#s5-2){.pf-ref} make both terms small.

:::

:::

:::

:::

:::
