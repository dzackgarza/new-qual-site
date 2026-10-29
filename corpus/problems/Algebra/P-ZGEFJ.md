---
schema: qual/card@1
id: P-ZGEFJ
kind: problem
title: $IS$ is a submodule of $A$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
---

::: {.problem}
Let $R$ be a ring, let $I\le R$ be a left ideal, let $A$ be a left $R$-module, and let $S\subseteq A$ be nonempty. Define
$$
IS=\left\{\sum_{i=1}^n r_i a_i:n\ge1,\ r_i\in I,\ a_i\in S\right\}.
$$
Show that $IS$ is a submodule of $A$.
:::

::: {.solution}
Let $x=\sum_{i=1}^n r_i a_i$ and $y=\sum_{j=1}^m s_j b_j$ be elements of $IS$, with $r_i,s_j\in I$ and $a_i,b_j\in S$, and let $r\in R$.

::: pf

::: pf-step

$0\in IS$.

::: pf-proof

Choose $a\in S$, which is possible since $S$ is nonempty. Then $0=0\cdot a\in IS$ because $0\in I$.

:::

:::

::: pf-step

$x+y\in IS$ and $-x\in IS$.

::: pf-proof

Concatenating the two sums writes $x+y$ as a sum of $n+m$ terms $r a$ with $r\in I$ and $a\in S$. Since $I$ is an additive subgroup, $-r_i\in I$, so $-x=\sum_i(-r_i)a_i\in IS$.

:::

:::

::: pf-step

$rx\in IS$, so $IS$ is a submodule of $A$.

::: pf-proof

$rx=\sum_i (rr_i)a_i$, and $rr_i\in I$ because $I$ is a left ideal. With the earlier steps, $IS$ is an additive subgroup closed under the $R$-action.

:::

:::

:::

:::
