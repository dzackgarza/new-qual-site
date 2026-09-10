---
schema: qual/card@1
id: P-PUOMT
kind: problem
title: Normal subgroups of $p$-groups meet the center nontrivially
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
---

::: problem
Let $G$ be a finite $p$-group and let $1\ne N\trianglelefteq G$. Prove that
\[
N\cap Z(G)\ne\{e\}.
\]
:::

::: {.solution}
Let $G$ act on $N$ by conjugation. This is well-defined because $N$ is normal. The fixed points are precisely
\[
N\cap Z(G).
\]
Every non-fixed orbit has size
\[
[G:C_G(x)],
\]
a positive power of $p$, hence divisible by $p$.

The class equation for the action gives
\[
|N|
=
|N\cap Z(G)|
+
\sum \text{(non-fixed orbit sizes)}.
\]
Since $N$ is a nontrivial subgroup of a $p$-group, $p\mid|N|$. Therefore
\[
p\mid |N\cap Z(G)|,
\]
so $N\cap Z(G)$ is nontrivial.
:::
