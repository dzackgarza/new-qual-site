---
schema: qual/card@1
id: E-2BCY2
kind: exercise
title: Intersections of nested families of closed connected sets are connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Theorem.
Let $X$ be a compact Hausdorff space.
Let $\mathcal{A}$ be a collection of closed connected subsets of $X$ that is simply ordered by proper inclusion.
Then

$$
Y = \bigcap_{A \in \mathcal{A}} A
$$

is connected.
[Hint: If $C \cup D$ is a separation of $Y$, choose disjoint open sets $U$ and $V$ of $X$ containing $C$ and $D$, respectively, and show that

$$
\bigcap_{A \in \mathcal{A}} (A - (U \cup V))
$$

is not empty.]
:::

::: solution
**Goal:** Prove that the intersection $Y = \bigcap_{A \in \mathcal{A}} A$ of a nested (simply ordered by inclusion) family $\mathcal{A}$ of closed connected subsets in a compact Hausdorff space $X$ is non-empty and connected.

<1>1. $Y$ is non-empty and compact:
    *Proof:*
    <2>1. Each $A \in \mathcal{A}$ is closed in $X$, hence compact.
    <2>2. Since $\mathcal{A}$ is simply ordered by inclusion, any finite subcollection $\{A_1, \dots, A_k\} \subset \mathcal{A}$ has a minimal element $A_0 = \min_i A_i \in \mathcal{A}$, so $\bigcap_{i=1}^k A_i = A_0 \neq \emptyset$.
    <2>3. Thus $\mathcal{A}$ satisfies the finite intersection property.
    <2>4. By compactness of $X$, $Y = \bigcap_{A \in \mathcal{A}} A$ is non-empty, closed, and compact.

<1>2. Separation assumption and neighborhood separation:
    Suppose for contradiction that $Y$ is not connected.
    *Proof:*
    <2>1. There exists a separation $Y = C \cup D$ into disjoint, non-empty closed subsets $C, D \subset Y$.
    <2>2. Since $Y$ is closed in $X$, $C$ and $D$ are disjoint closed subsets of the compact Hausdorff space $X$.
    <2>3. Every compact Hausdorff space is normal ($T_4$).
    <2>4. By normality of $X$, there exist disjoint open sets $U, V \subset X$ such that $C \subset U$ and $D \subset V$.
    <2>5. Then $Y = C \cup D \subset U \cup V$ and $U \cap V = \emptyset$.

<1>3. Finiteness reduction on $A \setminus (U \cup V)$:
    There exists a member $A_0 \in \mathcal{A}$ such that $A_0 \subset U \cup V$.
    *Proof:*
    <2>1. For each $A \in \mathcal{A}$, define $F_A = A \setminus (U \cup V) = A \cap (X \setminus (U \cup V))$.
    <2>2. Since $X \setminus (U \cup V)$ is closed in $X$, each $F_A$ is a closed (hence compact) subset of $X$.
    <2>3. The total intersection is:
        $$\bigcap_{A \in \mathcal{A}} F_A = \left(\bigcap_{A \in \mathcal{A}} A\right) \setminus (U \cup V) = Y \setminus (U \cup V) = \emptyset.$$
    <2>4. By compactness of $X$, the family of closed sets $\{F_A\}_{A \in \mathcal{A}}$ cannot satisfy the finite intersection property, so there exists a finite subfamily $\{A_1, \dots, A_k\} \subset \mathcal{A}$ with $\bigcap_{i=1}^k F_{A_i} = \emptyset$.
    <2>5. Since $\mathcal{A}$ is totally ordered by inclusion, choose $A_0 = \min\{A_1, \dots, A_k\} \in \mathcal{A}$.
    <2>6. Then $F_{A_0} = \bigcap_{i=1}^k F_{A_i} = \emptyset$, which means $A_0 \setminus (U \cup V) = \emptyset$, i.e., $A_0 \subset U \cup V$.

<1>4. Derivation of contradiction:
    *Proof:*
    <2>1. Since $A_0 \subset U \cup V$ and $U \cap V = \emptyset$, we can write $A_0 = (A_0 \cap U) \cup (A_0 \cap V)$ as a union of disjoint open sets in the subspace topology of $A_0$.
    <2>2. Furthermore:
        $$A_0 \cap U \supseteq Y \cap U \supseteq C \neq \emptyset \quad \text{and} \quad A_0 \cap V \supseteq Y \cap V \supseteq D \neq \emptyset.$$
    <2>3. Thus $A_0 = (A_0 \cap U) \cup (A_0 \cap V)$ constitutes a separation of $A_0$ into two non-empty disjoint open sets.
    <2>4. This strictly contradicts the hypothesis that $A_0 \in \mathcal{A}$ is connected.

<1>5. Conclusion:
    No separation of $Y$ can exist, so $Y = \bigcap_{A \in \mathcal{A}} A$ is connected. Q.E.D.
:::
