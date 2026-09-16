---
schema: qual/card@1
id: D-R6LA3
kind: definition
title: Singular cochain
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $G$ an abelian group, and $n\geq0$.
Let $C_n(X)$ be the free abelian group on the singular $n$-simplices $\sigma\colon\Delta^n\to X$, as in [[D-6BUWA|singular homology]].
A \dfn{singular $n$-cochain} of $X$ with coefficients in $G$ is a homomorphism $\varphi\colon C_n(X)\to G$, and
$$
C^n(X;G)\coloneqq\Hom(C_n(X),G)
$$
is the group of singular $n$-cochains [@Hat02].
:::

::: {.remark}
Since $C_n(X)$ is free on the singular $n$-simplices, a singular $n$-cochain is the same as an arbitrary function assigning to each singular $n$-simplex $\sigma$ an element $\varphi(\sigma)\in G$, extended linearly: $\varphi\qty{\sum_in_i\sigma_i}=\sum_in_i\varphi(\sigma_i)$.
:::
