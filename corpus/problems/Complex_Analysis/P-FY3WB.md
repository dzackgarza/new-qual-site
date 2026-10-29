---
schema: qual/card@1
id: P-FY3WB
kind: problem
title: The truncated exponential $\sum_{k=0}^n z^k/k!$ has no zeros in the open unit
  disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Prove that for every $n\in \ZZ^{\geq 0}$ the following polynomial has no roots in the open unit disc:
$$
f_n(z) \definedas \sum_{k=0}^n {z^k \over k!}
.$$
:::

::: {.hint}
Check $n=1,2$ directly.
:::

::: {.solution}
::: pf

::: pf-step
For $n=0$ and $n=1$, $f_n$ has no zeros in $\DD$.

::: pf-proof
$f_0\equiv 1$, and $f_1(z)=1+z$ vanishes only at $-1$, which is on the unit circle.
:::

:::

::: {.pf-step #tail}
For $n\geq 2$ and $\abs z = 1$, $\abs{e^z-f_n(z)}\leq \frac14$.

::: pf-proof
For $k\geq 3$ we have $k!\geq 2\cdot 3^{k-2}$, so
$$
\abs{e^z-f_n(z)} \leq \sum_{k=n+1}^\infty \frac1{k!} \leq \sum_{k=3}^\infty \frac1{k!} \leq \frac12\sum_{j=1}^\infty \frac1{3^j} = \frac14.
$$
:::

:::

::: {.pf-step #exp-lower}
For $\abs z = 1$, $\abs{e^z}>\frac14$.

::: pf-proof
$\abs{e^z} = e^{\Re z}\geq e^{-1}>\frac13$.
:::

:::

::: pf-step
For $n\geq 2$, $f_n$ has no zeros in $\DD$.

::: pf-proof
By steps [](#tail){.pf-ref} and [](#exp-lower){.pf-ref}, $\abs{e^z-f_n(z)}<\abs{e^z}$ on $\abs z = 1$. By Rouché's theorem, $f_n$ and $e^z$ have the same number of zeros in $\DD$, and $e^z$ has none.
:::

:::

:::

:::
