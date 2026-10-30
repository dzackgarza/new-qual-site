---
schema: qual/card@1
id: P-UGAP09S-04
kind: problem
title: Absolute convergence of the termwise product of two series
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
Prove that if $\sum a_n$ converges and $\sum b_n$ converges absolutely, then
$$
\sum a_nb_n
$$
converges absolutely. What can be said if $\sum a_n$ and $\sum b_n$ are both only conditionally convergent?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $\sum a_n$ converges, then the sequence $(a_n)$ is bounded.


::: pf-proof

Convergence of the series implies
$$
a_n\to0.
$$
Every convergent sequence is bounded, so there is $M>0$ such that
$$
\abs{a_n}\le M
$$
for every $n$.

:::

:::

::: {.pf-step #s1-2}

If $\sum b_n$ converges absolutely, then
$$
\boxed{\sum_{n=1}^\infty a_nb_n\text{ converges absolutely}}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{a_nb_n}
\le
M\abs{b_n}.
$$
Hence
$$
\sum_{n=1}^\infty\abs{a_nb_n}
\le
M\sum_{n=1}^\infty\abs{b_n}
<\infty.
$$
The comparison test gives absolute convergence.

:::

:::

::: {.pf-step #s1-3}

If both original series are only conditionally convergent, the product
series can converge absolutely.


::: pf-proof

Take
$$
a_n=b_n=\frac{(-1)^n}{n}.
$$
Each of
$$
\sum a_n,\qquad \sum b_n
$$
converges by the alternating-series test but fails to converge absolutely.
However,
$$
a_nb_n=\frac1{n^2},
$$
so
$$
\sum a_nb_n
$$
converges absolutely.

:::

:::

::: {.pf-step #s1-4}

If both original series are only conditionally convergent, the product
series can also diverge.


::: pf-proof

Take
$$
a_n=b_n=\frac{(-1)^n}{\sqrt n}.
$$
Again both original series converge by the alternating-series test and fail
to converge absolutely. But
$$
a_nb_n=\frac1n,
$$
so the product series is the harmonic series and diverges.

:::

:::

::: {.pf-step #s1-5}

Thus under conditional convergence alone,
$$
\boxed{\text{no general convergence conclusion for }\sum a_nb_n\text{ is possible}}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives a conditionally-convergent pair whose product series converges
absolutely, while step [](#s1-4){.pf-ref} gives one whose product series diverges.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves the first assertion, and step [](#s1-5){.pf-ref} answers the conditional
case.

:::

:::

:::
