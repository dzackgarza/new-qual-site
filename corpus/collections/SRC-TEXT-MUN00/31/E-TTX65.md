---
schema: qual/card@1
id: E-TTX65
kind: problem
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

::: pf

::: pf-step
Initial separation of disjoint closed sets:

::: pf-proof

::: pf-step
Let $A$ and $B$ be disjoint closed subsets of a normal space $X$ ($A \cap B = \emptyset$).

::: pf-proof
setup.
:::

:::

::: pf-step
By the definition of normality, there exist disjoint open sets $U, V \subseteq X$ such that:
\[
A \subseteq U, \quad B \subseteq V, \quad U \cap V = \emptyset.
\]

::: pf-proof
definition of a normal topological space.
:::

:::

::: pf-step
Since $U \cap V = \emptyset$, we have $U \subseteq X \setminus V$.
Since $V$ is open, $X \setminus V$ is closed, so taking closures yields:
\[
\overline{U} \subseteq X \setminus V \implies \overline{U} \cap V = \emptyset.
\]

::: pf-proof
closure of a subset of a closed set is contained in the closed set.
:::

:::

:::

:::

::: {.pf-step #strengthen-to-separated-closures}
Strengthening to separated closures:

::: pf-proof

::: pf-step
Consider the closed set $A$ and the closed set $X \setminus U$.
Since $A \subseteq U$, $A \cap (X \setminus U) = \emptyset$.

::: pf-proof
set complement.
:::

:::

::: {.pf-step #construct-w}
By normality, applying the open neighborhood lemma to $A$ and $X \setminus U$, there exists an open set $W \subseteq X$ such that:
\[
A \subseteq W \quad \text{and} \quad \overline{W} \subseteq U.
\]

::: pf-proof
characterization of normality ($A \subseteq U$ open $\implies \exists W$ open with $A \subseteq W \subseteq \overline{W} \subseteq U$).
:::

:::

::: {.pf-step #construct-g}
Symmetrically, since $B$ is closed and $B \subseteq V$, there exists an open set $G \subseteq X$ such that:
\[
B \subseteq G \quad \text{and} \quad \overline{G} \subseteq V.
\]

::: pf-proof
normality applied to $B \subseteq V$.
:::

:::

:::

:::

::: {.pf-step #closures-disjoint}
Prove that the closures of $W$ and $G$ are disjoint:

::: pf-proof

::: pf-step
By construction, $\overline{W} \subseteq U$ and $\overline{G} \subseteq V$.

::: pf-proof
Steps [](#construct-w){.pf-ref} and [](#construct-g){.pf-ref}.
:::

:::

::: pf-step
Therefore:
\[
\overline{W} \cap \overline{G} \subseteq U \cap V = \emptyset.
\]
Thus $\overline{W} \cap \overline{G} = \emptyset$.

::: pf-proof
subset of the empty set is empty.
:::

:::

:::

:::

::: pf-step
Conclusion:
$W$ and $G$ are open neighborhoods of $A$ and $B$ respectively with $\overline{W} \cap \overline{G} = \emptyset$. Q.E.D.

::: pf-proof
Steps [](#strengthen-to-separated-closures){.pf-ref} and [](#closures-disjoint){.pf-ref}.
:::

:::

:::

:::
