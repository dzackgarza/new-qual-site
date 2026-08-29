---
schema: qual/card@1
id: P-CWJBS
kind: problem
title: A compact metric space is complete and separable, and sequences with summable
  consecutive distances converge
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Assume $(X,d)$ is a compact metric space.

Prove that $X$ is both complete and separable.

Suppose $\{x_k\}_{k=1}^\infty \subseteq X$ is a sequence such that the series $\sum_{k=1}^\infty d(x_k, x_{k+1})$ converges.
Prove that the sequence $\{x_k\}_{k=1}^\infty$ converges in $X$.
:::
::: {.solution}
**Part 1a: completeness.**

<1>1. Every sequence in $X$ has a convergent subsequence.
Proof: compact metric spaces are sequentially compact.

<1>2. Every Cauchy sequence $(x_n)$ in $X$ converges.
<2>1. $(x_n)$ has a convergent subsequence $x_{n_k} \to x$.
Proof: <1>1. <2>2. $x_n \to x$.
Proof: for $\eps > 0$, choose $N$ with $d(x_n, x_m) < \eps/2$ for $n, m \ge N$ (Cauchy), and $k$ with $n_k \ge N$ and $d(x_{n_k}, x) < \eps/2$; then $d(x_n, x) \le d(x_n, x_{n_k}) + d(x_{n_k}, x) < \eps$ for $n \ge N$.

<1>3. Q.E.D.: $X$ is complete.
Proof: <1>2 is the definition.

**Part 1b: separability.**

<1>4. For each $m \in \NN$, $X$ has a finite $1/m$-net: finitely many points $x^{(m)}_1, \ldots, x^{(m)}_{N_m}$ with $X = \bigcup_j B(x^{(m)}_j, 1/m)$.
Proof: $\{B(x, 1/m)\}_{x \in X}$ is an open cover of the compact space $X$, so it has a finite subcover; take the centers.

<1>5. $D = \bigcup_{m \in \NN}\{x^{(m)}_1, \ldots, x^{(m)}_{N_m}\}$ is countable and dense.
Proof: $D$ is a countable union of finite sets, hence countable; given $x \in X$ and $\eps > 0$, choose $m > 1/\eps$ and $j$ with $x \in B(x^{(m)}_j, 1/m)$; then $d(x, x^{(m)}_j) < 1/m < \eps$.

**Part 2.**

<1>6. $(x_k)$ is Cauchy: for $n < m$, $d(x_n, x_m) \le \sum_{k=n}^{m-1} d(x_k, x_{k+1})$.
Proof: iterated triangle inequality.

<1>7. $d(x_n, x_m) \to 0$ as $n \to \infty$ uniformly in $m > n$.
Proof: <1>6 bounds $d(x_n, x_m)$ by the tail $\sum_{k \ge n} d(x_k, x_{k+1})$ of a convergent series, which tends to $0$.

<1>8. Q.E.D.: $(x_k)$ converges in $X$.
Proof: <1>6 and <1>7 show $(x_k)$ is Cauchy; completeness (<1>3) gives convergence.
:::
