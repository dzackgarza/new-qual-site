---
schema: qual/card@1
id: E-9OT3C
kind: problem
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

::: {.solution}
**Goal:** Prove that in a compact Hausdorff space $X$, two points $x, y \in X$ belong to the same quasicomponent if and only if they belong to the same connected component.

::: pf

::: pf-step
Part (a): Chains in $\mathcal{A}$ have lower bounds in $\mathcal{A}$.

::: pf-proof

::: pf-step
Let $\mathcal{B} \subseteq \mathcal{A}$ be a chain ordered by inclusion, and let $B_\infty = \bigcap_{B \in \mathcal{B}} B$.
:::

::: pf-step
As an intersection of closed subsets containing $\{x, y\}$, $B_\infty$ is a closed (hence compact) subspace of $X$ containing $x$ and $y$.
:::

::: pf-step
Suppose for contradiction that $x$ and $y$ do not belong to the same quasicomponent of $B_\infty$.
:::

::: pf-step
Then there exists a separation $B_\infty = C \cup D$, where $C, D$ are disjoint closed subsets of $B_\infty$ with $x \in C$ and $y \in D$.
:::

::: pf-step
Since $B_\infty$ is closed in the normal space $X$, $C$ and $D$ are disjoint closed subsets of $X$. By normality, choose disjoint open sets $U, V \subset X$ with $C \subseteq U$ and $D \subseteq V$.
:::

::: pf-step
Then $B_\infty \subseteq U \cup V$, so $\bigcap_{B \in \mathcal{B}} (B \setminus (U \cup V)) = \varnothing$.
:::

::: pf-step
By the Finite Intersection Property of compact closed sets in $X$, there exists $B_0 \in \mathcal{B}$ such that $B_0 \subseteq U \cup V$.
:::

::: pf-step
Then $B_0 \cap U$ and $B_0 \cap V$ form a separation of $B_0$ into disjoint open sets with $x \in B_0 \cap U$ and $y \in B_0 \cap V$, contradicting $B_0 \in \mathcal{A}$.
:::

::: pf-step
Hence $x$ and $y$ lie in the same quasicomponent of $B_\infty$, so $B_\infty \in \mathcal{A}$.
:::

:::

:::

::: pf-step
Part (b): Existence of a minimal element $D \in \mathcal{A}$.

::: pf-proof

::: pf-step
The collection $\mathcal{A}$ is non-empty because $X$ is closed and $x, y$ are in the same quasicomponent of $X$.
:::

::: pf-step
Order $\mathcal{A}$ by reverse inclusion ($A_1 \le A_2 \iff A_1 \supseteq A_2$).
:::

::: pf-step
By Part (a), every chain in $\mathcal{A}$ has an upper bound under this ordering (its intersection).
:::

::: pf-step
By Zorn's Lemma, $\mathcal{A}$ contains a maximal element with respect to reverse inclusion, which is a minimal element $D \in \mathcal{A}$ with respect to inclusion.
:::

:::

:::

::: pf-step
Part (c): Connectedness of $D$ and equality of components and quasicomponents.

::: pf-proof

::: pf-step
Suppose for contradiction that $D$ is disconnected, so $D = C_1 \cup D_1$ is a separation of $D$ into disjoint, non-empty closed sets.
:::

::: pf-step
Since $x$ and $y$ are in the same quasicomponent of $D$, they cannot be separated by this clopen partition; hence both $x, y \in C_1$ (without loss of generality).
:::

::: pf-step
$C_1$ is a closed subset of $D$ (hence of $X$). Because $D_1 \neq \varnothing$, $C_1 \subsetneq D$ is a strictly smaller closed subset.
:::

::: pf-step
If $x$ and $y$ were separated in $C_1$ by $C_1 = E \cup F$, then $D = E \cup (F \cup D_1)$ would be a separation of $D$ separating $x$ and $y$, contradicting $D \in \mathcal{A}$.
:::

::: pf-step
Thus $x, y$ lie in the same quasicomponent of $C_1$, which implies $C_1 \in \mathcal{A}$.
:::

::: pf-step
This contradicts the minimality of $D$ in $\mathcal{A}$.
:::

::: pf-step
Therefore $D$ is connected.
:::

::: pf-step
Since $D$ is a connected subspace containing both $x$ and $y$, $x$ and $y$ belong to the same connected component of $X$.
:::

:::

:::

::: pf-step
Conclusion:
In any compact Hausdorff space, the quasicomponent of any point coincides with its connected component. Q.E.D.
:::

:::

:::
