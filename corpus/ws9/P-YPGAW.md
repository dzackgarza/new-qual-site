---
schema: qual/card@1
id: P-YPGAW
kind: problem
title: $L^1$ convergence implies subsequence a.e. convergence, but not uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-functions
  - l1
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
For each natural number $n$, let $f_n : [0,1] \to \mathbb{R}$ be a sequence of absolutely integrable functions, and let $f : [0,1] \to \mathbb{R}$ be another absolutely integrable function such that $$\int_0^1 |f_n(x)-f(x)|dx \to 0, \text{ as } n \to \infty.$$

a. Show that there exists a subsequence $f_{n_j}$ of $f_n$ which converges to $f$ pointwise almost everywhere.
b. Give a counterexample to show that the assertion fails if "pointwise almost everywhere" is replaced by "uniformly".
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Given $\int_0^1 |f_n - f| \to 0$: (a) show some subsequence converges to $f$ pointwise a.e.; (b) counterexample showing "uniformly" fails.

<1>1. (a) There is a subsequence $f_{n_j}$ with $f_{n_j}(x) \to f(x)$ for almost every $x$.
<2>1. Choose $n_j$ with $\|f_{n_j} - f\|_1 < 2^{-j}$.
Proof: $\|f_n - f\|_1 \to 0$.
<2>2. $\sum_j \|f_{n_j} - f\|_1 < \infty$.
Proof: <2>1: geometric series.
<2>3. $\sum_j |f_{n_j}(x) - f(x)| < \infty$ for almost every $x$.
Proof: by MCT, $\int \sum_j |f_{n_j} - f| = \sum_j \int |f_{n_j} - f| = \sum_j \|f_{n_j} - f\|_1 < \infty$, so the nonnegative integrand is finite a.e. <2>4. $f_{n_j}(x) \to f(x)$ a.e. Proof: <2>3: the terms of the convergent series tend to $0$, so $|f_{n_j}(x) - f(x)| \to 0$ for a.e. $x$.
<2>5. Q.E.D. Proof: <2>1–<2>4 prove (a).

<1>2. (b) Counterexample: $f \equiv 0$ and $f_n = \chi_{(0, 1/n)}$.
<2>1. $\|f_n - 0\|_1 = \int_0^1 \chi_{(0,1/n)} = 1/n \to 0$.
Proof: the interval $(0, 1/n)$ has length $1/n$.
<2>2. $f_n(x) \to 0$ pointwise for every $x \in [0,1]$.
Proof: for $x = 0$ and $x \ge 1$ the values are $0$; for $x \in (0,1)$, eventually $1/n < x$, so $f_n(x) = 0$.
<2>3. $f_n$ does not converge to $0$ uniformly.
Proof: $\sup_{[0,1]} f_n = 1$ for all $n$ (attained on $(0, 1/n)$), and $1 \not\to 0$.
<2>4. Q.E.D. Proof: <2>1–<2>3 give $\|f_n - f\|_1 \to 0$ without uniform convergence: the assertion fails when "pointwise almost everywhere" is replaced by "uniformly".
:::
