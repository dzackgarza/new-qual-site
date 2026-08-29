---
schema: qual/card@1
id: P-RAF07F
kind: problem
title: "Vitali covering lemma for open balls"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $\mathcal{C}$ be a collection of open balls in $\mathbb{R}^n$, and let $U = \bigcup_{B \in \mathcal{C}} B$.
Prove that if $c < m(U)$, then there exist disjoint balls $B_1, \ldots, B_k$ in $\mathcal{C}$ such that $\sum_{i=1}^k m(B_i) > 3^{-n} c$.
[This statement is proved in Folland, but you are being asked to give a proof here.]
:::

::: {.solution}
<1>1. Since $c < m(U)$ and $U = \bigcup_{B \in \mathcal{C}} B$, there is a compact set $K \subseteq U$ with $m(K) > c$.
Proof: inner regularity of Lebesgue measure (a measurable set of finite measure is approximated from inside by compact sets).

<1>2. $K$ is covered by the open balls in $\mathcal{C}$, so by compactness there is a finite subcover $B_1', \ldots, B_N'$ of $K$.
Proof: compactness.

<1>3. Choose from $B_1', \ldots, B_N'$ a disjoint subcollection $B_1, \ldots, B_k$ greedily: pick the largest remaining ball, discard all balls intersecting it, and repeat.
Proof: greedy selection algorithm.

<1>4. Every discarded ball $B_j'$ is contained in a ball $\tilde B_j$ concentric with some selected $B_i$ but with $3$ times the radius.
Proof: if $B_j'$ (radius $r_j$) intersects a selected ball $B_i$ (radius $r_i \ge r_j$), then $B_j' \subseteq \tilde B_i$ where $\tilde B_i$ has the same center as $B_i$ and radius $3r_i$.

<1>5. Hence $K \subseteq \bigcup_{i=1}^k \tilde B_i$, where $\tilde B_i$ is the $3$-fold dilation of $B_i$.
Proof: <1>3 and <1>4 (every ball in the cover is either selected or contained in a $3$-fold dilation of a selected ball).

<1>6. Therefore $c < m(K) \le \sum_{i=1}^k m(\tilde B_i) = 3^n \sum_{i=1}^k m(B_i)$.
Proof: <1>1, <1>5, and $m(\tilde B_i) = 3^n m(B_i)$ (scaling by $3$ multiplies measure by $3^n$).

<1>7. Hence $\sum_{i=1}^k m(B_i) > 3^{-n} c$.
Proof: <1>6, dividing by $3^n$.

<1>8. Q.E.D.
Proof: <1>7.
:::
