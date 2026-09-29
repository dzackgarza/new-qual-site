---
schema: qual/card@1
id: E-5GHY2
kind: problem
title: Projections with compact factor are closed maps
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $Y$ is compact, then the projection $\pi_1: X \times Y \to X$ is a closed map.
:::

::: {.solution}
**Goal:** Prove that if $Y$ is a compact topological space, then the canonical projection $\pi_1: X \times Y \to X$ is a closed map (Kuratowski's projection theorem / Tube Lemma).

::: pf

::: pf-step
Setting and reduction to complement:
Let $C \subseteq X \times Y$ be a closed set.
We must show that $\pi_1(C)$ is closed in $X$, or equivalently, that $X \setminus \pi_1(C)$ is open in $X$.
:::

::: {.pf-step #tube-lemma-application}
Application of the Tube Lemma:
Let $x_0 \in X \setminus \pi_1(C)$.
Then the entire slice $\{x_0\} \times Y$ is contained in the open set $W = (X \times Y) \setminus C$.
There exists an open neighborhood $U \subseteq X$ of $x_0$ such that $U \times Y \subseteq W$.

::: pf-proof

::: pf-step
For each $y \in Y$, $(x_0, y) \in W$.
:::

::: pf-step
By definition of the product topology, there exist open sets $U_y \subseteq X$ and $V_y \subseteq Y$ such that $(x_0, y) \in U_y \times V_y \subseteq W$.
:::

::: pf-step
The family $\{V_y\}_{y \in Y}$ is an open cover of the compact space $Y$.
:::

::: pf-step
Hence there exists a finite subcover $\{V_{y_1}, \dots, V_{y_k}\}$ of $Y$.
:::

::: pf-step
Define $U = \bigcap_{i=1}^k U_{y_i}$. As a finite intersection of open neighborhoods of $x_0$, $U$ is an open neighborhood of $x_0$ in $X$.
:::

::: pf-step
For each $i \in \{1, \dots, k\}$, $U \times V_{y_i} \subseteq U_{y_i} \times V_{y_i} \subseteq W$.
:::

::: pf-step
Taking the union over $i = 1, \dots, k$:
$$U \times Y = U \times \left( \bigcup_{i=1}^k V_{y_i} \right) = \bigcup_{i=1}^k (U \times V_{y_i}) \subseteq W.$$
:::

:::

:::

::: pf-step
Openness of the complement:

::: pf-proof

::: pf-step
By step [](#tube-lemma-application){.pf-ref}, $(U \times Y) \cap C = \varnothing$.
:::

::: pf-step
Projecting to $X$, no point of $U$ can be the first coordinate of any point in $C$, so $U \cap \pi_1(C) = \varnothing$.
:::

::: pf-step
Thus $x_0 \in U \subseteq X \setminus \pi_1(C)$.
:::

::: pf-step
Since $x_0$ was an arbitrary point of $X \setminus \pi_1(C)$, the set $X \setminus \pi_1(C)$ is open in $X$.
:::

:::

:::

::: pf-step
Conclusion:
$\pi_1(C)$ is closed in $X$, so $\pi_1$ is a closed map. Q.E.D.
:::

:::

:::
