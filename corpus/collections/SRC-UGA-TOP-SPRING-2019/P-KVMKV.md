---
schema: qual/card@1
id: P-KVMKV
kind: problem
title: Complete bounded metric spaces need not be compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Completeness
  - Counterexamples
relations: []
review: draft
---

::: problem
Is every complete bounded metric space compact? If so, give a proof; if not, give a counterexample.
:::

::: solution
**Goal:** Disprove the claim by exhibiting an infinite discrete metric space and proving it is complete and bounded but not compact.

<1>1. Counterexample definition:
    *Proof:*
    Let $X = \mathbb{N} = \{1, 2, 3, \dots\}$ equipped with the discrete metric:
    $$d(x, y) = \begin{cases} 0 & \text{if } x = y, \\ 1 & \text{if } x \ne y. \end{cases}$$

<1>2. $(X, d)$ is bounded:
    *Proof:*
    <2>1. For all $x, y \in X$, $d(x, y) \le 1$.
    <2>2. Thus $\operatorname{diam}(X) = \sup_{x, y \in X} d(x, y) = 1 < \infty$.
    <2>3. Therefore $(X, d)$ is bounded.

<1>3. $(X, d)$ is complete:
    *Proof:*
    <2>1. Let $(x_n)_{n=1}^\infty$ be a Cauchy sequence in $(X, d)$.
    <2>2. Choose $\varepsilon = \frac{1}{2} > 0$.
    <2>3. By the definition of a Cauchy sequence, there exists an integer $N \in \mathbb{N}$ such that
    $$d(x_n, x_m) < \frac{1}{2} \quad \text{for all } n, m \ge N.$$
    <2>4. Since the discrete metric only takes values in $\{0, 1\}$, $d(x_n, x_m) < \frac{1}{2}$ implies $d(x_n, x_m) = 0$.
    <2>5. Thus $x_n = x_m = x_N$ for all $n \ge N$, so the sequence $(x_n)$ is eventually constant.
    <2>6. Every eventually constant sequence converges: $\lim_{n \to \infty} x_n = x_N \in X$.
    <2>7. Therefore $(X, d)$ is complete.

<1>4. $(X, d)$ is not compact:
    *Proof:*
    <2>1. For each $n \in X$, the open ball of radius $1/2$ centered at $n$ is the singleton:
    $$B_{1/2}(n) = \{x \in X \mid d(x, n) < 1/2\} = \{n\}.$$
    <2>2. Thus each singleton $\{n\}$ is an open set in $(X, d)$.
    <2>3. Consider the open cover of $X$ given by all singletons:
    $$\mathcal{U} = \{\{n\} \mid n \in \mathbb{N}\}.$$
    <2>4. The union satisfies $\bigcup_{n \in \mathbb{N}} \{n\} = \mathbb{N} = X$, so $\mathcal{U}$ is an open cover.
    <2>5. Since all elements of $\mathcal{U}$ are pairwise disjoint singletons and $X = \mathbb{N}$ is infinite, any finite subcollection $\mathcal{U}' = \{\{n_1\}, \dots, \{n_k\}\}$ covers only the finite set $\{n_1, \dots, n_k\} \subsetneq \mathbb{N}$.
    <2>6. Thus $\mathcal{U}$ admits no finite subcover.
    <2>7. Therefore $(X, d)$ is not compact.

<1>5. Conclusion:
    *Proof:*
    No, a complete bounded metric space need not be compact (compactness in metric spaces is equivalent to completeness plus *total* boundedness).
:::
