---
schema: qual/card@1
id: P-JWPNL
kind: problem
title: Simple groups; no simple group of order $56$
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Define a *simple group*. Prove that a group of order 56 can not be simple.
:::

::: {.solution}
A group $G$ is **simple** if $G\ne1$ and its only normal subgroups are $1$ and $G$.

Let $|G|=56=2^3\cdot7$. The number $n_7$ of Sylow $7$-subgroups satisfies
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid8,
\]
so $n_7=1$ or $8$. If $n_7=1$, the Sylow $7$-subgroup is normal and $G$ is not simple.

Assume $n_7=8$. Distinct subgroups of order $7$ intersect trivially, so their nonidentity elements are disjoint. Thus the eight Sylow $7$-subgroups contain
\[
8(7-1)=48
\]
nonidentity elements. Including the identity, this accounts for $49$ elements, leaving exactly $7$ nonidentity elements outside the Sylow $7$-subgroups.

A Sylow $2$-subgroup has order $8$, hence has exactly $7$ nonidentity elements, none of which can lie in a subgroup of order $7$. Therefore every Sylow $2$-subgroup consists of the identity together with precisely those same $7$ remaining elements. Hence the Sylow $2$-subgroup is unique and therefore normal. Again $G$ is not simple.

Thus no group of order $56$ is simple.
:::
