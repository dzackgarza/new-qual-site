---
schema: qual/card@1
id: P-RASP09A
kind: problem
title: "True or false: everywhere-large L^1 functions, Fubini with counting measure, signed measure absolute continuity, products in measure, norm lower semicontinuity"
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Tonelli-Fubini Theorem
  - Signed Measures
  - Absolute Continuity
  - Convergence in Measure
  - Weak Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2009 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Repaired the part (a) counterexample so it has the required property on every interval of R, then normalized legacy solution/proof blocks.
---

::: {.problem}
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample (or prove your assertion in another way, if you prefer).

(a) There does not exist a Lebesgue integrable function $f \in L^1(\mathbb{R})$ such that for any $A > 0$ and any interval $(a, b)$, $m(\{x \in (a,b) \mid f(x) > A\}) > 0$.

(b) Let $\mu(A) = \#A$ be the counting measure and $D = \{(x, y) \in [0, 1]^2 \mid x = y\}$ the diagonal in $[0, 1]^2$.
Then by the Tonelli-Fubini theorem, the iterated integrals
$$
\int_0^1 \int_0^1 \chi_D(x, y) \, dm(x) \, d\mu(y) = \int_0^1 \int_0^1 \chi_D(x, y) \, d\mu(y) \, dm(x).
$$
Here $m$ is the Lebesgue measure and $\chi_D$ is the characteristic function of $D$.

(c) Let $\nu$ be a signed measure and $\mu$ a positive measure.
Then $\nu \ll \mu$ if and only if $\nu^+ \ll \mu$ and $\nu^- \ll \mu$.

(d) Let $f_n$ and $g_n$ be real-valued Lebesgue measurable functions on $\mathbb{R}$.
Assume that $f_n \to f$ and $g_n \to g$ in measure; then $f_n g_n \to f g$ in measure.

(e) Let $D$ be a bounded domain in $\mathbb{R}^n$.
If $f_n \in L^p(D)$ for $1 < p < \infty$ and converges weakly to $f \in L^p(D)$, then $\|f\|_p \leq \liminf_{n \to \infty} \|f_n\|_p$.
:::

::: {.solution}
**(a) False.**

::: pf

::: pf-step
Enumerate the rationals in $\mathbb R$ as $\{q_n\}_{n \ge 1}$ and define
$$
f(x)=\sum_{n=1}^{\infty}2^{-n}|x-q_n|^{-1/2}\mathbf1_{\{|x-q_n|<1\}}.
$$

::: pf-proof
construct a candidate.
:::

:::

