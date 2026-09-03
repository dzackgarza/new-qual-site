---
schema: qual/card@1
id: E-0B5CJ
kind: problem
title: Punctured products of connected spaces are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $A$ be a proper subset of $X$, and let $B$ be a proper subset of $Y$.
If $X$ and $Y$ are connected, show that

$$
(X \times Y) - (A \times B)
$$

is connected.
:::

::: solution
**Goal:** Prove that the complement of a product of proper subsets in a product of connected spaces, $Z = (X \times Y) \setminus (A \times B)$, is connected.

<1>1. Selection of basepoint $(x_0, y_0)$:
    Since $A \subsetneq X$ and $B \subsetneq Y$ are proper subsets, there exist points $x_0 \in X \setminus A$ and $y_0 \in Y \setminus B$.

<1>2. Connected slices in $Z$:
    1. For every $x \in X \setminus A$, the vertical slice $V_x = \{x\} \times Y$ is homeomorphic to $Y$, hence connected, and satisfies $V_x \subseteq Z$.
    2. For every $y \in Y \setminus B$, the horizontal slice $H_y = X \times \{y\}$ is homeomorphic to $X$, hence connected, and satisfies $H_y \subseteq Z$.
    *Proof:*
    <2>1. If $x \notin A$, then for all $y \in Y$, $(x, y) \notin A \times B$, so $\{x\} \times Y \subseteq (X \times Y) \setminus (A \times B) = Z$.
    <2>2. If $y \notin B$, then for all $x \in X$, $(x, y) \notin A \times B$, so $X \times \{y\} \subseteq (X \times Y) \setminus (A \times B) = Z$.

<1>3. Central connected cross $C_0$:
    The set $C_0 = V_{x_0} \cup H_{y_0} = (\{x_0\} \times Y) \cup (X \times \{y_0\})$ is a connected subset of $Z$.
    *Proof:* $V_{x_0}$ and $H_{y_0}$ are connected subsets of $Z$ by <1>2, and $(x_0, y_0) \in V_{x_0} \cap H_{y_0} \neq \emptyset$. The union of connected spaces with a common point is connected.

<1>4. Decomposition of $Z$ into connected sets sharing $C_0$:
    For each point $(x, y) \in Z$, $(x, y)$ belongs to a connected subset of $Z$ containing $C_0$.
    *Proof:*
    <2>1. If $(x, y) \in Z = (X \times Y) \setminus (A \times B)$, then either $x \in X \setminus A$ or $y \in Y \setminus B$.
    <2>2. If $x \in X \setminus A$, then $V_x \subseteq Z$. Since $(x, y_0) \in V_x \cap H_{y_0} \subseteq V_x \cap C_0 \neq \emptyset$, the union $C_0 \cup V_x$ is connected, contains $(x, y)$, and is contained in $Z$.
    <2>3. If $y \in Y \setminus B$, then $H_y \subseteq Z$. Since $(x_0, y) \in H_y \cap V_{x_0} \subseteq H_y \cap C_0 \neq \emptyset$, the union $C_0 \cup H_y$ is connected, contains $(x, y)$, and is contained in $Z$.

<1>5. Conclusion:
    $Z = \bigcup_{x \in X \setminus A} (C_0 \cup V_x) \cup \bigcup_{y \in Y \setminus B} (C_0 \cup H_y)$ is a union of connected subspaces of $Z$ sharing the common point $(x_0, y_0) \in C_0$. Therefore $Z$ is connected. Q.E.D.
:::
