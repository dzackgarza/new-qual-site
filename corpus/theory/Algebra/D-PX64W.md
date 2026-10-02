---
schema: qual/card@1
id: D-PX64W
kind: definition
title: Centralizer of an element or subset
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Conjugacy
  - Group Actions
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group and $h\in G$.
The \dfn{centralizer} of $h$ is
$$
Z(h) \coloneqq C_G(h) \coloneqq \theset{ g\in G \st ghg^{-1} = h }.
$$
For a subset $H\subseteq G$, the \dfn{centralizer} of $H$ is
$$
Z(H) \coloneqq C_G(H) \coloneqq \theset{g\in G \suchthat ghg^{-1} = h \text{ for all } h\in H} = \Intersect_{h\in H} C_G(h).
$$
:::

::: {.remark}
For the action of $G$ on itself by conjugation, $C_G(h)$ is the stabilizer of $h$, and $C_G(H)$ is the subgroup of elements that fix every element of $H$.
:::
