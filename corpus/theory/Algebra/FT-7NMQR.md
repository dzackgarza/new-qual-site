---
schema: qual/card@1
id: FT-7NMQR
kind: theorem
title: Recognition theorem for internal direct products
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
Let $G$ be a group and let $H,K\le G$ be [[D-EKE4Q|normal subgroups]] with $H\cap K=\theset{e}$ and $HK=G$.
Then the map
$$
H\times K\to G,\qquad(h,k)\mapsto hk,
$$
is an isomorphism of groups.
:::

::: {.proof}
For $h\in H$ and $k\in K$, the commutator $hkh^{-1}k^{-1}$ lies in $K$ because $K$ is normal and in $H$ because $H$ is normal, so it is $e$ and $hk=kh$.
Hence $(h,k)(h',k')=(hh',kk')\mapsto hh'kk'=hkh'k'$, and the map is a homomorphism.
Its kernel consists of the pairs with $hk=e$, so $h=k^{-1}\in H\cap K=\theset{e}$, and the map is injective.
It is surjective because $HK=G$.
:::
