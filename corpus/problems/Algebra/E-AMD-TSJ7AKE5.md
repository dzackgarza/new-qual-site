---
schema: qual/card@1
id: E-AMD-TSJ7AKE5
kind: exercise
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
Given $H\subseteq G$, let $S(H)= \bigcup_{g\in G} gHg^{-1}$, so $\abs{S(H)}$ is the number of conjugates to $H$.
Show that $\abs{S(H)} = [G : N_G(H)]$.

- That is, the number of subgroups conjugate to $H$ equals the index of the normalizer of $H$.
:::

::: {.solution}
<1>1. Group action by conjugation on subgroups:
<2>1. Let $\mathcal{S}$ be the set of all subgroups of $G$.
Define a group action of $G$ on $\mathcal{S}$ by conjugation:
\[
g \cdot K = g K g^{-1} \quad \text{for } g \in G, \; K \in \mathcal{S}.
\]
<2>2. Verify the group action axioms:
- Identity: $e \cdot K = e K e^{-1} = K$.
- Compatibility: for all $g_1, g_2 \in G$,
\[
g_1 \cdot (g_2 \cdot K) = g_1 (g_2 K g_2^{-1}) g_1^{-1} = (g_1 g_2) K (g_1 g_2)^{-1} = (g_1 g_2) \cdot K.
\]
Thus this defines a valid left group action of $G$ on $\mathcal{S}$.

<1>2. Identification of the orbit and stabilizer:
<2>1. The orbit of the subgroup $H$ under this action is the set of all conjugate subgroups:
\[
\operatorname{Orb}_G(H) = \{g \cdot H \mid g \in G\} = \{g H g^{-1} \mid g \in G\} = \mathcal{C}(H).
\]
<2>2. The stabilizer of $H$ is:
\[
\operatorname{Stab}_G(H) = \{g \in G \mid g \cdot H = H\} = \{g \in G \mid g H g^{-1} = H\} = N_G(H),
\]
which is the normalizer of $H$ in $G$.

<1>3. Application of the Orbit–Stabilizer Theorem:
<2>1. By the Orbit–Stabilizer Theorem, the map:
\[
\Phi: G / N_G(H) \longrightarrow \operatorname{Orb}_G(H), \qquad g N_G(H) \longmapsto g H g^{-1}
\]
is a well-defined bijection between the set of left cosets $G / N_G(H)$ and the orbit $\operatorname{Orb}_G(H)$.
<2>2. Therefore the number of conjugate subgroups is:
\[
|\mathcal{C}(H)| = |\operatorname{Orb}_G(H)| = |G / N_G(H)| = [G : N_G(H)].
\]

<1>4. Conclusion:
The number of subgroups conjugate to $H$ equals $[G : N_G(H)]$. Q.E.D.
:::
