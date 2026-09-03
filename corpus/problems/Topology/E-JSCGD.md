---
schema: qual/card@1
id: E-JSCGD
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Let $X$ be a compact topological space and let $A \subseteq X$ be a closed subset of $X$.
Prove that $A$ is compact in the subspace topology.
:::

::: solution
**Goal:** Prove that every closed subset of a compact space is compact.

<1>1. Setting and Open Cover of $A$:
    *Proof:*
    <2>1. Let $X$ be a compact topological space, and let $A \subseteq X$ be a closed subset.
    <2>2. Let $\{V_i\}_{i \in I}$ be an arbitrary open cover of $A$ in the subspace topology on $A$:
        $$A \subseteq \bigcup_{i \in I} V_i.$$
    <2>3. By definition of the subspace topology, for each $i \in I$, there exists an open subset $U_i \subseteq X$ such that $V_i = U_i \cap A$.
    <2>4. Thus:
        $$A \subseteq \bigcup_{i \in I} U_i.$$

<1>2. Extending to an Open Cover of $X$:
    *Proof:*
    <2>1. Since $A$ is closed in $X$, the complement $X \setminus A$ is an **open subset** of $X$:
        $$X \setminus A \in \mathcal{T}_X.$$
    <2>2. We can cover the entire space $X$ by adjoining $X \setminus A$ to the family $\{U_i\}_{i \in I}$:
        $$X = A \cup (X \setminus A) \subseteq \left( \bigcup_{i \in I} U_i \right) \cup (X \setminus A).$$
    <2>3. Therefore, $\mathcal{U} = \{U_i\}_{i \in I} \cup \{X \setminus A\}$ is an **open cover of $X$**.

<1>3. Extracting a Finite Subcover:
    *Proof:*
    <2>1. Since $X$ is compact, every open cover of $X$ has a finite subcover.
    <2>2. Hence, there exists a finite subcollection $\{U_{i_1}, U_{i_2}, \dots, U_{i_k}\} \subseteq \{U_i\}_{i \in I}$ such that:
        $$X \subseteq U_{i_1} \cup U_{i_2} \cup \cdots \cup U_{i_k} \cup (X \setminus A).$$
    <2>3. Intersecting both sides of this inclusion with $A$:
        $$\begin{aligned}
        A &= X \cap A \\
        &\subseteq \left( \bigcup_{j=1}^k U_{i_j} \cup (X \setminus A) \right) \cap A \\
        &= \left( \bigcup_{j=1}^k (U_{i_j} \cap A) \right) \cup ((X \setminus A) \cap A) \\
        &= \left( \bigcup_{j=1}^k V_{i_j} \right) \cup \varnothing \\
        &= \bigcup_{j=1}^k V_{i_j}.
        \end{aligned}$$
    <2>4. Thus $\{V_{i_1}, V_{i_2}, \dots, V_{i_k}\}$ is a **finite subcover** of $A$ extracted from the original cover $\{V_i\}_{i \in I}$.

<1>4. Conclusion:
    Every open cover of $A$ has a finite subcover, so $A$ is compact. Q.E.D.
:::
