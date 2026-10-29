---
schema: qual/card@1
id: P-IM6MH
kind: problem
title: Invert $2z-1$, one coefficient at a time
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Laurent Series
relations: []
review: draft
---

::: {.exercise}
Let $A(z) \coloneqq 2z-1$ and find $1/A(z)$.
:::

::: {.solution}
Write $A(z) = \sum_k a_k z^k$ with $a_0 = -1$, $a_1 = 2$ and $a_k = 0$ for $k \geq 2$, and $1/A(z) = \sum_k b_k z^k$ near $0$.

::: pf

::: {.pf-step #recursion}
$b_0 = 1/a_0$ and $b_n = -\frac{1}{a_0}\sum_{j=1}^{n} a_j b_{n-j}$ for $n \geq 1$.

::: pf-proof
Since $a_0 \neq 0$, $1/A$ is holomorphic near $0$, and comparing coefficients in $A(z)\cdot\frac{1}{A(z)} = 1$ gives $a_0 b_0 = 1$ and $\sum_{j=0}^{n} a_j b_{n-j} = 0$ for $n \geq 1$.
:::

:::

::: {.pf-step #coefficients}
$b_n = -2^n$ for every $n \geq 0$.

::: pf-proof
Here step [](#recursion){.pf-ref} reads $b_0 = -1$ and $b_n = a_1 b_{n-1} = 2b_{n-1}$, so $b_0 = -1$, $b_1 = -2$, $b_2 = -4$, $b_3 = -8$, and by induction $b_n = -2^n$.
:::

:::

::: pf-step
For $\abs{z} < 1/2$,
$$
\boxed{\frac{1}{2z-1} = -1 - 2z - 4z^2 - 8z^3 - \cdots = -\sum_{k\geq 0} (2z)^k}.
$$

::: pf-proof
By step [](#coefficients){.pf-ref} this is the Taylor series of $1/A$ at $0$; it is the geometric series $-\frac{1}{1-2z}$, which converges exactly for $\abs{2z} < 1$, the disc up to the pole at $z = 1/2$.
:::

:::

:::
:::
