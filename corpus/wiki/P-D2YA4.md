---
schema: qual/card@1
id: P-D2YA4
kind: problem
title: $\ext(\ZZ\oplus\ZZ_2\oplus\ZZ_3,\ZZ\oplus\ZZ_4\oplus\ZZ_5)\cong\ZZ_{12}$
classification:
  areas:
  - topology
  topics:
  - homological-algebra
relations: []
review: draft
solved: false
---

::: problem
Facts Used:

1. $\ext(\ZZ, \ZZ_m) = \ZZ_m$

2. $\ext(\ZZ_m, \ZZ) = 0$

3. $\ext(\prod_i A_i, \prod_j B_j) = \prod_i \prod_j \ext(A_i, B_j)$

Break it up into a bigraded complex, take Ext of the pieces, and sum over the complex: $\ext(\downarrow, \rightarrow)$ | $\ZZ$   | $\ZZ_4$ | $\ZZ_5$ --------------------------------|---------|---------|-------- $\ZZ$                           | 0       | 0       | 0 $\ZZ_2$                         | $\ZZ_2$ | $\ZZ_2$ | 0 $\ZZ_3$                         | $\ZZ_3$ | 0       | 0

So the answer is $\ZZ_2 \times \ZZ_2 \times \ZZ_3 = \ZZ_{12}$.
$\qed$
:::
