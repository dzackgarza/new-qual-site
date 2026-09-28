---
schema: qual/card@1
id: D-XEDSI
kind: definition
title: Upper central series
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

::: {.definition}
Let $G$ be a group.
Define normal subgroups $Z_i\normal G$ inductively by $Z_0\coloneqq 1$ and, for $i\geq 0$,
$$
Z_{i+1}\coloneqq \pi_i^{-1}\bigl(Z(G/Z_i)\bigr),
$$
where $\pi_i\colon G\to G/Z_i$ is the quotient map and $Z(G/Z_i)$ is the [[D-NK7G7|center]] of $G/Z_i$.
The \dfn{upper central series} of $G$ is the chain $Z_0\leq Z_1\leq Z_2\leq\cdots$.
:::

::: {.remark}
The induction is well defined: if $Z_i\normal G$, then $Z(G/Z_i)$ is normal in $G/Z_i$, so its preimage $Z_{i+1}$ is normal in $G$.
$Z_{i+1}$ is the unique subgroup of $G$ containing $Z_i$ with $Z_{i+1}/Z_i=Z(G/Z_i)$; in particular $Z_1=Z(G)$.
:::
