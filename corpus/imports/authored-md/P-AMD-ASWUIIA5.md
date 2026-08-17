---
schema: qual/card@1
id: P-AMD-ASWUIIA5
kind: problem
title: 'Given: $R$ a commutative ring, $G$ a finite group, $RG$ a group ring.'
classification:
  areas:
  - algebra
  topics:
  - group-rings
  - conjugacy
  - centralizers-and-normalizers
relations: []
review: draft
solved: false
---

::: {.problem}
Given: $R$ a commutative ring, $G$ a finite group, $RG$ a group ring.
- Given: $\mathcal{K} = \{ k_1, k_2, \cdots k_m\}$ a conjugacy class in $G$
   - Show: $$K = \sum_{i=1}^m k_i \in RG \implies K \in Z(RG)$$
- Given: $\mathcal{K}_1\cdots \mathcal{K}_r$ distinct conjugacy classes in $G$, $K_i = \sum_{j}k_j \ni k_j \in \mathcal{K}_i$
   - Show that
   $$
   Z(RG) = \{\sum a_l K_l : \forall 1 \leq l \leq r, a_l \in R \}
   $$
   (All $R$-linear combinations of the $\mathcal{K}_i$)
:::
