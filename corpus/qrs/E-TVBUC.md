---
schema: qual/card@1
id: E-TVBUC
kind: exercise
title: "Show that if $E\\subseteq \\RR^n$ is measurable with $\\mu(E) < \\infty$ and $f\\in L^p(X)$ then $\\norm{f}_{L^p(X)} \\converges{p\\to\\infty}\\to \\norm{f}_\\infty$"
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - l-infty
  - limits
relations: []
review: draft
solved: true
---

::: exercise
- Show that if $E\subseteq \RR^n$ is measurable with $\mu(E) < \infty$ and $f\in L^p(X)$ then $$\norm{f}_{L^p(X)} \converges{p\to\infty}\to \norm{f}_\infty.$$
:::

::: {.solution}
> **AI-Generated Solution**

**Setup:** the card mixes $E$ and $X$; the intended statement is: if $(E, \mu)$ is a finite-measure space and $f$ is measurable with $\|f\|_p < \infty$ for all large $p$, then $\|f\|_{L^p(E)} \to \|f\|_{L^\infty(E)}$ as $p \to \infty$.

<1>1. Upper bound: $\limsup_{p \to \infty}\|f\|_p \le \|f\|_\infty$.
<2>1. $\|f\|_p \le \|f\|_\infty\,\mu(E)^{1/p}$ for every finite $p$.
Proof: $|f| \le \|f\|_\infty$ a.e., so $\int_E |f|^p \le \|f\|_\infty^p\,\mu(E)$.
<2>2. Q.E.D. Proof: $\mu(E)^{1/p} \to 1$ as $p \to \infty$ since $0 < \mu(E) < \infty$ (the case $\mu(E) = 0$ is trivial, and if $\|f\|_\infty = \infty$ the bound is vacuous but the lower bound below handles it).

<1>2. Lower bound: $\liminf_{p \to \infty}\|f\|_p \ge \|f\|_\infty$.
<2>1. For any $M < \|f\|_\infty$, the set $A_M = \{x : |f(x)| > M\}$ has $\mu(A_M) > 0$.
Proof: definition of the essential supremum.
<2>2. $\|f\|_p \ge M\,\mu(A_M)^{1/p}$ for every $p$.
Proof: on $A_M$, $|f|^p > M^p$, so $\int_E|f|^p \ge M^p\mu(A_M)$.
<2>3. $\liminf_{p\to\infty}\|f\|_p \ge M$, and letting $M \nearrow \|f\|_\infty$ gives $\liminf_p \|f\|_p \ge \|f\|_\infty$.
Proof: $\mu(A_M)^{1/p} \to 1$ as $p \to \infty$ (positive finite measure); if $\|f\|_\infty = \infty$, take $M$ arbitrarily large.
<2>4. Q.E.D. Proof: <2>1–<2>3.

<1>3. Q.E.D. Proof: <1>1 and <1>2 sandwich $\|f\|_p$ between quantities converging to $\|f\|_\infty$.
:::
