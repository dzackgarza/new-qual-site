---
schema: qual/card@1
id: P-6PMCN
kind: problem
title: Laurent series of $\frac{1}{z}+\frac{1}{z^2-1}$ on the largest annuli of validity
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
relations: []
review: draft
---

::: {.problem}
Let $\displaystyle f(z) = \frac{1}{z} + \frac{1}{z^2 -1}$.
Find all the Laurent series of $f$ and describe the largest annuli in which these series are valid.
:::

::: {.solution}
We expand about $0$.
The singularities of $f$ are $-1$, $0$ and $1$, so the maximal annuli centred at $0$ on which $f$ is holomorphic are $0<\abs{z}<1$ and $\abs{z}>1$.

::: pf

::: pf-step
On $0<\abs{z}<1$,
$$
\boxed{f(z)=\frac{1}{z}-\sum_{n=0}^\infty z^{2n} = \frac{1}{z}-1-z^2-z^4-\cdots}.
$$

::: pf-proof
For $\abs{z}<1$, $\frac{1}{z^2-1}=-\frac{1}{1-z^2}=-\sum_{n\ge0} z^{2n}$ by the geometric series.
:::

:::

::: pf-step
On $\abs{z}>1$,
$$
\boxed{f(z)=\frac{1}{z}+\sum_{n=0}^\infty z^{-2n-2} = \frac{1}{z}+\frac{1}{z^2}+\frac{1}{z^4}+\frac{1}{z^6}+\cdots}.
$$

::: pf-proof
For $\abs{z}>1$, $\frac{1}{z^2-1}=\frac{1}{z^2}\cdot\frac{1}{1-z^{-2}}=\sum_{n\ge0} z^{-2n-2}$ by the geometric series.
:::

:::

:::

:::
