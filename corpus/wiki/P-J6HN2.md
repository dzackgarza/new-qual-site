---
schema: qual/card@1
id: P-J6HN2
kind: problem
title: Fatou's lemma and summing series in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - fatou
  - convergence-of-integrals
  - l1
relations: []
review: draft
solved: true
---

::: problem
- Prove Fatou's lemma using the Monotone Convergence Theorem.

- Show that if $\theset{f_n}$ is in $L^1$ and $\sum \int \abs{f_n} < \infty$ then $\sum f_n$ converges to an $L^1$ function and $$\int \sum f_n = \sum \int f_n.$$
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (Fatou via MCT) For measurable $f_n \ge 0$: $\int \liminf_n f_n \le \liminf_n \int f_n$.
<2>1. Define $g_k = \inf_{n \ge k} f_n$; then $g_k \uparrow \liminf_n f_n$ pointwise.
Proof: $g_k$ is measurable (infimum of a countable family), nondecreasing in $k$, and $\sup_k g_k = \liminf_n f_n$ by definition.
<2>2. $\int g_k \le \int f_n$ for every $n \ge k$, so $\int g_k \le \inf_{n \ge k}\int f_n$.
Proof: $g_k \le f_n$ pointwise for $n \ge k$, and the integral is monotone.
<2>3. Q.E.D. Proof: monotone convergence: $\int \liminf_n f_n = \lim_k \int g_k \le \lim_k \inf_{n \ge k}\int f_n = \liminf_n \int f_n$.

<1>2. (Sum of $L^1$ functions) If $f_n \in L^1$ and $\sum \int |f_n| < \infty$, then $\sum_n f_n$ converges a.e. to an $L^1$ function and $\int \sum_n f_n = \sum_n \int f_n$.
<2>1. Let $g = \sum_n |f_n|$ (extended-valued); by MCT, $\int g = \sum_n \int |f_n| < \infty$.
Proof: monotone convergence applied to the partial sums of $|f_n|$.
<2>2. $g(x) < \infty$ for a.e. $x$, so $\sum_n f_n(x)$ converges absolutely (hence converges) for a.e. $x$.
Proof: $g \in L^1$ forces $g < \infty$ a.e.; absolute convergence implies convergence.
<2>3. $\sum_{n=1}^N f_n \to \sum_{n=1}^\infty f_n$ in $L^1$.
Proof: $\int \left|\sum_{n>N} f_n\right| \le \int g_N := \int\sum_{n>N}|f_n| = \sum_{n>N}\int|f_n| \to 0$ (tail of a convergent series), by MCT for the tail.
<2>4. $\int \sum_{n=1}^\infty f_n = \sum_{n=1}^\infty \int f_n$.
Proof: $\left|\int\sum_{n=1}^N f_n - \int\sum_{n=1}^\infty f_n\right| \le \int\left|\sum_{n>N} f_n\right| \to 0$ by <2>3, and $\int\sum_{n=1}^N f_n = \sum_{n=1}^N \int f_n$ (finite additivity), whose limit is the infinite sum.

<1>3. Q.E.D. Proof: <1>1 and <1>2 establish both claims.
:::
