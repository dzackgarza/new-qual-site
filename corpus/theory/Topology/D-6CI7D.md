---
schema: qual/card@1
id: D-6CI7D
kind: definition
title: Local orientation and orientation of a manifold
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
For $x\in M$, excision gives $H_n(M\mid x)\cong H_n(\RR^n, \RR^n\sm\ts{0};\ZZ)\cong\ZZ$.

- A \dfn{local orientation} of $M$ at $x$ is a generator $\mu_x$ of $H_n(M\mid x)$.

- An \dfn{orientation} of $M$ is a function $x\mapsto\mu_x$ assigning to each $x\in M$ a local orientation at $x$, such that each $x\in M$ has an open neighborhood $U\subseteq M$ with a homeomorphism $U\cong\RR^n$ and an open ball $B\subseteq U$ of finite radius containing $x$, together with a generator $\mu_B$ of $H_n(M\mid B)\cong\ZZ$ whose image under the map $H_n(M\mid B)\to H_n(M\mid y)$ induced by inclusion is $\mu_y$ for every $y\in B$.

- $M$ is \dfn{orientable} if an orientation of $M$ exists.
:::

::: {.remark}
Each $H_n(M\mid x)$ has exactly two generators, so $M$ has exactly two local orientations at each point.
The local orientations form the orientation double cover $\tilde M = \ts{\mu_x \st x\in M,\ \mu_x \text{ a local orientation of } M \text{ at } x}$, with $\mu_x\mapsto x$.
The manifold $\tilde M$ is orientable, and a connected manifold $M$ is orientable if and only if $\tilde M$ has two components [@Hat02, §3.3].
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
[@Hat02, §3.3, p. 234].
:::
