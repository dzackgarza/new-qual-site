---
schema: qual/card@1
id: P-TOPS10E
kind: problem
title: "Euler characteristic equals mod-2 Euler characteristic via UCT"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Universal Coefficient Theorem
  - Homology
relations: []
review: draft
solved: false
---

::: problem
For any topological space $X$, whose total homology is a finitely-generated abelian group, let $\chi(X)$ denote the usual Euler characteristic
$$
\chi(X) = \sum_i (-1)^i \dim_{\mathbb{Q}} H_i(X; \mathbb{Q})
$$
and let $\chi_2(X)$ be the "mod-$2$ homology Euler characteristic"
$$
\chi_2(X) = \sum_i (-1)^i \dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2).
$$
Use the universal coefficient theorem to show that $\chi(X) = \chi_2(X)$.
:::
