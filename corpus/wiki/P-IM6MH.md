---
schema: qual/card@1
id: P-IM6MH
kind: problem
title: Invert $2z-1$, one coefficient at a time
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Laurent Series
relations: []
review: draft
---

:::{.exercise title="Invert $2z-1$, one coefficient at a time"}
Let $A(z) \da 2z-1$ and find $1/A(z)$.
:::

:::{.solution}
To compute the inverse of $A(z) \da (2z-1)$, note $a_0 = -1, a_1 = 2$, so

- $b_0 = 1/a_0 = -1$
- $b_1 = -{1\over a_0}(a_1b_0) = 1(2\cdot -1) = -2$
- $b_2 = -{1\over a_0}(a_2 b_0 + a_1 b_1) = 1(0\cdot 1 + 2\cdot -2) = -4$
- $b_3 = -{1\over a_0}(a_3b_0 + a_2 b_1 + a_1 b_2) = 1(0 + 0 + 2\cdot -4) = -8$

so
\[
{1\over 1-2z} = -1 - 2z - 4z^2 - 8z^3 \cdots 
= - \sum_{k\geq 0} (2z)^k
.\]

:::

