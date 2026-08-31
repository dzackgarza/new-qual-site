---
schema: qual/card@1
id: P-MHQ6A
kind: problem
title: Disconnected subspaces as unions of sets with disjoint ambient closures
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Closure
  - Subspace Topology
relations: []
review: draft
---

::: problem
If $X$ is a topological space and $S \subseteq X$, define in terms of open subsets of $X$ what it means for $S$ **not** to be connected.

Show that if $S$ is not connected, there exist non-empty subsets $A, B \subseteq X$ such that
$$
A \cup B = S \quad \text{and} \quad A \cap \bar{B} = \bar{A} \cap B = \emptyset,
$$
where $\bar{A}$ and $\bar{B}$ denote the closures of $A$ and $B$ with respect to the topology on the ambient space $X$.
:::

::: solution
**Goal:** Define disconnectedness of a subspace via ambient open sets, and construct separated sets $A, B$ whose ambient closures do not intersect the other set.

<1>1. Definition of disconnected subspace in terms of open subsets of $X$:
    *Proof:*
    <2>1. A subspace $S \subseteq X$ is not connected (disconnected) if and only if there exist open sets $U, V \subseteq X$ such that:
        1. $S \cap U \ne \emptyset$ and $S \cap V \ne \emptyset$,
        2. $(S \cap U) \cap (S \cap V) = S \cap U \cap V = \emptyset$,
        3. $S \subseteq U \cup V$.
    <2>2. Equivalently, $S \cap U$ and $S \cap V$ form a separation of $S$ into disjoint non-empty sets open in the subspace topology on $S$.

<1>2. Construction of $A$ and $B$:
    *Proof:*
    <2>1. Assume $S$ is not connected, and choose ambient open sets $U, V \subseteq X$ satisfying <1>1.
    <2>2. Define $A = S \cap U$ and $B = S \cap V$.
    <2>3. By condition (1), $A \ne \emptyset$ and $B \ne \emptyset$.
    <2>4. By condition (3), $A \cup B = (S \cap U) \cup (S \cap V) = S \cap (U \cup V) = S$.

<1>3. Proof that $\bar{A} \cap B = \emptyset$:
    *Proof:*
    <2>1. From condition (2), $(S \cap U) \cap (S \cap V) = \emptyset$, which means $A \cap V = \emptyset$.
    <2>2. Thus $A \subseteq X \setminus V$.
    <2>3. Because $V$ is open in $X$, the complement $X \setminus V$ is closed in the ambient space $X$.
    <2>4. The closure $\bar{A} = \operatorname{cl}_X(A)$ is the smallest closed subset of $X$ containing $A$.
    <2>5. Since $X \setminus V$ is a closed set containing $A$, $\bar{A} \subseteq X \setminus V$.
    <2>6. Thus $\bar{A} \cap V = \emptyset$.
    <2>7. Since $B = S \cap V \subseteq V$, we obtain:
    $$\bar{A} \cap B \subseteq \bar{A} \cap V = \emptyset \implies \bar{A} \cap B = \emptyset.$$

<1>4. Proof that $A \cap \bar{B} = \emptyset$:
    *Proof:*
    <2>1. Symmetrically, condition (2) implies $B \cap U = \emptyset$, so $B \subseteq X \setminus U$.
    <2>2. Because $U$ is open in $X$, $X \setminus U$ is closed in $X$.
    <2>3. Therefore $\bar{B} = \operatorname{cl}_X(B) \subseteq X \setminus U$.
    <2>4. Thus $\bar{B} \cap U = \emptyset$.
    <2>5. Since $A = S \cap U \subseteq U$, we obtain:
    $$A \cap \bar{B} \subseteq U \cap \bar{B} = \emptyset \implies A \cap \bar{B} = \emptyset.$$

<1>5. Conclusion:
    *Proof:*
    The non-empty sets $A = S \cap U$ and $B = S \cap V$ satisfy $A \cup B = S$ and $A \cap \bar{B} = \bar{A} \cap B = \emptyset$.
:::

