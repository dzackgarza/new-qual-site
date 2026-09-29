---
schema: qual/card@1
id: E-KZPIX
kind: problem
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
::: pf

::: {.pf-step #s1}
The space $\mathbb{Q}^\infty$ is countable.

::: pf-proof

::: {.pf-step #s1-1}
$\mathbb{Q}^\infty = \bigcup_{k=1}^\infty X_k$, where $X_k = \{(x_n) \in \mathbb{Q}^\omega : x_n = 0 \text{ for all } n > k\}$.

::: pf-proof
definition of sequences ending in infinite strings of zeros.
:::

:::

::: {.pf-step #s1-2}
For each $k$, $X_k \cong \mathbb{Q}^k$ is countable, being a finite product of countable sets.

::: pf-proof
countability of $\mathbb{Q}$ and finite cartesian products of countable sets.
:::

:::

::: pf-step
$\mathbb{Q}^\infty$ is a countable union of countable sets, hence countable.

::: pf-proof
steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s2}
$\mathbb{Q}^\infty$ is separable.

::: pf-proof
$\mathbb{Q}^\infty$ is a countable subset of itself and is dense in itself, so $\mathbb{Q}^\infty$ has a countable dense subset.
:::

:::

::: {.pf-step #s3}
$\mathbb{Q}^\infty$ is Lindelöf.

::: pf-proof

::: pf-step
Let $\mathcal{U}$ be an open cover of $\mathbb{Q}^\infty$.

::: pf-proof
setup.
:::

:::

::: pf-step
For each point $x \in \mathbb{Q}^\infty$, choose an open set $U_x \in \mathcal{U}$ containing $x$.

::: pf-proof
$\mathcal{U}$ covers $\mathbb{Q}^\infty$.
:::

:::

::: {.pf-step #s3-3}
The subcollection $\{U_x : x \in \mathbb{Q}^\infty\}$ covers $\mathbb{Q}^\infty$ and is countable since $\mathbb{Q}^\infty$ is countable by step [](#s1){.pf-ref}.

::: pf-proof
image of a countable set under a choice function.
:::

:::

::: pf-step
Hence every open cover has a countable subcover.

::: pf-proof
step [](#s3-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s4}
$\mathbb{Q}^\infty$ is not first-countable (and hence not second-countable).

::: pf-proof

::: pf-step
A basic open neighborhood of $\mathbf{0} = (0, 0, \dots)$ in the subspace box topology has the form $V = \left(\prod_{n=1}^\infty (-\varepsilon_n, \varepsilon_n)\right) \cap \mathbb{Q}^\infty$ for positive reals $\varepsilon_n > 0$.

::: pf-proof
definition of the box topology and subspace topology.
:::

:::

::: pf-step
Suppose $\{B_k\}_{k=1}^\infty$ is a countable neighborhood basis at $\mathbf{0}$.

::: pf-proof
hypothesis for contradiction.
:::

:::

::: pf-step
For each $k \ge 1$, choose a basic neighborhood $V_k = \left(\prod_{n=1}^\infty (-\varepsilon_{k,n}, \varepsilon_{k,n})\right) \cap \mathbb{Q}^\infty \subseteq B_k$ with $\varepsilon_{k,n} > 0$.

::: pf-proof
$\{B_k\}$ are neighborhoods of $\mathbf{0}$.
:::

:::

::: pf-step
Define $\delta_n = \frac{1}{2} \varepsilon_{n,n} > 0$ for each $n \ge 1$, and let $W = \left(\prod_{n=1}^\infty (-\delta_n, \delta_n)\right) \cap \mathbb{Q}^\infty$.

::: pf-proof
$W$ is an open neighborhood of $\mathbf{0}$ in $\mathbb{Q}^\infty$.
:::

:::

::: pf-step
For each $k \ge 1$, choose $q_k \in \mathbb{Q}$ such that $\delta_k < |q_k| < \varepsilon_{k,k}$.

::: pf-proof
$\delta_k = \frac{1}{2}\varepsilon_{k,k} < \varepsilon_{k,k}$ and $\mathbb{Q}$ is dense in $\mathbb{R}$.
:::

:::

::: {.pf-step #s4-6}
The point $y^{(k)} = (0, \dots, 0, q_k, 0, \dots)$ (with $q_k$ in the $k$-th coordinate) lies in $\mathbb{Q}^\infty$ and satisfies $y^{(k)} \in V_k \subseteq B_k$.

::: pf-proof
$|y^{(k)}_n| = 0 < \varepsilon_{k,n}$ for $n \neq k$ and $|y^{(k)}_k| = |q_k| < \varepsilon_{k,k}$.
:::

:::

::: {.pf-step #s4-7}
But $|y^{(k)}_k| = |q_k| > \delta_k$, so $y^{(k)} \notin W$.

::: pf-proof
definition of $W$.
:::

:::

::: {.pf-step #s4-8}
Thus $B_k \not\subseteq W$ for all $k \ge 1$, contradicting that $\{B_k\}$ is a neighborhood basis at $\mathbf{0}$.

::: pf-proof
steps [](#s4-6){.pf-ref} and [](#s4-7){.pf-ref}.
:::

:::

::: pf-step
Hence $\mathbb{Q}^\infty$ is not first-countable, and therefore not second-countable.

::: pf-proof
step [](#s4-8){.pf-ref} and second-countability implies first-countability.
:::

:::

:::

:::

::: pf-step
Conclusion: $\mathbb{Q}^\infty$ satisfies the Lindelöf and separability axioms, but does not satisfy the first-countability or second-countability axioms.

::: pf-proof
steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}.
:::

:::

:::
