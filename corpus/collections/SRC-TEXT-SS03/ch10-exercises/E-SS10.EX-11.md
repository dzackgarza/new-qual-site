---
schema: qual/card@1
id: E-SS10.EX-11
kind: exercise
title: "SS 10.11: Generating functions for divisor-power sums"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
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
<1>1. Geometric series expansion:
<2>1. For any $|z| < 1$ and integer $n \ge 1$, we have $|z^n| = |z|^n < 1$.
The term $\frac{z^n}{1 - z^n}$ expands as a convergent geometric series:
\[
\frac{z^n}{1 - z^n} = \sum_{k=1}^\infty (z^n)^k = \sum_{k=1}^\infty z^{nk}.
\]
Proof: geometric series formula for $|z^n| < 1$.
<2>2. Multiplying by $n^\ell$:
\[
\frac{n^\ell z^n}{1 - z^n} = \sum_{k=1}^\infty n^\ell z^{nk}.
\]
Proof: scalar multiplication on absolutely convergent series.

<1>2. Absolute convergence of the double series:
<2>1. Set $r = |z| < 1$.
Using the bound $\frac{r^n}{1 - r^n} \le \frac{r^n}{1 - r}$ for all $n \ge 1$:
\[
\sum_{n=1}^\infty \sum_{k=1}^\infty n^\ell |z|^{nk} = \sum_{n=1}^\infty n^\ell \frac{r^n}{1 - r^n} \le \frac{1}{1 - r} \sum_{n=1}^\infty n^\ell r^n.
\]
Proof: termwise bound with $1 - r^n \ge 1 - r$.
<2>2. By the ratio test, the power series $\sum_{n=1}^\infty n^\ell r^n$ converges for all $r \in [0, 1)$.
Thus the double series $\sum_{n=1}^\infty \sum_{k=1}^\infty n^\ell z^{nk}$ converges absolutely.
Proof: ratio test $\lim_{n \to \infty} \frac{(n+1)^\ell r^{n+1}}{n^\ell r^n} = r < 1$.

<1>3. Rearrangement and identification of divisor sums:
<2>1. Because the double series is absolutely convergent, we may rearrange terms by setting $m = nk \ge 1$:
\[
\sum_{n=1}^\infty \frac{n^\ell z^n}{1 - z^n} = \sum_{n=1}^\infty \sum_{k=1}^\infty n^\ell z^{nk} = \sum_{m=1}^\infty \left( \sum_{n \mid m} n^\ell \right) z^m.
\]
Proof: Fubini's Theorem / absolute convergence allows regrouping over the bijection $(n, k) \leftrightarrow (n, m/n)$.
<2>2. By definition of the divisor-power sum function:
\[
\sigma_\ell(m) = \sum_{d \mid m} d^\ell.
\]
Therefore the coefficient of $z^m$ is precisely $\sigma_\ell(m)$.
Proof: definition of $\sigma_\ell$.

<1>4. Conclusion:
For all $|z| < 1$:
\[
\sum_{n=1}^\infty \sigma_\ell(n) z^n = \sum_{n=1}^\infty \frac{n^\ell z^n}{1 - z^n}.
\]
Q.E.D.
Proof: <1>1 through <1>3.
:::
