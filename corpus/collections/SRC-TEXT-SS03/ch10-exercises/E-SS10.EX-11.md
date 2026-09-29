---
schema: qual/card@1
id: E-SS10.EX-11
kind: problem
title: Lambert series for the divisor-power sums $\sigma_\ell(n)$
classification:
  areas:
  - complex-analysis
  topics:
  - Number Theory
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
11. Recall from Problem 2 in Chapter 2, that

$$
\sum_ {n = 1} ^ {\infty} d (n) z ^ {n} = \sum_ {n = 1} ^ {\infty} \frac {z ^ {n}}{1 - z ^ {n}}, \quad | z | <   1
$$

where $d ( n )$ denotes the number of divisors of $n$ .

More generally, show that

$$
\sum_ {n = 1} ^ {\infty} \sigma_ {\ell} (n) z ^ {n} = \sum_ {n = 1} ^ {\infty} \frac {n ^ {\ell} z ^ {n}}{1 - z ^ {n}}, \quad | z | <   1
$$

where $\sigma _ { \ell } ( n )$ is the sum of the $\ell ^ { \mathrm { t h } }$ powers of divisors of $n .$ .
:::

::: {.solution}
Fix $\abs z<1$ and put $r=\abs z$.

::: pf

::: {.pf-step #s1}

For every $n\ge1$, $\dfrac{n^\ell z^n}{1 - z^n} = \displaystyle\sum_{k=1}^\infty n^\ell z^{nk}$.

::: pf-proof

Since $\abs{z^n} = r^n < 1$, the geometric series gives $\frac{z^n}{1 - z^n} = \sum_{k\ge1} z^{nk}$.

:::

:::

::: {.pf-step #s2}

The double series $\sum_{n\ge1} \sum_{k\ge1} n^\ell z^{nk}$ converges absolutely.

::: pf-proof

Using $\frac{r^n}{1 - r^n} \le \frac{r^n}{1 - r}$,
$$\sum_{n=1}^\infty \sum_{k=1}^\infty n^\ell r^{nk} = \sum_{n=1}^\infty n^\ell \frac{r^n}{1 - r^n} \le \frac{1}{1 - r} \sum_{n=1}^\infty n^\ell r^n,$$
and $\sum n^\ell r^n$ converges by the ratio test.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref} the double series may be summed along the values $m = nk$. By step [](#s1){.pf-ref},
$$\sum_{n=1}^\infty \frac{n^\ell z^n}{1 - z^n} = \sum_{n=1}^\infty \sum_{k=1}^\infty n^\ell z^{nk} = \sum_{m=1}^\infty \Bigl( \sum_{n \mid m} n^\ell \Bigr) z^m = \sum_{m=1}^\infty \sigma_\ell(m) z^m.$$

:::

:::

:::
