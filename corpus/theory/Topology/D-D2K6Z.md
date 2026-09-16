---
schema: qual/card@1
id: D-D2K6Z
kind: definition
title: Coboundary
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $G$ an abelian group, and let $C^n(X;G)\coloneqq\Hom(C_n(X), G)$ be the group of $n$-cochains, where $C_n(X)$ is the group of [[D-6BUWA|singular $n$-chains]] with boundary map $\del_n\colon C_n(X)\to C_{n-1}(X)$.
The \dfn{coboundary map} $\delta^n\colon C^n(X;G)\to C^{n+1}(X;G)$ is $\delta^n(\varphi)\coloneqq\varphi\circ\del_{n+1}$.
An $n$-cochain $\varphi$ is a \dfn{coboundary} if $\varphi\in B^n(X;G)\coloneqq\im\delta^{n-1}$, with $B^0(X;G)\coloneqq 0$.
:::

::: {.proposition}
For every $n\geq 0$, $\delta^{n+1}\circ\delta^n = 0$; hence $B^{n+1}(X;G)\subseteq\ker\delta^{n+1}$.
:::

::: {.proof}
For $\varphi\in C^n(X;G)$, $\delta^{n+1}\delta^n\varphi = \varphi\circ\del_{n+1}\circ\del_{n+2} = 0$ since $\del_{n+1}\circ\del_{n+2} = 0$.
:::

::: {.concept}
See [@Hat02, §3.1, p. 198].
:::
