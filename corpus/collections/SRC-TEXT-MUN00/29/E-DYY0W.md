---
schema: qual/card@1
id: E-DYY0W
kind: exercise
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
<1>1. Let $\pi : G \to G/H$ be the quotient map, and let $gH \in G/H$ be an arbitrary coset.
Proof: fix a point of $G/H$.

<1>2. Since $G$ is locally compact, there is a compact neighborhood $K$ of $g$ in $G$.
Proof: definition of local compactness.

<1>3. $\pi(K)$ is a compact neighborhood of $gH$ in $G/H$.
Proof: $\pi$ is continuous and surjective, so $\pi(K)$ is compact; and $\pi$ is an open map (the quotient map of a topological group by a subgroup is open), so $\pi(K)$ is a neighborhood of $\pi(g) = gH$.

<1>4. Hence every point of $G/H$ has a compact neighborhood, so $G/H$ is locally compact.
Proof: <1>1 and <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
