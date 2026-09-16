---
schema: qual/card@1
id: D-EILQL
kind: definition
title: Cochain
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $R$ a commutative ring, $p\geq 0$, and $C_p(X;R)$ the free $R$-module on the singular $p$-simplices $\sigma\colon\Delta^p\to X$.
A \dfn{$p$-cochain} on $X$ with coefficients in $R$ is an $R$-linear map $c\colon C_p(X;R)\to R$.
The $p$-cochains form the $R$-module $C^p(X;R)\coloneqq\Hom_R(C_p(X;R), R)$.
:::

::: {.remark}
Since $C_p(X;R)$ is free on the singular $p$-simplices, restriction to them identifies $C^p(X;R)$ with the $R$-module of all functions from the set of singular $p$-simplices of $X$ to $R$.
:::
