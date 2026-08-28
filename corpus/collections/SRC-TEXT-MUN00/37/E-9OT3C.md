---
schema: qual/card@1
id: E-9OT3C
kind: exercise
title: Quasicomponents equal components in compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Here is another theorem whose proof uses Zorn's lemma.
Recall that if $A$ is a space and if $x, y \in A$, we say that $x$ and $y$ belong to the same quasicomponent of $A$ if there is no separation $A = C \cup D$ of $A$ into two disjoint sets open in $A$ such that $x \in C$ and $y \in D$.

Theorem.
Let $X$ be a compact Hausdorff space.
Then $x$ and $y$ belong to the same quasicomponent of $X$ if and only if they belong to the same component of $X$.

(a) Let $\mathcal{A}$ be the collection of all closed subspaces $A$ of $X$ such that $x$ and $y$ lie in the same quasicomponent of $A$.
Let $\mathcal{B}$ be a subcollection of $\mathcal{A}$ that is simply ordered by proper inclusion.
Show that the intersection of the elements of $\mathcal{B}$ belongs to $\mathcal{A}$.
[Hint: Compare Exercise 11 of §26.]

(b) Show $\mathcal{A}$ has a minimal element $D$.

(c) Show $D$ is connected.
:::

::: solution
**Goal:** Prove that in a compact Hausdorff space $X$, two points $x, y \in X$ belong to the same quasicomponent if and only if they belong to the same connected component.

<1>1. Part (a): Chains in $\mathcal{A}$ have lower bounds in $\mathcal{A}$.
    *Proof:*
    <2>1. Let $\mathcal{B} \subseteq \mathcal{A}$ be a chain ordered by inclusion, and let $B_\infty = \bigcap_{B \in \mathcal{B}} B$.
    <2>2. As an intersection of closed subsets containing $\{x, y\}$, $B_\infty$ is a closed (hence compact) subspace of $X$ containing $x$ and $y$.
    <2>3. Suppose for contradiction that $x$ and $y$ do not belong to the same quasicomponent of $B_\infty$.
    <2>4. Then there exists a separation $B_\infty = C \cup D$, where $C, D$ are disjoint closed subsets of $B_\infty$ with $x \in C$ and $y \in D$.
    <2>5. Since $B_\infty$ is closed in the normal space $X$, $C$ and $D$ are disjoint closed subsets of $X$. By normality, choose disjoint open sets $U, V \subset X$ with $C \subseteq U$ and $D \subseteq V$.
    <2>6. Then $B_\infty \subseteq U \cup V$, so $\bigcap_{B \in \mathcal{B}} (B \setminus (U \cup V)) = \varnothing$.
    <2>7. By the Finite Intersection Property of compact closed sets in $X$, there exists $B_0 \in \mathcal{B}$ such that $B_0 \subseteq U \cup V$.
    <2>8. Then $B_0 \cap U$ and $B_0 \cap V$ form a separation of $B_0$ into disjoint open sets with $x \in B_0 \cap U$ and $y \in B_0 \cap V$, contradicting $B_0 \in \mathcal{A}$.
    <2>9. Hence $x$ and $y$ lie in the same quasicomponent of $B_\infty$, so $B_\infty \in \mathcal{A}$.

<1>2. Part (b): Existence of a minimal element $D \in \mathcal{A}$.
    *Proof:*
    <2>1. The collection $\mathcal{A}$ is non-empty because $X$ is closed and $x, y$ are in the same quasicomponent of $X$.
    <2>2. Order $\mathcal{A}$ by reverse inclusion ($A_1 \le A_2 \iff A_1 \supseteq A_2$).
    <2>3. By Part (a), every chain in $\mathcal{A}$ has an upper bound under this ordering (its intersection).
    <2>4. By Zorn's Lemma, $\mathcal{A}$ contains a maximal element with respect to reverse inclusion, which is a minimal element $D \in \mathcal{A}$ with respect to inclusion.

<1>3. Part (c): Connectedness of $D$ and equality of components and quasicomponents.
    *Proof:*
    <2>1. Suppose for contradiction that $D$ is disconnected, so $D = C_1 \cup D_1$ is a separation of $D$ into disjoint, non-empty closed sets.
    <2>2. Since $x$ and $y$ are in the same quasicomponent of $D$, they cannot be separated by this clopen partition; hence both $x, y \in C_1$ (without loss of generality).
    <2>3. $C_1$ is a closed subset of $D$ (hence of $X$). Because $D_1 \neq \varnothing$, $C_1 \subsetneq D$ is a strictly smaller closed subset.
    <2>4. If $x$ and $y$ were separated in $C_1$ by $C_1 = E \cup F$, then $D = E \cup (F \cup D_1)$ would be a separation of $D$ separating $x$ and $y$, contradicting $D \in \mathcal{A}$.
    <2>5. Thus $x, y$ lie in the same quasicomponent of $C_1$, which implies $C_1 \in \mathcal{A}$.
    <2>6. This contradicts the minimality of $D$ in $\mathcal{A}$.
    <2>7. Therefore $D$ is connected.
    <2>8. Since $D$ is a connected subspace containing both $x$ and $y$, $x$ and $y$ belong to the same connected component of $X$.

<1>4. Conclusion:
    In any compact Hausdorff space, the quasicomponent of any point coincides with its connected component. Q.E.D.
:::
