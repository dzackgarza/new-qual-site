---
schema: qual/card@1
id: P-VFAXW
kind: problem
title: Invert $1-z$, one coefficient at a time
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
---

:::{.exercise}
Use this formulation to show that if $A(z)= 1-z$ then $1/A(z) = \sum z^k$.
:::

:::{.solution}
Noting $a_0 = 1, a_1 = -1$, we have

- $b_0 = 1/a_0 = 1$
- $b_1 = -{1\over a_0}(a_1 b_0) = -1(-1\cdot 1) = 1$
- $b_2 = -{1\over a_0}(a_2 b_0 + a_1 b_1) = -1(0\cdot 1 + -1\cdot 1) = 1$, 

and so on, so
\[
{1\over A(z)} = 1 + 1\cdot z + 1\cdot z^2 + \cdots
.\]

:::

