---
schema: qual/card@1
id: D-OH4ON
kind: definition
title: Cycle
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, let $C_n(X)$ be the group of [[D-6BUWA|singular $n$-chains]] of $X$, and let $\del_n\colon C_n(X)\to C_{n-1}(X)$ be the boundary map.
An $n$-chain $\alpha\in C_n(X)$ is an \dfn{$n$-cycle} if $\del_n\alpha=0$ [@Hat02].
The $n$-cycles form the subgroup $Z_n(X)\coloneqq\ker\del_n$.
:::

::: {.remark}
With $B_n(X)\coloneqq\im\del_{n+1}$ the group of $n$-boundaries, the relation $\del_n\circ\del_{n+1}=0$ gives $B_n(X)\subseteq Z_n(X)$, and the singular homology group is $H_n(X)=Z_n(X)/B_n(X)$.
:::
