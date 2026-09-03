---
schema: qual/card@1
id: E-AL52O
kind: problem
title: The Euler number is a topological invariant
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that the Euler number of a finite linear graph $X$ is a topological invariant of $X$.
[Hint: First consider the case where $X$ is connected.]
:::

::: solution
**Goal:** Prove that the Euler characteristic $\chi(X) = V - E$ of a finite linear graph (1-dimensional CW complex) $X$ is a topological invariant.

<1>1. Connected finite graphs:
    *Proof:*
    <2>1. Let $X$ be a connected finite graph with $V$ vertices and $E$ edges.
    <2>2. Choose a maximal spanning tree $T \subseteq X$.
    <2>3. Because $T$ is a tree with $V$ vertices, it has exactly $V - 1$ edges and is contractible.
    <2>4. The quotient space $X / T$ is homeomorphic to a wedge sum of $k$ circles:
        $$X / T \cong \bigvee_{j=1}^k S^1,$$
        where the number of circles equals the number of remaining edges $E - (V - 1) = E - V + 1 = 1 - \chi(X)$.
    <2>5. Because $(X, T)$ is a CW pair with contractible subcomplex $T$, the quotient projection $q: X \to X / T$ is a homotopy equivalence (Theorem 84.1).
    <2>6. Thus the fundamental group of $X$ is a free group of rank $k$:
        $$\pi_1(X, x_0) \cong \pi_1\left(\bigvee_{j=1}^k S^1\right) \cong F_k.$$
    <2>7. The rank $k$ of a finitely generated free group is uniquely determined by its abelianization $\pi_1(X)^{\text{ab}} \cong \mathbb{Z}^k$ (or first homology $H_1(X) \cong \mathbb{Z}^k$).
    <2>8. Expressing $\chi(X)$ in terms of the rank gives:
        $$\chi(X) = 1 - k = 1 - \operatorname{rank}(\pi_1(X, x_0)).$$
    <2>9. Because the fundamental group is a topological (and homotopy) invariant, $\chi(X)$ is a topological invariant for any connected finite graph $X$.

<1>2. General finite graphs (disconnected case):
    *Proof:*
    <2>1. Let $X$ be a finite graph with $c$ connected components $X_1, \dots, X_c$.
    <2>2. The vertex and edge counts satisfy $V = \sum_{i=1}^c V_i$ and $E = \sum_{i=1}^c E_i$, so:
        $$\chi(X) = V - E = \sum_{i=1}^c (V_i - E_i) = \sum_{i=1}^c \chi(X_i).$$
    <2>3. Applying <1>1 to each connected component $X_i$:
        $$\chi(X) = \sum_{i=1}^c \big(1 - \operatorname{rank}(\pi_1(X_i))\big) = c - \sum_{i=1}^c \operatorname{rank}(\pi_1(X_i)).$$
    <2>4. The number of connected components $c$ and the fundamental groups of the individual components are all topological invariants of the space $X$.

<1>3. Conclusion:
    The Euler number $\chi(X)$ is completely determined by the topology of $X$, and hence is a topological invariant. Q.E.D.
:::
