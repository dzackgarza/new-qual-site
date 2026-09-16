---
schema: qual/card@1
id: D-STPAM
kind: definition
title: Exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring and let
$$
\cdots\to A_{n+1}\mapsvia{d_{n+1}}A_n\mapsvia{d_n}A_{n-1}\to\cdots
$$
be a sequence of $R$-modules and $R$-linear maps.
The sequence is \dfn{exact at $A_n$} if $\im d_{n+1}=\ker d_n$, and \dfn{exact} if it is exact at every term that has both an incoming and an outgoing map [@Hat02, p. 113].
:::

::: {.remark}
The sequence is a chain complex when $\im d_{n+1}\subseteq\ker d_n$ for all $n$.
A chain complex is exact at $A_n$ if and only if its homology $\ker d_n/\im d_{n+1}$ at $A_n$ is zero.
:::
