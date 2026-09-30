---
schema: qual/card@1
id: D-TS7TZ
kind: definition
title: Fundamental class
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Manifolds
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $M$ be a [[D-SYKQW|closed]] connected $n$-manifold with an [[D-CNLBT|orientation]] $x\mapsto\mu_x\in H_n(M,M\setminus\theset{x};\ZZ)$.
A \dfn{fundamental class} of $M$ is a class $[M]\in H_n(M;\ZZ)$ whose image under $H_n(M;\ZZ)\to H_n(M,M\setminus\theset{x};\ZZ)$ is $\mu_x$ for every $x\in M$.
:::

::: {.theorem}
Let $M$ be a closed connected $n$-manifold with an orientation $x\mapsto\mu_x$.
Then $H_n(M;\ZZ)\cong\ZZ$, the fundamental class $[M]$ exists and is unique, and it generates $H_n(M;\ZZ)$ [@Hat02].
:::
