---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW3
kind: problem
title: Decide whether the set of binary sequences is countable (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Countability
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Is the set of all sequences $x_1,x_2,\ldots$ with $x_i\in\{0,1\}$ for $i=1,2,\ldots$ countable?
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. The set $\{0,1\}^{\mathbb{N}}$ of binary sequences is NOT countable.
Proof: suppose it were countable, enumerated as $x^{(1)}, x^{(2)}, x^{(3)}, \ldots$ with $x^{(m)} = (x^{(m)}_1, x^{(m)}_2, \ldots)$.
<1>2. Diagonal construction.
Proof: define the sequence $y = (y_1, y_2, \ldots)$ by $y_n = 1 - x^{(n)}_n$, i.e. $y_n$ differs from the $n$-th entry of the $n$-th listed sequence.
Then $y \in \{0,1\}^{\mathbb{N}}$ since each $y_n \in \{0,1\}$.
<1>3. $y$ is not in the enumeration.
Proof: for every $m$, $y_m = 1 - x^{(m)}_m \ne x^{(m)}_m$, so $y \ne x^{(m)}$.
Hence the enumeration missed $y$, contradicting surjectivity.
<1>4. Q.E.D.
:::
