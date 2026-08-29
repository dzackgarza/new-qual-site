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
---

::: problem
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

<1>1. Enumerate the rationals in $[0,1]$ as $\{q_n\}_{n \ge 1}$ and define
$$f(x) = \sum_{n=1}^{\infty} 2^{-n} |x - q_n|^{-1/2} \cdot \chi_{[0,1]}(x).$$
Proof: construct a candidate.

<1>2. $f \in L^1(\mathbb{R})$.
Proof: $\int_0^1 |x - q_n|^{-1/2}\,dx \le 2$ for each $n$, so $\int f \le \sum_n 2^{-n} \cdot 2 = 2 < \infty$.

<1>3. For any interval $(a,b)$ and any $A > 0$, there is a rational $q_n \in (a,b)$.
Proof: the rationals are dense.

<1>4. Near $q_n$, $|x - q_n|^{-1/2} \to \infty$, so $f(x) > A$ on a set of positive measure inside $(a,b)$.
Proof: <1>1 and <1>3; the term $2^{-n}|x-q_n|^{-1/2}$ dominates near $q_n$.

<1>5. Hence the statement "there does not exist such an $f$" is **false**.
Proof: <1>2 and <1>4 exhibit such an $f$.

**(b) False.**

<1>1. The counting measure $\mu$ on $[0,1]$ is not $\sigma$-finite.
Proof: $[0,1]$ is uncountable, so it is not a countable union of sets of finite counting measure.

<1>2. Hence the Tonelli–Fubini theorem does not apply.
Proof: <1>1 (the theorem requires $\sigma$-finite measures).

<1>3. $\int_0^1 \int_0^1 \chi_D(x,y)\,dm(x)\,d\mu(y) = 0$.
Proof: for fixed $y$, $\chi_D(x,y) = 1$ only at the single point $x = y$, so the inner integral is $m(\{y\}) = 0$.

<1>4. $\int_0^1 \int_0^1 \chi_D(x,y)\,d\mu(y)\,dm(x) = 1$.
Proof: for fixed $x$, $\chi_D(x,y) = 1$ only at $y = x$, so the inner integral is $\mu(\{x\}) = 1$, and $\int_0^1 1\,dm = 1$.

<1>5. The two iterated integrals are unequal ($0 \ne 1$), so the claimed equality is **false**.
Proof: <1>3 and <1>4.

**(c) True.**

<1>1. Let $\nu = \nu^+ - \nu^-$ be the Jordan decomposition, with $P \cup N$ a Hahn decomposition.
Proof: Jordan decomposition theorem.

<1>2. ($\Rightarrow$) Suppose $\nu \ll \mu$ and $\mu(E) = 0$. Then $\nu(E) = 0$.
Proof: definition of absolute continuity.

<1>3. $\nu^+(E) = \nu(E \cap P) = 0$ and $\nu^-(E) = -\nu(E \cap N) = 0$.
Proof: $E \cap P \subseteq E$ has $\mu$-measure $0$, so $\nu(E \cap P) = 0$ by <1>2; similarly for $N$.

<1>4. Hence $\nu^+ \ll \mu$ and $\nu^- \ll \mu$.
Proof: <1>3.

<1>5. ($\Leftarrow$) Suppose $\nu^+ \ll \mu$ and $\nu^- \ll \mu$, and $\mu(E) = 0$. Then $\nu(E) = \nu^+(E) - \nu^-(E) = 0 - 0 = 0$.
Proof: <1>1 and the hypotheses.

<1>6. Hence $\nu \ll \mu$ iff $\nu^+ \ll \mu$ and $\nu^- \ll \mu$; the statement is **true**.
Proof: <1>4 and <1>5.

**(d) False.**

<1>1. Take $f_n(x) = x$ and $g_n(x) = 1/n$ on $\mathbb{R}$.
Proof: construct a counterexample.

<1>2. $f_n \to f = x$ in measure.
Proof: $f_n = x$ exactly, so $m(\{|f_n - x| > \varepsilon\}) = 0$ for all $n$.

<1>3. $g_n \to g = 0$ in measure.
Proof: for $n > 1/\varepsilon$, $m(\{|1/n| > \varepsilon\}) = 0$.

<1>4. $f_n g_n = x/n$, and $m(\{|x/n| > \varepsilon\}) = m(\{|x| > n\varepsilon\}) = \infty$ for every $n$.
Proof: the set $\{|x| > n\varepsilon\}$ has infinite Lebesgue measure.

<1>5. Hence $f_n g_n$ does not converge to $0 = fg$ in measure, so the statement is **false**.
Proof: <1>4.

**(e) True.**

<1>1. $L^p(D)$ is reflexive for $1 < p < \infty$, and its dual is $L^q(D)$ with $1/p + 1/q = 1$.
Proof: standard duality theorem.

<1>2. Since $f_n \rightharpoonup f$ weakly, for every $g \in L^q(D)$ with $\|g\|_q = 1$, $\int f g = \lim_n \int f_n g$.
Proof: definition of weak convergence.

<1>3. Choose $g \in L^q(D)$ with $\|g\|_q = 1$ and $\int f g = \|f\|_p$.
Proof: the norm is attained on the unit sphere of the dual (Hahn–Banach / duality).

<1>4. Then $\|f\|_p = \int f g = \lim_n \int f_n g \le \liminf_n \|f_n\|_p \|g\|_q = \liminf_n \|f_n\|_p$.
Proof: <1>2, <1>3, and Hölder's inequality.

<1>5. Hence $\|f\|_p \le \liminf_n \|f_n\|_p$; the statement is **true**.
Proof: <1>4.
:::
