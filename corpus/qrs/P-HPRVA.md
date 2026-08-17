---
schema: qual/card@1
id: P-HPRVA
kind: problem
title: "Give an example of a continuous $f\\in L^1(\\RR)$ such that $f(x) \\not\\to 0$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - l1
  - counterexamples
  - limits
relations: []
review: draft
solved: true
---

::: problem
1. Give an example of a continuous $f\in L^1(\RR)$ such that $f(x) \not\to 0$ as$\abs x \to \infty$.

2. Show that if $f$ is *uniformly* continuous, then
\[
\lim_{\abs x \to \infty} f(x) = 0.
\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. A continuous $L^1$ function need not tend to $0$ at infinity.
<2>1. For each $n \ge 2$ let $T_n$ be the tent function of height $n$ and base $\left[n - \frac{1}{2n^3}, n + \frac{1}{2n^3}\right]$: $T_n(x) = n\left(1 - 2n^3|x - n|\right)$ on that interval and $0$ elsewhere.
Proof: $T_n$ is continuous, non-negative, $T_n(n) = n$, and supported in an interval of length $1/n^3$.
<2>2. $f = \sum_{n \ge 2} T_n$ is continuous and $f \in L^1(\RR)$.
Proof: the supports of the $T_n$ are pairwise disjoint, so $f$ is continuous (each point lies in at most one tent; away from the tents $f = 0$); and $\int f = \sum_n \frac{1}{2} n \cdot \frac{1}{n^3} = \frac{1}{2}\sum_{n\ge 2}\frac{1}{n^2} < \infty$.
<2>3. $f(x) \not\to 0$ as $|x| \to \infty$.
Proof: $f(n) = T_n(n) = n \to \infty$ along $x = n$.
<2>4. Q.E.D. Proof: <2>2 and <2>3.

<1>2. If $f \in L^1$ is uniformly continuous, then $\lim_{|x|\to\infty} f(x) = 0$.
<2>1. Suppose not: there is $\eps > 0$ and a sequence $|x_k| \to \infty$ with $|f(x_k)| \ge \eps$.
Proof: negation of the claim $\lim_{|x|\to\infty}f(x) = 0$.
<2>2. Uniform continuity gives $\delta > 0$ such that $|f(y) - f(x)| < \eps/2$ whenever $|y - x| < \delta$; hence $|f| \ge \eps/2$ on each interval $[x_k - \delta, x_k + \delta]$.
Proof: $|f(y)| \ge |f(x_k)| - |f(y) - f(x_k)| \ge \eps - \eps/2 = \eps/2$ by the reverse triangle inequality.
<2>3. For $k$ large the intervals $[x_k - \delta, x_k + \delta]$ are pairwise disjoint.
Proof: $|x_k| \to \infty$, so the intervals are eventually separated; discard finitely many.
<2>4. $\int_\RR |f| \ge \sum_k \frac{\eps}{2}\cdot 2\delta = \infty$, contradicting $f \in L^1$.
Proof: <2>2 and <2>3 give the lower bound on disjoint sets of measure $2\delta$.
<2>5. Q.E.D. Proof: <2>4 contradicts the hypothesis, so the supposition in <2>1 is false.
:::
