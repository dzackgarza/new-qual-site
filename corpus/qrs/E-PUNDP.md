---
schema: qual/card@1
id: E-PUNDP
kind: exercise
title: "- Is it true that the converse to the DCT holds?"
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - counterexamples
relations: []
review: draft
solved: true
---

::: exercise
- Is it true that the converse to the DCT holds?
  I.e. if $\int f_n \to \int f$, is there a $g\in L^p$ such that $f_n < g$ a.e. for every $n$?
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. No: $\int f_n \to \int f$ does not imply the existence of an integrable dominating function for the $f_n$.
<2>1. Take $f \equiv 0$ and $f_n = n\chi_{[1/(n+1), 1/n)}$ for $n \ge 1$.
Proof: these are non-negative measurable functions with $f_n \to 0$ pointwise (indeed $f_n(x) \ne 0$ only for $x \in [1/(n+1), 1/n)$, which shrinks to $\{0\}$). <2>2. $\int f_n = n\left(\frac{1}{n} - \frac{1}{n+1}\right) = \frac{1}{n+1} \to 0 = \int f$.
Proof: direct computation of the integral of a step function.
<2>3. $\int \sup_n f_n = \infty$.
Proof: the intervals $[1/(n+1), 1/n)$ are pairwise disjoint and $f_n$ is supported on its own interval, so $\sup_n f_n = n$ on $[1/(n+1), 1/n)$; hence $\int \sup_n f_n = \sum_{n=1}^\infty n \cdot \frac{1}{n(n+1)} = \sum_{n=1}^\infty \frac{1}{n+1} = \infty$.
<2>4. No $g \in L^p$ ($p \ge 1$) can dominate all the $f_n$.
Proof: a dominating $g$ satisfies $g \ge \sup_n f_n$ a.e.; then $\int g^p \ge \int (\sup_n f_n)^p = \sum_n n^p \cdot \frac{1}{n(n+1)} \ge \sum_n \frac{n^{p-1}}{2n} = \frac{1}{2}\sum_n n^{p-2} = \infty$ for $p \ge 1$ (for $p = 1$ this is $\sum 1/(n+1) = \infty$), so $g \notin L^p$.
<2>5. Q.E.D. Proof: <2>2 satisfies the hypothesis of the converse, while <2>4 shows no dominating function exists; the converse to the dominated convergence theorem fails.
:::
