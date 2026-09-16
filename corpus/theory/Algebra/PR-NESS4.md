---
schema: qual/card@1
id: PR-NESS4
kind: proposition
title: 'N/C theorem: $N_G(H)/C_G(H)$ embeds in $\Aut(H)$'
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Automorphisms
  - Isomorphism Theorems
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a group and $H\leq G$ a subgroup, with [[D-OZ2RR|normalizer]] $N_G(H)$ and [[D-PX64W|centralizer]] $C_G(H)$.
The map $c\colon N_G(H)\to\Aut(H)$, $c(g)(h)=ghg^{-1}$, is a group homomorphism with kernel $C_G(H)$.
Hence $C_G(H)\normal N_G(H)$ and $c$ induces an injective homomorphism
$$
N_G(H)/C_G(H)\hookrightarrow\Aut(H).
$$
:::

::: {.proof}
For $g\in N_G(H)$ we have $gHg^{-1}=H$, so $c(g)$ is a bijection $H\to H$, and $c(g)(hh')=ghg^{-1}gh'g^{-1}=c(g)(h)\,c(g)(h')$; thus $c(g)\in\Aut(H)$.
Since $c(gg')(h)=gg'h(gg')^{-1}=c(g)(c(g')(h))$, the map $c$ is a homomorphism.
Its kernel is $\theset{g\in N_G(H)\suchthat ghg^{-1}=h\ \forall h\in H}=C_G(H)$.
The first isomorphism theorem gives $N_G(H)/C_G(H)\cong c(N_G(H))\leq\Aut(H)$.
:::
