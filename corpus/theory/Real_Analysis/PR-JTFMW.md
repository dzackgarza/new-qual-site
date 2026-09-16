---
schema: qual/card@1
id: PR-JTFMW
kind: proposition
title: The Cantor set is closed and has empty interior
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
:::

::: {.proof}
Each $C_k$ is a finite union of closed intervals, hence closed, so $C$ is closed.
If $C$ contained an open interval $I$ of length $\ell>0$, then $I\subseteq C_k$ for every $k$; since $I$ is connected, it would lie in one of the intervals of length $3^{-k}$ making up $C_k$, so $\ell\leq 3^{-k}$ for every $k$, which is impossible.
:::
