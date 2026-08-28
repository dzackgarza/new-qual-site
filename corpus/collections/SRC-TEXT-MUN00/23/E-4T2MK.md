---
schema: qual/card@1
id: E-4T2MK
kind: exercise
title: Connected fibers over a connected base connect the total space
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $p: X \to Y$ be a quotient map.
Show that if each set $p^{-1}(\ts{y})$ is connected, and if $Y$ is connected, then $X$ is connected.
:::

::: solution
**Goal:** Prove that if $p: X \to Y$ is a quotient map with connected fibers $p^{-1}(\{y\})$ over a connected base $Y$, then the total space $X$ is connected.

<1>1. Setting and hypothesis:
    Suppose for contradiction that $X$ is disconnected.
    Then there exists a separation of $X$, i.e., non-empty disjoint open sets $U, V \subseteq X$ such that $X = U \cup V$.

<1>2. Saturatedness of $U$ and $V$ via connected fibers:
    For every $y \in Y$, either $p^{-1}(\{y\}) \subseteq U$ or $p^{-1}(\{y\}) \subseteq V$.
    *Proof:*
    <2>1. Fix $y \in Y$. The fiber $F_y = p^{-1}(\{y\})$ is connected by hypothesis.
    <2>2. The sets $F_y \cap U$ and $F_y \cap V$ are disjoint open subsets of the subspace $F_y$, and $(F_y \cap U) \cup (F_y \cap V) = F_y \cap (U \cup V) = F_y$.
    <2>3. Because $F_y$ is connected, one of these sets must be empty and the other must be all of $F_y$.
    <2>4. Hence, either $F_y \subseteq U$ or $F_y \subseteq V$.
    <2>5. Consequently, $U$ and $V$ are saturated sets: $p^{-1}(p(U)) = U$ and $p^{-1}(p(V)) = V$.

<1>3. Separation of the base space $Y$:
    The sets $p(U)$ and $p(V)$ form a separation of $Y$.
    *Proof:*
    <2>1. **Non-emptiness:** Since $U$ and $V$ are non-empty and $p$ is surjective, $p(U) \neq \varnothing$ and $p(V) \neq \varnothing$.
    <2>2. **Disjointness:** If $y \in p(U) \cap p(V)$, then $F_y$ intersects both $U$ and $V$, contradicting <1>2. Thus $p(U) \cap p(V) = \varnothing$.
    <2>3. **Union:** $p(U) \cup p(V) = p(U \cup V) = p(X) = Y$.
    <2>4. **Openness:** By <1>2, $p^{-1}(p(U)) = U$, which is open in $X$. By the definition of the quotient topology, $p(U)$ is open in $Y$. Similarly, $p^{-1}(p(V)) = V$ is open in $X$, so $p(V)$ is open in $Y$.

<1>4. Contradiction and conclusion:
    <1>3 proves that $Y = p(U) \cup p(V)$ is a separation of $Y$ into two disjoint non-empty open sets, which contradicts the connectedness of $Y$.
    Therefore, no separation of $X$ exists, and $X$ is connected. Q.E.D.
:::
