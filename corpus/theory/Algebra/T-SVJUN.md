---
schema: qual/card@1
id: T-SVJUN
kind: theorem
title: Recognizing internal direct products
classification:
  areas:
  - algebra
  topics:
  - Direct Products
  - Normal Subgroups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group with subgroups $H$ and $K$ such that

1. $H, K \normal G$,

2. $G = HK$, and

3. $H\intersect K = \theset{e}$.

Then the map $H \times K\to G$, $(h,k)\mapsto hk$, is an isomorphism, so $G \cong H \times K$.
:::

::: {.remark}
Hypothesis 1 may be replaced by the condition that $hk=kh$ for all $h\in H$ and $k\in K$: together with $G=HK$, this condition implies that $H$ and $K$ are [[D-EKE4Q|normal]] in $G$.
:::
