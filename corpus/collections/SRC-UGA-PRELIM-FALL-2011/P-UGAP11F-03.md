---
schema: qual/card@1
id: P-UGAP11F-03
kind: problem
title: A power series whose interval of convergence is exactly $(1,3]$
classification:
  areas: [prelim]
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give an example, with proof, of a real power series that converges exactly on the interval $(1,3]$.
:::

::: {.solution}

Consider
$$
\boxed{
\sum_{n=1}^\infty
\frac{(-1)^n}{n}(x-2)^n}.
$$

::: pf

::: {.pf-step #s1-1}

The radius of convergence is $1$.


::: pf-proof

The coefficients are
$$
a_n=\frac{(-1)^n}{n}.
$$
Hence
$$
\limsup_{n\to\infty}\abs{a_n}^{1/n}
=
\lim_{n\to\infty}n^{-1/n}
=1.
$$
By the Cauchy--Hadamard formula, the radius of convergence is
$$
R=1.
$$
Thus the series converges absolutely for
$$
\abs{x-2}<1,
$$
i.e. for $1<x<3$, and diverges for $\abs{x-2}>1$.

:::

:::

::: {.pf-step #s1-2}

At $x=3$, the series converges.


::: pf-proof

Substituting $x=3$ gives
$$
\sum_{n=1}^\infty
\frac{(-1)^n}{n},
$$
the alternating harmonic series, which converges by the alternating-series test.

:::

:::

::: {.pf-step #s1-3}

At $x=1$, the series diverges.


::: pf-proof

Substituting $x=1$ gives
$$
\sum_{n=1}^\infty
\frac{(-1)^n}{n}(-1)^n
=
\sum_{n=1}^\infty\frac1n,
$$
which is the harmonic series and diverges.

:::

:::

::: {.pf-step #s1-4}

Therefore the set of real points where the power series converges is exactly
$$
\boxed{(1,3]}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives convergence on $(1,3)$ and divergence outside $[1,3]$. Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} determine the two endpoints.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested example and its exact interval of convergence.

:::

:::

:::
