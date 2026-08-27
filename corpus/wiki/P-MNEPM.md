---
schema: qual/card@1
id: P-MNEPM
kind: problem
title: 'Linear functionals: definition, boundedness equivalent to continuity, and
  completeness of the dual'
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let $X$ be a normed vector space.

a. Give the definition of what it means for a map $L:X\to \CC$ to be a *linear functional*.

b. Define what it means for $L$ to be *bounded* and show $L$ is bounded $\iff L$ is continuous.

c. Prove that $(X\dual, \norm{\wait}_{\op})$ is a Banach space.
:::
::: {.solution}
<1>1. (a) Definition: $L : X \to \CC$ is a linear functional iff $L(x + y) = L(x) + L(y)$ and $L(\alpha x) = \alpha L(x)$ for all $x, y \in X$, $\alpha \in \CC$.
Proof: definition.

<1>2. (b) $L$ is bounded iff $L$ is continuous.
<2>1. Definitions: $L$ is bounded iff $\|L\|_{\op} := \sup_{\|x\| \le 1}|L(x)| < \infty$; $L$ is continuous iff $x_n \to x \Rightarrow L(x_n) \to L(x)$ (or the $\eps$-$\delta$ form).
Proof: definitions.
<2>2. Bounded $\Rightarrow$ continuous: $|L(x_n) - L(x)| = |L(x_n - x)| \le \|L\|_{\op}\|x_n - x\| \to 0$.
Proof: linearity and the operator norm bound.
<2>3. Continuous $\Rightarrow$ bounded: if $L$ were unbounded, there would be $x_n$ with $\|x_n\| = 1$ and $|L(x_n)| \ge n$; then $y_n = x_n/n \to 0$ but $|L(y_n)| = |L(x_n)|/n \ge 1 \not\to 0$, contradicting continuity at $0$.
Proof: contrapositive; continuity at $0$ suffices (linearity).

<1>3. (c) $X\dual = \{L : X \to \CC \text{ bounded linear}\}$ with $\|\cdot\|_{\op}$ is a Banach space.
<2>1. $\|\cdot\|_{\op}$ is a norm on $X\dual$.
Proof: $\|L\|_{\op} = 0$ iff $L = 0$ (evaluate on unit vectors); $\|\alpha L\| = |\alpha|\|L\|$; triangle inequality $\|L + M\| \le \|L\| + \|M\|$ (sup of the sum $\le$ sum of sups).
<2>2. Completeness: let $(L_n)$ be Cauchy in $X\dual$; then for each $x$, $(L_n(x))$ is Cauchy in $\CC$ (since $|L_n(x) - L_m(x)| \le \|L_n - L_m\|_{\op}\|x\|$), so $L_n(x) \to L(x)$ pointwise.
Proof: completeness of $\CC$; define $L(x) = \lim_n L_n(x)$.
<2>3. $L$ is linear: $L(\alpha x + y) = \lim_n L_n(\alpha x + y) = \lim_n (\alpha L_n(x) + L_n(y)) = \alpha L(x) + L(y)$.
Proof: pass limits through the linear combination.
<2>4. $L$ is bounded and $\|L_n - L\|_{\op} \to 0$.
Proof: for $\eps > 0$ choose $N$ with $\|L_n - L_m\| < \eps$ for $n, m \ge N$; then for $\|x\| \le 1$, $|L(x) - L_N(x)| = \lim_m |L_m(x) - L_N(x)| \le \eps$, so $\|L - L_N\| \le \eps$; hence $L \in X\dual$ (bounded: $\|L\| \le \|L_N\| + \eps$) and $L_n \to L$ in norm.

<1>4. Q.E.D. Proof: <1>1–<1>3 settle (a), (b), (c).
:::
