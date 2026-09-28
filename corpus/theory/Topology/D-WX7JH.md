---
schema: qual/card@1
id: D-WX7JH
kind: definition
title: Orientation cover
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Covering Spaces
  - Manifolds
relations: []
review: draft
---

::: {.definition}
Let $M$ be an $n$-[[D-UBWVX|manifold]], and for $A\subseteq M$ write $H_n(M\mid A) \coloneqq H_n(M, M\sm A;\ZZ)$.
The \dfn{orientation double cover} of $M$ is the set $\tilde M$ of all [[D-6CI7D|local orientations]] $\mu_x$ of $M$ at points $x\in M$, with the map $p\colon\tilde M\to M$, $\mu_x\mapsto x$, and the topology with basis the sets
$$
U(\mu_B) \coloneqq \ts{ \mu_x \st x\in B,\ \mu_x \text{ the image of } \mu_B \text{ under } H_n(M\mid B)\to H_n(M\mid x) },
$$
where $B$ ranges over the open balls of finite radius in charts $\RR^n\subseteq M$ and $\mu_B$ over the generators of $H_n(M\mid B)\cong\ZZ$.
:::

::: {.proposition}
Let $M$ be an $n$-manifold with orientation double cover $p\colon\tilde M\to M$.
Then $p$ is a two-sheeted [[D-ANO2D|covering space]], and $\tilde M$ is an orientable $n$-manifold.
If $M$ is connected, then $M$ is orientable if and only if $\tilde M$ has two components.
:::

::: {.concept}
[@Hat02].
:::
