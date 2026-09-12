---
schema: qual/card@1
id: P-BKS03-1B
kind: problem
title: Measure-preserving bijections between half-spaces
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
(a) Prove there is no continuously differentiable measure-preserving bijection $f:\mathbb R\to\mathbb R_{>0}$.

(b) Find a continuously differentiable measure-preserving bijection
\[
f:\mathbb R^2\to\mathbb R\times\mathbb R_{>0}.
\]
:::

::: {.solution}
For either (a) or (b), the measure-preserving condition is that the Jacobian determinant $J ( f )$ has absolute value 1 everywhere.
By continuity, we must have $J ( f ) = 1$ or $J ( f ) = - 1$ identically.
In (a), this would mean $f ^ { \prime } ( x ) = 1$ or $f ^ { \prime } ( x ) = - 1$ , so $f ( x ) = c + x$ or $f ( x ) = c - x$ . Thus f cannot map R into $\mathbb { R } _ { > 0 }$ . One possible example for (b) is $f ( x , y ) =$ $( e ^ { - y } x , e ^ { y } )$
:::
