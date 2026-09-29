---
schema: qual/card@1
id: E-E3JL6
kind: problem
title: Products of Hausdorff spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Show that the product of two Hausdorff spaces is Hausdorff.
:::

::: {.solution}
Let $X$ and $Y$ be Hausdorff, and let $p_1=(x_1,y_1)$ and $p_2=(x_2,y_2)$ be distinct points of $X\times Y$, so that $x_1\ne x_2$ or $y_1\ne y_2$.

::: pf

::: {.pf-step #separate-by-x}
If $x_1\ne x_2$, then $p_1$ and $p_2$ have disjoint open neighborhoods.

::: pf-proof
Choose disjoint open $U_1\ni x_1$ and $U_2\ni x_2$ in $X$.
Then $U_1\times Y$ and $U_2\times Y$ are open in $X\times Y$, contain $p_1$ and $p_2$, and $(U_1\times Y)\cap(U_2\times Y)=(U_1\cap U_2)\times Y=\varnothing$.
:::

:::

::: {.pf-step #separate-by-y}
If $y_1\ne y_2$, then $p_1$ and $p_2$ have disjoint open neighborhoods.

::: pf-proof
Choose disjoint open $V_1\ni y_1$ and $V_2\ni y_2$ in $Y$; then $X\times V_1$ and $X\times V_2$ are disjoint open neighborhoods of $p_1$ and $p_2$, as in step [](#separate-by-x){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#separate-by-x){.pf-ref} and [](#separate-by-y){.pf-ref} cover both cases.
:::

:::

:::
