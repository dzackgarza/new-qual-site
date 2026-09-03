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
Given a subgroup $H\leq G$, let
\[
\mathcal C(H)=\ts{gHg^{-1}:g\in G}
\]
be the set of subgroups conjugate to $H$.
Show that
\[
\abs{\mathcal C(H)}=[G:N_G(H)].
\]
:::

::: {.solution}
<1>1. Let $G$ act on the set of its subgroups by conjugation:
\[
g \cdot K = g K g^{-1} \quad \text{for } g \in G, \; K \in \mathcal{S}.
\]
Here $\mathcal S$ denotes the set of subgroups of $G$.

<1>2. The orbit of $H$ is exactly the set of its conjugate subgroups:
\[
\operatorname{Orb}_G(H) = \{g \cdot H \mid g \in G\} = \{g H g^{-1} \mid g \in G\} = \mathcal{C}(H).
\]

<1>3. The stabilizer of $H$ is its normalizer:
\[
\operatorname{Stab}_G(H) = \{g \in G \mid g \cdot H = H\} = \{g \in G \mid g H g^{-1} = H\} = N_G(H),
\]

<1>4. By orbit--stabilizer,
\[
|\mathcal{C}(H)| = |\operatorname{Orb}_G(H)| = |G / N_G(H)| = [G : N_G(H)].
\]
:::
