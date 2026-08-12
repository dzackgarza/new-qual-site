---
schema: qual/card@1
id: D-NRRIT
kind: definition
title: "Quadratic Form"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.definition title="Quadratic Form"}
A function $q: V\to k$ on a $k\dash$vector space with $q(\lambda x) = \lambda^2 q(x)$ for all $\lambda\in k$ and such that
\[
b_q(x, y) \da q(x+y) - q(x) - q(y)
\]
is bilinear.
When $\ch k \neq 2$ this is the same data as a symmetric bilinear form, via $q(x) = b(x,x)$ and $b = \frac12 b_q$.
In coordinates $q$ is a homogeneous degree-$2$ polynomial, $q(x) = \sum_{i \leq j} a_{ij} x_i x_j$.
:::

:::{.concept}
See Artin, *Algebra*, ch. 8.
:::
