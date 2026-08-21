---
schema: qual/card@1
id: D-XEDSI
kind: definition
title: Upper Central Series
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Nilpotent Groups
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.definition title="Upper Central Series"}
Set $Z_0 = 1$, $Z_1 = Z(G)$, and $Z_{i+1} \leq G$ to be the subgroup satisfying $Z_{i+1}/Z_i = Z(G/Z_i)$.
Then $Z_0 \leq Z_1 \leq \cdots$ is the *upper central series* of $G$.

Equivalently, since $Z_i\normal G$, there is a quotient map $\pi:G\to G/Z_i$, so define $Z_{i+1} \definedas \pi\inv(Z(G/Z_i))$ (?).

> Mnemonic: "upper" because the chain is ascending.
> "Take higher centers".
:::
