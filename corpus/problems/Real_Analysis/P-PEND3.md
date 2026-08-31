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

::: problem
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
<1>1. (Continuity from below.)
If $E_j \nearrow E$, then $\mu^*(E_j) \nearrow \mu^*(E)$.
::: {.proof}
monotonicity of $\mu^*$ gives $\mu^*(E_j) \le \mu^*(E)$ for each $j$.
:::
For the reverse inequality, use that for Lebesgue outer measure every set has a measurable envelope: $\mu^*(A) = \inf\{\mu(B) : B \supseteq A,\ B \text{ measurable}\}$.
Choose measurable $B_j \supseteq E_j$ with $\mu(B_j) \le \mu^*(E_j) + \eps/2^j$, and set $B_j' = \cap_{k \ge j} B_k$; then $B_j' \supseteq E_j$ (since $E_j \subseteq E_k \subseteq B_k$ for $k \ge j$), the $B_j'$ increase, and $\mu(B_j') \le \mu(B_j)$.
Hence, by continuity from below for the measure $\mu$ on measurable sets, \[ \mu^*(E) \le \mu\!\Big(\bigcup_j B_j'\Big) = \lim_j \mu(B_j') \le \lim_j \big(\mu^*(E_j) + \eps/2^j\big) = \lim_j \mu^*(E_j), \] and $\eps > 0$ is arbitrary.
<1>2. (Continuity from above.)
If $E_j \searrow E$ and $\mu^*(E_1) < \infty$, then $\mu^*(E_j) \searrow \mu^*(E)$.
::: {.proof}
monotonicity gives $\mu^*(E_j) \ge \mu^*(E)$.
:::
Conversely, choose measurable $B_j \supseteq E_j$ with $\mu(B_j) \le \mu^*(E_j) + \eps/2^j$ and set $B_j' = \cap_{k \le j} B_k$; then $B_j' \supseteq E_j$ (since $E_j \subseteq E_k \subseteq B_k$ for $k \le j$), the $B_j'$ decrease, and $\mu(B_j') \le \mu(B_j)$.
By continuity from above for $\mu$ (finite first measure), \[ \mu^*(E) \le \mu\!\Big(\bigcap_j B_j'\Big) = \lim_j \mu(B_j') \le \lim_j \big(\mu^*(E_j) + \eps/2^j\big) = \lim_j \mu^*(E_j), \] so the limit is exactly $\mu^*(E)$.
The hypothesis $\mu^*(E_1) < \infty$ is needed: $E_j = [j,\infty) \searrow \emptyset$ has $\mu^*(E_j) = \infty$ for every $j$.
<1>3. (Countable unions of null sets.)
If $\mu^*(E_k) = 0$ for all $k$, then $\mu^*(\cup_k E_k) = 0$.
::: {.proof}
countable subadditivity of $\mu^*$ gives $\mu^*(\cup_k E_k) \le \sum_k \mu^*(E_k) = 0$.
:::
<1>4. (Zero integral on every measurable set.)
For $f \ge 0$ measurable: $f = 0$ a.e. iff $\int_E f = 0$ for every measurable $E$.
::: {.proof}
if $f = 0$ a.e., then $f\chi_E = 0$ a.e., so $\int_E f = 0$.
:::
Conversely, if $\int_E f = 0$ for all measurable $E$, take $E = \{f > 0\} = \cup_n \{f \ge 1/n\}$; then $0 = \int_E f \ge \frac{1}{n}\mu\{f \ge 1/n\}$, so $\mu\{f \ge 1/n\} = 0$ for all $n$, hence $\mu\{f>0\} = 0$.
<1>5. (Zero integral.)
For $f \ge 0$ measurable: $f = 0$ a.e. iff $\int f = 0$.
::: {.proof}
$\int f = 0$ and $\int f \ge \frac{1}{n}\mu\{f \ge 1/n\}$ force $\mu\{f\ge 1/n\} = 0$ for every $n$; conversely $f = 0$ a.e. gives $\int f = 0$.
:::
(The equivalence can fail for signed $f$, e.g. $\chi_{[0,1]} - \chi_{[1,2]}$.)
<1>6. (Bounded functions.)
On a finite measure space, a bounded measurable function is Lebesgue integrable; and a bounded function that is Lebesgue integrable is measurable.
::: {.proof}
if $f$ is measurable and $|f| \le M$, then $|f| \le M\chi_X \in L^1$, so $f \in L^1$.
:::
Conversely, Lebesgue integrability is defined only for measurable functions.
(The first implication needs $\mu(X) < \infty$; on infinite measure spaces bounded measurable functions need not be integrable.)
<1>7. (Simple functions are dense in $L^1$.)
::: {.proof}
write $f = f^+ - f^-$ with $f^\pm \ge 0$; it suffices to approximate $g \in L^1$, $g \ge 0$.
:::
The dyadic truncations \[ s_n = \min\!\Big(\frac{\lfloor 2^n g\rfloor}{2^n},\, n\Big) \] are simple, $s_n \nearrow g$, and $0 \le g - s_n \le 2^{-n}\chi_{\{g \le n\}} + g\chi_{\{g > n\}} \to 0$ pointwise a.e. with domination by $g \in L^1$; the dominated convergence theorem gives $\norm{s_n - g}_1 \to 0$.
<1>8. (Step functions are dense in $L^1$.)
::: {.proof}
it suffices (by <1>7) to approximate $\chi_E$ for measurable $E$ with $m(E) < \infty$ by step functions.
:::
Outer regularity gives an open $G \supseteq E$ with $m(G\setminus E) < \eps$; $G$ is a countable disjoint union of open intervals $I_k$, so $G_N = \cup_{k\le N} I_k$ has $m(G \setminus G_N) \to 0$; then $\chi_{G_N}$, a step function, satisfies $\norm{\chi_{G_N} - \chi_E}_1 \le m(G_N \triangle E) < 2\eps$ for large $N$.
<1>9. (Smooth compactly supported functions are dense in $L^1$.)
::: {.proof}
by <1>7 and <1>8 it suffices to approximate $\chi_{[a,b]}$; and $\chi_{[a,b]}$ is approximated in $L^1$ by smooth bump functions (e.g. mollify $\chi_{[a,b]}$ against $\phi_\eps$ with a small $\eps$). In general: truncate $f$ to a large ball ($\norm{f - f\chi_{B(0,R)}}_1 < \eps/2$) and mollify: $\norm{f\chi_{B(0,R)} \ast \phi_\eps - f\chi_{B(0,R)}}_1 \to 0$ as $\eps \to 0$ by translation continuity in $L^1$.
:::
<1>10. Q.E.D.
:::
