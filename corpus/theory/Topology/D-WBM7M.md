---
schema: qual/card@1
id: D-WBM7M
kind: definition
title: Free module
classification:
  areas:
  - topology
  topics:
  - Modules
  - Bases
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
A left $R$-module $M$ is \dfn{free} if it has a [[D-I7D56|basis]].
:::

::: {.proposition}
Let $R$ be a ring, $M$ a left $R$-module, $S\subseteq M$ a subset, and $R^{(S)} \coloneqq \bigoplus_{s\in S} R$ with standard basis $(e_s)_{s\in S}$.
There is a unique $R$-linear map $\varphi\colon R^{(S)}\to M$ with $\varphi(e_s) = s$ for all $s\in S$.

(a) $\varphi$ is surjective if and only if $S$ is a [[D-DUCA5|generating set]] of $M$; in that case $M\cong R^{(S)}/\ker\varphi$.

(b) $\varphi$ is an isomorphism if and only if $S$ is a basis of $M$.
In particular, $M$ is free if and only if $M\cong R^{(T)}$ for some set $T$.
:::

::: {.concept}
[@DF04].
:::
