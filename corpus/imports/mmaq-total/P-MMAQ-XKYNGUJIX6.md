---
schema: qual/card@1
id: P-MMAQ-XKYNGUJIX6
kind: problem
title: Let $C([0, 1])$ denote the space of all continuous real-valued…
classification:
  areas:
  - real-analysis
  topics:
  - function-spaces
  - norms
  - completeness
relations: []
review: draft
solved: true
---

::: problem
Let $C([0, 1])$ denote the space of all continuous real-valued functions on $[0, 1]$.

a.  Prove that $C([0, 1])$ is complete under the uniform norm $\norm{f}_u := \displaystyle\sup_{x\in [0,1]} |f (x)|$.
b.  Prove that $C([0, 1])$ is not complete under the $L^1\dash$norm $\norm{f}_1 = \displaystyle\int_0^1 |f (x)| ~dx$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) Prove $C([0,1])$ is complete under the uniform norm $\norm{f}_u = \sup_{x \in [0,1]} |f(x)|$; (b) prove it is not complete under the $L^1$ norm $\norm{f}_1 = \int_0^1 |f(x)| \, dx$.

<1>1. Proof of (a): completeness under the uniform norm.
<2>1. Let $\{f_n\}$ be Cauchy in $(C([0,1]), \norm{\cdot}_u)$.
For each $x \in [0,1]$, $\{f_n(x)\}$ is a Cauchy sequence of real numbers.
Proof: $|f_n(x) - f_m(x)| \leq \norm{f_n - f_m}_u \to 0$ as $n, m \to \infty$.
<2>2. Define $f(x) := \lim_n f_n(x)$; then $f_n \to f$ uniformly.
Proof: given $\varepsilon > 0$, choose $N$ with $\norm{f_n - f_m}_u < \varepsilon$ for all $n, m \geq N$.
For $n \geq N$ and every $x$, $|f_n(x) - f(x)| = \lim_m |f_n(x) - f_m(x)| \leq \varepsilon$, so $\norm{f_n - f}_u \leq \varepsilon$.
<2>3. $f$ is continuous.
Proof: $f$ is the uniform limit of continuous functions: given $x_0$ and $\varepsilon > 0$, pick $n$ with $\norm{f_n - f}_u < \varepsilon/3$; then for $x$ with $|x - x_0|$ small enough that $|f_n(x) - f_n(x_0)| < \varepsilon/3$ (continuity of $f_n$), the triangle inequality gives $|f(x) - f(x_0)| < \varepsilon$.
<2>4. Q.E.D. Proof: <2>2 and <2>3 show every Cauchy sequence converges in $C([0,1])$.

<1>2. Proof of (b): incompleteness under $\norm{\cdot}_1$.
<2>1. For $n \geq 2$ define $f_n(x) = 0$ on $[0, \frac12 - \frac1n]$, $f_n(x) = 1$ on $[\frac12, 1]$, and linear in between.
Each $f_n$ is continuous, and $\{f_n\}$ is Cauchy in $\norm{\cdot}_1$.
Proof: continuity is clear for piecewise-linear functions.
For $m \geq n$, $f_n$ and $f_m$ differ only on $[\frac12 - \frac1n, \frac12]$, where both take values in $[0,1]$; hence $\norm{f_n - f_m}_1 \leq m([\frac12 - \frac1n, \frac12]) = \frac1n \to 0$.
<2>2. The pointwise limit of $f_n$ is $\chi_{[\frac12, 1]}$, and $f_n \to \chi_{[\frac12,1]}$ in $L^1$; but $\chi_{[\frac12,1]}$ is not continuous.
Proof: $f_n(\frac12) = 1$ for all $n$; for $x < \frac12$, $f_n(x) = 0$ for all large $n$; for $x > \frac12$, $f_n(x) = 1$.
And $\norm{f_n - \chi_{[\frac12,1]}}_1 \leq \frac1n \to 0$.
<2>3. No continuous $f$ can be the $L^1$-limit of $\{f_n\}$.
Proof: if $\norm{f_n - f}_1 \to 0$ with $f$ continuous, the triangle inequality gives $\norm{f - \chi_{[\frac12,1]}}_1 = 0$, so $f = \chi_{[\frac12,1]}$ a.e. A continuous function equal a.e. to $\chi_{[\frac12,1]}$ would have to be $0$ on $[0, \frac12)$ and $1$ on $(\frac12, 1]$, contradicting continuity at $\frac12$.
<2>4. Q.E.D. Proof: <2>1 and <2>3 exhibit a Cauchy sequence with no limit in $C([0,1])$, so the space is not complete under $\norm{\cdot}_1$.
:::
