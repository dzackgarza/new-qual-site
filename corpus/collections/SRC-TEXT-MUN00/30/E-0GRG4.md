---
schema: qual/card@1
id: E-0GRG4
kind: problem
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

Which of our four countability axioms does $\RR^\omega$ in the uniform topology satisfy?
:::

::: {.solution}

::: pf

::: pf-step
Metric characterization of the uniform topology:
The uniform topology on $\RR^\omega$ is induced by the uniform metric:
$$\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{n \in \ZZ_+} \bar{d}(x_n, y_n), \quad \text{where } \bar{d}(a, b) = \min\{|a - b|, 1\}.$$
:::

::: pf-step
$\RR^\omega$ is first-countable:

::: pf-proof
Every metric space is first-countable. For each point $\mathbf{x} \in \RR^\omega$, the countable collection of open balls $\{B_{\bar{\rho}}(\mathbf{x}, \frac{1}{k}) : k \in \ZZ_+\}$ forms a neighborhood basis at $\mathbf{x}$.
:::

:::

::: {.pf-step #uncountable-discrete-subspace}
Construction of an uncountable discrete subspace:
Let $S = \{0, 1\}^\omega \subset \RR^\omega$ be the set of all binary sequences $\mathbf{x} = (x_n)_{n=1}^\infty$ with $x_n \in \{0, 1\}$.

::: pf-proof

::: pf-step
The set $S$ has cardinality $|S| = 2^{\aleph_0} > \aleph_0$, so $S$ is uncountable.
:::

::: pf-step
For any two distinct sequences $\mathbf{x}, \mathbf{y} \in S$, there exists an index $m \in \ZZ_+$ such that $x_m \neq y_m$.
:::

::: pf-step
Then $\bar{d}(x_m, y_m) = |x_m - y_m| = 1$, so $\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{n} \bar{d}(x_n, y_n) = 1$.
:::

::: pf-step
The open balls $\{B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2}) : \mathbf{x} \in S\}$ are pairwise disjoint in $\RR^\omega$.
:::

:::

:::

::: pf-step
$\RR^\omega$ is not second-countable:

::: pf-proof
Let $\mathcal{B}$ be any basis for the uniform topology on $\RR^\omega$. For each $\mathbf{x} \in S$, the open set $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$ must contain a basis element $U_\mathbf{x} \in \mathcal{B}$ with $\mathbf{x} \in U_\mathbf{x} \subseteq B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$. Since the balls are pairwise disjoint (step [](#uncountable-discrete-subspace){.pf-ref}), the assignment $\mathbf{x} \mapsto U_\mathbf{x}$ is injective. Hence $|\mathcal{B}| \ge |S| = 2^{\aleph_0}$, so no countable basis exists.
:::

:::

::: pf-step
$\RR^\omega$ is not separable:

::: pf-proof
Let $D \subset \RR^\omega$ be any dense subset. For each $\mathbf{x} \in S$, the non-empty open ball $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$ must contain a point $d_\mathbf{x} \in D$. By pairwise disjointness, all $d_\mathbf{x}$ are distinct, so $|D| \ge |S| = 2^{\aleph_0}$. Thus no countable dense subset exists.
:::

:::

::: pf-step
$\RR^\omega$ is not Lindelöf:

::: pf-proof
For each $\mathbf{x} \in S$, the set $F_\mathbf{x} = \{\mathbf{x}\}$ is closed in $\RR^\omega$. Consider the open cover of $\RR^\omega$ given by $\mathcal{U} = \{B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2}) : \mathbf{x} \in S\} \cup \{\RR^\omega \setminus S\}$. Any subcover must contain every ball $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$ because $\mathbf{x} \in S$ belongs to no other member of $\mathcal{U}$. Since $S$ is uncountable, no countable subcover exists.
:::

:::

::: pf-step
Conclusion:
$\RR^\omega$ in the uniform topology satisfies the **first countability axiom**, but satisfies **none of the other three** (second-countable, separable, Lindelöf). Q.E.D.
:::

:::

:::
