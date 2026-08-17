---
schema: qual/card@1
id: P-RA16M3
kind: problem
title: 'UGA analysis qualifying exam, May 2016, problem 3'
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - completeness
  - metric-spaces
relations: []
review: draft
---

:::{.problem title="?"}
Assume $(X,d)$ is a compact metric space.

(a) Prove that $X$ is both complete and separable.

(b) Suppose $\{x_k\}_{k=1}^{\infty}\subseteq X$ is a sequence such that the series
$\sum_{k=1}^{\infty}d(x_k,x_{k+1})$ is convergent. Prove that the sequence $\{x_k\}_{k=1}^{\infty}$ converges in $X$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** (a) Prove compact metric $(X,d)$ is complete and separable; (b) if $\sum_k d(x_k, x_{k+1}) < \infty$ then $\{x_k\}$ converges in $X$.

<1>1. (a) $X$ is complete.
    <2>1. Let $\{x_n\}$ be a Cauchy sequence in $X$.
    <2>2. Some subsequence $\{x_{n_j}\}$ converges to some $x \in X$.
        Proof: compact metric spaces are sequentially compact.
    <2>3. $x_n \to x$.
        Proof: Cauchy + convergent subsequence: for $\varepsilon > 0$ choose $N$ with $d(x_n, x_m) < \varepsilon/2$ for $n, m \ge N$, and $j$ with $n_j \ge N$ and $d(x_{n_j}, x) < \varepsilon/2$; then $d(x_n, x) \le d(x_n, x_{n_j}) + d(x_{n_j}, x) < \varepsilon$ for $n \ge N$.
    <2>4. Q.E.D.
        Proof: <2>1–<2>3 show every Cauchy sequence converges: completeness.

<1>2. (a) $X$ is separable.
    <2>1. For each $n \in \mathbb N$, the balls $B(x, 1/n)$, $x \in X$, cover $X$; choose a finite subcover with centers $x_{n,1}, \ldots, x_{n,m_n}$.
        Proof: compactness.
    <2>2. $D := \{x_{n,j} : n \in \mathbb N, 1 \le j \le m_n\}$ is countable and dense.
        Proof: countable union of finite sets; dense because every $x \in X$ lies in some $B(x_{n,j}, 1/n)$ for each $n$, so $d(x, x_{n,j}) < 1/n$.
    <2>3. Q.E.D.
        Proof: <2>2 gives a countable dense subset.

<1>3. (b) $\sum_k d(x_k, x_{k+1}) < \infty$ implies $\{x_k\}$ converges.
    <2>1. $\{x_k\}$ is Cauchy.
        Proof: for $m > n$, $d(x_n, x_m) \le \sum_{j=n}^{m-1} d(x_j, x_{j+1}) \le \sum_{j=n}^{\infty} d(x_j, x_{j+1})$, the tail of a convergent series, which $\to 0$ as $n \to \infty$.
    <2>2. $\{x_k\}$ converges.
        Proof: $X$ is complete by <1>1, and Cauchy sequences in complete spaces converge.

<1>4. Q.E.D.
    Proof: <1>1–<1>2 prove (a); <1>3 proves (b).

:::
