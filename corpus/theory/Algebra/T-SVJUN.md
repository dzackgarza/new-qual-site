---
schema: qual/card@1
id: T-SVJUN
kind: theorem
title: Recognizing internal direct products
slogan: 'Normal complementary factors with trivial intersection form a direct product.'
prompts:
- What conditions on subgroups $H, K \leq G$ give $G \cong H \times K$?
classification:
  areas:
  - algebra
  topics:
  - Direct Products
  - Normal Subgroups
  - Subgroups
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

::: {.proof}
For $h\in H$ and $k\in K$, the commutator $hkh^{-1}k^{-1}$ lies in $K$ because $K$ is normal and in $H$ because $H$ is normal, so it is $e$ and $hk=kh$.
Hence $(h,k)(h',k')=(hh',kk')\mapsto hh'kk'=hkh'k'$, and the map is a homomorphism.
Its kernel consists of the pairs with $hk=e$, so $h=k^{-1}\in H\cap K=\theset{e}$, and the map is injective.
It is surjective because $HK=G$.
:::

::: {.remark}
Hypothesis 1 may be replaced by the condition that $hk=kh$ for all $h\in H$ and $k\in K$: together with $G=HK$, this condition implies that $H$ and $K$ are [[D-EKE4Q|normal]] in $G$.
:::
