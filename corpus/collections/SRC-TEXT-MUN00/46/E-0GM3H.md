---
schema: qual/card@1
id: E-0GM3H
kind: exercise
title: The fine topology on function spaces
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
---

::: {.exercise title="Munkres §46.11"}

Let $(Y, d)$ be a metric space; let $X$ be a space.
Define a topology on $\mathcal{C}(X, Y)$ as follows.
Given $f \in \mathcal{C}(X, Y)$, and given a positive continuous function $\delta: X \to \mathbb{R}_+$ on $X$, let

$$
B(f, \delta) = \ts{g \mid d(f(x), g(x)) < \delta(x) \text{ for all } x \in X}.
$$

(a) Show that the sets $B(f, \delta)$ form a basis for a topology on $\mathcal{C}(X, Y)$.
We call it the fine topology.

(b) Show that the fine topology contains the uniform topology.

(c) Show that if $X$ is compact, the fine and uniform topologies agree.

(d) Show that if $X$ is discrete, then $\mathcal{C}(X, Y) = Y^X$ and the fine and box topologies agree.
:::
