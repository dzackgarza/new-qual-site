---
schema: qual/card@1
id: P-UGAP13F-03
kind: problem
title: A power series whose interval of convergence is exactly $[2,4)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give an example, with proof, of a real power series that converges exactly on the interval $[2,4)$.
:::

::: {.solution}

Consider
$$
\boxed{
\sum_{n=1}^{\infty}
\frac{(x-3)^n}{n}.
}
$$

::: pf

::: {.pf-step #s1-1}

The radius of convergence is
$$
R=1.
$$


::: pf-proof

The coefficients are
$$
a_n=\frac1n.
$$
By the Cauchy--Hadamard formula,
$$
\frac1R
=
\limsup_{n\to\infty}
|a_n|^{1/n}
=
\lim_{n\to\infty}
n^{-1/n}
=
1.
$$
Hence
$$
R=1.
$$
Therefore the series converges absolutely for
$$
|x-3|<1,
$$
that is,
$$
2<x<4,
$$
and diverges for
$$
|x-3|>1.
$$

:::

:::

::: {.pf-step #s1-2}

At the left endpoint
$$
x=2,
$$
the series becomes
$$
\sum_{n=1}^{\infty}
\frac{(-1)^n}{n},
$$
which converges.


::: pf-proof

This is the alternating harmonic series.
The terms
$$
\frac1n
$$
decrease monotonically to $0$, so the alternating-series test gives
convergence.

:::

:::

::: {.pf-step #s1-3}

At the right endpoint
$$
x=4,
$$
the series becomes
$$
\sum_{n=1}^{\infty}
\frac1n,
$$
which diverges.


::: pf-proof

This is the harmonic series.

:::

:::

::: {.pf-step #s1-4}

For
$$
x<2
\quad\text{or}\quad
x>4,
$$
the series diverges.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
|x-3|>1.
$$
Then
$$
\left|
\frac{(x-3)^n}{n}
\right|
$$
does not tend to $0$; indeed the exponential factor
$$
|x-3|^n
$$
dominates the linear denominator $n$.
Therefore the necessary term test fails.

:::

:::

::: {.pf-step #s1-5}

Hence the exact interval of convergence is
$$
\boxed{
[2,4).
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} show:

- convergence for every
  $$
  2<x<4;
  $$
- convergence at
  $$
  x=2;
  $$
- divergence at
  $$
  x=4;
  $$
- divergence outside
  $$
  [2,4].
  $$

Thus the convergence set is exactly
$$
[2,4).
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required example and proof.

:::

:::

:::
