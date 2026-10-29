---
schema: qual/card@1
id: PR-JTFMW
kind: proposition
title: The Cantor set is closed and nowhere dense
slogan: 'The Cantor set is closed but contains no interval, so it is nowhere dense.'
classification:
  areas:
  - real-analysis
  topics:
  - Cantor Set
  - Density
  - Closure
relations: []
review: draft
---

::: {.proposition}
Let $C_0\coloneqq[0,1]$, and let $C_{k+1}$ be obtained from $C_k$ by removing the open middle third of each of the $2^k$ disjoint closed intervals of length $3^{-k}$ whose union is $C_k$.
The Cantor set $C\coloneqq\bigcap_{k\geq 0}C_k$ is a closed subset of $\RR$ with empty interior.
In particular, $C$ is [[D-2MJRE|nowhere dense]] in $\RR$.
:::

::: {.proof}
Each $C_k$ is a finite union of closed intervals, so it is closed, and $C$ is closed as an intersection of closed sets.
If $C$ contained an open interval $I$ of length $\ell>0$, then $I\subseteq C_k$ for every $k$; since $I$ is connected, it would lie in one of the intervals of length $3^{-k}$ making up $C_k$, so $\ell\leq 3^{-k}$ for every $k$, which is impossible.
Hence $C$ has empty interior, and since $C=\overline{C}$, its closure has empty interior.
:::
