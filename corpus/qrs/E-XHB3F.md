---
schema: qual/card@1
id: E-XHB3F
kind: exercise
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
---

::: exercise
- Show that if $f$ is a measurable function, then $f=0$ a.e. iff $\int f = 0$.

- Show that a bounded function is Lebesgue integrable iff it is measurable.

- Show that simple functions are dense in $L^1$.

- Show that step functions are dense in $L^1$.

- Show that smooth compactly supported functions are dense in $L^1$.
:::

::: {.solution}
**Honesty note:** the first bullet is true as stated only for non-negative measurable $f$ (or for $|f|$): for signed $f \in L^1$, $\int f = 0$ does not imply $f = 0$ a.e. (e.g. $f = \chi_{[0,1]} - \chi_{[1,2]}$). The solution proves the correct statement and records the counterexample.

<1>1. For non-negative measurable $f$: $f = 0$ a.e. $\iff$ $\int f = 0$.
<2>1. If $f = 0$ a.e., then $\int f = 0$.
Proof: an integral over a null set vanishes; every non-negative measurable function zero a.e. has integral $0$ (e.g. by definition of the integral via simple functions).
<2>2. If $\int f = 0$ and $f \ge 0$, then $f = 0$ a.e. Proof: write $\{f > 0\} = \bigcup_{k} \{f > 1/k\}$; if $\mu\{f > 1/k\} > 0$ for some $k$, then $\int f \ge \frac{1}{k}\mu\{f > 1/k\} > 0$, contradicting $\int f = 0$.
<2>3. The signed version fails.
Proof: $f = \chi_{[0,1]} - \chi_{[1,2]}$ is measurable with $\int f = 0$ but $f \ne 0$ on a set of measure $2$.
<2>4. Q.E.D. Proof: <2>1 and <2>2; <2>3 records the failure of the unrestricted statement.

<1>2. A bounded function on a finite measure space is Lebesgue integrable iff it is measurable.
<2>1. If a bounded function is integrable, it is measurable.
Proof: Lebesgue integrability is defined for measurable functions.
<2>2. A bounded measurable function on a finite measure space is integrable.
Proof: $|f| \le M$ a.e. for some $M$, so $|f|$ is dominated by the integrable constant function $M$ (constant functions are integrable since the measure is finite), and the dominated convergence theorem (or the definition of the integral) gives integrability.
<2>3. The finiteness of the measure is needed.
Proof: on $\RR$ with Lebesgue measure, the bounded measurable function $f \equiv 1$ is not integrable ($\int 1 = \infty$). For compactly supported bounded functions the claim holds without a finite measure assumption.
<2>4. Q.E.D. Proof: <2>1 and <2>2.

<1>3. Simple functions are dense in $L^1$.
<2>1. It suffices to approximate non-negative $f \in L^1$; then handle $f = f^+ - f^-$.
Proof: $\|f - s\|_1 \le \|f^+ - s_1\|_1 + \|f^- - s_2\|_1$.
<2>2. For non-negative $f \in L^1$, define $s_k = \sum_{j=1}^{k 2^k}\frac{j-1}{2^k}\chi_{\{\frac{j-1}{2^k} \le f < \frac{j}{2^k}\}} + k\chi_{\{f \ge k\}}$.
Proof: standard dyadic approximation; each $s_k$ is simple, $s_k \nearrow f$ pointwise, and $s_k \le f$.
<2>3. $\|s_k - f\|_1 \to 0$.
Proof: $|s_k - f| = f - s_k \le f \in L^1$ and $f - s_k \to 0$ pointwise (as $s_k \nearrow f$), so dominated convergence applies.
<2>4. Q.E.D. Proof: <2>1–<2>3.

<1>4. Step functions are dense in $L^1$.
<2>1. Every indicator $\chi_E$ of a measurable set of finite measure is approximated in $L^1$ by step functions.
Proof: outer regularity gives an open $U \supseteq E$ with $m(U \setminus E) < \eps$, and $U$ is a countable disjoint union of open intervals $U = \bigcup_i I_i$; the finite union $U_N = \bigcup_{i \le N} I_i$ has $\chi_{U_N} \to \chi_U$ pointwise with $|\chi_{U_N} - \chi_U| \le \chi_U \in L^1$ (since $m(U) \le m(E) + \eps < \infty$), so $\|\chi_{U_N} - \chi_U\|_1 \to 0$ by dominated convergence; then $\|\chi_E - \chi_{U_N}\|_1 \le \|\chi_E - \chi_U\|_1 + \|\chi_U - \chi_{U_N}\|_1 = m(U \setminus E) + m(U \setminus U_N) < 2\eps$ for $N$ large.
<2>2. Every simple function is approximated in $L^1$ by step functions.
Proof: finite linear combinations of the approximations from <2>1, with $\|s - s'\|_1 \le \sum_i |a_i|\,\|\chi_{E_i} - \chi_{I_i}\|_1$.
<2>3. Q.E.D. Proof: <1>3 approximates $f$ by simple functions, <2>1–<2>2 approximate simple functions by step functions, and the triangle inequality combines them ($\eps/3$ argument).

<1>5. Smooth compactly supported functions are dense in $L^1(\RR^n)$.
<2>1. First truncate: $f_R = f\chi_{B(0,R)}$ has $\|f - f_R\|_1 \to 0$ as $R \to \infty$.
Proof: $|f - f_R| = |f|\chi_{\RR^n \setminus B(0,R)} \to 0$ pointwise with domination by $|f| \in L^1$; dominated convergence.
<2>2. Convolve with a mollifier: $\|f_R \ast \phi_\eps - f_R\|_1 \to 0$ as $\eps \to 0$.
Proof: $\phi_\eps$ is an approximate identity, and $\|g \ast \phi_\eps - g\|_1 \to 0$ for $g \in L^1$ (standard; the translation-continuity argument).
<2>3. $f_R \ast \phi_\eps$ is smooth and compactly supported.
Proof: differentiation under the integral gives smoothness; and $\supp(f_R \ast \phi_\eps) \subseteq \overline{\supp f_R + \supp \phi_\eps}$, which is compact.
<2>4. Q.E.D. Proof: $\|f - f_R \ast \phi_\eps\|_1 \le \|f - f_R\|_1 + \|f_R - f_R \ast \phi_\eps\|_1 \to 0$ by <2>1 and <2>2, and <2>3 shows the approximants are smooth with compact support.
:::
