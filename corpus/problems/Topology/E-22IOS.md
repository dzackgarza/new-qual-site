---
schema: qual/card@1
id: E-22IOS
kind: problem
title: Metric spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Hausdorff Spaces
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that every metric space is Hausdorff in its metric topology.
:::

::: solution
**Goal:** Prove that any metric space $(X, d)$ equipped with its metric topology is Hausdorff ($T_2$).

<1>1. Point separation: Let $x, y \in X$ be distinct points ($x \neq y$). By the positive-definiteness axiom of a metric, $r := d(x, y) > 0$.

<1>2. Construction of open neighborhoods: Define $\varepsilon = \frac{r}{2} > 0$.
Let $U = B_d(x, \varepsilon) = \{z \in X : d(x, z) < \varepsilon\}$ and $V = B_d(y, \varepsilon) = \{z \in X : d(y, z) < \varepsilon\}$.
*Proof:* Metric open balls are open sets in the metric topology, and $d(x, x) = 0 < \varepsilon \implies x \in U$, while $d(y, y) = 0 < \varepsilon \implies y \in V$.

<1>3. Disjointness of $U$ and $V$: $U \cap V = \emptyset$.
*Proof:* <2>1. Suppose for contradiction that there exists $z \in U \cap V$.
<2>2. Then $d(x, z) < \varepsilon = \frac{r}{2}$ and $d(z, y) = d(y, z) < \varepsilon = \frac{r}{2}$.
<2>3. By the triangle inequality: $$d(x, y) \le d(x, z) + d(z, y) < \frac{r}{2} + \frac{r}{2} = r.$$ <2>4. This strictly contradicts $d(x, y) = r$.
<2>5. Hence no such $z$ exists, so $U \cap V = \emptyset$.

<1>4. Conclusion: Every pair of distinct points in $(X, d)$ can be separated by disjoint open sets, so $(X, d)$ is Hausdorff.
Q.E.D.
:::
