---
schema: qual/card@1
id: E-3OAGD
kind: problem
title: Inner approximation of a finite-measure set by compact subsets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: exercise
- Show that if $E\subseteq \RR^n$ is measurable with $m(E) < \infty$, then
  $$m(E) = \sup \{ m(K) \mid K \subseteq E \text{ is compact}\}$$
  if and only if for all $\eps > 0$, there exists a compact set $K \subseteq E$ such that $m(K) \geq m(E) - \eps$.
:::

::: {.solution}
Let $E \subseteq \RR^n$ be a Lebesgue measurable set with $m(E) < \infty$, and consider the set of real numbers:
$$
\mathcal{S} = \{ m(K) \mid K \subseteq E \text{ is compact} \}.
$$
By monotonicity of the Lebesgue measure, for every compact $K \subseteq E$, we have $m(K) \leq m(E)$.
Thus $m(E)$ is an upper bound for the set $\mathcal{S}$.

**$(\Longrightarrow)$ Suppose $m(E) = \sup \mathcal{S}$:**
By the definition of the supremum of a set of real numbers:
For any $\eps > 0$, $m(E) - \eps$ is strictly less than the supremum $\sup \mathcal{S}$.
Therefore, $m(E) - \eps$ cannot be an upper bound for $\mathcal{S}$.
Hence, there exists an element $m(K) \in \mathcal{S}$ (where $K \subseteq E$ is compact) such that:
$$
m(K) > m(E) - \eps \implies m(K) \geq m(E) - \eps.
$$

**$(\Longleftarrow)$ Suppose that for all $\eps > 0$, there exists compact $K_\eps \subseteq E$ with $m(K_\eps) \geq m(E) - \eps$:**
1. Since $m(K) \leq m(E)$ for all compact $K \subseteq E$, $m(E)$ is an upper bound of $\mathcal{S}$.
   Therefore $\sup \mathcal{S} \leq m(E)$.
2. For each $\eps > 0$, since $m(K_\eps) \in \mathcal{S}$, we have:
   $$
   \sup \mathcal{S} \geq m(K_\eps) \geq m(E) - \eps.
   $$
3. Taking the limit as $\eps \to 0^+$ (or because the inequality holds for all $\eps > 0$):
   $$
   \sup \mathcal{S} \geq m(E).
   $$
Combining both inequalities gives:
$$
m(E) = \sup \{ m(K) \mid K \subseteq E \text{ is compact} \}.
$$
:::
