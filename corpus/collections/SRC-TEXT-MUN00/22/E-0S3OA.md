---
schema: qual/card@1
id: E-0S3OA
kind: problem
title: Subgroups and closures of subgroups are topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $H$ be a subspace of the topological group $G$.
Show that if $H$ is also a subgroup of $G$, then both $H$ and $\overline{H}$ are topological groups.
:::

::: solution
**Goal:** Prove that any subgroup $H$ of a topological group $G$ is a topological group under the subspace topology, and that its topological closure $\overline{H}$ is also a subgroup and a topological group.

<1>1. $H$ is a topological group:
    *Proof:*
    <2>1. $H$ is an abstract group under the restricted group operation since $H \le G$.
    <2>2. The multiplication map $m_G: G \times G \to G$ and inversion map $i_G: G \to G$ are continuous by the definition of a topological group.
    <2>3. The subspace topology on $H \times H \subseteq G \times G$ is identical to the product topology of the subspace topologies on $H$.
    <2>4. The restriction $m_H = m_G|_{H \times H}: H \times H \to H$ and $i_H = i_G|_H: H \to H$ are continuous because restrictions of continuous maps to subspaces (with codomain restricted to invariant subsets) are continuous.
    <2>5. Thus $H$ is a topological group.

<1>2. $\overline{H}$ is closed under inverses ($(\overline{H})^{-1} = \overline{H}$):
    *Proof:*
    <2>1. The inversion map $i_G: G \to G$ defined by $i_G(x) = x^{-1}$ is a homeomorphism because $i_G \circ i_G = \operatorname{id}_G$ and $i_G$ is continuous.
    <2>2. Since $i_G$ is a homeomorphism, it commutes with the closure operation: $i_G(\overline{S}) = \overline{i_G(S)}$ for any $S \subseteq G$.
    <2>3. Since $H$ is a subgroup, $i_G(H) = H^{-1} = H$.
    <2>4. Therefore $(\overline{H})^{-1} = i_G(\overline{H}) = \overline{i_G(H)} = \overline{H}$.

<1>3. $\overline{H}$ is closed under multiplication ($\overline{H} \cdot \overline{H} \subseteq \overline{H}$):
    *Proof:*
    <2>1. Let $x, y \in \overline{H}$. We prove $xy \in \overline{H}$ by showing that every open neighborhood $W$ of $xy$ in $G$ intersects $H$.
    <2>2. Let $W$ be an open neighborhood of $xy$ in $G$.
    <2>3. Since multiplication $m_G$ is continuous and $m_G(x, y) = xy \in W$, there exist open neighborhoods $U$ of $x$ and $V$ of $y$ in $G$ such that $U \cdot V \subseteq W$.
    <2>4. Since $x \in \overline{H}$, the neighborhood $U$ contains an element $h_1 \in H$.
    <2>5. Since $y \in \overline{H}$, the neighborhood $V$ contains an element $h_2 \in H$.
    <2>6. Since $H$ is a subgroup, $h_1 h_2 \in H$.
    <2>7. Since $h_1 \in U$ and $h_2 \in V$, $h_1 h_2 \in U \cdot V \subseteq W$.
    <2>8. Thus $h_1 h_2 \in W \cap H$, so $W \cap H \neq \emptyset$.
    <2>9. Since every open neighborhood $W$ of $xy$ meets $H$, $xy \in \overline{H}$.

<1>4. $\overline{H}$ is a topological group:
    *Proof:*
    <2>1. The identity element $e \in H \subseteq \overline{H}$.
    <2>2. By <1>2 and <1>3, $\overline{H}$ is closed under inverses and products, so $\overline{H}$ is a subgroup of $G$.
    <2>3. By the same subspace restriction argument as in <1>1, the restricted multiplication and inversion maps on $\overline{H}$ are continuous under the subspace topology.
    <2>4. Therefore $\overline{H}$ is a topological group. Q.E.D.
:::
