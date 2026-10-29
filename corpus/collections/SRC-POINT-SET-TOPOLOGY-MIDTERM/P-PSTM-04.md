---
schema: qual/card@1
id: P-PSTM-04
kind: problem
title: Separating a compact set from an exterior point
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $X$ be a Hausdorff space.
Suppose $A$ is a compact subspace, and $x \in X \setminus A$.
Show that there exist disjoint open sets $U$ and $V$ containing $A$ and $x$, respectively.
:::

::: {.solution}
::: pf

::: {.pf-step #pointwise}
For each $y \in A$, there are disjoint open sets $U_y \ni y$ and $V_y \ni x$.

::: pf-proof
Since $x \notin A$, we have $y \neq x$, and $X$ is Hausdorff.
:::

:::

::: {.pf-step #finite}
There are $y_1, \ldots, y_n \in A$ with $A \subseteq U_{y_1} \cup \cdots \cup U_{y_n}$.

::: pf-proof
By step [](#pointwise){.pf-ref}, the sets $U_y$, $y \in A$, form an open cover of $A$, and $A$ is compact.
If $A = \emptyset$, take $n = 0$.
:::

:::

::: pf-step
The sets $U \coloneqq \bigcup_{i=1}^n U_{y_i}$ and $V \coloneqq \bigcap_{i=1}^n V_{y_i}$, with $V = X$ when $n = 0$, are disjoint open sets with $A \subseteq U$ and $x \in V$.

::: pf-proof
$U$ is a union of open sets, and $V$ is a finite intersection of open sets, so both are open.
$A \subseteq U$ by step [](#finite){.pf-ref}, and $x \in V$ because $x \in V_{y_i}$ for each $i$.
For each $i$, $U_{y_i} \cap V \subseteq U_{y_i} \cap V_{y_i} = \emptyset$, so $U \cap V = \emptyset$.
:::

:::

:::
:::
