---
schema: qual/card@1
id: FF-JKLWM
kind: fact
title: Coefficients of the reciprocal of a power series
prompts:
- For $A(z) = \sum c_k z^k$, how are the coefficients of $1/A(z)$ computed from the $c_k$?
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Series of Functions
relations: []
review: draft
---

::: {.fact}
Let $A(z)=\sum_{k\ge0}c_kz^k$ be a power series with positive radius of convergence and $c_0\neq0$.
Then $1/A$ is holomorphic near $0$, and its Taylor series $1/A(z)=\sum_{k\ge0}b_kz^k$ has coefficients determined recursively by
$$
b_0=c_0\inv,\qquad b_n=-c_0\inv\sum_{k=1}^{n}c_kb_{n-k}\quad(n\ge1).
$$
In particular, $b_1=-c_0\inv c_1b_0$ and $b_2=-c_0\inv(c_2b_0+c_1b_1)$.
:::

::: {.proof}
Since $A(0)=c_0\neq0$ and $A$ is continuous, $A$ has no zeros near $0$, so $1/A$ is holomorphic there and has a Taylor series $\sum_k b_kz^k$.
The Cauchy product of the two series is $A(z)\cdot\frac{1}{A(z)}=1$, so comparing coefficients gives $c_0b_0=1$ and $\sum_{k=0}^{n}c_kb_{n-k}=0$ for $n\ge1$.
Solving the last equation for $b_n$ gives the recursion.
:::
