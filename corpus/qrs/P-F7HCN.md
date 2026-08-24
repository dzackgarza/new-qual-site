---
schema: qual/card@1
id: P-F7HCN
kind: problem
title: Convergence of $\sum nz^n$, $\sum z^n/n^2$, and $\sum z^n/n$ on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
---

::: problem
Prove the following:

a. $\sum_{n} nz^n$ does not converge at any point of $S^1$

b. $\sum_n {z^n \over n^2}$ converges at every point of $S^1$.

c. $\sum_n {z^n \over n}$ converges at every point of $S^1$ except $z=1$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove: (a) $\sum_{n} nz^n$ does not converge at any point of $S^1$; (b) $\sum_n z^n/n^2$ converges at every point of $S^1$; (c) $\sum_n z^n/n$ converges at every point of $S^1$ except $z = 1$.

<1>1. Part (a): for $\abs z = 1$, the terms do not tend to $0$.
Proof: $\abs{n z^n} = n \cdot \abs z^n = n \to \infty$ as $n \to \infty$; a necessary condition for convergence of a series is that its terms tend to $0$.

<1>2. Part (b): $\sum_n \frac{z^n}{n^2}$ converges absolutely at every point of $S^1$.
<2>1. $\abs{\frac{z^n}{n^2}} = \frac{1}{n^2}$ for $\abs z = 1$.
Proof: $\abs{z^n} = 1$.
<2>2. $\sum_n \frac{1}{n^2}$ converges.
Proof: $p$-series with $p = 2 > 1$.
<2>3. Hence the series converges absolutely, in particular converges, at every $z \in S^1$.
Proof: Absolute convergence (comparison test, <2>1--<2>2) implies convergence.

<1>3. Part (c) at $z = 1$: $\sum_n \frac{1}{n}$ diverges.
Proof: Harmonic series.

<1>4. Part (c) at $z \in S^1 \setminus \theset{1}$: $\sum_n \frac{z^n}{n}$ converges.
<2>1. The partial sums $A_N := \sum_{n=1}^{N} z^n$ are bounded.
Proof: Geometric series: $A_N = \frac{z - z^{N+1}}{1 - z}$, so $\abs{A_N} \leq \frac{2}{\abs{1 - z}}$, a constant independent of $N$, since $z \neq 1$.
<2>2. The sequence $\frac{1}{n}$ decreases to $0$.
Proof: Monotone and bounded below by $0$.
<2>3. Dirichlet's test applies: $\sum \frac{z^n}{n}$ converges.
Proof: Dirichlet's test: a series $\sum a_n b_n$ converges if the partial sums of $\sum a_n$ are bounded and $b_n \downarrow 0$; take $a_n = z^n$, $b_n = 1/n$, using <2>1 and <2>2.

<1>5. Q.E.D. Proof: <1>1 proves (a); <1>2 proves (b); <1>3 and <1>4 prove (c).
:::
