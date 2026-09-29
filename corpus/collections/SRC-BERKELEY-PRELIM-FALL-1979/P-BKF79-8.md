---
schema: qual/card@1
id: P-BKF79-8
kind: problem
title: A harmonic-block sum converges to $\log2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Reindexed the harmonic block as the right-endpoint Riemann sum
    (1/n) sum_{j=1}^n 1/(1+j/n) for the continuous function
    1/(1+x) on [0,1], whose integral is log 2.
---

::: {.problem}
Prove that
\[
\lim_{n\to\infty}
\left(
\frac1{n+1}+\frac1{n+2}+\cdots+\frac1{2n}
\right)
=\log2.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #sum-riemann-form}
For every $n\geq1$,
$$
\sum_{k=n+1}^{2n}\frac1k
=
\frac1n
\sum_{j=1}^{n}
\frac{1}{1+j/n}.
$$

::: pf-proof
Put $k=n+j$. Then $k$ runs from $n+1$ through $2n$ exactly when $j$
runs from $1$ through $n$, and
$$
\frac1{n+j}
=
\frac1n\frac1{1+j/n}.
$$
Summing gives the identity.
:::

:::

::: {.pf-step #riemann-sum-converges}
The right-hand side in step [](#sum-riemann-form){.pf-ref} converges to
$$
\int_0^1\frac{dx}{1+x}.
$$

::: pf-proof
The function
$$
g(x)=\frac1{1+x}
$$
is continuous on $[0,1]$. The expression
$$
\frac1n
\sum_{j=1}^{n}g\left(\frac jn\right)
$$
is its right-endpoint Riemann sum for the uniform partition of
$[0,1]$ into $n$ subintervals. Hence it converges to the displayed
integral.
:::

:::

::: {.pf-step #integral-value}
One has
$$
\int_0^1\frac{dx}{1+x}=\log2.
$$

::: pf-proof
Direct integration gives
$$
\int_0^1\frac{dx}{1+x}
=
\left[\log(1+x)\right]_0^1
=
\log2.
$$
:::

:::

::: {.pf-step #final-limit}
Therefore
$$
\boxed{
\lim_{n\to\infty}
\left(
\frac1{n+1}+\frac1{n+2}+\cdots+\frac1{2n}
\right)
=
\log2.
}
$$

::: pf-proof
Combine steps [](#sum-riemann-form){.pf-ref}, [](#riemann-sum-converges){.pf-ref}, and [](#integral-value){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-limit){.pf-ref} is the required conclusion.
:::

:::
:::
