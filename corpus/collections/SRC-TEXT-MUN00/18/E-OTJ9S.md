---
schema: qual/card@1
id: E-OTJ9S
kind: exercise
title: Coordinate slices are imbeddings
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Given $x_0 \in X$ and $y_0 \in Y$, show that the maps $f: X \to X \times Y$ and $g: Y \to X \times Y$ defined by

$$
f(x) = x \times y_0 \quad \text{and} \quad g(y) = x_0 \times y
$$

are imbeddings.
:::

::: {.solution}
<1>1. $f : X \to X \times Y$, $f(x) = (x, y_0)$ is injective.
Proof: if $f(x_1) = f(x_2)$ then $(x_1, y_0) = (x_2, y_0)$, so $x_1 = x_2$.

<1>2. $f$ is continuous.
Proof: the coordinate functions are $\pi_1 \circ f = \operatorname{id}_X$ (continuous) and $\pi_2 \circ f = \text{constant } y_0$ (continuous), so $f$ is continuous (a map into a product is continuous iff its coordinates are).

<1>3. $f$ is a homeomorphism onto its image $X \times \{y_0\}$.
Proof: the inverse is the projection $\pi_1$ restricted to $X \times \{y_0\}$, which is continuous.

<1>4. Hence $f$ is an imbedding.
Proof: <1>1–<1>3 (an imbedding is an injective continuous map that is a homeomorphism onto its image).

<1>5. The same argument shows $g : Y \to X \times Y$, $g(y) = (x_0, y)$ is an imbedding.
Proof: symmetric to <1>1–<1>4, using $\pi_2$ as the inverse.

<1>6. Q.E.D.
Proof: <1>4 and <1>5.
:::
