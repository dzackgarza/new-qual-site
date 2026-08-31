---
schema: qual/card@1
id: P-7PCEH
kind: problem
title: Definition of deformation retract; isomorphic $\pi_1$ of the figure-eight and
  the theta space; $\pi_1$ of the theta space free on two generators
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
a. Let $A$ be a subspace of a topological space $X$.
Define what it means for $A$ to be a **deformation retract** of $X$.

b. Consider $X_1$ the "planar figure eight" and $$X_2 = S^1 \cup ({0} \times [-1, 1])$$ (the "theta space"). Show that $X_1$ and $X_2$ have isomorphic fundamental groups.

c. Prove that the fundamental group of $X_2$ is a free group on two generators.
:::

::: solution
**Goal:** Define deformation retract, prove $\pi_1(X_1) \cong \pi_1(X_2)$ for the figure-eight and theta spaces, and prove $\pi_1(X_2) \cong F_2$.

<1>1. Part (a): Definition of deformation retract.
    *Proof:*
    <2>1. Let $A$ be a subspace of a topological space $X$.
    <2>2. The subspace $A$ is a deformation retract of $X$ if there exists a continuous map $H: X \times [0, 1] \to X$ (a homotopy) such that for all $x \in X$ and all $a \in A$:
    $$H(x, 0) = x, \qquad H(x, 1) \in A, \qquad H(a, 1) = a.$$
    <2>3. If additionally $H(a, t) = a$ for all $a \in A$ and all $t \in [0, 1]$, then $A$ is called a strong deformation retract of $X$.
    <2>4. In either case, the inclusion $\iota: A \hookrightarrow X$ and the retraction $r(x) = H(x, 1)$ form a homotopy equivalence $X \simeq A$.

<1>2. Part (b): Homotopy equivalence and fundamental groups of $X_1$ and $X_2$.
    *Proof:*
    <2>1. Let $X_1 = S^1 \vee S^1$ be the figure-eight space (two circles joined at a single basepoint).
    <2>2. Let $X_2 = S^1 \cup (\{0\} \times [-1, 1]) \subset \mathbb{R}^2$ be the theta space, viewed as a 1-dimensional CW complex with 2 vertices $v_1 = (0, 1)$, $v_2 = (0, -1)$ and 3 edges: the left semicircle $e_1$, the right semicircle $e_2$, and the vertical diameter $e_3 = \{0\} \times [-1, 1]$.
    <2>3. The central vertical edge $e_3 \subset X_2$ is homeomorphic to the closed interval $[-1, 1]$, which is contractible.
    <2>4. In a CW complex, collapsing a contractible subcomplex produces a homotopy equivalent quotient space (Hatcher, Proposition 0.17). Therefore the quotient map $q: X_2 \to X_2 / e_3$ is a homotopy equivalence:
    $$X_2 \simeq X_2 / e_3.$$
    <2>5. The quotient space $X_2 / e_3$ identifies the two vertices $v_1$ and $v_2$ to a single point, while leaving the two remaining edges $e_1$ and $e_2$ as closed loops based at that point. Thus $X_2 / e_3 \cong S^1 \vee S^1 = X_1$.
    <2>6. Since $X_2 \simeq X_1$, the induced map on fundamental groups is an isomorphism:
    $$\pi_1(X_1) \cong \pi_1(X_2).$$

<1>3. Part (c): Computation showing $\pi_1(X_2) \cong F_2$.
    *Proof:*
    <2>1. By <1>2, $\pi_1(X_2) \cong \pi_1(S^1 \vee S^1)$.
    <2>2. By the Seifert–van Kampen Theorem applied to the wedge sum of two circles based at their common point:
    $$\pi_1(S^1 \vee S^1) \cong \pi_1(S^1) * \pi_1(S^1) \cong \mathbb{Z} * \mathbb{Z} = F_2,$$
    where $F_2 = \langle a, b \mid \varnothing \rangle$ denotes the free group on two generators.
    <2>3. Alternatively, viewing $X_2$ as a connected graph with $V = 2$ vertices and $E = 3$ edges: any maximal spanning tree $T \subset X_2$ has $V - 1 = 1$ edge (for instance, the vertical segment $e_3$).
    <2>4. The fundamental group of a connected graph is the free group of rank $E - V + 1 = 3 - 2 + 1 = 2$, with one free generator for each edge outside the spanning tree (namely $e_1$ and $e_2$).
    <2>5. Therefore $\pi_1(X_2) \cong F_2$.

<1>4. Conclusion:
    *Proof:*
    Parts (a), (b), and (c) are verified: $X_2 \simeq S^1 \vee S^1 \cong X_1$, so $\pi_1(X_2) \cong \pi_1(X_1) \cong F_2$.
:::
