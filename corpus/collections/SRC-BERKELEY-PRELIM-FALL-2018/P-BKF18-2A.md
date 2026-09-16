---
schema: qual/card@1
id: P-BKF18-2A
kind: problem
title: A differential inequality with $f(0)=0$
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

::: {.problem}
Suppose $f:\mathbb R\to\mathbb R$ is differentiable and satisfies $f'(x)>f(x)$ for all real $x$.
Show that if $f(0)=0$, then $f(x)>0$ for all $x>0$.
:::

::: {.solution}
Since $f ^ { \prime } ( 0 ) > 0$ we have $f ( x ) = x \cdot f ^ { \prime } ( 0 ) + o ( | x | )$ in a neighborhood of zero, so there is a $t > 0$ such that f is positive on $( 0 , t )$ . Assume for contradiction that $f ( x ) \leq 0$ for some $x > 0$ and let $x _ { 0 }$ be the first such x. Then $f ( x ) > 0$ on $( 0 , x _ { 0 } )$ , which means that $f ^ { \prime } ( x ) > 0$ on $( 0 , x _ { 0 } )$ , so $f ( x _ { 0 } ) > f ( 0 ) = 0$ , a contradiction
:::
