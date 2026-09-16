---
schema: qual/card@1
id: PR-WDPF7
kind: proposition
title: Orthogonal complement of a sum of subspaces
classification:
  areas:
  - algebra
  topics:
  - Inner Product Spaces
  - Vector Spaces
relations: []
review: draft
---

::: {.proposition}
Let $V$ be an inner product space and $(W_i)_{i\in I}$ a family of subspaces of $V$, where $W^\perp\coloneqq\theset{v\in V\suchthat \inner{w}{v}=0\ \forall w\in W}$.
Then
$$
\qty{ \sum_{i\in I} W_i}^\perp = \bigcap_{i\in I} W_i^\perp.
$$
:::

::: {.proof}
Each $W_i\subseteq\sum_i W_i$, so $\qty{\sum_i W_i}^\perp\subseteq W_i^\perp$ for every $i$.
Conversely, if $v\in\bigcap_i W_i^\perp$ and $w=w_{i_1}+\cdots+w_{i_r}$ with $w_{i_j}\in W_{i_j}$, then $\inner{w}{v}=\sum_j\inner{w_{i_j}}{v}=0$.
:::
