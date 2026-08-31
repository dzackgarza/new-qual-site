---
schema: qual/card@1
id: P-PATOJ
kind: problem
title: The one-point compactification of a Hausdorff space is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Point-Set Topology
relations: []
review: draft
---

::: problem
Let $X$ be a Hausdorff space, and recall that the *one-point compactification* $X^* = X \cup \{\infty\}$ (where $\infty \notin X$) is defined with the collection of open sets $\mathcal{T}^*$ such that $U \subseteq X^*$ belongs to $\mathcal{T}^*$ if and only if either:
1. $U \subseteq X$ and $U$ is open in $X$, or
2. $\infty \in U$ and $X \setminus U$ is a compact subset of $X$.

Prove that $\mathcal{T}^*$ defines a topology on $X^*$ and that $(X^*, \mathcal{T}^*)$ is a compact space.
:::

::: solution
**Goal:** Prove that $\mathcal{T}^*$ satisfies the topology axioms (empty set/whole space, arbitrary unions, finite intersections) and that every open cover of $X^*$ has a finite subcover.

<1>1. $\mathcal{T}^*$ contains $\emptyset$ and $X^*$:
    *Proof:*
    <2>1. The empty set $\emptyset \subseteq X$ is open in $X$, so $\emptyset \in \mathcal{T}^*$ by condition (1).
    <2>2. The whole space $X^*$ contains $\infty$, and $X \setminus X^* = \emptyset$.
    <2>3. The empty set $\emptyset$ is compact in $X$, so $X^* \in \mathcal{T}^*$ by condition (2).

<1>2. $\mathcal{T}^*$ is closed under arbitrary unions:
    *Proof:*
    <2>1. Let $\{U_\alpha\}_{\alpha \in A} \subseteq \mathcal{T}^*$, and define $U = \bigcup_{\alpha \in A} U_\alpha$.
    <2>2. Case 1 (for all $\alpha \in A$, $\infty \notin U_\alpha$):
        - Each $U_\alpha$ is an open subset of $X$.
        - The union $U = \bigcup_{\alpha \in A} U_\alpha \subseteq X$ is an open subset of $X$.
        - Thus $U \in \mathcal{T}^*$ by condition (1).
    <2>3. Case 2 (there exists $\alpha_0 \in A$ such that $\infty \in U_{\alpha_0}$):
        - Then $\infty \in U$.
        - Compute the complement in $X$:
        $$X \setminus U = X \setminus \bigcup_{\alpha \in A} U_\alpha = \bigcap_{\alpha \in A} (X \setminus U_\alpha) \subseteq X \setminus U_{\alpha_0}.$$
        - For every $\alpha \in A$:
            - If $\infty \in U_\alpha$, $X \setminus U_\alpha$ is compact in $X$. Since $X$ is Hausdorff, every compact subset is closed in $X$, so $X \setminus U_\alpha$ is closed in $X$.
            - If $\infty \notin U_\alpha$, $U_\alpha$ is open in $X$, so $X \setminus U_\alpha$ is closed in $X$.
        - Thus $X \setminus U = \bigcap_{\alpha \in A} (X \setminus U_\alpha)$ is an intersection of closed sets, hence closed in $X$.
        - Since $X \setminus U$ is a closed subset of the compact set $X \setminus U_{\alpha_0}$, $X \setminus U$ is compact in $X$.
        - Thus $U \in \mathcal{T}^*$ by condition (2).

<1>3. $\mathcal{T}^*$ is closed under finite intersections:
    *Proof:*
    <2>1. Let $U_1, U_2 \in \mathcal{T}^*$, and define $U = U_1 \cap U_2$.
    <2>2. Case 1 ($\infty \notin U_1$ or $\infty \notin U_2$):
        - WLOG assume $\infty \notin U_1$, so $U_1$ is open in $X$.
        - Then $U = U_1 \cap U_2 = U_1 \cap (U_2 \cap X)$.
        - If $\infty \notin U_2$, $U_2$ is open in $X$, so $U$ is the intersection of two open sets in $X$, hence open in $X$.
        - If $\infty \in U_2$, $X \setminus U_2$ is compact (hence closed in Hausdorff $X$), so $U_2 \cap X = X \setminus (X \setminus U_2)$ is open in $X$.
        - Then $U = U_1 \cap (U_2 \cap X)$ is open in $X$.
        - Thus $U \in \mathcal{T}^*$ by condition (1).
    <2>3. Case 2 ($\infty \in U_1$ and $\infty \in U_2$):
        - Then $\infty \in U_1 \cap U_2 = U$.
        - Compute the complement in $X$:
        $$X \setminus U = X \setminus (U_1 \cap U_2) = (X \setminus U_1) \cup (X \setminus U_2).$$
        - Since $X \setminus U_1$ and $X \setminus U_2$ are compact subsets of $X$, their finite union is compact in $X$.
        - Thus $U \in \mathcal{T}^*$ by condition (2).
    <2>4. By induction, $\mathcal{T}^*$ is closed under all finite intersections.

<1>4. $X^*$ is compact:
    *Proof:*
    <2>1. Let $\mathcal{U} = \{U_i\}_{i \in I}$ be an open cover of $X^*$.
    <2>2. Since $\infty \in X^* = \bigcup_{i \in I} U_i$, there exists an index $i_0 \in I$ such that $\infty \in U_{i_0}$.
    <2>3. By condition (2), $K = X \setminus U_{i_0}$ is a compact subset of $X$.
    <2>4. For each $i \in I$, the set $V_i = U_i \cap X$ is open in $X$.
    <2>5. The collection $\{V_i\}_{i \in I}$ is an open cover of $K$ in $X$:
    $$K = X^* \setminus U_{i_0} \subseteq \bigcup_{i \in I} U_i \setminus U_{i_0} \subseteq \bigcup_{i \in I} (U_i \cap X) = \bigcup_{i \in I} V_i.$$
    <2>6. Since $K$ is compact, there exists a finite subcollection $\{V_{i_1}, \dots, V_{i_m}\}$ covering $K$:
    $$K \subseteq V_{i_1} \cup \dots \cup V_{i_m} \subseteq U_{i_1} \cup \dots \cup U_{i_m}.$$
    <2>7. Since $X^* = U_{i_0} \cup K$, the finite subcollection $\{U_{i_0}, U_{i_1}, \dots, U_{i_m}\} \subseteq \mathcal{U}$ satisfies
    $$X^* = U_{i_0} \cup K \subseteq U_{i_0} \cup U_{i_1} \cup \dots \cup U_{i_m}.$$
    <2>8. Thus every open cover of $X^*$ has a finite subcover, so $X^*$ is compact.

<1>5. Conclusion:
    *Proof:*
    $\mathcal{T}^*$ is a topology on $X^*$ and $(X^*, \mathcal{T}^*)$ is compact.
:::

