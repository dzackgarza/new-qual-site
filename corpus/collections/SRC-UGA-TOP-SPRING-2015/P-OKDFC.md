---
schema: qual/card@1
id: P-OKDFC
kind: problem
title: A countable base implies a countable dense subset, and the converse in metric
  spaces
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
a. Prove that a topological space that has a countable base for its topology also contains a countable dense subset.

b. Prove that the converse to (a) holds if the space is a metric space.
:::

::: {.solution}
<1>1. Part (a): Second countable implies separable:
<2>1. Let $\mathcal{B} = \{B_n\}_{n=1}^\infty$ be a countable basis for the topology of $X$.
For each non-empty basis element $B_n \in \mathcal{B}$, choose an element $x_n \in B_n$.
Define the set:
\[
D = \{x_n \mid B_n \in \mathcal{B}, \, B_n \neq \emptyset\}.
\]
As a subset of the indexed set of positive integers, $D$ is at most countable.
<2>2. To prove $D$ is dense in $X$, let $U \subseteq X$ be any non-empty open set.
Since $\mathcal{B}$ is a basis, there exists a non-empty basis element $B_k \in \mathcal{B}$ such that $B_k \subseteq U$.
<2>3. By construction, $x_k \in B_k \subseteq U$, so $x_k \in D \cap U \neq \emptyset$.
Thus $D$ intersects every non-empty open set of $X$, so $\overline{D} = X$.
Hence $X$ has a countable dense subset (is separable).

<1>2. Part (b): Separable metric space implies second countable:
<2>1. Let $(X, d)$ be a metric space containing a countable dense subset $D = \{d_n\}_{n=1}^\infty$.
Consider the collection of open balls with centers in $D$ and rational radii:
\[
\mathcal{B} = \{ B(d_n, r) \mid d_n \in D, \, r \in \mathbb{Q}_{>0} \}.
\]
As a product of two countable sets $D \times \mathbb{Q}_{>0}$, $\mathcal{B}$ is a countable collection of open subsets of $X$.
<2>2. Let $U \subseteq X$ be an open set and $x \in U$.
By definition of the metric topology, there exists $\epsilon > 0$ such that $B(x, \epsilon) \subseteq U$.
Choose a rational number $r \in \mathbb{Q}$ such that $0 < r < \epsilon / 2$.
<2>3. Since $D$ is dense in $X$, the open ball $B(x, r)$ contains some point $d_n \in D$, so $d(x, d_n) < r$.
Then $x \in B(d_n, r)$.
<2>4. For any $y \in B(d_n, r)$, by the triangle inequality:
\[
d(y, x) \le d(y, d_n) + d(d_n, x) < r + r = 2r < \epsilon.
\]
Thus $y \in B(x, \epsilon) \subseteq U$, which proves $B(d_n, r) \subseteq U$.
Therefore $x \in B(d_n, r) \subseteq U$ with $B(d_n, r) \in \mathcal{B}$.
<2>5. Thus $\mathcal{B}$ is a countable basis for the topology of $X$, so $X$ is second countable.

<1>3. Conclusion:
Every second countable space is separable, and every separable metric space is second countable. Q.E.D.
:::
