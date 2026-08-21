---
schema: qual/card@1
id: E-XFXGM
kind: exercise
title: Product metrics, finite and countable
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

::: {.exercise title="Munkres §21.3"}


Let $X_n$ be a metric space with metric $d_n$, for $n \in \mathbb{Z}_+$.

(a) Show that

$$
\rho(x, y) = \max\ts{d_1(x_1, y_1), \dots, d_n(x_n, y_n)}
$$

is a metric for the product space $X_1 \times \cdots \times X_n$.

(b) Let $\bar{d}_i = \min\ts{d_i, 1}$. Show that

$$
D(x, y) = \sup\ts{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $\prod X_i$.
:::
