---
schema: qual/card@1
id: FF-UBJ3S
kind: fact
title: Künneth isomorphism with free homology
prompts:
- State the Kunneth isomorphism in the torsion-free case.
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
---

::: {.fact}
Let $X, Y$ be CW complexes, let $R$ be a principal ideal domain, and suppose $H_i(X;R)$ is a free $R$-module for every $i$ (for example, $R$ a field).
Then for each $k$ the cross product gives an isomorphism
$$
\bigoplus_{i+j=k}H_{i}(X;R)\tensor_R H_{j}(Y;R) \xrightarrow{\ \sim\ } H_{k}(X\times Y;R)
$$
[@Hat02].
:::
