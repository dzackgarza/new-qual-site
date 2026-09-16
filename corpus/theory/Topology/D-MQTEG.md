---
schema: qual/card@1
id: D-MQTEG
kind: definition
title: Cocycle
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $G$ an abelian group.
Let $C^n(X;G)\coloneqq\Hom(C_n(X),G)$ be the group of singular [[D-EILQL|$n$-cochains]], where $C_n(X)$ is the group of [[D-6BUWA|singular $n$-chains]] with boundary map $\del_{n+1}\colon C_{n+1}(X)\to C_n(X)$, and let $\delta^n\colon C^n(X;G)\to C^{n+1}(X;G)$ be the coboundary map $\delta^n\psi\coloneqq\psi\circ\del_{n+1}$.
An $n$-cochain $\psi\in C^n(X;G)$ is an \dfn{$n$-cocycle} if $\delta^n\psi=0$ [@Hat02, p. 198].
The $n$-cocycles form the subgroup $Z^n(X;G)\coloneqq\ker\delta^n$.
:::

::: {.proposition}
An $n$-cochain $\psi\in C^n(X;G)$ is a cocycle if and only if $\psi(b)=0$ for every boundary $b\in\im\del_{n+1}$.
:::

::: {.proof}
$\delta^n\psi=\psi\circ\del_{n+1}$ is zero exactly when $\psi$ vanishes on $\im\del_{n+1}$.
:::

::: {.remark}
With $B^n(X;G)\coloneqq\im\delta^{n-1}$ the group of [[D-D2K6Z|coboundaries]], the relation $\delta^n\circ\delta^{n-1}=0$ gives $B^n(X;G)\subseteq Z^n(X;G)$, and the singular cohomology group is $H^n(X;G)=Z^n(X;G)/B^n(X;G)$.
:::
