---
schema: qual/card@1
id: FS-ACP4W
kind: strategy
title: Replacing a sequence of sets by a sequence of disjoint sets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.strategy}
Let $(E_j)_{j\in \NN}$ be a sequence of subsets of a set $X$, and put
$$
F_j\coloneqq E_j \setminus \bigcup_{k<j} E_k .
$$
The sets $F_j$ are pairwise disjoint, $F_j\subseteq E_j$, and $\bigcup_{j\le n} F_j=\bigcup_{j\le n} E_j$ for every $n$, so $\bigcup_j E_j = \coprod_j F_j$.
If each $E_j$ belongs to a $\sigma$-algebra $\mcm$ on $X$, then so does each $F_j$.
:::
