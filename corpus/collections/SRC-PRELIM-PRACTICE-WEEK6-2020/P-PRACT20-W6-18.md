---
schema: qual/card@1
id: P-PRACT20-W6-18
kind: problem
title: Probability that $X<Y$ for $X$ uniform on $[0,3]$ and $Y$ uniform on $[0,4]$
classification:
  areas:
  - prelim
  topics:
  - Probability
relations: []
review: draft
---

::: {.problem}
If $X$ is drawn uniformly from $[0, 3]$ and $Y$ is drawn independently and uniformly from $[0, 4]$, what is the probability that $X < Y$?
:::

::: {.solution}
Split into the disjoint cases $Y\in[0,3]$ and $Y\in(3,4]$. By the law of total probability,

$$
P(X<Y)=P(X<Y\given Y\leq3)\,P(Y\leq3)+P(X<Y\given Y>3)\,P(Y>3).
$$

Given $Y\leq3$, $Y$ is uniform on $[0,3]$ and independent of $X$, so by symmetry $P(X<Y\given Y\leq3)=1/2$. If $Y>3$, then $X<Y$ always. Thus

$$
P(X<Y)=\frac12\cdot\frac34+1\cdot\frac14=\frac58.
$$

This agrees with intuition: $X<Y$ should be slightly more likely than $X\geq Y$, since $Y$ is drawn from a larger interval.
:::
