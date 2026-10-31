---
schema: qual/card@1
id: P-PRACT20-W6-19
kind: problem
title: Probability that the first player tosses heads first
classification:
  areas:
  - prelim
  topics:
  - Probability
  - Geometric Series
relations: []
review: draft
---

::: {.problem}
Two players take turns tossing a fair coin; the winner is the first who tosses heads.
What is the probability that the first player wins?
:::

::: {.solution}
Write $H$ for heads and $T$ for tails. The first player wins exactly on the toss sequences

$$
H,\quad TTH,\quad TTTTH,\quad\dots,
$$

that is, $2n$ tails followed by heads, for $n=0,1,2,\dots$. Since the tosses are independent and the coin is fair, such a sequence has probability $\left(\frac12\right)^{2n}\cdot\frac12$. Summing over $n$, the first player wins with probability

$$
\sum_{n=0}^\infty\left(\frac12\right)^{2n}\cdot\frac12=\frac12\sum_{n=0}^\infty\frac{1}{4^n}=\frac12\cdot\frac{1}{1-1/4}=\frac23.
$$

Alternatively, let $p$ be the probability that the first player wins. If the first two tosses are tails, the game starts again, so

$$
p=\frac12+\frac14p,
$$

where $\frac12$ is the probability that the first player wins on the first toss and $\frac14p$ is the probability of reaching the restart and then winning. Solving gives $p=2/3$.
:::
