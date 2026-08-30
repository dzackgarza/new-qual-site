---
schema: qual/card@1
id: E-TTX65
kind: exercise
title: Normal spaces have disjoint closure neighborhoods of closed sets
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Show that if $X$ is normal, every pair of disjoint closed sets have neighborhoods whose closures are disjoint.
:::

::: {.solution}
<1>1. Initial separation of disjoint closed sets:
<2>1. Let $A$ and $B$ be disjoint closed subsets of a normal space $X$ ($A \cap B = \emptyset$).
Proof: setup.
<2>2. By the definition of normality, there exist disjoint open sets $U, V \subseteq X$ such that:
\[
A \subseteq U, \quad B \subseteq V, \quad U \cap V = \emptyset.
\]
Proof: definition of a normal topological space.
<2>3. Since $U \cap V = \emptyset$, we have $U \subseteq X \setminus V$.
Since $V$ is open, $X \setminus V$ is closed, so taking closures yields:
\[
\overline{U} \subseteq X \setminus V \implies \overline{U} \cap V = \emptyset.
\]
Proof: closure of a subset of a closed set is contained in the closed set.

<1>2. Strengthening to separated closures:
<2>1. Consider the closed set $A$ and the closed set $X \setminus U$.
Since $A \subseteq U$, $A \cap (X \setminus U) = \emptyset$.
Proof: set complement.
<2>2. By normality, applying the open neighborhood lemma to $A$ and $X \setminus U$, there exists an open set $W \subseteq X$ such that:
\[
A \subseteq W \quad \text{and} \quad \overline{W} \subseteq U.
\]
Proof: characterization of normality ($A \subseteq U$ open $\implies \exists W$ open with $A \subseteq W \subseteq \overline{W} \subseteq U$).
<2>3. Symmetrically, since $B$ is closed and $B \subseteq V$, there exists an open set $G \subseteq X$ such that:
\[
B \subseteq G \quad \text{and} \quad \overline{G} \subseteq V.
\]
Proof: normality applied to $B \subseteq V$.

<1>3. Prove that the closures of $W$ and $G$ are disjoint:
<2>1. By construction, $\overline{W} \subseteq U$ and $\overline{G} \subseteq V$.
Proof: <1>2 steps <2>2 and <2>3.
<2>2. Therefore:
\[
\overline{W} \cap \overline{G} \subseteq U \cap V = \emptyset.
\]
Thus $\overline{W} \cap \overline{G} = \emptyset$.
Proof: subset of the empty set is empty.

<1>4. Conclusion:
$W$ and $G$ are open neighborhoods of $A$ and $B$ respectively with $\overline{W} \cap \overline{G} = \emptyset$. Q.E.D.
Proof: <1>2 and <1>3.
:::
