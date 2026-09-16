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

::: {.proof}
Let $\mu$ be an orientation of $M$.
Then $x\mapsto-\mu_x$ is an orientation, distinct from $\mu$ since $\mu_x\neq-\mu_x$ in $\ZZ$.
Let $\nu$ be any orientation.
For $x\in M$ choose a ball $B$ about $x$ inside the balls given by the consistency conditions for $\mu$ and $\nu$; for a ball $B'\supseteq B$ in the same chart, $H_n(M, M\sm B';\ZZ)\to H_n(M, M\sm B;\ZZ)\to H_n(M, M\sm\ts{y};\ZZ)$ are isomorphisms for $y\in B$, so $\mu$ and $\nu$ restrict from generators $\mu_B, \nu_B$ of $H_n(M, M\sm B;\ZZ)\cong\ZZ$.
Then $\nu_B = \pm\mu_B$, so the sign $\varepsilon(y)\in\ts{\pm1}$ with $\nu_y = \varepsilon(y)\mu_y$ is constant on $B$.
Thus $\varepsilon\colon M\to\ts{\pm1}$ is locally constant, hence constant on the connected space $M$, and $\nu = \mu$ or $\nu = -\mu$.
:::

::: {.theorem}
Let $M$ be a closed connected oriented $n$-manifold with orientation $\mu$.
There is a unique class $[M]\in H_n(M;\ZZ)$ whose image in $H_n(M, M\sm\ts{x};\ZZ)$ is $\mu_x$ for every $x\in M$, and $[M]$ generates $H_n(M;\ZZ)\cong\ZZ$.
:::

::: {.remark}
The class $[M]$ is the [[D-TS7TZ|fundamental class]] of $M$.
:::

::: {.concept}
See [@Hat02, §3.3, pp. 234 and 236, Theorem 3.26].
:::
