---
schema: qual/card@1
id: E-6A0RO
kind: problem
title: Hausdorff spaces and the closed diagonal
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that $X$ is Hausdorff if and only if the diagonal $\Delta = \ts{x \times x \mid x \in X}$ is closed in $X \times X$.
:::

::: solution
**Goal:** Prove that a topological space $X$ is Hausdorff if and only if the diagonal subspace $\Delta = \{(x, x) \mid x \in X\}$ is closed in the product space $X \times X$.

<1>1. Direct implication ($\implies$): If $X$ is Hausdorff, then $\Delta$ is closed in $X \times X$.
    *Proof:*
    <2>1. We show that the complement $(X \times X) \setminus \Delta$ is open in $X \times X$.
    <2>2. Let $(x, y) \in (X \times X) \setminus \Delta$, which means $x \neq y$.
    <2>3. Because $X$ is Hausdorff, there exist open subsets $U, V \subseteq X$ such that $x \in U$, $y \in V$, and $U \cap V = \varnothing$.
    <2>4. The product set $U \times V$ is an open neighborhood of $(x, y)$ in the product topology on $X \times X$.
    <2>5. We claim $(U \times V) \cap \Delta = \varnothing$: if $(z, z) \in (U \times V) \cap \Delta$, then $z \in U \cap V = \varnothing$, a contradiction.
    <2>6. Thus $(x, y) \in U \times V \subseteq (X \times X) \setminus \Delta$.
    <2>7. Since $(x, y)$ was arbitrary, $(X \times X) \setminus \Delta$ is open, so $\Delta$ is closed.

<1>2. Converse implication ($\impliedby$): If $\Delta$ is closed in $X \times X$, then $X$ is Hausdorff.
    *Proof:*
    <2>1. Assume $\Delta$ is closed, so $(X \times X) \setminus \Delta$ is open in $X \times X$.
    <2>2. Let $x, y \in X$ be distinct points ($x \neq y$).
    <2>3. Then $(x, y) \in (X \times X) \setminus \Delta$.
    <2>4. By definition of the product topology, there exist open sets $U, V \subseteq X$ such that:
        $$(x, y) \in U \times V \subseteq (X \times X) \setminus \Delta.$$
    <2>5. Since $U \times V$ is disjoint from $\Delta$, there is no $z \in X$ such that $(z, z) \in U \times V$, which means $U \cap V = \varnothing$.
    <2>6. Thus $U$ and $V$ are disjoint open neighborhoods of $x$ and $y$, proving $X$ is Hausdorff.

<1>3. Conclusion:
    $X$ is Hausdorff if and only if $\Delta$ is closed in $X \times X$. Q.E.D.
:::
