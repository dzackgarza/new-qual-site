---
schema: qual/card@1
id: P-YCLOT
kind: problem
title: "(Important) Classify all groups of order $p^2$."
classification:
  areas:
  - algebra
  topics:
  - classification
  - p-groups
  - abelian-groups
relations: []
review: draft
---

::: problem
- (**Important**) Classify all groups of order $p^2$.

  > Must be abelian since quotient is cyclic.
  > If there's an element of order $p^2$, cyclic, done.
  > Else every element $a\neq 1$ must have order $p$.
  > Then $\gens{a}\neq G$, so pick $b$ in its complement, it has order $p$.
  > Call these two subgroups $H, K$ Recognize direct products: abelian implies both are normal, $H \intersect K = \ts{1}$.
  > and $\size HK = \size H \size K / \size(H \intersect K) = p\cdot p/1 = p^2$
:::
