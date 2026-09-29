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
---

::: {.problem}
- Show that continuity of measure from above/below holds for outer measures.

- Show that a countable union of null sets is null.

Measurability

- Show that $f=0$ a.e. iff $\int_E f = 0$ for every measurable set $E$.

Integrability

- Show that if $f$ is a measurable function, then $f=0$ a.e. iff $\int f = 0$.

- Show that a bounded function is Lebesgue integrable iff it is measurable.

- Show that simple functions are dense in $L^1$.

- Show that step functions are dense in $L^1$.

- Show that smooth compactly supported functions are dense in $L^1$.
:::

::: {.solution}
Let $m^*$ be Lebesgue outer measure on $\RR^n$ and $m$ Lebesgue measure. For every $A \subseteq \RR^n$ and $\eps > 0$ there is a measurable $B \supseteq A$ with $m(B) \le m^*(A) + \eps$, by outer regularity.

::: pf

::: {.pf-step #s1}
If $E_1 \subseteq E_2 \subseteq \cdots$ and $E = \bigcup_j E_j$, then $m^*(E_j) \to m^*(E)$.

::: pf-proof
Monotonicity gives $m^*(E_j) \le m^*(E_{j+1}) \le m^*(E)$. Fix $\eps > 0$ and choose measurable $B_k \supseteq E_k$ with $m(B_k) \le m^*(E_k) + \eps$. Put $C_j = \bigcap_{k \ge j} B_k$. Since $E_j \subseteq E_k \subseteq B_k$ for $k \ge j$, $C_j \supseteq E_j$; the $C_j$ increase; and $m(C_j) \le m(B_j)$. So $E \subseteq \bigcup_j C_j$, and continuity from below for $m$ gives $m^*(E) \le \lim_j m(C_j) \le \lim_j m^*(E_j) + \eps$.
:::

:::

::: {.pf-step #s2}
Continuity from above fails for $m^*$: there are $E_1 \supseteq E_2 \supseteq \cdots$ in $[-1, 2]$ with $\bigcap_j E_j = \emptyset$ and $\inf_j m^*(E_j) > 0$.

::: pf-proof
Let $N \subseteq [0,1]$ contain exactly one point of each coset of $\QQ$ in $\RR$ meeting $[0,1]$, a Vitali set; $N$ is not measurable, so $m^*(N) > 0$. Let $(q_k)$ enumerate $\QQ \cap [-1,1]$; the translates $N + q_k$ are pairwise disjoint. Put $E_j = \bigcup_{k \ge j}(N + q_k)$. Then $E_j$ decreases, a point of $\bigcap_j E_j$ would lie in $N + q_k$ for infinitely many $k$, so $\bigcap_j E_j = \emptyset$, and $m^*(E_j) \ge m^*(N + q_j) = m^*(N)$.
:::

:::

::: pf-step
A countable union of null sets is null.

::: pf-proof
$m^*(\bigcup_k E_k) \le \sum_k m^*(E_k) = 0$ by countable subadditivity.
:::

:::

::: pf-step
For measurable $f \ge 0$, $f = 0$ a.e. if and only if $\int f = 0$, if and only if $\int_E f = 0$ for every measurable $E$.

::: pf-proof
If $f = 0$ a.e., then $f\chi_E = 0$ a.e. and $\int_E f = 0$ for every $E$, in particular for $E = \RR^n$. If $\int f = 0$, then $\int f \ge \frac1n m\theset{f \ge 1/n}$ gives $m\theset{f \ge 1/n} = 0$ for every $n$, and $\theset{f > 0} = \bigcup_n \theset{f \ge 1/n}$ is null.
:::

:::

::: pf-step
On a measure space with $\mu(X) < \infty$, a bounded function is integrable if and only if it is measurable.

::: pf-proof
Lebesgue integrability is defined for measurable functions. If $f$ is measurable and $|f| \le M$, then $\int |f| \le M\mu(X) < \infty$.
:::

:::

::: {.pf-step #s6}
Simple functions are dense in $L^1$.

::: pf-proof
It suffices to approximate $g \in L^1$ with $g \ge 0$, and then $f^+$ and $f^-$ separately. The simple functions $s_n = \min\big(2^{-n}\lfloor 2^n g\rfloor, n\big)$ satisfy $0 \le s_n \le g$ and $s_n \to g$ wherever $g < \infty$, hence a.e., so dominated convergence with dominating function $g$ gives $\|g - s_n\|_1 \to 0$.
:::

:::

::: pf-step
Step functions are dense in $L^1(\RR)$.

::: pf-proof
By step [](#s6){.pf-ref} it suffices to approximate $\chi_E$ with $m(E) < \infty$. Outer regularity gives an open $G \supseteq E$ with $m(G \setminus E) < \eps$. $G$ is a countable disjoint union of open intervals $I_k$, and $G_N = \bigcup_{k \le N} I_k$ satisfies $m(G \setminus G_N) \to 0$. So $\|\chi_{G_N} - \chi_E\|_1 = m(G_N \triangle E) < 2\eps$ for large $N$.
:::

:::

::: pf-step
$C_c^\infty(\RR^n)$ is dense in $L^1(\RR^n)$.

::: pf-proof
Given $f \in L^1$, dominated convergence gives $R$ with $\|f - f\chi_{B(0,R)}\|_1 < \eps/2$. Let $\phi \ge 0$ be smooth with compact support and $\int \phi = 1$, and $\phi_\delta(x) = \delta^{-n}\phi(x/\delta)$. Then $(f\chi_{B(0,R)}) \ast \phi_\delta$ is smooth with compact support, and $\|(f\chi_{B(0,R)}) \ast \phi_\delta - f\chi_{B(0,R)}\|_1 \to 0$ as $\delta \to 0$ by continuity of translation in $L^1$.
:::

:::

:::

:::

::: {.remark}
Erratum: continuity from below holds for Lebesgue outer measure (step [](#s1){.pf-ref}), but not for every outer measure; see [[E-ASWCD]]. Continuity from above fails even for Lebesgue outer measure on sets of finite outer measure (step [](#s2){.pf-ref}); it holds for measurable sets. The integral statements need $f \ge 0$: for $f = \chi_{[0,1]} - \chi_{[1,2]}$, $\int f = 0$ but $f \neq 0$ on a set of measure $2$. The boundedness statement needs a finite measure space.
:::
