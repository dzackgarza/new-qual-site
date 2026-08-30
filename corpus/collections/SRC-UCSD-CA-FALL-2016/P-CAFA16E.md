---
schema: qual/card@1
id: P-CAFA16E
kind: problem
title: "Normal family of functions vanishing at a point has a convergent subsequence"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $U \subset \mathbb{C}$ be a connected open set and let $a \in U$.
Let $f_n: U \to \mathbb{D}$ be a sequence of analytic functions such that $f_n(a) = 0$ for all $n \geq 1$.
Prove that there exists an analytic function $f: U \to \mathbb{D}$ and a subsequence $\{f_{n_k}\}$ of $\{f_n\}$ which converges uniformly to $f$ on compact subsets of $U$.
:::

::: solution
**Goal:** Extract a uniformly convergent compactly convergent subsequence in $\mathbb{D}$.

<1>1. Bounded holomorphic family: *Proof:*\
Each $f_n$ maps $U$ to $\mathbb D$, so the family $\{f_n\}$ is locally bounded (bounded by $1$ on every compact set).

<1>2. Montel compactness: *Proof:*\
By Montel, bounded families of holomorphic functions on a domain are normal.
Therefore there is a subsequence $\{f_{n_k}\}$ converging uniformly on every compact $K\subset U$ to a holomorphic limit $f$.

<1>3. Preserve codomain condition: *Proof:*\
Uniform convergence on compact sets and the pointwise bound $|f_{n_k}(z)|\le1$ imply for each $z\in U$, $|f(z)|=\lim_k|f_{n_k}(z)|\le1$.
Hence $f:U\to\overline{\mathbb D}$.
In fact, maximum principle or Hurwitz prevents interior values with $|f|=1$ unless constant.
Because $f(a)=\lim_k f_{n_k}(a)=0$, nonconstant behavior is allowed and we get $|f(z)|<1$ for all $z\in U$.

<1>4. Finalization: *Proof:*\
Take the subsequence from <2>; it is the required one and converges compactly to the analytic function $f:U\to\mathbb D$.
:::
