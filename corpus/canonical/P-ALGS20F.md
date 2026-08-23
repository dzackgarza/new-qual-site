---
schema: qual/card@1
id: P-ALGS20F
kind: problem
title: "Tensor product of finite field extensions is a field if and only if linear independence transfers"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
solved: false
---

::: problem
Let $F$ be a field with algebraic closure $\overline{F}$.
Let $F \subseteq K \subseteq \overline{F}$ and $F \subseteq L \subseteq \overline{F}$, where $K$ and $L$ are fields with $[K:F] < \infty$ and $[L:F] < \infty$.
Prove that the following conditions are equivalent:

(1) $K \otimes_F L$ is a field.

(2) Given any $F$-linearly independent elements $\alpha_1, \ldots, \alpha_m \in K$, then $\alpha_1, \ldots, \alpha_m$ are linearly independent over $L$.
:::
