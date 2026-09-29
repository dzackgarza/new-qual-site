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
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 1 of the official UGA Spring 2019 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified that the infinite discrete metric space is bounded and complete while its singleton open cover has no finite subcover.
---

::: {.problem}
Is every complete bounded metric space compact? If so, give a proof; if not, give a counterexample.
:::

::: {.solution}
**Goal:** Disprove the claim by exhibiting an infinite discrete metric space and proving it is complete and bounded but not compact.

::: pf

::: pf-step

Counterexample definition:

::: pf-proof

Let $X = \mathbb{N} = \{1, 2, 3, \dots\}$ equipped with the discrete metric:
$$d(x, y) = \begin{cases} 0 & \text{if } x = y, \\ 1 & \text{if } x \ne y. \end{cases}$$

:::

:::

::: pf-step

$(X, d)$ is bounded:

::: pf-proof

::: pf-step

For all $x, y \in X$, $d(x, y) \le 1$.

:::

::: pf-step

Thus $\operatorname{diam}(X) = \sup_{x, y \in X} d(x, y) = 1 < \infty$.

:::

::: pf-step

Therefore $(X, d)$ is bounded.

:::

:::

:::

::: pf-step

$(X, d)$ is complete:

::: pf-proof

::: pf-step

Let $(x_n)_{n=1}^\infty$ be a Cauchy sequence in $(X, d)$.

:::

::: pf-step

Choose $\varepsilon = \frac{1}{2} > 0$.

:::

::: pf-step

By the definition of a Cauchy sequence, there exists an integer $N \in \mathbb{N}$ such that
    $$d(x_n, x_m) < \frac{1}{2} \quad \text{for all } n, m \ge N.$$

:::

::: pf-step

Since the discrete metric only takes values in $\{0, 1\}$, $d(x_n, x_m) < \frac{1}{2}$ implies $d(x_n, x_m) = 0$.

:::

::: pf-step

Thus $x_n = x_m = x_N$ for all $n \ge N$, so the sequence $(x_n)$ is eventually constant.

:::

::: pf-step

Every eventually constant sequence converges: $\lim_{n \to \infty} x_n = x_N \in X$.

:::

::: pf-step

Therefore $(X, d)$ is complete.

:::

:::

:::

::: pf-step

$(X, d)$ is not compact:

::: pf-proof

::: pf-step

For each $n \in X$, the open ball of radius $1/2$ centered at $n$ is the singleton:
    $$B_{1/2}(n) = \{x \in X \mid d(x, n) < 1/2\} = \{n\}.$$

:::

::: pf-step

Thus each singleton $\{n\}$ is an open set in $(X, d)$.

:::

::: pf-step

Consider the open cover of $X$ given by all singletons:
    $$\mathcal{U} = \{\{n\} \mid n \in \mathbb{N}\}.$$

:::

::: pf-step

The union satisfies $\bigcup_{n \in \mathbb{N}} \{n\} = \mathbb{N} = X$, so $\mathcal{U}$ is an open cover.

:::

::: pf-step

Since all elements of $\mathcal{U}$ are pairwise disjoint singletons and $X = \mathbb{N}$ is infinite, any finite subcollection $\mathcal{U}' = \{\{n_1\}, \dots, \{n_k\}\}$ covers only the finite set $\{n_1, \dots, n_k\} \subsetneq \mathbb{N}$.

:::

::: pf-step

Thus $\mathcal{U}$ admits no finite subcover.

:::

::: pf-step

Therefore $(X, d)$ is not compact.

:::

:::

:::

::: pf-step

Conclusion:

::: pf-proof

No, a complete bounded metric space need not be compact (compactness in metric spaces is equivalent to completeness plus *total* boundedness).

:::

:::

:::

:::