::: {.pf-step #p1-s2}
$f \in L^1(\mathbb{R})$.

::: pf-proof
By Tonelli's theorem,
\[
\int_{\mathbb R}f(x)\,dx
=\sum_{n=1}^\infty2^{-n}
\int_{|x-q_n|<1}|x-q_n|^{-1/2}\,dx.
\]
The inner integral equals
\[
2\int_0^1 t^{-1/2}\,dt=4.
\]
Hence
\[
\int_{\mathbb R}f\le4\sum_{n=1}^\infty2^{-n}=4<\infty.
\]
:::

:::

::: pf-step
For any interval $(a,b)$ and any $A > 0$, there is a rational $q_n \in (a,b)$.

::: pf-proof
the rationals are dense.
:::

:::

::: {.pf-step #p1-s4}
Near $q_n$, the $n$th summand forces $f(x)>A$ on a set of positive measure inside $(a,b)$.

::: pf-proof
Choose $\delta>0$ so small that
\[
(q_n-\delta,q_n+\delta)\subset(a,b),
\qquad
\delta<1,
\qquad
2^{-n}\delta^{-1/2}>A.
\]
Then for every $x$ with $0<|x-q_n|<\delta$,
\[
f(x)\ge2^{-n}|x-q_n|^{-1/2}>A.
\]
This punctured interval has positive measure.
:::

:::

::: pf-step
Hence the statement "there does not exist such an $f$" is **false**.

::: pf-proof
step [](#p1-s2){.pf-ref} and step [](#p1-s4){.pf-ref} exhibit such an $f$.
:::

:::

:::

**(b) False.**

::: pf

::: {.pf-step #p2-s1}
The counting measure $\mu$ on $[0,1]$ is not $\sigma$-finite.

::: pf-proof
$[0,1]$ is uncountable, so it is not a countable union of sets of finite counting measure.
:::

:::

::: pf-step
Hence the Tonelli–Fubini theorem does not apply.

::: pf-proof
step [](#p2-s1){.pf-ref} (the theorem requires $\sigma$-finite measures).
:::

:::

::: {.pf-step #p2-s3}
$\int_0^1 \int_0^1 \chi_D(x,y)\,dm(x)\,d\mu(y) = 0$.

::: pf-proof
for fixed $y$, $\chi_D(x,y) = 1$ only at the single point $x = y$, so the inner integral is $m(\{y\}) = 0$.
:::

:::

::: {.pf-step #p2-s4}
$\int_0^1 \int_0^1 \chi_D(x,y)\,d\mu(y)\,dm(x) = 1$.

::: pf-proof
for fixed $x$, $\chi_D(x,y) = 1$ only at $y = x$, so the inner integral is $\mu(\{x\}) = 1$, and $\int_0^1 1\,dm = 1$.
:::

:::

::: pf-step
The two iterated integrals are unequal ($0 \ne 1$), so the claimed equality is **false**.

::: pf-proof
step [](#p2-s3){.pf-ref} and step [](#p2-s4){.pf-ref}.
:::

:::

:::

**(c) True.**

::: pf

::: {.pf-step #p3-s1}
Let $\nu = \nu^+ - \nu^-$ be the Jordan decomposition, with $P \cup N$ a Hahn decomposition.

::: pf-proof
Jordan decomposition theorem.
:::

:::

::: {.pf-step #p3-s2}
($\Rightarrow$) Suppose $\nu \ll \mu$ and $\mu(E) = 0$. Then $\nu(E) = 0$.

::: pf-proof
definition of absolute continuity.
:::

:::

::: {.pf-step #p3-s3}
$\nu^+(E) = \nu(E \cap P) = 0$ and $\nu^-(E) = -\nu(E \cap N) = 0$.

::: pf-proof
$E \cap P \subseteq E$ has $\mu$-measure $0$, so $\nu(E \cap P) = 0$ by step [](#p3-s2){.pf-ref}; similarly for $N$.
:::

:::

::: {.pf-step #p3-s4}
Hence $\nu^+ \ll \mu$ and $\nu^- \ll \mu$.

::: pf-proof
step [](#p3-s3){.pf-ref}.
:::

:::

::: {.pf-step #p3-s5}
($\Leftarrow$) Suppose $\nu^+ \ll \mu$ and $\nu^- \ll \mu$, and $\mu(E) = 0$. Then $\nu(E) = \nu^+(E) - \nu^-(E) = 0 - 0 = 0$.

::: pf-proof
step [](#p3-s1){.pf-ref} and the hypotheses.
:::

:::

::: pf-step
Hence $\nu \ll \mu$ iff $\nu^+ \ll \mu$ and $\nu^- \ll \mu$; the statement is **true**.

::: pf-proof
step [](#p3-s4){.pf-ref} and step [](#p3-s5){.pf-ref}.
:::

:::

:::

**(d) False.**

::: pf

::: pf-step
Take $f_n(x) = x$ and $g_n(x) = 1/n$ on $\mathbb{R}$.

::: pf-proof
construct a counterexample.
:::

:::

::: pf-step
$f_n \to f = x$ in measure.

::: pf-proof
$f_n = x$ exactly, so $m(\{|f_n - x| > \varepsilon\}) = 0$ for all $n$.
:::

:::

::: pf-step
$g_n \to g = 0$ in measure.

::: pf-proof
for $n > 1/\varepsilon$, $m(\{|1/n| > \varepsilon\}) = 0$.
:::

:::

::: {.pf-step #p4-s4}
$f_n g_n = x/n$, and $m(\{|x/n| > \varepsilon\}) = m(\{|x| > n\varepsilon\}) = \infty$ for every $n$.

::: pf-proof
the set $\{|x| > n\varepsilon\}$ has infinite Lebesgue measure.
:::

:::

::: pf-step
Hence $f_n g_n$ does not converge to $0 = fg$ in measure, so the statement is **false**.

::: pf-proof
step [](#p4-s4){.pf-ref}.
:::

:::

:::

**(e) True.**

::: pf

::: pf-step
$L^p(D)$ is reflexive for $1 < p < \infty$, and its dual is $L^q(D)$ with $1/p + 1/q = 1$.

::: pf-proof
standard duality theorem.
:::

:::

::: {.pf-step #p5-s2}
Since $f_n \rightharpoonup f$ weakly, for every $g \in L^q(D)$ with $\|g\|_q = 1$, $\int f g = \lim_n \int f_n g$.

::: pf-proof
definition of weak convergence.
:::

:::

::: {.pf-step #p5-s3}
Choose $g \in L^q(D)$ with $\|g\|_q = 1$ and $\int f g = \|f\|_p$.

::: pf-proof
the norm is attained on the unit sphere of the dual (Hahn–Banach / duality).
:::

:::

::: {.pf-step #p5-s4}
Then $\|f\|_p = \int f g = \lim_n \int f_n g \le \liminf_n \|f_n\|_p \|g\|_q = \liminf_n \|f_n\|_p$.

::: pf-proof
step [](#p5-s2){.pf-ref}, step [](#p5-s3){.pf-ref}, and Hölder's inequality.
:::

:::

::: pf-step
Hence $\|f\|_p \le \liminf_n \|f_n\|_p$; the statement is **true**.

::: pf-proof
step [](#p5-s4){.pf-ref}.
:::

:::

:::
:::
