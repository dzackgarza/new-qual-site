---
schema: qual/card@1
id: E-0GRG4
kind: exercise
title: Countability axioms of R^omega in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Countability
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Which of our four countability axioms does $\mathbb{R}^\omega$ in the uniform topology satisfy?
:::

::: solution
**Goal:** Determine which of the four countability axioms (first-countable, second-countable, Lindelöf, separable) are satisfied by $\mathbb{R}^\omega$ equipped with the uniform metric topology.

<1>1. Metric characterization of the uniform topology:
    The uniform topology on $\mathbb{R}^\omega$ is induced by the uniform metric:
    $$\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{n \in \mathbb{Z}_+} \bar{d}(x_n, y_n), \quad \text{where } \bar{d}(a, b) = \min\{|a - b|, 1\}.$$

<1>2. $\mathbb{R}^\omega$ is first-countable:
    *Proof:* Every metric space is first-countable. For each point $\mathbf{x} \in \mathbb{R}^\omega$, the countable collection of open balls $\{B_{\bar{\rho}}(\mathbf{x}, \frac{1}{k}) : k \in \mathbb{Z}_+\}$ forms a neighborhood basis at $\mathbf{x}$.

<1>3. Construction of an uncountable discrete subspace:
    Let $S = \{0, 1\}^\omega \subset \mathbb{R}^\omega$ be the set of all binary sequences $\mathbf{x} = (x_n)_{n=1}^\infty$ with $x_n \in \{0, 1\}$.
    *Proof:*
    <2>1. The set $S$ has cardinality $|S| = 2^{\aleph_0} > \aleph_0$, so $S$ is uncountable.
    <2>2. For any two distinct sequences $\mathbf{x}, \mathbf{y} \in S$, there exists an index $m \in \mathbb{Z}_+$ such that $x_m \neq y_m$.
    <2>3. Then $\bar{d}(x_m, y_m) = |x_m - y_m| = 1$, so $\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{n} \bar{d}(x_n, y_n) = 1$.
    <2>4. The open balls $\{B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2}) : \mathbf{x} \in S\}$ are pairwise disjoint in $\mathbb{R}^\omega$.

<1>4. $\mathbb{R}^\omega$ is not second-countable:
    *Proof:* Let $\mathcal{B}$ be any basis for the uniform topology on $\mathbb{R}^\omega$. For each $\mathbf{x} \in S$, the open set $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$ must contain a basis element $U_\mathbf{x} \in \mathcal{B}$ with $\mathbf{x} \in U_\mathbf{x} \subseteq B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$. Since the balls are pairwise disjoint (<1>3), the assignment $\mathbf{x} \mapsto U_\mathbf{x}$ is injective. Hence $|\mathcal{B}| \ge |S| = 2^{\aleph_0}$, so no countable basis exists.

<1>5. $\mathbb{R}^\omega$ is not separable:
    *Proof:* Let $D \subset \mathbb{R}^\omega$ be any dense subset. For each $\mathbf{x} \in S$, the non-empty open ball $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$ must contain a point $d_\mathbf{x} \in D$. By pairwise disjointness, all $d_\mathbf{x}$ are distinct, so $|D| \ge |S| = 2^{\aleph_0}$. Thus no countable dense subset exists.

<1>6. $\mathbb{R}^\omega$ is not Lindelöf:
    *Proof:* For each $\mathbf{x} \in S$, the set $F_\mathbf{x} = \{\mathbf{x}\}$ is closed in $\mathbb{R}^\omega$. Consider the open cover of $\mathbb{R}^\omega$ given by $\mathcal{U} = \{B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2}) : \mathbf{x} \in S\} \cup \{\mathbb{R}^\omega \setminus S\}$. Any subcover must contain every ball $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$ because $\mathbf{x} \in S$ belongs to no other member of $\mathcal{U}$. Since $S$ is uncountable, no countable subcover exists.

<1>7. Conclusion:
    $\mathbb{R}^\omega$ in the uniform topology satisfies the **first countability axiom**, but satisfies **none of the other three** (second-countable, separable, Lindelöf). Q.E.D.
:::
