---
schema: qual/card@1
id: P-MMAQ-K6UP2R5BUV
kind: problem
title: "Give an example of a continuous $f\\in L^1(\\RR)$ such that $f(x) \\not\\to 0$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - l1
  - uniform-continuity
  - small-tails
relations: []
review: draft
solved: true
---

::: problem
1. Give an example of a continuous $f\in L^1(\RR)$ such that $f(x) \not\to 0$ as$\abs x \to \infty$.

2. Show that if $f$ is *uniformly* continuous, then
   $$
   \lim_{\abs{x} \to \infty} f(x) = 0.
   $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) Exhibit a continuous $L^1$ function that does not decay at infinity.
(2) Show that uniform continuity forces decay at infinity for an $L^1$ function.

<1>1. Construction of the example for (1). <2>1. For each integer $n \geq 2$, place a triangular "tent" of height $1$ and base $\frac{2}{n^2}$ centered at $x = n$: $g_n(x) \definedas \max(0, 1 - n^2 \abs{x - n})$.
Proof: $g_n$ is continuous, supported in $[n - \frac{1}{n^2},\, n + \frac{1}{n^2}]$, with $g_n(n) = 1$ and area $\frac{1}{n^2}$ (base $\times$ height $\div 2$). <2>2. Define $f \definedas \sum_{n=2}^\infty g_n$.
Proof: Only finitely many $g_n$ are nonzero at each $x$ (their supports are disjoint for $n$ large, since $\frac{1}{n^2} + \frac{1}{(n+1)^2} < 1$ for $n \geq 2$), so the sum is locally finite and $f$ is continuous.
<2>3. $f \in L^1(\RR)$, since $\int f = \sum_n \int g_n = \sum_n \frac{1}{n^2} < \infty$.
Proof: Monotone convergence for the nonnegative summands, and $\sum 1/n^2$ converges.
<2>4. $f(n) = 1$ for every $n$, so $f(x) \not\to 0$ as $\abs{x} \to \infty$.
Proof: Along the sequence $x = n \to \infty$, $f$ takes the constant value $1$.
<2>5. Q.E.D. Proof: By <2>3 and <2>4, $f$ is a continuous $L^1$ function without decay at infinity.

<1>2. Proof of (2): a uniformly continuous $L^1$ function decays at infinity.
<2>1. Suppose, toward a contradiction, that $f(x) \not\to 0$ as $\abs{x} \to \infty$.
Proof: Assume the negation of the conclusion.
<2>2. Then there exist $\eps > 0$ and points $x_k \to \infty$ with $\abs{f(x_k)} \geq \eps$.
Proof: Negating $\lim_{\abs{x}\to\infty} f(x) = 0$: some $\eps > 0$ is attained with $\abs{x}$ arbitrarily large.
<2>3. Uniform continuity gives $\delta > 0$ with $\abs{f(x) - f(x_k)} < \eps/2$ whenever $\abs{x - x_k} < \delta$.
Proof: Definition of uniform continuity applied with $\eps/2$.
<2>4. Hence $\abs{f(x)} \geq \eps/2$ on each interval $(x_k - \delta, x_k + \delta)$.
Proof: $\abs{f(x)} \geq \abs{f(x_k)} - \abs{f(x) - f(x_k)} \geq \eps - \eps/2$ by <2>2 and <2>3. <2>5. Pass to a subsequence with $\abs{x_k - x_j} > 2\delta$; the intervals $(x_k - \delta, x_k + \delta)$ are then pairwise disjoint.
Proof: $x_k \to \infty$, so a subsequence with consecutive gaps $> 2\delta$ exists.
<2>6. Then $\int_\RR \abs{f} \geq \sum_k \int_{x_k - \delta}^{x_k + \delta} \abs{f} \geq \sum_k 2\delta \cdot \frac{\eps}{2} = \infty$.
Proof: Disjointness (<2>5) gives additivity of the integral over the union, and <2>4 bounds each integral below by $2\delta \cdot \eps/2$.
<2>7. Contradiction: $f \in L^1$ forces $\int \abs{f} < \infty$.
Proof: <2>6 contradicts $f \in L^1$.
<2>8. Q.E.D. Proof: The supposition <2>1 is impossible, so $\lim_{\abs{x}\to\infty} f(x) = 0$.

<1>3. Conclusion: both claims hold.
Proof: (1) by <1>1; (2) by <1>2.
:::
