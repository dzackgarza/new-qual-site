---
schema: qual/card@1
id: P-OCOSY
kind: problem
title: Invert $\cos(z)$, one coefficient at a tiem
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Trigonometry
  - Laurent Series
relations: []
review: draft
solved: true
---

:::{.exercise title="Invert $\cos(z)$, one coefficient at a tiem"}
Find $1/\cos(z)$ using this method.
:::

:::{.solution}
We have $\cos(z) = c_0 +c_2^2 + c_4 z^4 + \bigo(z^6)$ where

- $c_0 = 1$
- $c_2 = -1/2!$
- $c_4 = 1/4!$

Note that $c_i$ for $i$ odd all vanish.
Write $1/\cos(z) = \sum b_k z^k$, then

- $b_0 = c_0\inv = 1$.
- $b_1 = -c_0\inv(c_1 b_0) = -(0) = 0$.
- $b_2 = -c_0\inv(c_2 b_0 + c_1b_1) = -(c_2 + 0) = -c_2 = 1/2!$
- $b_3 = -c_0\inv(c_3b_0 + c_2b_1 + c_1b_2) = -(0 +0 + 0)= 0$
- $b_4 = -c_0\inv(c_4b_0 + c_3b_1 + c_2 b_2 + c_1b_3)=-(c_4 + 0 + (-1/2!)(1/2!) + 0) = 5/24$.

So
\[
{1\over \cos(z)} = 1 + {1\over 2!}z^2 + {5\over 24}z^4 + \bigo(z^6)
.\]
:::

