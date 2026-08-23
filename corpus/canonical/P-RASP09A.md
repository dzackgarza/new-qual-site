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
solved: false
---

::: problem
Determine if the statements below are True or False. If True, give a brief proof. If False, give a counterexample (or prove your assertion in another way, if you prefer).

(a) There does not exist a Lebesgue integrable function $f \in L^1(\mathbb{R})$ such that for any $A > 0$ and any interval $(a, b)$, $m(\{x \in (a,b) \mid f(x) > A\}) > 0$.

(b) Let $\mu(A) = \#A$ be the counting measure and $D = \{(x, y) \in [0, 1]^2 \mid x = y\}$ the diagonal in $[0, 1]^2$. Then by the Tonelli-Fubini theorem, the iterated integrals
$$
\int_0^1 \int_0^1 \chi_D(x, y) \, dm(x) \, d\mu(y) = \int_0^1 \int_0^1 \chi_D(x, y) \, d\mu(y) \, dm(x).
$$
Here $m$ is the Lebesgue measure and $\chi_D$ is the characteristic function of $D$.

(c) Let $\nu$ be a signed measure and $\mu$ a positive measure. Then $\nu \ll \mu$ if and only if $\nu^+ \ll \mu$ and $\nu^- \ll \mu$.

(d) Let $f_n$ and $g_n$ be real-valued Lebesgue measurable functions on $\mathbb{R}$. Assume that $f_n \to f$ and $g_n \to g$ in measure; then $f_n g_n \to f g$ in measure.

(e) Let $D$ be a bounded domain in $\mathbb{R}^n$. If $f_n \in L^p(D)$ for $1 < p < \infty$ and converges weakly to $f \in L^p(D)$, then $\|f\|_p \leq \liminf_{n \to \infty} \|f_n\|_p$.
:::