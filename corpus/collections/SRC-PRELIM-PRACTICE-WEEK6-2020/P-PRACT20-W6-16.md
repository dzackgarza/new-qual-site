---
schema: qual/card@1
id: P-PRACT20-W6-16
kind: problem
title: Maximum of two independent geometric random variables
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose X, Y are i.i.d. random variables taking value $n \in \mathbb N$ with probability $\frac { 1 } { 2 ^ { n } }$ What is the probability that max $\{ X , Y \} > 3 \}$
:::

::: {.solution}
We see that max $\{ X , Y \} > 3$ iff $X > 3$ or $Y > 3$ and

$$
\operatorname* { P r o b } \{ X > 3 { \mathrm { ~ o r ~ } } Y > 3 \} = 1 - \operatorname* { P r o b } \{ X \leq 3 { \mathrm { ~ a n d ~ } } Y \leq 3 \} = 1 - \operatorname* { P r o b } \{ X \leq 3 \} \operatorname* { P r o b } \{ Y \leq 3 \}
$$

where the last step follows by independence.
Now

$$
\operatorname { P r o b } \{ X \leq 3 \} = \sum _ { i = 1 } ^ { 3 } \operatorname { P r o b } \{ X = i \} = { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } + { \frac { 1 } { 8 } } = { \frac { 7 } { 8 } } ,
$$

and likewise for Y since they are identically distributed.
Thus

$$
{ \mathrm { P r o b } } \{ X > 3 { \mathrm { ~ o r ~ } } Y > 3 \} = 1 - \left( { \frac { 7 } { 8 } } \right) ^ { 2 } = { \frac { 1 5 } { 6 4 } } .
$$
:::
