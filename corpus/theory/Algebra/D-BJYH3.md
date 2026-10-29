---
schema: qual/card@1
id: D-BJYH3
kind: definition
title: Exact sequences
classification:
  areas:
  - algebra
  - topology
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
A sequence of $R$-modules and $R$-linear maps
$$
M_0 \mapsvia{f_1} M_1 \mapsvia{f_2} \cdots \mapsvia{f_n} M_n
$$
is \dfn{exact} at $M_i$, for $0 < i < n$, if $\im f_i = \ker f_{i+1}$; it is \dfn{exact} if it is exact at $M_i$ for every $0 < i < n$.
:::

::: {.remark title="Variations"}
The same definition applies to a sequence indexed by $\ZZ$ or by an infinite interval of $\ZZ$,
$$
\cdots\to A_{n+1}\mapsvia{d_{n+1}}A_n\mapsvia{d_n}A_{n-1}\to\cdots:
$$
it is exact at $A_n$ if $\im d_{n+1}=\ker d_n$, and exact if it is exact at every term that has both an incoming and an outgoing map [@Hat02].
:::

::: {.remark}
The sequence is a chain complex when $\im d_{n+1}\subseteq\ker d_n$ for all $n$.
A chain complex is exact at $A_n$ if and only if its homology $\ker d_n/\im d_{n+1}$ at $A_n$ is zero.
:::

::: {.example}
A sequence of $R$-module maps
$$
0 \mapsvia{d_1} A \mapsvia{d_2} B \mapsvia{d_3} C \mapsvia{d_4} 0
$$
is exact if and only if $\im d_i = \ker d_{i+1}$ for $i = 1, 2, 3$, that is, if and only if $d_2$ is injective, $\im d_2 = \ker d_3$, and $d_3$ is surjective.
:::
