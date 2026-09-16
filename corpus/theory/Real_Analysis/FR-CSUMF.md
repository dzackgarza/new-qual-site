---
schema: qual/card@1
id: FR-CSUMF
kind: proof
title: First Borel--Cantelli lemma for measures
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $(E_j)_{j\geq 1}$ be a sequence in $\mcm$ with $\sum_{j\geq 1}\mu(E_j) < \infty$, and let $E\coloneqq\limsup_j E_j$ be its [[D-PAEDW|limit superior]].
Then $E\in\mcm$ and $\mu(E) = 0$.
:::

::: {.proof}
We have $E = \bigcap_{k\geq 1}\bigcup_{j\geq k} E_j$, a countable intersection of countable unions of sets in $\mcm$, so $E\in\mcm$.
For every $k\geq 1$, $E\subseteq\bigcup_{j\geq k}E_j$, so by countable subadditivity
$$
\mu(E)\leq\sum_{j\geq k}\mu(E_j).
$$
The right side is the tail of a convergent series, so it tends to $0$ as $k\to\infty$, and $\mu(E) = 0$.
:::
