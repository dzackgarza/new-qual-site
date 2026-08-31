---
schema: qual/card@1
id: E-E3JL6
kind: exercise
title: Products of Hausdorff spaces are Hausdorff
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
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Show that the product of two Hausdorff spaces is Hausdorff.
:::

::: solution
**Goal:** Prove that if $X$ and $Y$ are Hausdorff topological spaces, then their Cartesian product $X \times Y$ (endowed with the product topology) is Hausdorff.

<1>1. Definition of the Hausdorff property:
    *Proof:*
    <2>1. A topological space is Hausdorff ($T_2$) if for every pair of distinct points, there exist disjoint open neighborhoods containing them.
    <2>2. Let $p_1 = (x_1, y_1)$ and $p_2 = (x_2, y_2)$ be two distinct points in $X \times Y$.
    <2>3. Since $p_1 \neq p_2$, at least one coordinate must differ: either $x_1 \neq x_2$ in $X$, or $y_1 \neq y_2$ in $Y$.

<1>2. Separation when the first coordinates differ ($x_1 \neq x_2$):
    *Proof:*
    <2>1. Since $X$ is Hausdorff and $x_1 \neq x_2$, there exist open sets $U_1, U_2 \subseteq X$ such that
    $$x_1 \in U_1, \qquad x_2 \in U_2, \qquad U_1 \cap U_2 = \emptyset.$$
    <2>2. Define $W_1 = U_1 \times Y$ and $W_2 = U_2 \times Y$.
    <2>3. By the definition of the product topology, $W_1$ and $W_2$ are open subsets of $X \times Y$.
    <2>4. We have $p_1 = (x_1, y_1) \in W_1$ since $x_1 \in U_1$ and $y_1 \in Y$, and $p_2 = (x_2, y_2) \in W_2$ since $x_2 \in U_2$ and $y_2 \in Y$.
    <2>5. The intersection is
    $$W_1 \cap W_2 = (U_1 \times Y) \cap (U_2 \times Y) = (U_1 \cap U_2) \times Y = \emptyset \times Y = \emptyset.$$
    <2>6. Thus $W_1$ and $W_2$ are disjoint open neighborhoods separating $p_1$ and $p_2$.

<1>3. Separation when the second coordinates differ ($y_1 \neq y_2$):
    *Proof:*
    <2>1. Since $Y$ is Hausdorff and $y_1 \neq y_2$, there exist open sets $V_1, V_2 \subseteq Y$ such that
    $$y_1 \in V_1, \qquad y_2 \in V_2, \qquad V_1 \cap V_2 = \emptyset.$$
    <2>2. Define $W_1 = X \times V_1$ and $W_2 = X \times V_2$.
    <2>3. Both $W_1$ and $W_2$ are open in $X \times Y$ with $p_1 \in W_1$ and $p_2 \in W_2$.
    <2>4. The intersection is
    $$W_1 \cap W_2 = (X \times V_1) \cap (X \times V_2) = X \times (V_1 \cap V_2) = X \times \emptyset = \emptyset.$$
    <2>5. Thus $W_1$ and $W_2$ are disjoint open neighborhoods separating $p_1$ and $p_2$.

<1>4. Conclusion:
    *Proof:*
    In both cases, any two distinct points in $X \times Y$ can be separated by disjoint open sets. Therefore $X \times Y$ is Hausdorff.
:::
