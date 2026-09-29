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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Fall 2007 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing greedy Vitali-selection proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $\mathcal{C}$ be a collection of open balls in $\mathbb{R}^n$, and let $U = \bigcup_{B \in \mathcal{C}} B$.
Prove that if $c < m(U)$, then there exist disjoint balls $B_1, \ldots, B_k$ in $\mathcal{C}$ such that $\sum_{i=1}^k m(B_i) > 3^{-n} c$.
[This statement is proved in Folland, but you are being asked to give a proof here.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Since $c < m(U)$ and $U = \bigcup_{B \in \mathcal{C}} B$, there is a compact set $K \subseteq U$ with $m(K) > c$.

::: pf-proof

inner regularity of Lebesgue measure (a measurable set of finite measure is approximated from inside by compact sets).

:::

:::

::: pf-step

$K$ is covered by the open balls in $\mathcal{C}$, so by compactness there is a finite subcover $B_1', \ldots, B_N'$ of $K$.

::: pf-proof

compactness.

:::

:::

::: {.pf-step #s3}

Choose from $B_1', \ldots, B_N'$ a disjoint subcollection $B_1, \ldots, B_k$ greedily: pick the largest remaining ball, discard all balls intersecting it, and repeat.

::: pf-proof

greedy selection algorithm.

:::

:::

::: {.pf-step #s4}

Every discarded ball $B_j'$ is contained in a ball $\tilde B_j$ concentric with some selected $B_i$ but with $3$ times the radius.

::: pf-proof

if $B_j'$ (radius $r_j$) intersects a selected ball $B_i$ (radius $r_i \ge r_j$), then $B_j' \subseteq \tilde B_i$ where $\tilde B_i$ has the same center as $B_i$ and radius $3r_i$.

:::

:::

::: {.pf-step #s5}

Hence $K \subseteq \bigcup_{i=1}^k \tilde B_i$, where $\tilde B_i$ is the $3$-fold dilation of $B_i$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} (every ball in the cover is either selected or contained in a $3$-fold dilation of a selected ball).

:::

:::

::: {.pf-step #s6}

Therefore $c < m(K) \le \sum_{i=1}^k m(\tilde B_i) = 3^n \sum_{i=1}^k m(B_i)$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s5){.pf-ref}, and $m(\tilde B_i) = 3^n m(B_i)$ (scaling by $3$ multiplies measure by $3^n$).

:::

:::

::: {.pf-step #s7}

Hence $\sum_{i=1}^k m(B_i) > 3^{-n} c$.

::: pf-proof

Step [](#s6){.pf-ref}, dividing by $3^n$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
