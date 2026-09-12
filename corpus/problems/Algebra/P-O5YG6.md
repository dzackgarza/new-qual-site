---
schema: qual/card@1
id: P-O5YG6
kind: problem
title: Distinct Sylow subgroups intersect trivially; normal subgroups of $p$-groups
  meet the center
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - p-Groups
  - Centralizers and Normalizers
relations: []
review: draft
---

::: problem
1. Show that a Sylow $p_1$-subgroup and a Sylow $p_2$-subgroup intersect trivially when $p_1\ne p_2$.
2. Show that every nontrivial normal subgroup of a finite $p$-group intersects the center nontrivially.
:::

::: {.solution}
<1>1. Let $P_1$ and $P_2$ be $p_1$- and $p_2$-subgroups with $p_1\ne p_2$.
::: {.proof}
The order of $P_1\cap P_2$ divides both $|P_1|$, a power of $p_1$, and $|P_2|$, a power of $p_2$. Hence
\[
|P_1\cap P_2|=1,
\]
so $P_1\cap P_2=\{e\}$.
:::

<1>2. Let $G$ be a finite $p$-group and let $1\ne N\trianglelefteq G$.
::: {.proof}
Let $G$ act on $N$ by conjugation. Because $N$ is normal, this action is well-defined. Its fixed points are exactly
\[
N\cap Z(G).
\]
Every non-fixed orbit has size
\[
[G:C_G(x)],
\]
a positive power of $p$, hence is divisible by $p$. Therefore the class equation for this action gives
\[
|N|\equiv |N\cap Z(G)|\pmod p.
\]
Since $N$ is a nontrivial subgroup of a $p$-group, $p\mid |N|$. Hence
\[
p\mid |N\cap Z(G)|.
\]
Thus $N\cap Z(G)$ contains more than the identity.
:::
:::
