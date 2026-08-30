---
schema: qual/card@1
id: P-6XN3Z
kind: problem
title: Whether the covering $S^2\to\RP^2$ is null-homotopic
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $S^2 \to \RP^2$ be the universal covering map.

Is this map null-homotopic?
Give a proof of your answer.
:::

::: solution
**Goal:** Show the universal covering map is not null-homotopic.

<1> Let $p:S^2\to \RP^2$ be the given covering map.
    *Proof:* Since $p$ is a covering map, for $n\ge2$ the induced map
    $$
    p_*:\pi_n(S^2)\to\pi_n(\RP^2)
    $$
    is an isomorphism.

<1> In degree $2$, $\pi_2(S^2)\cong\mathbf Z$ and therefore
    $\pi_2(\RP^2)\cong\mathbf Z$.
    Since $p_*:\pi_2(S^2)\to\pi_2(\RP^2)$ is an isomorphism, it is nonzero.

<1> If $p$ were null-homotopic, then the induced map on every homotopy group is zero; in particular $p_*:\pi_2(S^2)\to\pi_2(\RP^2)$ would be zero.
    This contradicts the isomorphism property above.

<1> Therefore the covering map $S^2\to\RP^2$ is not null-homotopic.

Authored by **Codex 5.3 Spark Extra High**.
:::
