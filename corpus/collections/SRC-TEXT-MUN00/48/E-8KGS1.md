---
schema: qual/card@1
id: E-8KGS1
kind: exercise
title: Local Baireness implies Baireness
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if every point $x$ of $X$ has a neighborhood that is a Baire space, then $X$ is a Baire space.
[Hint: Use the open set formulation of the Baire condition.]
:::

::: solution
**Goal:** Prove that if every point $x \in X$ has a neighborhood that is a Baire space, then the topological space $X$ is a Baire space.

<1>1. Reduction to an open cover by Baire open sets:
    *Proof:*
    <2>1. If a point $x \in X$ has a neighborhood $N$ that is a Baire space, there exists an open neighborhood $U_x \subseteq N$ containing $x$.
    <2>2. Since every open subspace of a Baire space is a Baire space, $U_x$ is an open subspace of $X$ that is a Baire space.
    <2>3. Thus $X$ possesses an open covering $\mathcal{U} = \{U_\alpha\}_{\alpha \in J}$ such that each $U_\alpha$ is open in $X$ and is a Baire space in the subspace topology.

<1>2. Open set / nowhere dense formulation of the Baire condition:
    *Proof:*
    <2>1. A topological space $X$ is a Baire space if and only if for every countable collection $\{A_n\}_{n=1}^\infty$ of closed subsets of $X$ each having empty interior ($\operatorname{Int}_X(A_n) = \varnothing$), and every non-empty open set $W \subseteq X$, the difference $W \setminus \bigcup_{n=1}^\infty A_n$ is non-empty.

<1>3. Verification of the Baire property on $X$:
    *Proof:*
    <2>1. Let $\{A_n\}_{n=1}^\infty$ be a sequence of closed subsets of $X$ with $\operatorname{Int}_X(A_n) = \varnothing$ for all $n$, and let $W \subseteq X$ be an arbitrary non-empty open set.
    <2>2. Pick a point $x_0 \in W$.
    <2>3. Since $\mathcal{U}$ covers $X$, choose an open Baire set $U \in \mathcal{U}$ containing $x_0$.
    <2>4. The intersection $V = W \cap U$ is a non-empty open subset of $U$.
    <2>5. For each $n$, the set $F_n = A_n \cap U$ is closed in $U$.
    <2>6. Because $U$ is open in $X$, the interior in $U$ satisfies:
        $$\operatorname{Int}_U(F_n) = \operatorname{Int}_X(A_n) \cap U = \varnothing \cap U = \varnothing.$$
    <2>7. Since $U$ is a Baire space and $V$ is a non-empty open set in $U$, $V \not\subseteq \bigcup_{n=1}^\infty F_n$.
    <2>8. Thus there exists a point $y \in V$ such that $y \notin \bigcup_{n=1}^\infty F_n$.
    <2>9. Because $y \in V \subseteq U$, $y \notin F_n \implies y \notin A_n$ for all $n \ge 1$.
    <2>10. Since $y \in V \subseteq W$, we have $y \in W \setminus \bigcup_{n=1}^\infty A_n$.

<1>4. Conclusion:
    $W \not\subseteq \bigcup_{n=1}^\infty A_n$, so $\operatorname{Int}_X(\bigcup_{n=1}^\infty A_n) = \varnothing$.
    Thus $X$ is a Baire space. Q.E.D.
:::
