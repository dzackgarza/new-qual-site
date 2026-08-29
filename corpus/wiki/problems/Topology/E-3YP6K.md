---
schema: qual/card@1
id: E-3YP6K
kind: exercise
title: Compact subsets of Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that if $X$ is Hausdorff and $A\subseteq X$ is compact then $A$ is closed.
:::

::: solution
**Goal:** Prove that every compact subset $A$ of a Hausdorff topological space $X$ is closed in $X$.

<1>1. Strategy: We show that the complement $X \setminus A$ is an open subset of $X$ by constructing an open neighborhood around each point $x \in X \setminus A$ that is disjoint from $A$.

<1>2. Construction of separating neighborhoods: *Proof:* <2>1. Let $x \in X \setminus A$.
<2>2. For every $y \in A$, we have $x \neq y$.
Since $X$ is Hausdorff ($T_2$), there exist open sets $U_y, V_y \subseteq X$ such that $y \in U_y$, $x \in V_y$, and $U_y \cap V_y = \emptyset$.
<2>3. The collection $\{U_y\}_{y \in A}$ is an open cover of $A$ in $X$.
<2>4. Since $A$ is compact, there exists a finite subcover $\{U_{y_1}, \dots, U_{y_n}\}$ such that: $$A \subseteq \bigcup_{i=1}^n U_{y_i}.$$ <2>5. Define $V = \bigcap_{i=1}^n V_{y_i}$.
<2>6. As a finite intersection of open sets containing $x$, $V$ is an open neighborhood of $x$ in $X$.

<1>3. Disjointness of $V$ and $A$: *Proof:* <2>1. For each $i \in \{1, \dots, n\}$, $V \subseteq V_{y_i}$, so $V \cap U_{y_i} \subseteq V_{y_i} \cap U_{y_i} = \emptyset$.
<2>2. Therefore: $$V \cap A \subseteq V \cap \left(\bigcup_{i=1}^n U_{y_i}\right) = \bigcup_{i=1}^n (V \cap U_{y_i}) = \emptyset.$$ <2>3. Thus $V \subseteq X \setminus A$.

<1>4. Conclusion: Every point $x \in X \setminus A$ has an open neighborhood $V \subseteq X \setminus A$.
Hence $X \setminus A$ is open in $X$, so $A$ is closed in $X$.
Q.E.D.
:::
