---
schema: qual/card@1
id: P-CH8-6
kind: problem
title: $\ZZ_8\oplus\ZZ_2\not\cong\ZZ_4\oplus\ZZ_4$
classification:
  areas:
    - algebra
  topics:
    - Direct Products
relations: []
review: draft
---

::: {.problem}
Prove, by comparing orders of elements, that $\ZZ_{8} \oplus \ZZ_{2}$ is not isomorphic to $\ZZ_{4} \oplus \ZZ_{4}$.
:::

::: {.solution}
Notice that $\ZZ _ { 8 } \oplus \ZZ _ { 2 }$ has an element of order 8, namely (1, 1), but $\ZZ _ { 4 } \oplus \ZZ _ { 4 }$ can not have an element of order 8 since the orders in $\ZZ _ { 4 }$ are 1, 2, and 4. (There is no way to get a least common multiple of 8 from 1, 2, and 4.)
:::

::: {.remark}
Certificate. `proofs/cards/CH8DirectProduct.g` (`P-CH8-6`) computes the
element-order multisets of both groups in GAP: $\ZZ_{8}\oplus\ZZ_{2}$ has one
element of order $8$ and four of order $4$, $\ZZ_{4}\oplus\ZZ_{4}$ has none of
order $8$ and twelve of order $4$, so the multisets differ and the groups are
not isomorphic.
:::
