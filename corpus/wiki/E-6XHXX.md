---
schema: qual/card@1
id: E-6XHXX
kind: exercise
title: $\mathbb{R}$ is separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that $\RR$ is separable.
:::

::: solution
**Goal:** Prove that the real line $\mathbb{R}$ is separable by showing that the rational numbers $\mathbb{Q} \subset \mathbb{R}$ form a countable dense subset.

<1>1. Definition of separability:
    A topological space $X$ is separable if it contains a countable subset $D \subseteq X$ whose closure is all of $X$ ($\overline{D} = X$).

<1>2. Countability of $\mathbb{Q}$:
    *Proof:*
    <2>1. The rational numbers $\mathbb{Q} = \{p/q \mid p \in \mathbb{Z}, q \in \mathbb{Z}_+\}$ are the image of the Cartesian product $\mathbb{Z} \times \mathbb{Z}_+$ under the map $(p, q) \mapsto p/q$.
    <2>2. As a product of two countable sets, $\mathbb{Z} \times \mathbb{Z}_+$ is countable.
    <2>3. The image of a countable set under a surjective map is countable, so $\mathbb{Q}$ is countable.

<1>3. Density of $\mathbb{Q}$ in $\mathbb{R}$:
    For every non-empty open set $U \subseteq \mathbb{R}$, $U \cap \mathbb{Q} \neq \varnothing$.
    *Proof:*
    <2>1. Since the collection of open intervals forms a basis for the Euclidean topology on $\mathbb{R}$, any non-empty open set $U$ contains a non-empty open interval $(a, b)$ with $a < b$.
    <2>2. Because $b - a > 0$, by the Archimedean property of $\mathbb{R}$, there exists an integer $q \in \mathbb{Z}_+$ such that $q > \frac{1}{b - a}$, which implies $q b - q a > 1$.
    <2>3. The interval $(q a, q b)$ has length greater than $1$, so there exists an integer $p \in \mathbb{Z}$ satisfying $q a < p < q b$ (for instance, $p = \lfloor q a \rfloor + 1$).
    <2>4. Dividing by $q > 0$ gives $a < \frac{p}{q} < b$.
    <2>5. Thus the rational number $r = \frac{p}{q} \in \mathbb{Q}$ belongs to $(a, b) \subseteq U$, so $U \cap \mathbb{Q} \neq \varnothing$.

<1>4. Conclusion:
    $\mathbb{Q}$ is a countable dense subset of $\mathbb{R}$, so $\mathbb{R}$ is separable. Q.E.D.
:::
