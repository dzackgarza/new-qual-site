---
schema: qual/card@1
id: P-L7SEG
kind: problem
title: Image, kernel, and injectivity of group homomorphisms
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Normal Subgroups
  - Homomorphisms
relations: []
review: draft
solved: false
---

::: problem
- Let $G_1, G_2$ be groups and $H_2 \leq G_2$ a subgroup.
  Suppose $\phi: G_1\to G_2$ is a group morphism.
  - Show that the image $\phi(G_1) \leq G_2$ is a subgroup of $G_2$
  - Show that the preimage $\phi\inv(H_2) \leq G_1$ is a subgroup of $G_1$, 
  - Show that the kernel $\ker \phi \normal G_1$ is a normal subgroup of $G_1$.
  - Prove that group morphisms *preserve coset structure* in the following sense:
  \[
  xH_1 = yH_1 \iff \phi(x)H_2 = \phi(y)H_2
  .\]
  - Prove the **first isomorphism theorem**: 
  $\phi$ is injective $\iff \ker \phi = \ts{ e_{G_1} }$.
:::
