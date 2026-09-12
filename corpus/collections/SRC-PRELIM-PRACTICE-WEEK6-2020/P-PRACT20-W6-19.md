---
schema: qual/card@1
id: P-PRACT20-W6-19
kind: problem
title: "Week 6: Miscellaneous Topics, problem 19"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Two players take turns tossing a fair coin; the winner is the first who tosses heads.
What is the probability that the first player wins?
:::

::: {.solution}
Let H denote heads and T denote tails.
If the first player wins, the sequence of events must be one of

$$
\{ H , T T H , T T T T H , T T T T T T . . . \} .
$$

That is, there must be 2n tails tossed and then a heads, where $n = 0 , 1 , 2 , \ldots$ Since the tosses are independent and the coin is fair, the probability of one such event occuring is $\left( { \frac { 1 } { 2 } } \right) ^ { 2 n } \cdot \left( { \frac { 1 } { 2 } } \right)$ . Summing over all $n ,$ we find that player one wins with probability

$$
\sum _ { n = 0 } ^ { \infty } \left( { \frac { 1 } { 2 } } \right) ^ { 2 n } \cdot \left( { \frac { 1 } { 2 } } \right) = { \frac { 1 } { 2 } } \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { 4 ^ { n } } } = { \frac { 1 } { 2 } } \cdot { \frac { 1 } { 1 - 1 / 4 } } = { \frac { 2 } { 3 } } .
$$

There is another clever way to reason through this problem without doing the computation.
Let $p$ denote the probability that player one wins.
Since the game is essentially reset if the first two tosses are tails, we have

$$
p = { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } p
$$

where $\begin{array} { l } { { \frac { 1 } { 2 } } } \end{array}$ represents the probability that player one wins on the first toss and ${ \scriptstyle { \frac { 1 } { 4 } } } p$ represents the probability of reaching the reset point and player one winning thereafter.
Solving this gives $p = 2 / 3$ •
:::
