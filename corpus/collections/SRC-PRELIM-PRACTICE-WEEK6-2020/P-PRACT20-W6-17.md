---
schema: qual/card@1
id: P-PRACT20-W6-17
kind: problem
title: Probability that neither of two numbers from $1$ to $10$ is the square of the other
classification:
  areas:
  - prelim
  topics:
  - Probability
  - Combinatorics
relations: []
review: draft
---

::: {.problem}
Two random numbers are drawn uniformly and independently from $\{1, \ldots, 10\}$. What is the probability that neither is the square of the other?
:::

::: {.solution}
The only squares in $\{1,\dots,10\}$ are $1,4,9$, so one number is the square of the other only for the ordered pairs $(1,1),(2,4),(4,2),(3,9),(9,3)$. The $100$ ordered pairs $(i,j)$ with $i,j\in\{1,\dots,10\}$ are equally likely, since the draws are independent and uniform. So the probability that neither is the square of the other is $\frac{95}{100}=\frac{19}{20}$.
:::
