---
schema: qual/card@1
id: E-DYY0W
kind: problem
title: Coset spaces of locally compact groups are locally compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Show that if $G$ is a locally compact topological group and $H$ is a subgroup, then $G/H$ is locally compact.
:::

::: {.solution}

::: pf

::: {.pf-step #pi-definition}
Let $\pi : G \to G/H$ be the quotient map, and let $gH \in G/H$ be an arbitrary coset.

::: pf-proof
fix a point of $G/H$.
:::

:::

::: pf-step
Since $G$ is locally compact, there is a compact neighborhood $K$ of $g$ in $G$.

::: pf-proof
definition of local compactness.
:::

:::

::: {.pf-step #pi-k-compact-neighborhood}
$\pi(K)$ is a compact neighborhood of $gH$ in $G/H$.

::: pf-proof
$\pi$ is continuous and surjective, so $\pi(K)$ is compact; and $\pi$ is an open map (the quotient map of a topological group by a subgroup is open), so $\pi(K)$ is a neighborhood of $\pi(g) = gH$.
:::

:::

::: {.pf-step #every-point-has-compact-neighborhood}
Hence every point of $G/H$ has a compact neighborhood, so $G/H$ is locally compact.

::: pf-proof
Steps [](#pi-definition){.pf-ref} and [](#pi-k-compact-neighborhood){.pf-ref}.
:::

:::

::: pf-qed
Step [](#every-point-has-compact-neighborhood){.pf-ref}.
:::

:::

:::
