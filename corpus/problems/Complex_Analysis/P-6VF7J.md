---
schema: qual/card@1
id: P-6VF7J
kind: problem
title: 'Power series of radius $1$: convergence on the circle versus analyticity on
  the circle'
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is analytic on a region $\Omega$ such that $\DD \subseteq \Omega \subseteq \CC$ and $f(z) = \sum_{n=0}^\infty a_n z^n$ is a power series with radius of convergence exactly 1.

(a) Give an example of such an $f$ that converges at every point of $S^1$.

(b) Give an example of such an $f$ which is analytic at $1$ but $\sum_{n=0}^\infty a_n$ diverges.

(c) Prove that $f$ can not be analytic at *every* point of $S^1$.
:::

::: {.solution}

::: pf

::: pf-step
(a) $f(z)=\sum_{n\ge1} \frac{z^n}{n^2}$ on $\Omega=\DD$ has radius of convergence $1$ and converges at every point of $S^1$.

::: pf-proof
$\limsup_{n\to\infty}(1/n^2)^{1/n}=1$, so the radius is $1$.
For $\abs{z}=1$ the series converges absolutely by comparison with $\sum n^{-2}$.
:::

:::

::: pf-step
(b) $f(z)=\frac{1}{1+z}=\sum_{n\ge0}(-1)^nz^n$ on $\Omega=\CC\setminus\theset{-1}$ is analytic at $1$, and $\sum_n a_n=\sum_n(-1)^n$ diverges.

::: pf-proof
The Taylor series at $0$ has radius exactly $1$, because $f$ is holomorphic on $\DD$ and unbounded near $-1$.
$f$ is holomorphic near $z=1$, and the partial sums of $\sum(-1)^n$ alternate between $1$ and $0$.
:::

:::

::: pf-step
(c) $f$ is not analytic at every point of $S^1$.

::: pf-proof
Suppose $f$ were analytic at every point of $S^1$, so that its domain of analyticity is an open set $U$ containing the compact set $\overline\DD$.
Then $\overline\DD$ has positive distance from $\CC\setminus U$, so $U\supseteq\theset{\abs{z}<1+\varepsilon}$ for some $\varepsilon>0$.
The Taylor series of $f$ at $0$ then has radius of convergence at least $1+\varepsilon$, contrary to the hypothesis.
:::

:::

:::

:::
