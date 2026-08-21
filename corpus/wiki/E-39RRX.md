---
schema: qual/card@1
id: E-39RRX
kind: exercise
title: Four topologies on l2 and the Hilbert cube
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §20.8"}

Let $X$ be the subset of $\mathbb{R}^\omega$ consisting of all sequences $\mathbf{x}$ such that $\sum x_i^2$ converges.
Then the formula

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

defines a metric on $X$.
(See Exercise 10.) On $X$ we have the three topologies it inherits from the box, uniform, and product topologies on $\mathbb{R}^\omega$.
We have also the topology given by the metric $d$, which we call the $\ell^2$-topology.

(a) Show that on $X$, we have the inclusions

$$
\text{box topology} \supset \ell^2\text{-topology} \supset \text{uniform topology}.
$$

(b) The set $\mathbb{R}^\infty$ of all sequences that are eventually zero is contained in $X$.
Show that the four topologies that $\mathbb{R}^\infty$ inherits as a subspace of $X$ are all distinct.

(c) The set

$$
H = \prod_{n \in \mathbb{Z}_+} [0, 1/n]
$$

is contained in $X$; it is called the Hilbert cube.
Compare the four topologies that $H$ inherits as a subspace of $X$.
:::
