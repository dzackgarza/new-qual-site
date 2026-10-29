---
schema: qual/card@1
id: E-AMD-TSJ7AKE5
kind: problem
title: The number of conjugates of $H$ equals $[G:N_G(H)]$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Let $G$ be a group. Given a subgroup $H\leq G$, let
$$
\mathcal C(H)=\theset{gHg^{-1}:g\in G}
$$
be the set of subgroups conjugate to $H$.
Show that
$$
\abs{\mathcal C(H)}=[G:N_G(H)].
$$
:::

::: {.solution}
Let $\mathcal S$ denote the set of subgroups of $G$, and let $G$ act on $\mathcal S$ by conjugation:
$$
g \cdot K = g K g^{-1} \quad \text{for } g \in G, \; K \in \mathcal{S}.
$$

::: pf

::: pf-step
The orbit of $H$ is exactly the set of its conjugate subgroups:
$$
\Orb_G(H) = \{g \cdot H \mid g \in G\} = \{g H g^{-1} \mid g \in G\} = \mathcal{C}(H).
$$
:::

::: pf-step
The stabilizer of $H$ is its normalizer:
$$
\Stab_G(H) = \{g \in G \mid g \cdot H = H\} = \{g \in G \mid g H g^{-1} = H\} = N_G(H).
$$
:::

::: pf-step
By orbit--stabilizer,
$$
\abs{\mathcal{C}(H)} = \abs{\Orb_G(H)} = \abs{G / N_G(H)} = [G : N_G(H)].
$$
:::

:::

:::
