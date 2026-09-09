---
schema: qual/card@1
id: P-MXATB
kind: problem
title: A $p$-cycle and a transposition generate $S_p$ for $p$ prime
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Presentations
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $p$ be prime, let $\sigma\in S_p$ be a $p$-cycle, and let $\tau\in S_p$ be any transposition. Show that
\[
\langle\sigma,\tau\rangle=S_p.
\]
:::

::: {.solution}
Label the $p$ points by the additive group $\ZZ/p\ZZ$ so that
\[
\sigma(x)=x+1.
\]
Write
\[
\tau=(a,b),
\qquad d=b-a\ne0\pmod p.
\]

For every $k\in\ZZ/p\ZZ$,
\[
\sigma^k\tau\sigma^{-k}=(a+k,b+k).
\]
Thus the subgroup $H=\langle\sigma,\tau\rangle$ contains the transposition joining $x$ to $x+d$ for every $x\in\ZZ/p\ZZ$.

Consider the graph with vertex set $\ZZ/p\ZZ$ and edges
\[
\{x,x+d\}.
\]
Because $p$ is prime and $d\ne0$, the element $d$ generates the additive group $\ZZ/p\ZZ$. Hence this graph is connected (indeed it is a $p$-cycle).

The transpositions corresponding to the edges of any connected graph on $p$ vertices generate the full symmetric group: a spanning tree suffices, since transpositions along the unique path from a fixed root to a vertex generate the star transpositions, and star transpositions generate $S_p$.

Therefore the conjugates of $\tau$ already generate $S_p$, and hence
\[
\langle\sigma,\tau\rangle=S_p.
\]
:::
