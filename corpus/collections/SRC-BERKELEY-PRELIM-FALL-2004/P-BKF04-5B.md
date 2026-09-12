---
schema: qual/card@1
id: P-BKF04-5B
kind: problem
title: UC Berkeley Fall 2004 prelim 5B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the cardinality of the smallest field F of characteristic $7$ such that the equation $x ^ { 1 8 } + x ^ { 1 7 } + \cdot \cdot \cdot + x + 1 = 0$ has a solution $x \in F ?$
:::

::: {.solution}
We have the identity

$$
( x - 1 ) ( x ^ { 1 8 } + x ^ { 1 7 } + \cdot \cdot \cdot + x + 1 ) = x ^ { 1 9 } - 1 ,
$$

and the latter has no repeated factors over a field of characteristic $7$ (since $x ^ { 1 9 } - 1$ has no factors in common with its derivative), so the given condition is equivalent to the condition that the multiplicative group $F ^ { * }$ contain a nontrivial element of order dividing 19. Since 19 is prime and $F ^ { * }$ is a finite abelian group, this is equivalent to $1 9 \mid \# F ^ { * }$ . The size of $F$ is $7 ^ { m }$ for some m $\geq 1$ , so the condition becomes $1 9 \ : | \ : ( 7 ^ { m } - 1 )$ . We compute $7 ^ { 2 } \equiv 1 1$ (mod 19) and $7 ^ { 3 } \equiv 1$ (mod 19), so the smallest possible m is $^ { 3 , }$ and the smallest possible field $F$ satisfying the conditions is the field $\mathbb { F } _ { 7 ^ { 3 } }$ of $7 ^ { 3 } = 3 4 3$ elements.
:::
