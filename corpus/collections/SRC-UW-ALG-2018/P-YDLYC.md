---
schema: qual/card@1
id: P-YDLYC
kind: problem
title: No finite group is the union of conjugates of a proper subgroup
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Show that no finite group is the union of conjugates of a proper subgroup.
:::

::: {.solution}
Let $G$ be a finite group and let $H < G$ be a proper subgroup, so $[G : H] = k > 1$.

1. The number of distinct conjugate subgroups of $H$ in $G$ is $[G : N_G(H)] \leq [G : H] = k$.
   Let these conjugates be $H_1, H_2, \ldots, H_m$, where $m \leq k$.

2. Each conjugate $H_i$ has order $\abs{H_i} = \abs H$, and every conjugate contains the identity element $e$.

3. Count the number of non-identity elements in $\bigcup_{i=1}^m H_i$:
$$
\abs{\bigcup_{i=1}^m (H_i \setminus \{e\})} \leq \sum_{i=1}^m (\abs{H_i} - 1) = m(\abs H - 1).
$$

4. Therefore:
$$
\abs{\bigcup_{i=1}^m H_i} \leq 1 + m(\abs H - 1) \leq 1 + k(\abs H - 1) = 1 + [G:H](\abs H - 1) = 1 + \abs G - [G:H].
$$

5. Since $H < G$ is proper, $[G : H] \geq 2$, which implies:
$$
1 + \abs G - [G:H] \leq \abs G - 1 < \abs G.
$$

Thus $\bigcup_{g \in G} gHg^{-1} \subsetneq G$, so $G$ cannot be the union of the conjugates of any proper subgroup.
:::
