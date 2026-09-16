---
schema: qual/card@1
id: P-SD42B
kind: problem
title: Bounds on alternating partial sums of a decreasing positive sequence
classification:
  areas:
  - prelim
  topics:
  - Series of Numbers
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $a_0, a_1, a_2, \ldots$ be a decreasing sequence of positive real numbers.
Prove that for every nonnegative integer $m$, $$0 \le \sum_{i=0}^{m}(-1)^i a_i \le a_0.$$ (Hint: $\sum_{i=0}^{m+1}(-1)^i a_i = a_0 - \sum_{i=0}^{m}(-1)^i a_{i+1}$.)
:::

::: {.solution}
Let
\[
S_m=\sum_{i=0}^m(-1)^ia_i.
\]
Because $(a_i)$ is decreasing and positive, each difference $a_{2j}-a_{2j+1}$ is nonnegative.

If $m=2r+1$ is odd, then
\[
S_m=(a_0-a_1)+(a_2-a_3)+\cdots +(a_{2r}-a_{2r+1})\ge0.
\]
If $m=2r$ is even, then
\[
S_m=(a_0-a_1)+\cdots +(a_{2r-2}-a_{2r-1})+a_{2r}\ge0.
\]
Thus $S_m\ge0$ in all cases.

For the upper bound, if $m=2r$, then
\[
S_m=a_0-(a_1-a_2)-\cdots-(a_{2r-1}-a_{2r})\le a_0.
\]
If $m=2r+1$, then
\[
S_m=a_0-(a_1-a_2)-\cdots-(a_{2r-1}-a_{2r})-a_{2r+1}\le a_0.
\]
Therefore
\[
0\le S_m\le a_0
\]
for every $m\ge0$.
:::
