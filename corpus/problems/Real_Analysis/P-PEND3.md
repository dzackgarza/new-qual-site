---
schema: qual/card@1
id: P-PEND3
kind: problem
title: Continuity of outer measure, vanishing integrals, and density in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Density
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source asked for continuity from above and below for outer measures, f=0 a.e. iff int f=0 for measurable f, and bounded implies integrable with no finiteness hypothesis; continuity from above fails for outer measure, int f=0 needs f>=0, and boundedness needs finite measure. The statement now asks for continuity from below of Lebesgue outer measure and from above for measurable sets of finite measure, assumes f integrable or f>=0, and assumes a finite measure space.'
---

::: {.problem}

(a) Show that Lebesgue outer measure $m^*$ on $\RR^n$ is continuous from below, and that Lebesgue measure is continuous from above on decreasing sequences of measurable sets $E_1 \supseteq E_2 \supseteq \cdots$ with $m(E_1) < \infty$.

(b) Show that a countable union of null sets is null.

(c) Show that an integrable real-valued $f$ satisfies $f=0$ a.e. iff $\int_E f = 0$ for every measurable set $E$.

(d) Show that if $f \geq 0$ is a measurable function, then $f=0$ a.e. iff $\int f = 0$.

(e) Show that on a measure space of finite measure, a bounded function is Lebesgue integrable iff it is measurable.

(f) Show that simple functions are dense in $L^1(\RR^n)$.

(g) Show that step functions are dense in $L^1(\RR)$.

(h) Show that smooth compactly supported functions are dense in $L^1(\RR^n)$.

:::

::: {.solution}

Let $m^*$ be Lebesgue outer measure on $\RR^n$ and $m$ Lebesgue measure. For every $A \subseteq \RR^n$ and $\eps > 0$ there is a measurable $B \supseteq A$ with $m(B) \le m^*(A) + \eps$, by outer regularity.

::: pf

::: {.pf-step #s1}

(a) If $E_1 \subseteq E_2 \subseteq \cdots$ and $E = \bigcup_j E_j$, then $m^*(E_j) \to m^*(E)$.

::: pf-proof

Monotonicity gives $m^*(E_j) \le m^*(E_{j+1}) \le m^*(E)$. Fix $\eps > 0$ and choose measurable $B_k \supseteq E_k$ with $m(B_k) \le m^*(E_k) + \eps$. Put $C_j = \bigcap_{k \ge j} B_k$. Since $E_j \subseteq E_k \subseteq B_k$ for $k \ge j$, $C_j \supseteq E_j$; the $C_j$ increase; and $m(C_j) \le m(B_j)$. So $E \subseteq \bigcup_j C_j$, and continuity from below for $m$ gives $m^*(E) \le \lim_j m(C_j) \le \lim_j m^*(E_j) + \eps$. Since $\eps$ is arbitrary, $m^*(E) \le \lim_j m^*(E_j)$.

:::

:::

::: {.pf-step #s2}

(a) If $E_1 \supseteq E_2 \supseteq \cdots$ are measurable, $m(E_1) < \infty$, and $E = \bigcap_j E_j$, then $m(E_j) \to m(E)$.

::: pf-proof

The sets $E_1 \setminus E_j$ increase to $E_1 \setminus E$, so continuity from below for $m$ gives $m(E_1 \setminus E_j) \to m(E_1 \setminus E)$. All these measures are finite, so $m(E_1 \setminus E_j) = m(E_1) - m(E_j)$ and $m(E_1 \setminus E) = m(E_1) - m(E)$; hence $m(E_j) \to m(E)$.

:::

:::

::: pf-step

(b) A countable union of null sets is null.

::: pf-proof

$m^*(\bigcup_k E_k) \le \sum_k m^*(E_k) = 0$ by countable subadditivity.

:::

:::

::: {.pf-step #nonneg}

If $g \ge 0$ is measurable and $\int g = 0$, then $g = 0$ a.e.

::: pf-proof

For every $k$, $\int g \ge \frac1k m\theset{g \ge 1/k}$ gives $m\theset{g \ge 1/k} = 0$, so $\theset{g > 0} = \bigcup_k \theset{g \ge 1/k}$ is null by (b).

:::

:::

::: pf-step

(c) For integrable real-valued $f$, $f = 0$ a.e. if and only if $\int_E f = 0$ for every measurable $E$.

::: pf-proof

If $f = 0$ a.e., then $f\chi_E = 0$ a.e. and $\int_E f = 0$. Conversely, $E = \theset{f > 0}$ gives $\int f^+ = \int_E f = 0$, so $f^+ = 0$ a.e. by step [](#nonneg){.pf-ref}; $E = \theset{f < 0}$ gives $\int f^- = -\int_E f = 0$, so $f^- = 0$ a.e. Hence $f = f^+ - f^- = 0$ a.e.

:::

:::

::: pf-step

(d) For measurable $f \ge 0$, $f = 0$ a.e. if and only if $\int f = 0$.

::: pf-proof

If $f = 0$ a.e., then $\int f = 0$. The converse is step [](#nonneg){.pf-ref}.

:::

:::

::: pf-step

(e) On a measure space with $\mu(X) < \infty$, a bounded function is integrable if and only if it is measurable.

::: pf-proof

Lebesgue integrability is defined for measurable functions. If $f$ is measurable and $|f| \le M$, then $\int |f| \le M\mu(X) < \infty$.

:::

:::

::: {.pf-step #s6}

(f) Simple functions are dense in $L^1$.

::: pf-proof

It suffices to approximate $g \in L^1$ with $g \ge 0$, and then $f^+$ and $f^-$ separately. The simple functions $s_n = \min\big(2^{-n}\lfloor 2^n g\rfloor, n\big)$ satisfy $0 \le s_n \le g$ and $s_n \to g$ wherever $g < \infty$, hence a.e., so dominated convergence with dominating function $g$ gives $\|g - s_n\|_1 \to 0$.

:::

:::

::: pf-step

(g) Step functions are dense in $L^1(\RR)$.

::: pf-proof

By step [](#s6){.pf-ref} it suffices to approximate $\chi_E$ with $m(E) < \infty$. Outer regularity gives an open $G \supseteq E$ with $m(G \setminus E) < \eps$. $G$ is a countable disjoint union of open intervals $I_k$, and $G_N = \bigcup_{k \le N} I_k$ satisfies $m(G \setminus G_N) \to 0$. So $\|\chi_{G_N} - \chi_E\|_1 = m(G_N \triangle E) < 2\eps$ for large $N$.

:::

:::

::: pf-step

(h) $C_c^\infty(\RR^n)$ is dense in $L^1(\RR^n)$.

::: pf-proof

Given $f \in L^1$, dominated convergence gives $R$ with $\|f - f\chi_{B(0,R)}\|_1 < \eps/2$. Let $\phi \ge 0$ be smooth with compact support and $\int \phi = 1$, and $\phi_\delta(x) = \delta^{-n}\phi(x/\delta)$. Then $(f\chi_{B(0,R)}) \ast \phi_\delta$ is smooth with compact support, and $\|(f\chi_{B(0,R)}) \ast \phi_\delta - f\chi_{B(0,R)}\|_1 \to 0$ as $\delta \to 0$ by continuity of translation in $L^1$.

:::

:::

:::

:::

