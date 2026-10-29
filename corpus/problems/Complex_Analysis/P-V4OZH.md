---
schema: qual/card@1
id: P-V4OZH
kind: problem
title: $f(z)=b$ has $n$ solutions in the unit disk for a product of Blaschke factors
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Rouché
  - Zeros
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
For $k=1,2,\ldots, n$, suppose $\abs{a_k} < 1$, and suppose $\abs{b}<1$. Let
$$
f(z) \coloneqq \qty{z - a_1 \over 1 - \bar a_1 z} \qty{z-a_2 \over 1 - \bar a_2 z} \cdots \qty{z - a_n \over 1 - \bar a_n z}.
$$
Show that $f(z) = b$ has $n$ solutions in $\abs{z} < 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #hol}

$f$ is holomorphic on a neighborhood of $\bar\DD$.

::: pf-proof

The poles of $f$ are at the points $1/\bar a_k$ with $a_k \neq 0$, and $\abs{1/\bar a_k} > 1$.

:::

:::

::: {.pf-step #mod}

$\abs{f(z)} = 1$ for $\abs{z} = 1$.

::: pf-proof

For $\abs{z} = 1$, $\abs{1-\bar a_k z} = \abs{\bar z}\,\abs{1-\bar a_k z} = \abs{\bar z - \bar a_k} = \abs{z - a_k}$, so each factor has modulus $1$.

:::

:::

::: pf-step

$f(z) = b$ has exactly $n$ solutions in $\DD$, counted with multiplicity.

::: pf-proof

By step [](#mod){.pf-ref}, $\abs{(f - b) - f} = \abs{b} < 1 = \abs{f}$ on $\abs{z} = 1$. By step [](#hol){.pf-ref} and Rouché's theorem, $f - b$ and $f$ have the same number of zeros in $\DD$, counted with multiplicity. The zeros of $f$ in $\DD$ are $a_1, \ldots, a_n$, counted with multiplicity, so there are $n$ of them.

:::

:::

:::

:::
