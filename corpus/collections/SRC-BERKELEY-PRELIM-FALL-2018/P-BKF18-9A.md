---
schema: qual/card@1
id: P-BKF18-9A
kind: problem
title: Cauchy's theorem for elements of prime order
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose a prime $p$ divides the order of a finite group $G$.
Prove that there exists an element $g\in G$ of order $p$.
:::

::: {.solution}
Consider the set $X = \{ ( g _ { 1 } , \dotsc , g _ { p } ) \in G ^ { p } \mid g _ { 1 } \cdot \cdot \cdot g _ { p } = e \}$ . It is acted upon by the cyclic group $\mathbf { Z } / p \mathbf { Z }$ with ${ \bf 1 } \in { \bf Z } / p { \bf Z }$ acting as the cyclic shift

$$
( g _ { 1 } , \dotsc , g _ { p } ) \longmapsto ( g _ { p } , g _ { 1 } , \dotsc , g _ { p - 1 } ) .
$$

A fixed point of this action is a constant p-tuple $( g , \ldots , g )$ such that $g ^ { p } = e$ . The number of fixed points is not zero, since $( e , \ldots , e )$ is a fixed point, and is congruent modulo $p$ to

$$
| X | = | G | ^ { p - 1 } ,
$$

i.e., it is divisible by $p ,$ since $p > 1$ . It follows that there is an element $g \neq e$ with $g ^ { p } = e$
:::
