---
schema: qual/card@1
id: D-CNLBT
kind: definition
title: Oriented manifold
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
Let $M$ be an $n$-[[D-UBWVX|manifold]].
An \dfn{orientation} of $M$ is a function $x\mapsto\mu_x$ assigning to each $x\in M$ a [[D-6CI7D|local orientation]] $\mu_x$, a generator of $H_n(M, M\sm\ts{x};\ZZ)\cong\ZZ$, such that every $x\in M$ has an open ball neighborhood $B$ of finite radius in a chart $\RR^n\subseteq M$ and a class $\mu_B\in H_n(M, M\sm B;\ZZ)$ whose image under the map $H_n(M, M\sm B;\ZZ)\to H_n(M, M\sm\ts{y};\ZZ)$ induced by inclusion is $\mu_y$ for every $y\in B$.
An \dfn{oriented manifold} is a pair consisting of a manifold and an orientation of it.
The manifold $M$ is \dfn{orientable} if an orientation of $M$ exists.
:::

::: {.proposition}
A nonempty connected orientable $n$-manifold has exactly two orientations.
:::

::: {.theorem}
Let $M$ be a closed connected oriented $n$-manifold with orientation $\mu$.
There is a unique class $[M]\in H_n(M;\ZZ)$ whose image in $H_n(M, M\sm\ts{x};\ZZ)$ is $\mu_x$ for every $x\in M$, and $[M]$ generates $H_n(M;\ZZ)\cong\ZZ$.
:::

::: {.remark}
The class $[M]$ is the [[D-TS7TZ|fundamental class]] of $M$.
:::

::: {.concept}
See [@Hat02, §3.3, pp. 234--236, Theorem 3.26].
:::
