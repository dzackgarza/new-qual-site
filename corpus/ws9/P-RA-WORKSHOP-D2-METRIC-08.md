---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-08
kind: problem
title: 'Closedness, boundedness, and compactness in the rational metric space'
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - metric-spaces
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2009, #4a) Consider the metric space $(\mathbb Q,d)$ where $\mathbb Q$ denotes the rational numbers and $d(x,y)=|x-y|$.
Let $$E=\{x\in\mathbb Q:x>0,\ 2<x^2<3\}.$$ Is $E$ closed and bounded in $\mathbb Q$?
Is $E$ compact in $\mathbb Q$?
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $E$ is closed in $\mathbb{Q}$.
Proof: $E = \{x \in \mathbb{Q} : 2 < x^2 < 3\} = \mathbb{Q}\cap(\sqrt2,\sqrt3)$.
Since $\sqrt2, \sqrt3 \notin \mathbb{Q}$, we have $\mathbb{Q}\cap(\sqrt2,\sqrt3) = \mathbb{Q}\cap[\sqrt2,\sqrt3]$, and the latter is the intersection of $\mathbb{Q}$ with a closed subset of $\mathbb{R}$, hence closed in the relative (metric) topology of $\mathbb{Q}$.
<1>2. $E$ is bounded in $\mathbb{Q}$.
Proof: $2 < x^2$ forces $|x| > 1$; together with $x > 0$ and $x^2 < 3$ we get $1 < x < \sqrt3$, so $E \subseteq (1, 2)$, and $E$ is bounded (e.g. $d(x,y) \le 1$ for all $x,y \in E$). <1>3. $E$ is NOT compact in $\mathbb{Q}$.
Proof: choose a sequence $(q_n)$ of rationals with $\sqrt2 < q_n < \sqrt3$ and $q_n \to \sqrt2$ in $\mathbb{R}$ (possible since $\mathbb{Q}$ is dense).
Then $q_n \in E$ for all $n$.
If a subsequence converged in $\mathbb{Q}$, its limit would have to be $\sqrt2$ (limits in $\mathbb{R}$ are unique), but $\sqrt2 \notin \mathbb{Q}$.
Hence no subsequence converges in $\mathbb{Q}$, so $E$ is not sequentially compact, and a metric space is compact iff sequentially compact.
<1>4. Q.E.D.
:::
