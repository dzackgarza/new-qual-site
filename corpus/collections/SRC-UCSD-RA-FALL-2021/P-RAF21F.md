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
**Theorem.**  
Let
$$\mu=\sum_{j\ge1} c_j\delta_{x_j},\qquad c_j>0.$$
Then $\mu$ is Radon iff every convergent subsequence $\{x_{j_k}\}$ satisfies
$$
\sum_{k=1}^\infty c_{j_k}<\infty.
$$

*Proof.* We prove both directions.

1. Assume $\mu$ is Radon and let $\{x_{j_k}\}$ be any convergent subsequence.
   1.1 Put
   $$
   K:=\{x\}\cup\{x_{j_k}:k\ge1\}.
   $$
   Then $K$ is compact.
   1.2 Radon means locally finite, so $\mu(K)<\infty$.
   1.3 Distinct atoms are disjoint, hence
   $$
   \sum_{k=1}^\infty c_{j_k}\le\mu(K)<\infty.
   $$
   So the subseries is finite.

2. Assume every convergent subsequence has finite mass.
   2.1 Suppose by contradiction that some compact $C\subseteq\mathbb R^n$ has $\mu(C)=\infty$.
   2.2 Fix any $x\in C$. If some $r>0$ satisfied
   $\mu(C\cap B(x,r))<\infty$ for all smaller $r$, then compactness of $C$
   would imply $\mu(C)<\infty$ by a finite cover; this contradicts 2.1.
   2.3 Therefore there are radii $r_m\downarrow0$ with
   $$
   \mu(C\cap B(x,r_m))=\infty.
   $$
   2.4 For each $m$ choose a finite block
   $$
   I_m\subseteq\{j:x_j\in C\cap B(x,r_m)\},\qquad \max I_{m-1}<\min I_m,
   $$
   such that
   $$
   \sum_{j\in I_m}c_j>1.
   $$
   2.5 Concatenate $I_1,I_2,\dots$ to get a convergent subsequence
   $\{x_{j_k}\}$ with limit $x$.
   Then
   $$
   \sum_{k=1}^\infty c_{j_k}
   =\sum_{m=1}^\infty\sum_{j\in I_m}c_j=\infty,
   $$
   contradicting the hypothesis.
   So every compact set has finite measure.

3. Assume every compact set has finite $\mu$-mass.
   3.1 For an atomic Borel measure on $\mathbb R^n$, this is equivalent to local finiteness.
   3.2 Local finiteness is the definition of being Radon on $\mathbb R^n$.

From 1, 2, 3, the equivalence is proved.
∎
:::
