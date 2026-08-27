---
schema: qual/card@1
id: E-Q7W4S
kind: exercise
title: Separate continuity does not imply continuity
subtitle: Munkres §18.12
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Let $F: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ be defined by the equation

$$
F(x \times y) =
\begin{cases}
xy/(x^2 + y^2) & \text{if } x \times y \neq 0 \times 0, \\
0 & \text{if } x \times y = 0 \times 0.
\end{cases}
$$

(a) Show that $F$ is continuous in each variable separately.

(b) Compute the function $g: \mathbb{R} \to \mathbb{R}$ defined by $g(x) = F(x \times x)$.

(c) Show that $F$ is not continuous.
:::
