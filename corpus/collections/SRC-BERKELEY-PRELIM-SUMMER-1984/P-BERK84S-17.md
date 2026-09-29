---
schema: qual/card@1
id: P-BERK84S-17
kind: problem
title: Entire growth after factorial damping of coefficients
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 17 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the coefficient estimate from absolute convergence at radius r and the resulting exponential majorant.
---

::: {.problem}
Suppose

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }
$$

has radius of convergence $R > 0$ . Show that

$$
h ( z ) = \sum _ { n = 0 } ^ { \infty } { \frac { a _ { n } z ^ { n } } { n ! } }
$$

is entire and that for $0 < r < R$ , there is a constant M such that

$$
| h ( z ) | \leqslant M e ^ { | z | / r } .
$$
:::

::: {.solution}
Fix $r$ with $0<r<R$.

::: pf

::: {.pf-step #s1}

There is a constant $C<\infty$ such that
\[
|a_n|\le C r^{-n}
\qquad(n\ge0).
\]

::: pf-proof

Because $r<R$, the power series for $f$ converges absolutely at $z=r$.
Therefore
\[
C:=\sum_{n=0}^{\infty}|a_n|r^n<\infty.
\]
Each summand is nonnegative, so for every $n$,
\[
|a_n|r^n\le C.
\]
Since $r>0$, this gives $|a_n|\le Cr^{-n}$.

:::

:::

::: {.pf-step #s2}

The series defining $h$ converges absolutely for every $z\in\mathbb C$.

::: pf-proof

By step [](#s1){.pf-ref}, for every $z\in\mathbb C$,
\[
\sum_{n=0}^{\infty}\left|\frac{a_nz^n}{n!}\right|
\le C\sum_{n=0}^{\infty}\frac{(|z|/r)^n}{n!}
=C e^{|z|/r}<\infty.
\]
Thus the power series for $h$ has infinite radius of convergence.
Hence $h$ is entire.

:::

:::

::: pf-step

The required growth estimate holds.

::: pf-proof

The same estimate from step [](#s2){.pf-ref} gives directly
\[
|h(z)|
\le\sum_{n=0}^{\infty}\left|\frac{a_nz^n}{n!}\right|
\le C e^{|z|/r}.
\]
Thus the statement holds with $M=C$.

:::

:::

:::

:::
