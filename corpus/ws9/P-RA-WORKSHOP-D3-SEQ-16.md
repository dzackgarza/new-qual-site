---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-16
kind: problem
title: 'Interchange two nonnegative double-series summations'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2006 #5) Let $a_{m,n}\ge0$ for $m,n\in\mathbb N$ and assume that the partial sums
$$
\sum_{m=1}^{M}\sum_{n=1}^{N}a_{m,n}
$$
are bounded above.
Prove carefully that
$$
\sum_{m=1}^{\infty}\left(\sum_{n=1}^{\infty}a_{m,n}\right)
\quad\text{and}\quad
\sum_{n=1}^{\infty}\left(\sum_{m=1}^{\infty}a_{m,n}\right)
$$
exist and are equal.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. The doubly-indexed partial sums are bounded, by assumption; call $B = \sup_{M,N}\sum_{m=1}^M\sum_{n=1}^N a_{m,n} < \infty$.
<1>2. The inner series exist and the iterated sums exist in $[0,\infty]$.
Proof: for each fixed $m$, the partial sums $\sum_{n=1}^N a_{m,n}$ are increasing in $N$ and bounded by $B$, so $A_m := \sum_{n=1}^\infty a_{m,n}$ converges with $A_m \le B$.
Then $\sum_{m=1}^M A_m$ is increasing in $M$ and bounded by $B$ (as $\sum_{m=1}^M A_m = \sup_N\sum_{m=1}^M\sum_{n=1}^N a_{m,n} \le B$), so $\sum_{m=1}^\infty A_m$ converges and equals $\sup_M\sum_{m=1}^M A_m \le B$.
Symmetrically $\sum_{n=1}^\infty\big(\sum_{m=1}^\infty a_{m,n}\big)$ converges.
<1>3. Both iterated sums equal $\sup_{M,N} S_{M,N}$.
Proof: for every $M, N$, $S_{M,N} := \sum_{m=1}^M\sum_{n=1}^N a_{m,n} \le \sum_{m=1}^M A_m \le \sup_M\sum_{m=1}^M A_m$, so $\sup_{M,N}S_{M,N} \le \sum_{m=1}^\infty A_m$.
Conversely, for fixed $M$, $S_{M,N} \nearrow \sum_{m=1}^M A_m$ as $N \to \infty$ (monotone convergence), so $\sum_{m=1}^M A_m = \sup_N S_{M,N} \le \sup_{M,N}S_{M,N}$; taking the sup over $M$ gives $\sum_{m=1}^\infty A_m \le \sup_{M,N}S_{M,N}$.
Hence equality: $\sum_{m=1}^\infty\big(\sum_{n=1}^\infty a_{m,n}\big) = \sup_{M,N}S_{M,N}$.
The same argument with the roles of $m$ and $n$ exchanged gives $\sum_{n=1}^\infty\big(\sum_{m=1}^\infty a_{m,n}\big) = \sup_{M,N}S_{M,N}$.
<1>4. Q.E.D. Proof: both iterated sums exist and equal the same finite number $\sup_{M,N}S_{M,N}$.
:::
