---
schema: qual/card@1
id: E-KZPIX
kind: exercise
title: Countability axioms of the rationals in the box topology
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Give $\mathbb{R}^\omega$ the box topology.
Let $\mathbb{Q}^\infty$ denote the subspace consisting of sequences of rationals that end in an infinite string of 0's. Which of our four countability axioms does this space satisfy?
:::

::: {.solution}
<1>1. The space $\mathbb{Q}^\infty$ is countable.
<2>1. $\mathbb{Q}^\infty = \bigcup_{k=1}^\infty X_k$, where $X_k = \{(x_n) \in \mathbb{Q}^\omega : x_n = 0 \text{ for all } n > k\}$.
Proof: definition of sequences ending in infinite strings of zeros.
<2>2. For each $k$, $X_k \cong \mathbb{Q}^k$ is countable, being a finite product of countable sets.
Proof: countability of $\mathbb{Q}$ and finite cartesian products of countable sets.
<2>3. $\mathbb{Q}^\infty$ is a countable union of countable sets, hence countable.
Proof: <2>1 and <2>2.

<1>2. $\mathbb{Q}^\infty$ is separable.
Proof: $\mathbb{Q}^\infty$ is a countable subset of itself and is dense in itself, so $\mathbb{Q}^\infty$ has a countable dense subset.

<1>3. $\mathbb{Q}^\infty$ is Lindelöf.
<2>1. Let $\mathcal{U}$ be an open cover of $\mathbb{Q}^\infty$.
Proof: setup.
<2>2. For each point $x \in \mathbb{Q}^\infty$, choose an open set $U_x \in \mathcal{U}$ containing $x$.
Proof: $\mathcal{U}$ covers $\mathbb{Q}^\infty$.
<2>3. The subcollection $\{U_x : x \in \mathbb{Q}^\infty\}$ covers $\mathbb{Q}^\infty$ and is countable since $\mathbb{Q}^\infty$ is countable by <1>1. Proof: image of a countable set under a choice function.
<2>4. Hence every open cover has a countable subcover.
Proof: <2>3.

<1>4. $\mathbb{Q}^\infty$ is not first-countable (and hence not second-countable).
<2>1. A basic open neighborhood of $\mathbf{0} = (0, 0, \dots)$ in the subspace box topology has the form $V = \left(\prod_{n=1}^\infty (-\varepsilon_n, \varepsilon_n)\right) \cap \mathbb{Q}^\infty$ for positive reals $\varepsilon_n > 0$.
Proof: definition of the box topology and subspace topology.
<2>2. Suppose $\{B_k\}_{k=1}^\infty$ is a countable neighborhood basis at $\mathbf{0}$.
Proof: hypothesis for contradiction.
<2>3. For each $k \ge 1$, choose a basic neighborhood $V_k = \left(\prod_{n=1}^\infty (-\varepsilon_{k,n}, \varepsilon_{k,n})\right) \cap \mathbb{Q}^\infty \subseteq B_k$ with $\varepsilon_{k,n} > 0$.
Proof: $\{B_k\}$ are neighborhoods of $\mathbf{0}$.
<2>4. Define $\delta_n = \frac{1}{2} \varepsilon_{n,n} > 0$ for each $n \ge 1$, and let $W = \left(\prod_{n=1}^\infty (-\delta_n, \delta_n)\right) \cap \mathbb{Q}^\infty$.
Proof: $W$ is an open neighborhood of $\mathbf{0}$ in $\mathbb{Q}^\infty$.
<2>5. For each $k \ge 1$, choose $q_k \in \mathbb{Q}$ such that $\delta_k < |q_k| < \varepsilon_{k,k}$.
Proof: $\delta_k = \frac{1}{2}\varepsilon_{k,k} < \varepsilon_{k,k}$ and $\mathbb{Q}$ is dense in $\mathbb{R}$.
<2>6. The point $y^{(k)} = (0, \dots, 0, q_k, 0, \dots)$ (with $q_k$ in the $k$-th coordinate) lies in $\mathbb{Q}^\infty$ and satisfies $y^{(k)} \in V_k \subseteq B_k$.
Proof: $|y^{(k)}_n| = 0 < \varepsilon_{k,n}$ for $n \neq k$ and $|y^{(k)}_k| = |q_k| < \varepsilon_{k,k}$.
<2>7. But $|y^{(k)}_k| = |q_k| > \delta_k$, so $y^{(k)} \notin W$.
Proof: definition of $W$.
<2>8. Thus $B_k \not\subseteq W$ for all $k \ge 1$, contradicting that $\{B_k\}$ is a neighborhood basis at $\mathbf{0}$.
Proof: <2>6 and <2>7. <2>9. Hence $\mathbb{Q}^\infty$ is not first-countable, and therefore not second-countable.
Proof: <2>8 and second-countability implies first-countability.

<1>5. Conclusion: $\mathbb{Q}^\infty$ satisfies the Lindelöf and separability axioms, but does not satisfy the first-countability or second-countability axioms.
Q.E.D. Proof: <1>2, <1>3, <1>4.
:::
