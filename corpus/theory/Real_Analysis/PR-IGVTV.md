---
schema: qual/card@1
id: PR-IGVTV
kind: proposition
title: Convergent series have terms and tails tending to zero
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Small Tails
relations: []
review: draft
---

::: {.proposition}
Let $(a_n)_{n\geq1}$ be a sequence in $\CC$ such that $\sum_{n=1}^\infty a_n$ converges.
Then $a_n\to0$ as $n\to\infty$, and
$$
\sum_{n=N}^\infty a_n \convergesto{N\to\infty} 0 .
$$
:::

::: {.proof}
Let $s_N\coloneqq\sum_{n=1}^N a_n$ and $s\coloneqq\lim_N s_N$.
Then $a_N=s_N-s_{N-1}\to s-s=0$, and $\sum_{n=N}^\infty a_n=s-s_{N-1}\to0$.
:::
