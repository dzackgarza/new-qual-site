---
schema: qual/card@1
id: E-KNLQ0
kind: exercise
title: Uniform convergence as convergence in the uniform metric
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a set, and let $f_n: X \to \mathbb{R}$ be a sequence of functions.
Let $\bar{\rho}$ be the uniform metric on the space $\mathbb{R}^X$.
Show that the sequence $(f_n)$ converges uniformly to the function $f: X \to \mathbb{R}$ if and only if the sequence $(f_n)$ converges to $f$ as elements of the metric space $(\mathbb{R}^X, \bar{\rho})$.
:::

::: {.solution}
**Goal.** Show uniform convergence of $f_n \to f$ is equivalent to convergence in the uniform metric $\bar\rho$.

<1>1. The uniform metric is $\bar\rho(f, g) = \sup_{x \in X} \min(|f(x) - g(x)|, 1)$.
Proof: definition of the standard bounded (uniform) metric on $\RR^X$.

<1>2. ($\Rightarrow$) Uniform convergence implies convergence in $\bar\rho$.
<2>1. Uniform convergence: for every $\eps > 0$ there is $N$ with $\sup_x |f_n(x) - f(x)| < \eps$ for $n \ge N$.
Proof: definition of uniform convergence.
<2>2. For $\eps < 1$, this gives $\bar\rho(f_n, f) = \sup_x \min(|f_n(x) - f(x)|, 1) < \eps$ for $n \ge N$.
Proof: since $|f_n - f| < \eps < 1$, the min is $|f_n - f| < \eps$.
<2>3. Hence $f_n \to f$ in $\bar\rho$.
Proof: <1>2.2.

<1>3. ($\Leftarrow$) Convergence in $\bar\rho$ implies uniform convergence.
<2>1. $f_n \to f$ in $\bar\rho$: for every $\eps > 0$ there is $N$ with $\bar\rho(f_n, f) < \eps$ for $n \ge N$.
Proof: definition of metric convergence.
<2>2. For $\eps < 1$, $\bar\rho(f_n, f) < \eps$ means $\sup_x \min(|f_n(x) - f(x)|, 1) < \eps < 1$, so $\min(|f_n(x) - f(x)|, 1) = |f_n(x) - f(x)|$ for all $x$.
Proof: since the min is $< 1$, it equals $|f_n(x) - f(x)|$.
<2>3. Hence $\sup_x |f_n(x) - f(x)| < \eps$ for $n \ge N$, so $f_n \to f$ uniformly.
Proof: <1>3.2.

<1>4. Q.E.D.
Proof: <1>2 and <1>3 give both directions.
:::
:::
