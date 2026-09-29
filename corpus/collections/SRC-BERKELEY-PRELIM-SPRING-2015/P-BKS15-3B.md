---
schema: qual/card@1
id: P-BKS15-3B
kind: problem
title: A summable sequence eventually dominating countably many summable sequences
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the finite-tail truncations, finiteness of each x_n, boundedness of the partial sums of sum x_n, and eventual domination of every original series.
---

::: {.problem}
Suppose
$$
a_{1,1}+a_{1,2}+\cdots,\qquad a_{2,1}+a_{2,2}+\cdots,\qquad\ldots
$$
is a countable collection of convergent series of nonnegative real numbers.
Show that there is a convergent series $x_1+x_2+\cdots$ of real numbers converging more slowly than any of the given series, in the sense that for every $m$ one has $x_n\ge a_{m,n}$ for all sufficiently large $n$.

Hint: the problem is not affected by changing a finite number of terms of each given series.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For each $m\geq1$, choose an integer $N_m$ such that
$$
\sum_{n=N_m}^{\infty}a_{m,n}
\leq
2^{-m}.
$$

::: pf-proof

The series
$$
\sum_{n=1}^{\infty}a_{m,n}
$$
converges and has nonnegative terms, so its tails tend to $0$. Hence a tail with sum at most $2^{-m}$ exists.

:::

:::

::: {.pf-step #s2}

Define
$$
b_{m,n}
\coloneqq
\begin{cases}
0,&n<N_m,\\
a_{m,n},&n\geq N_m.
\end{cases}
$$
Then
$$
\sum_{n=1}^{\infty}b_{m,n}
\leq
2^{-m},
$$
and $b_{m,n}=a_{m,n}$ for all sufficiently large $n$.

::: pf-proof

This follows directly from the definition and step [](#s1){.pf-ref}. Only the finitely many terms with $n<N_m$ have been changed.

:::

:::

::: {.pf-step #s3}

For every $n\geq1$, the series
$$
x_n
\coloneqq
\sum_{m=1}^{\infty}b_{m,n}
$$
converges to a finite nonnegative real number.

::: pf-proof

For every $m,n$,
$$
0
\leq
b_{m,n}
\leq
\sum_{k=1}^{\infty}b_{m,k}
\leq
2^{-m}
$$
by step [](#s2){.pf-ref}. Therefore
$$
0
\leq
\sum_{m=1}^{M}b_{m,n}
\leq
\sum_{m=1}^{M}2^{-m}
<
1
$$
for every $M$. The increasing partial sums are bounded, so they converge.

:::

:::

::: {.pf-step #s4}

The series
$$
\sum_{n=1}^{\infty}x_n
$$
converges.

::: pf-proof

Fix $N\geq1$. By step [](#s3){.pf-ref} and nonnegativity,
$$
\begin{aligned}
\sum_{n=1}^{N}x_n
&=
\lim_{M\to\infty}
\sum_{n=1}^{N}\sum_{m=1}^{M}b_{m,n}\\
&=
\lim_{M\to\infty}
\sum_{m=1}^{M}\sum_{n=1}^{N}b_{m,n}\\
&\leq
\lim_{M\to\infty}
\sum_{m=1}^{M}2^{-m}\\
&\leq
1.
\end{aligned}
$$
Thus the partial sums of the nonnegative series $\sum_nx_n$ are bounded above by $1$, so the series converges.

:::

:::

::: {.pf-step #s5}

For every fixed $m\geq1$,
$$
x_n\geq a_{m,n}
$$
for all $n\geq N_m$.

::: pf-proof

If $n\geq N_m$, then step [](#s2){.pf-ref} gives
$$
b_{m,n}=a_{m,n}.
$$
Since all $b_{j,n}$ are nonnegative,
$$
x_n
=
\sum_{j=1}^{\infty}b_{j,n}
\geq
b_{m,n}
=
a_{m,n}.
$$

:::

:::

::: {.pf-step #s6}

Therefore the convergent series
$$
\boxed{x_1+x_2+\cdots}
$$
converges more slowly than every given series in the required sense.

::: pf-proof

Convergence is step [](#s4){.pf-ref}. For each $m$, step [](#s5){.pf-ref} supplies the threshold $N_m$ beyond which $x_n\geq a_{m,n}$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is exactly the required conclusion.

:::

:::

:::
