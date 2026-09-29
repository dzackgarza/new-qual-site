---
schema: qual/card@1
id: E-ARJT3
kind: problem
title: Separable space
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
- What is a **separable** space?
:::

::: {.solution}

::: pf

::: pf-step
Definition of a separable space:

::: pf-proof

::: pf-step
A topological space $(X, \mathcal{T})$ is called **separable** if there exists a subset $D \subseteq X$ such that:

1. $D$ is at most countable (i.e., $|D| \le \aleph_0$),
2. $D$ is dense in $X$, meaning that the topological closure of $D$ equals $X$:
\[
\overline{D} = X.
\]

:::

:::

:::

::: pf-step
Equivalent characterizations:

::: pf-proof

::: pf-step
A space $X$ is separable if and only if there exists a countable set $D \subseteq X$ that intersects every non-empty open set:
\[
\forall U \in \mathcal{T} \setminus \{\emptyset\}, \qquad U \cap D \neq \emptyset.
\]

:::

:::

:::

::: pf-step
Properties and examples:

::: pf-proof

::: pf-step
Every second-countable space is separable (choosing one point from each element of a countable basis).

:::

::: pf-step
For metric spaces, separability is equivalent to being second-countable and equivalent to being Lindelöf.

:::

::: pf-step
The Euclidean space $\mathbb{R}^n$ with the standard topology is separable, with countable dense subset $\mathbb{Q}^n$.

:::

:::

:::

::: pf-qed
Conclusion:
A separable space is a topological space containing a countable dense subset.
:::

:::

:::
