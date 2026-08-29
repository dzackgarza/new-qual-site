---
schema: qual/card@1
id: P-RAF21F
kind: problem
title: "When is an atomic measure Radon? Summability over convergent subsequences"
classification:
  areas:
  - real-analysis
  topics:
  - Radon Measures
  - Dirac Measures
  - Borel Measures
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $\delta_x$ denote the Dirac delta mass at $x \in \mathbb{R}^n$.
Let $\{x_j\}_{j=1}^\infty$ be a sequence in $\mathbb{R}^n$, $\{c_j\}_{j=1}^\infty$ a sequence of positive numbers, and $\mu$ the Borel measure on $\mathbb{R}^n$ corresponding to the series $\sum_{j=1}^\infty c_j \delta_{x_j}$.
Prove that $\mu$ is Radon if and only if for all convergent subsequences $\{x_{j_k}\}_{k=1}^\infty$ it holds that $\sum_{k=1}^\infty c_{j_k} < \infty$.
:::

::: solution
Write the measure as
\[
\mu=\sum_{j\ge1} c_j\delta_{x_j}.
\]

($\Rightarrow$) If $\mu$ is Radon, it is locally finite.  
Let $\{x_{j_k}\}$ converge to $x$. Then
\[
K:=\{x\}\cup\{x_{j_k}:k\ge1\}
\]
is compact in $\mathbb R^n$, so $\mu(K)<\infty$.
Because atoms at distinct points are disjoint,
\[
\sum_{k=1}^\infty c_{j_k}\le \mu(K)<\infty.
\]

($\Leftarrow$) Assume every convergent subsequence has finite weight.
To show $\mu$ is Radon on $\mathbb R^n$, it is enough to show $\mu(K)<\infty$ for every compact $K$.

Suppose some compact $K$ has $\mu(K)=\infty$.
Since $K$ is infinite as a support set for the atoms, choose a convergent sequence
$x_{j_k}\in K$ with limit $x\in K$ such that
\[
\sum_{k=1}^\infty c_{j_k}=\infty.
\]
This is possible by picking, for each $m$, a finite set of points in
$K\cap B(x,1/m)$ with total mass $>1$ and ordering these finite blocks for
decreasing radii; concatenating them gives a sequence converging to $x$ with
divergent total mass.
This contradicts the hypothesis.

Hence $\mu(K)<\infty$ for all compact $K$, so the atomic measure is locally finite.
For atomic Borel measures on $\mathbb R^n$, local finiteness gives inner and outer
regularity on Borel sets, so $\mu$ is Radon.
:::
