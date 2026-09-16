---
schema: qual/card@1
id: FF-JXE7U
kind: fact
title: $\Hom_R(R,A)\cong A$
prompts:
- What is $\mathop{\mathrm{Hom}}_R(R, A)$ for a left $R$-module $A$?
classification:
  areas:
  - topology
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
---

::: {.fact}
Let $R$ be a ring with $1$ and $A$ a left $R$-module.
The map $\Hom_R(R, A)\to A$, $f\mapsto f(1)$, is an isomorphism of abelian groups, with inverse sending $a\in A$ to the homomorphism $r\mapsto ra$; if $R$ is commutative, it is an isomorphism of $R$-modules.
:::
