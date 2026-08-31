---
schema: qual/card@1
id: E-ARJT3
kind: exercise
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

::: exercise
- What is a **separable** space?
:::

::: {.solution}
<1>1. Definition of a separable space:
<2>1. A topological space $(X, \mathcal{T})$ is called **separable** if there exists a subset $D \subseteq X$ such that:
1. $D$ is at most countable (i.e., $|D| \le \aleph_0$),
2. $D$ is dense in $X$, meaning that the topological closure of $D$ equals $X$:
\[
\overline{D} = X.
\]

<1>2. Equivalent characterizations:
<2>1. A space $X$ is separable if and only if there exists a countable set $D \subseteq X$ that intersects every non-empty open set:
\[
\forall U \in \mathcal{T} \setminus \{\emptyset\}, \qquad U \cap D \neq \emptyset.
\]

<1>3. Essential properties and examples:
<2>1. Every second-countable space is separable (choosing one point from each element of a countable basis).
<2>2. For metric spaces, separability is equivalent to being second-countable and equivalent to being Lindelöf.
<2>3. The Euclidean space $\mathbb{R}^n$ with the standard topology is separable, with countable dense subset $\mathbb{Q}^n$.

<1>4. Conclusion:
A separable space is a topological space containing a countable dense subset. Q.E.D.
:::
