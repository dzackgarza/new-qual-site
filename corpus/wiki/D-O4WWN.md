---
schema: qual/card@1
id: D-O4WWN
kind: definition
title: "Nondegenerate Bilinear Form"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.definition title="Nondegenerate Bilinear Form"}
A bilinear form $b: V\cross V \to k$ is **nondegenerate** iff its adjoint map
\[
V &\to V\dual \\
x &\mapsto b(x, \wait)
\]
is injective, equivalently an isomorphism when $\dim_k V < \infty$.
Equivalently, the radical $\ts{ x \in V \st b(x,y) = 0 \text{ for all } y \in V }$ is zero, equivalently any Gram matrix of $b$ is invertible.
:::

::: {.concept}
See Artin, *Algebra*, ch. 8.
:::
