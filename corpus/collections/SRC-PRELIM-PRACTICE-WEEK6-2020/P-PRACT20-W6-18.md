---
schema: qual/card@1
id: P-PRACT20-W6-18
kind: problem
title: Probability that $X<Y$ for $X$ uniform on $[0,3]$ and $Y$ uniform on $[0,4]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
If X is drawn uniformly from [0, 3] and Y is drawn uniformly from [0, 4], what is the probability that $X < Y ?$
:::

::: {.solution}
We can split this up into the cases that $Y \in [ 0 , 3 ]$ or $Y \in ( 3 , 4 ]$ . Since these cases are disjoint and cover all possibilities, the law of total probability says that

$$
\operatorname* { P r o b } \{ X < Y \} = \operatorname* { P r o b } \{ X < Y | Y \leq 3 \} \operatorname* { P r o b } \{ Y \leq 3 \} + \operatorname* { P r o b } \{ X < Y | Y > 3 \} \operatorname* { P r o b } \{ Y > 3 \} .
$$

Given that $Y \le 3 , Y$ is distributed uniformly in $[ 0 , 3 ]$ and so by symmetry, the probability that $X < Y$ is $1 / 2$ . If $Y > 3$ , then probability that $X < Y$ is 1. Thus we have

$$
\operatorname { P r o b } \{ X < Y \} = { \frac { 1 } { 2 } } \cdot { \frac { 3 } { 4 } } + 1 \cdot { \frac { 1 } { 4 } } = { \frac { 5 } { 8 } } .
$$

This fits with our intution: it should be slightly more like that $X \prec Y$ than $X \geq Y$ since Y is drawn from a larger set.
:::
