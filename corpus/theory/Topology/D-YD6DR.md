---
schema: qual/card@1
id: D-YD6DR
kind: definition
title: $R$-orientability
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
Let $R$ be a commutative ring with identity and $M$ an $n$-[[D-UBWVX|manifold]], and for $A\subseteq M$ write $H_n(M\mid A;R)\coloneqq H_n(M, M\sm A; R)$, so that $H_n(M\mid x;R)\cong R$ for $x\in M$.
An \dfn{$R$-orientation} of $M$ is a function $x\mapsto\mu_x$ assigning to each $x\in M$ a generator $\mu_x$ of the $R$-module $H_n(M\mid x;R)$ that is locally consistent: each $x\in M$ has a neighborhood $\RR^n\subseteq M$ containing an open ball $B$ of finite radius about $x$ and an element $\mu_B\in H_n(M\mid B;R)$ whose image under the map $H_n(M\mid B;R)\to H_n(M\mid y;R)$ induced by inclusion is $\mu_y$ for every $y\in B$.
The manifold $M$ is \dfn{$R$-orientable} if it has an $R$-orientation.
:::

::: {.proposition}
Let $M$ be an $n$-manifold.

(a) $M$ is $\ZZ/2$-orientable.

(b) If $M$ is [[D-YCPJX|orientable]], then $M$ is $R$-orientable for every commutative ring $R$ with identity.

(c) If $R$ is a commutative ring with identity in which $2\neq 0$, then $M$ is $R$-orientable if and only if $M$ is orientable.
:::

::: {.concept}
[@Hat02].
:::
