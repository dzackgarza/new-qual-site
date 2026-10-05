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
\[
\sum a_nb_n
\]
converges absolutely. What can be said if $\sum a_n$ and $\sum b_n$ are both only conditionally convergent?
:::

::: {.solution}
<1>1. If $\sum a_n$ converges, then the sequence $(a_n)$ is bounded.

::: {.proof}
Convergence of the series implies
\[
a_n\to0.
\]
Every convergent sequence is bounded, so there is $M>0$ such that
\[
|a_n|\le M
\]
for every $n$.
:::

<1>2. If $\sum b_n$ converges absolutely, then
\[
\boxed{\sum_{n=1}^\infty a_nb_n\text{ converges absolutely}}.
\]

::: {.proof}
By step <1>1,
\[
|a_nb_n|
\le
M|b_n|.
\]
Hence
\[
\sum_{n=1}^\infty|a_nb_n|
\le
M\sum_{n=1}^\infty|b_n|
<\infty.
\]
The comparison test gives absolute convergence.
:::

<1>3. If both original series are only conditionally convergent, the product
series can converge absolutely.

::: {.proof}
Take
\[
a_n=b_n=\frac{(-1)^n}{n}.
\]
Each of
\[
\sum a_n,\qquad \sum b_n
\]
converges by the alternating-series test but fails to converge absolutely.
However,
\[
a_nb_n=\frac1{n^2},
\]
so
\[
\sum a_nb_n
\]
converges absolutely.
:::

<1>4. If both original series are only conditionally convergent, the product
series can also diverge.

::: {.proof}
Take
\[
a_n=b_n=\frac{(-1)^n}{\sqrt n}.
\]
Again both original series converge by the alternating-series test and fail
to converge absolutely. But
\[
a_nb_n=\frac1n,
\]
so the product series is the harmonic series and diverges.
:::

<1>5. Thus under conditional convergence alone,
\[
\boxed{\text{no general convergence conclusion for }\sum a_nb_n\text{ is possible}}.
\]

::: {.proof}
Step <1>3 gives a conditionally-convergent pair whose product series converges
absolutely, while step <1>4 gives one whose product series diverges.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves the first assertion, and step <1>5 answers the conditional
case.
:::
:::
