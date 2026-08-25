---
schema: qual/card@1
id: E-01BSA
kind: exercise
title: Isometries of compact metric spaces are surjective
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise title="Munkres §28.6"}

Let $(X, d)$ be a metric space.
If $f: X \to X$ satisfies the condition

$$
d(f(x), f(y)) = d(x, y)
$$

for all $x, y \in X$, then $f$ is called an isometry of $X$.
Show that if $f$ is an isometry and $X$ is compact, then $f$ is bijective and hence a homeomorphism.
[Hint: If $a \notin f(X)$, choose $\epsilon$ so that the $\epsilon$-neighborhood of $a$ is disjoint from $f(X)$. Set $x_1 = a$, and $x_{n+1} = f(x_n)$ in general. Show that $d(x_n, x_m) \geq \epsilon$ for $n \neq m$.]
:::
