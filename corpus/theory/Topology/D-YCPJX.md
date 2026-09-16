---
schema: qual/card@1
id: D-YCPJX
kind: definition
title: Orientation of a manifold
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
Let $M$ be an $n$-[[D-UBWVX|manifold]], and for $A\subseteq M$ write $H_n(M\mid A)\coloneqq H_n(M, M\sm A;\ZZ)$.
An \dfn{orientation} of $M$ is a function $x\mapsto\mu_x$ assigning to each $x\in M$ a [[D-6CI7D|local orientation]] $\mu_x$, a generator of $H_n(M\mid x)\cong\ZZ$, that is locally consistent: each $x\in M$ has a neighborhood $\RR^n\subseteq M$ containing an open ball $B$ of finite radius about $x$ and a generator $\mu_B$ of $H_n(M\mid B)$ such that for every $y\in B$, $\mu_y$ is the image of $\mu_B$ under the map $H_n(M\mid B)\to H_n(M\mid y)$ induced by inclusion.
The manifold $M$ is \dfn{orientable} if it has an orientation.
:::

::: {.proposition}
Let $M$ be a connected $n$-manifold with [[D-WX7JH|orientation double cover]] $p\colon\tilde M\to M$, and let $x\in M$.
The following are equivalent:

(a) $M$ is orientable.

(b) $\tilde M$ is disconnected.

(c) $\tilde M$ has two components, each mapped homeomorphically onto $M$ by $p$.

(d) $p$ has a continuous section $s\colon M\to\tilde M$, $p\circ s = \id_M$.

(e) The homomorphism $\pi_1(M, x)\to\ZZ/2$ given by the action of $\pi_1(M,x)$ on the two-point fiber $p\inv(x)$ is trivial.
:::

::: {.concept}
[@Hat02, §3.3, pp. 234--235, Proposition 3.25].
:::
