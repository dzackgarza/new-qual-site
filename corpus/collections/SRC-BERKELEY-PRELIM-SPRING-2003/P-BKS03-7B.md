---
schema: qual/card@1
id: P-BKS03-7B
kind: problem
title: Two fixed points force a disk self-map to be the identity
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $f$ be analytic on the unit disk with $|f(z)|\le1$.
If $f$ has two distinct fixed points in the disk, prove that $f(z)=z$ identically.
:::

::: {.solution}
Let S be a linear fractional transformation which maps D onto itself so that $S ( 0 ) = x _ { 1 }$ . Then $g = S ^ { - 1 } \circ f \circ S$ has the same properties as f and its two fixed points are $0 = S ^ { - 1 } ( z _ { 1 } )$ and $y = S ^ { - 1 } ( z _ { 2 } )$

Since $g ( 0 ) = 0$ we can define the analytic function $h ( z ) = g ( z ) / z$ . On the circle $| z | = 1 - \epsilon$ for fixed $\epsilon \in ( 0 , 1 )$ , we have $| h ( z ) | = | g ( z ) | / | z | \le 1 / ( 1 - \epsilon )$ , so the maximum principle implies $| h ( z ) | \leq 1 / ( 1 - \epsilon )$ for $| z | \le 1 - \epsilon$ . This holds for arbitrarily small $\epsilon > 0$ , so $| h ( z ) | \leq 1$ for all $z \in D$

On the other hand we know that $h ( y ) = 1$ , so h assumes a maximum inside D. By the maximum principle h must be constant; that is, $h = 1$ . This implies that $g ( z ) = z$ and then $f ( z ) = z$
:::
