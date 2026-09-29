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

::: {.problem}
If $X$ is a topological space and $S \subseteq X$, define in terms of open subsets of $X$ what it means for $S$ **not** to be connected.

Show that if $S$ is not connected, there exist non-empty subsets $A, B \subseteq X$ such that
$$
A \cup B = S \quad \text{and} \quad A \cap \bar{B} = \bar{A} \cap B = \emptyset,
$$
where $\bar{A}$ and $\bar{B}$ denote the closures of $A$ and $B$ with respect to the topology on the ambient space $X$.
:::

::: {.solution}
**Goal:** Define disconnectedness of a subspace via ambient open sets, and construct separated sets $A, B$ whose ambient closures do not intersect the other set.

::: pf

::: {.pf-step #s1}
Definition of disconnected subspace in terms of open subsets of $X$:

::: pf-proof

::: pf-step
A subspace $S \subseteq X$ is not connected (disconnected) if and only if there exist open sets $U, V \subseteq X$ such that:

1. $S \cap U \ne \emptyset$ and $S \cap V \ne \emptyset$,
2. $(S \cap U) \cap (S \cap V) = S \cap U \cap V = \emptyset$,
3. $S \subseteq U \cup V$.

:::

::: pf-step
Equivalently, $S \cap U$ and $S \cap V$ form a separation of $S$ into disjoint non-empty sets open in the subspace topology on $S$.

:::

:::

:::

::: pf-step
Construction of $A$ and $B$:

::: pf-proof

::: pf-step
Assume $S$ is not connected, and choose ambient open sets $U, V \subseteq X$ satisfying step [](#s1){.pf-ref}.

:::

::: pf-step
Define $A = S \cap U$ and $B = S \cap V$.

:::

::: pf-step
By condition (1), $A \ne \emptyset$ and $B \ne \emptyset$.

:::

::: pf-step
By condition (3), $A \cup B = (S \cap U) \cup (S \cap V) = S \cap (U \cup V) = S$.

:::

:::

:::

::: pf-step
Proof that $\bar{A} \cap B = \emptyset$:

::: pf-proof

::: pf-step
From condition (2), $(S \cap U) \cap (S \cap V) = \emptyset$, which means $A \cap V = \emptyset$.

:::

::: pf-step
Thus $A \subseteq X \setminus V$.

:::

::: pf-step
Because $V$ is open in $X$, the complement $X \setminus V$ is closed in the ambient space $X$.

:::

::: pf-step
The closure $\bar{A} = \operatorname{cl}_X(A)$ is the smallest closed subset of $X$ containing $A$.

:::

::: pf-step
Since $X \setminus V$ is a closed set containing $A$, $\bar{A} \subseteq X \setminus V$.

:::

::: pf-step
Thus $\bar{A} \cap V = \emptyset$.

:::

::: pf-step
Since $B = S \cap V \subseteq V$, we obtain:
$$\bar{A} \cap B \subseteq \bar{A} \cap V = \emptyset \implies \bar{A} \cap B = \emptyset.$$

:::

:::

:::

::: pf-step
Proof that $A \cap \bar{B} = \emptyset$:

::: pf-proof

::: pf-step
Symmetrically, condition (2) implies $B \cap U = \emptyset$, so $B \subseteq X \setminus U$.

:::

::: pf-step
Because $U$ is open in $X$, $X \setminus U$ is closed in $X$.

:::

::: pf-step
Therefore $\bar{B} = \operatorname{cl}_X(B) \subseteq X \setminus U$.

:::

::: pf-step
Thus $\bar{B} \cap U = \emptyset$.

:::

::: pf-step
Since $A = S \cap U \subseteq U$, we obtain:
$$A \cap \bar{B} \subseteq U \cap \bar{B} = \emptyset \implies A \cap \bar{B} = \emptyset.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The non-empty sets $A = S \cap U$ and $B = S \cap V$ satisfy $A \cup B = S$ and $A \cap \bar{B} = \bar{A} \cap B = \emptyset$.
:::

:::

:::

:::

