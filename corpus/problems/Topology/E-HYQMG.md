---
schema: qual/card@1
id: E-HYQMG
kind: exercise
title: $X$ is Hausdorff if and only if $\Delta(X)$ is closed in $X\times X$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Show that a topological space $X$ is Hausdorff if and only if the diagonal $\Delta(X) = \{(x, x) \mid x \in X\}$ is closed in $X \times X$ with the product topology.
:::

::: solution
**Goal:** Prove that $X$ is Hausdorff $\iff$ $\Delta(X) = \{(x, x) \mid x \in X\} \subseteq X \times X$ is closed.

<1>1. Forward direction ($X$ Hausdorff $\implies \Delta(X)$ closed):
    *Proof:*
    <2>1. To show $\Delta(X)$ is closed in $X \times X$, it suffices to show that its complement $(X \times X) \setminus \Delta(X)$ is open.
    <2>2. Let $(x, y) \in (X \times X) \setminus \Delta(X)$. Then $x \ne y$ in $X$.
    <2>3. Because $X$ is Hausdorff ($T_2$), there exist disjoint open neighborhoods $U, V \subseteq X$ such that $x \in U$, $y \in V$, and $U \cap V = \varnothing$.
    <2>4. In the product topology, $U \times V$ is an open neighborhood of $(x, y)$ in $X \times X$.
    <2>5. **$(U \times V) \cap \Delta(X) = \varnothing$:** If there were a point $(z, z) \in (U \times V) \cap \Delta(X)$, then $z \in U$ and $z \in V$, so $z \in U \cap V$, contradicting $U \cap V = \varnothing$.
    <2>6. Thus $(x, y) \in U \times V \subseteq (X \times X) \setminus \Delta(X)$.
    <2>7. Since every point of $(X \times X) \setminus \Delta(X)$ has an open neighborhood contained in the complement, $(X \times X) \setminus \Delta(X)$ is open, so $\Delta(X)$ is closed.

<1>2. Reverse direction ($\Delta(X)$ closed $\implies X$ Hausdorff):
    *Proof:*
    <2>1. Suppose $\Delta(X)$ is closed in $X \times X$, so $(X \times X) \setminus \Delta(X)$ is open.
    <2>2. Let $x, y \in X$ with $x \ne y$.
    <2>3. Then $(x, y) \in (X \times X) \setminus \Delta(X)$.
    <2>4. Since the complement is open, by definition of the product topology there exists a basic open set $U \times V \subseteq X \times X$ (with $U, V \subseteq X$ open) such that:
        $$(x, y) \in U \times V \subseteq (X \times X) \setminus \Delta(X).$$
    <2>5. In particular, $x \in U$ and $y \in V$.
    <2>6. Since $(U \times V) \cap \Delta(X) = \varnothing$, there is no element $z \in X$ such that $(z, z) \in U \times V$.
    <2>7. This implies $U \cap V = \varnothing$.
    <2>8. Thus $U$ and $V$ are disjoint open neighborhoods separating $x$ and $y$, which proves $X$ is Hausdorff.

<1>3. Conclusion:
    $X$ is Hausdorff if and only if $\Delta(X)$ is closed in $X \times X$. Q.E.D.
:::
