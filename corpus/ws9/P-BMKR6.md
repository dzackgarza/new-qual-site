---
schema: qual/card@1
id: P-BMKR6
kind: problem
title: A normed space is Banach iff every absolutely convergent series converges
classification:
  areas:
  - real-analysis
  topics:
  - completeness
  - norms
  - series-of-functions
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Prove that a normed vector space $(X, \|\cdot\|)$ is Banach if and only if every normally (sometimes called also absolutely) convergent series is convergent.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. ($\Rightarrow$) If $X$ is Banach and $\sum_n\|x_n\| < \infty$, then $\sum_n x_n$ converges.
Proof: let $s_N = \sum_{n\le N}x_n$ be the partial sums.
For $K > M$, \[ \|s_K - s_M\| = \Big\|\sum_{n=M+1}^{K}x_n\Big\| \le \sum_{n=M+1}^{K}\|x_n\| \le \sum_{n>M}\|x_n\| \to 0 \] as $M \to \infty$ (tail of a convergent series).
So $(s_N)$ is Cauchy in the complete space $X$, hence converges.
<1>2. ($\Leftarrow$) If every absolutely convergent series converges, then $X$ is complete.
Proof: let $(x_n)$ be a Cauchy sequence.
Pass to a subsequence with $\|x_{n_{k+1}} - x_{n_k}\| \le 2^{-k}$ (possible since $(x_n)$ is Cauchy).
The series $\sum_k (x_{n_{k+1}} - x_{n_k})$ is absolutely convergent, so by hypothesis it converges; hence its partial sums, which telescope to $x_{n_{m+1}} - x_{n_1}$, converge, so the subsequence $(x_{n_k})$ converges to some $x \in X$.
Since $(x_n)$ is Cauchy and has a convergent subsequence, the whole sequence converges to $x$.
<1>3. Q.E.D.
:::
