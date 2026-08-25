---
schema: qual/card@1
id: E-OD5RT
kind: exercise
title: Countable products of compact metrizable spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise title="Munkres §45.1"}

If $X_n$ is metrizable with metric $d_n$, then

$$
D(\mathbf{x}, \mathbf{y}) = \sup\ts{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $X = \prod X_n$.
Show that $X$ is totally bounded under $D$ if each $X_n$ is totally bounded under $d_n$.
Conclude without using the Tychonoff theorem that a countable product of compact metrizable spaces is compact.
:::
