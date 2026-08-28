---
schema: qual/card@1
id: E-20CHL
kind: exercise
title: Continuity implies separate continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $F: X \times Y \to Z$.
We say that $F$ is continuous in each variable separately if for each $y_0$ in $Y$, the map $h: X \to Z$ defined by $h(x) = F(x \times y_0)$ is continuous, and for each $x_0$ in $X$, the map $k: Y \to Z$ defined by $k(y) = F(x_0 \times y)$ is continuous.
Show that if $F$ is continuous, then $F$ is continuous in each variable separately.
:::

::: solution
**Goal:** Prove that joint continuity of a bivariate function $F: X \times Y \to Z$ implies separate continuity in each coordinate variable.

<1>1. Continuity of the slice embeddings:
    For any fixed $y_0 \in Y$, the slice injection $i_{y_0}: X \to X \times Y$ defined by $i_{y_0}(x) = (x, y_0)$ is continuous.
    Similarly, for any fixed $x_0 \in X$, the slice injection $j_{x_0}: Y \to X \times Y$ defined by $j_{x_0}(y) = (x_0, y)$ is continuous.
    *Proof:*
    <2>1. The coordinate projections of $i_{y_0}$ are $\pi_X \circ i_{y_0} = \operatorname{id}_X: X \to X$ and $\pi_Y \circ i_{y_0} = c_{y_0}: X \to Y$ (the constant function at $y_0$).
    <2>2. Both the identity map $\operatorname{id}_X$ and the constant function $c_{y_0}$ are continuous.
    <2>3. By the characteristic universal property of the product topology, a map into a product space is continuous if and only if each coordinate projection is continuous. Hence $i_{y_0}$ is continuous.
    <2>4. By the exact same reasoning on coordinate projections $\pi_X \circ j_{x_0} = c_{x_0}$ and $\pi_Y \circ j_{x_0} = \operatorname{id}_Y$, $j_{x_0}$ is continuous.

<1>2. Continuity of the restricted maps $h$ and $k$:
    *Proof:*
    <2>1. The map $h: X \to Z$ defined by $h(x) = F(x, y_0)$ is the composition $h = F \circ i_{y_0}$.
    <2>2. Since $i_{y_0}$ is continuous by <1>1 and $F: X \times Y \to Z$ is continuous by hypothesis, their composition $h = F \circ i_{y_0}$ is continuous.
    <2>3. The map $k: Y \to Z$ defined by $k(y) = F(x_0, y)$ is the composition $k = F \circ j_{x_0}$.
    <2>4. Since $j_{x_0}$ is continuous by <1>1 and $F$ is continuous, their composition $k = F \circ j_{x_0}$ is continuous.

<1>3. Conclusion:
    $F$ is continuous in each variable separately. Q.E.D.
:::
