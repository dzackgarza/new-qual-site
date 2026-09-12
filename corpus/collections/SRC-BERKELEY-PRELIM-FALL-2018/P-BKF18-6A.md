---
schema: qual/card@1
id: P-BKF18-6A
kind: problem
title: Square root of a unipotent matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $A$ be an $n\times n$ real matrix such that $(A-I)^m=0$ for some $m\ge1$.
Prove that there exists an $n\times n$ real matrix $B$ such that $B^2=A$.
:::

::: {.solution}
Write $A = I + N$ , so $N ^ { m } = 0$ . Let $P ( x )$ be the m-th Taylor polynomial of the function $\sqrt { 1 + x }$ , so $P ( x ) ^ { 2 } \equiv 1 + x$ (mod $x ^ { m } )$ . In other words

$$
P ( x ) ^ { 2 } = 1 + x + x ^ { m } Q ( x )
$$

for some $Q ( x ) \in \mathbb { R } [ x ]$ . Then

$$
P ( N ) ^ { 2 } = I + N + N ^ { m } Q ( N ) = I + N = A ,
$$

so $B : = P ( N )$ satisfies $B ^ { 2 } = A$ . S
:::
