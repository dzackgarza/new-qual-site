---
schema: qual/card@1
id: P-BKF18-8B
kind: problem
title: No positive integer solutions to $x^2+y^2=7xy$
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
Show that there are no natural numbers $x,y\ge1$ such that
\[
x^2+y^2=7xy.
\]
:::

::: {.solution}
Assume that there was such a solution.
Taking remainders modulo 7 gives us

$$
x ^ { 2 } + y ^ { 2 } \equiv 0 \mod 7 .
$$

The quadratic remainders modulo 7 are 0, 1, 2, 4. The only two quadratic remainders whose sum is $\equiv 0$ are 0 and 0. So

$$
x ^ { 2 } \equiv y ^ { 2 } \equiv 0 \mod 7 .
$$

It follows that $x , y$ are both divisible by 7, i.e. $x = 7 x _ { 1 } , y = 7 y _ { 1 }$ , for some natural numbers $x _ { 1 } , y _ { 1 }$ . It follows that

$$
x _ { 1 } ^ { 2 } + y _ { 1 } ^ { 2 } = 7 x _ { 1 } y _ { 1 } .
$$

Repeating this process would produce an infinite sequence of pairs $( x , y ) , ( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } ) , . . .$ such that $x _ { i }$ and $y _ { i }$ are strictly decreasing sequences of integers.
Contradiction.
:::
