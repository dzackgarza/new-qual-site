---
schema: qual/card@1
id: P-PRACT20-W3-18
kind: problem
title: Partial derivative of the elementary symmetric polynomial $\sum_{i<j}x_ix_j$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f ( x _ { 1 } , \ldots , x _ { n } ) = \sum _ { 1 \leq i < j \leq n } x _ { i } x _ { j }$ . Find $\frac { \partial f } { \partial x _ { n } }$
:::

::: {.solution}
::: pf

::: {.pf-step #split}
$f = x_n\sum_{i=1}^{n-1}x_i + \sum_{1\leq i<j\leq n-1}x_ix_j$.

::: pf-proof
A term $x_ix_j$ with $i<j\leq n$ contains $x_n$ only if $i=n$ or $j=n$.
The case $i=n$ is impossible, because $i<j\leq n$.
So the terms that contain $x_n$ are exactly $x_ix_n$ for $1\leq i\leq n-1$, and every other term has $j\leq n-1$.
:::

:::

::: pf-step
$\dfrac{\partial f}{\partial x_n} = \boxed{\sum_{i=1}^{n-1}x_i}$.

::: pf-proof
In step [](#split){.pf-ref}, the second sum does not depend on $x_n$, and the first is $x_n$ times a polynomial that does not depend on $x_n$.
:::

:::

:::

:::
