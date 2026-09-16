---
schema: qual/card@1
id: P-PRACT20-W6-22
kind: problem
title: Factorials ending in exactly $99$ zeros
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For how many integers k does k! end in exactly 99 zeros?
:::

::: {.solution}
We find that k! ends with n zeros when $k ! = K \cdot 1 0 ^ { n } = K \cdot 2 ^ { n } \cdot 5 ^ { n }$ where K is not divisible by 10. There will always be more factors of 2 than factors of 5 in k! so we gain a zero when we pass a multiple of five.
Thus there will be 5 numbers k such that k! ends in exactly 99 zeros and they have the form $k = 5 N + \ell$ for $\ell = 0 , 1 , 2 , 3 , 4$ for some $N \in  { \mathbb { N } }$ .

Actually, it is possible that there are no natural numbers k such that k! ends in exactly 99 zeros.
It is possible that some $k - 1$ is such that $( k - 1 ) !$ ends in exactly 98 zeros and that k is divisible by 25, meaning that at least two extra zeros get added and k! ends in 100 or more zeros.
This is somewhat unlikely.
Indeed, only $1 / 5$ multiples of 5 is divisible by 25, and $1 / 2 5$ of all multiples of 5 are divisible by 125, etc. which means (roughly speaking) that for a given number n, there is a

$$
\sum _ { j = 1 } ^ { \infty } { \frac { 1 } { 5 ^ { j } } } = { \frac { 1 / 5 } { 1 - 1 / 5 } } = { \frac { 1 } { 4 } }
$$

chance that there are no $k \in \mathbb N$ such that k! ends with exactly n zeros.
To give a definitive answer, one would need to check that 99 is not such an n. Indeed, 99 doesn’t get skipped.
Counting multiples of 5, we see that for each 100 numbers, $\{ 1 0 0 \ell + 1 , 1 0 0 \ell + 2 , \cdot \cdot \cdot , 1 0 0 ( \ell + 1 ) \} , \ell = 0 , 1 , 2 , 3 ,$ there are twenty multiples of 5, four of which are divisible by 25, and possibly one of which is divisible by 125. Thus, 100! ends in 24 zeros, 200! ends in 49 zeros, 300 ends in 74 zeros and 400! ends in 99 zeros (as do 401!, 402!, 403! and 404!).
:::
