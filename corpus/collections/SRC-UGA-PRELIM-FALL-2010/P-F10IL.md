---
schema: qual/card@1
id: P-F10IL
kind: problem
title: Independent images under a linear map imply independent preimages
classification:
  areas:
  - prelim
  topics:
  - Linear Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; the mathematics is unchanged and was checked: applying
    T to a vanishing combination and using linearity gives a relation among the images,
    whose triviality is the hypothesis, and that is exactly the defining condition for
    independence of the v_i. The argument is the card's own: no retained solution set covers
    this problem.
---

::: {.problem}
Suppose $V$ and $W$ are vector spaces and $T: V \to W$ is a linear transformation.
Suppose $v_1, \dots, v_k \in V$.
Prove that if $T(v_1), \dots, T(v_k)$ form a linearly independent set in $W$, then $v_1, \dots, v_k$ form a linearly independent set in $V$.
:::

::: {.solution}
The argument is the card's own; no retained solution set covers this problem.

::: pf

::: {.pf-step #annihilate}
If $a_1v_1+\cdots+a_kv_k=0$ with the $a_i$ scalars, then $a_i=0$ for every $i$.

::: pf-proof
Applying $T$ to the vanishing combination and using additivity and homogeneity of $T$ gives
$$
0=T(0)=T(a_1v_1+\cdots+a_kv_k)=a_1T(v_1)+\cdots+a_kT(v_k).
$$
The vectors $T(v_1),\ldots,T(v_k)$ are linearly independent by hypothesis, so every coefficient in this relation vanishes, that is $a_i=0$ for each $i$.
:::

:::

::: {.pf-step}
$v_1,\ldots,v_k$ are linearly independent in $V$.

::: pf-proof
By definition of linear independence, a vanishing linear combination has all coefficients zero, which is exactly step [](#annihilate){.pf-ref}.
:::

:::

:::
:::
