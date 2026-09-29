---
schema: qual/card@1
id: P-BKF15-1A
kind: problem
title: Convergence and sum of the binomial series in $\bigl(2x/(1+x^2)\bigr)^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: the series
    is the binomial series for (1-t)^(-1/2), with
    t=(2x/(1+x^2))^2, and the absolute value in the resulting square root is
    essential.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the convergence condition, divergence at x=+-1, and the
    simplification sqrt((1-x^2)^2)=|1-x^2|.
---

::: {.problem}
Find the real values of $x$ for which

$$
\sum _ { n = 0 } ^ { \infty } { \frac { ( 1 / 2 ) ( 3 / 2 ) \cdots ( ( 2 n - 1 ) / 2 ) } { n ! } } { ( \frac { 2 x } { 1 + x ^ { 2 } } ) } ^ { 2 n } = 1 + { \frac { 1 } { 2 } } { \bigl ( } { \frac { 2 x } { 1 + x ^ { 2 } } } { \bigr ) } ^ { 2 } + { \frac { 1 } { 2 } } { \frac { 3 } { 4 } } { \bigl ( } { \frac { 2 x } { 1 + x ^ { 2 } } } { \bigr ) } ^ { 4 } + \cdots
$$

converges and sum it for these numbers.
Caution: there is something unusual about the sum of this series.
:::

::: {.solution}
Put
$$
t\coloneqq\left(\frac{2x}{1+x^2}\right)^2.
$$

::: pf

::: {.pf-step #s1}

For every real $x$,
$$
0\le t\le1,
$$
with $t=1$ if and only if $x=\pm1$.

::: pf-proof

Since
$$
(1+x^2)^2-4x^2=(1-x^2)^2\ge0,
$$
one has
$$
\abs{\frac{2x}{1+x^2}}\le1.
$$
Equality holds exactly when $(1-x^2)^2=0$, namely when $x=\pm1$.
Squaring gives the claim.

:::

:::

::: {.pf-step #s2}

For $\abs{t}<1$,
$$
\sum_{n=0}^{\infty}
\frac{(1/2)(3/2)\cdots((2n-1)/2)}{n!}t^n
=
(1-t)^{-1/2}.
$$

::: pf-proof

The generalized binomial theorem gives
$$
(1-t)^{-1/2}
=
\sum_{n=0}^{\infty}
\frac{(1/2)_n}{n!}t^n,
\qquad
\abs{t}<1,
$$
where
$$
(1/2)_n
=
\frac12\frac32\cdots\frac{2n-1}{2}
$$
for $n\ge1$ and $(1/2)_0=1$. These are exactly the coefficients in
the given series.

:::

:::

::: {.pf-step #s3}

The series diverges when $x=\pm1$.

::: pf-proof

By step [](#s1){.pf-ref}, these are precisely the cases $t=1$. Let
$$
a_n\coloneqq
\frac{(1/2)(3/2)\cdots((2n-1)/2)}{n!}.
$$
Then
$$
a_n
=
\frac{(2n)!}{4^n(n!)^2}
=
\frac1{4^n}\binom{2n}{n}.
$$
Since
$$
4^n
=
\sum_{k=0}^{2n}\binom{2n}{k}
\le
(2n+1)\binom{2n}{n},
$$
we have
$$
a_n\ge\frac1{2n+1}.
$$
Thus $\sum_{n\ge0}a_n$ diverges by comparison with the harmonic
series.

:::

:::

::: {.pf-step #s4}

The given series converges exactly for
$$
\boxed{x\in\RR\setminus\{-1,1\}}.
$$

::: pf-proof

If $x\ne\pm1$, step [](#s1){.pf-ref} gives $0\le t<1$, so convergence follows from
step [](#s2){.pf-ref}. Step [](#s3){.pf-ref} excludes the two remaining real values.

:::

:::

::: {.pf-step #s5}

For every $x\ne\pm1$, the sum is
$$
\boxed{\frac{1+x^2}{\abs{1-x^2}}}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\begin{aligned}
(1-t)^{-1/2}
&=
\left(
1-\frac{4x^2}{(1+x^2)^2}
\right)^{-1/2}\\
&=
\left(
\frac{(1-x^2)^2}{(1+x^2)^2}
\right)^{-1/2}\\
&=
\frac{1+x^2}{\abs{1-x^2}}.
\end{aligned}
$$
The square root is the nonnegative real square root, so the sum is
$(1+x^2)/(1-x^2)$ for $\abs{x}<1$ and $(1+x^2)/(x^2-1)$ for
$\abs{x}>1$; the sum is not given by one rational function of $x$.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the complete convergence set and the sum on
that set.

:::

:::

:::
