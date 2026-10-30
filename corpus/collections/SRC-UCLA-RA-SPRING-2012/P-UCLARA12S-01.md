---
schema: qual/card@1
id: P-UCLARA12S-01
kind: problem
title: 'Modes of convergence in $L^3$'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(f_n)$ be a sequence in $L^3([0,1])$.
Determine whether each statement is true or false:

(a) If $f_n\to f$ almost everywhere, then some subsequence converges to $f$ in $L^3$.

(b) If $f_n\to f$ in $L^3$, then some subsequence converges almost everywhere.

(c) If $f_n\to f$ in measure, then $f_n\to f$ in $L^3$.

(d) If $f_n\to f$ in $L^3$, then $f_n\to f$ in measure.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (a) is false.


::: pf-proof

Define
$$
f_n(x)=n\mathbf 1_{[0,1/n]}(x).
$$
For every $x>0$, one has $f_n(x)=0$ for all sufficiently large $n$, so
$$
f_n(x)\longrightarrow0
$$
for almost every $x\in[0,1]$.

However,
$$
\norm{f_n}_3^3
=
\int_0^{1/n}n^3\,dx
=
n^2.
$$
Thus
$$
\norm{f_n}_3=n^{2/3},
$$
which does not tend to $0$ along any subsequence. Hence no subsequence converges to the almost-everywhere limit $0$ in $L^3$.

:::

:::

::: {.pf-step #s1-2}

Statement (b) is true.


::: pf-proof

Assume
$$
f_n\longrightarrow f
$$
in $L^3([0,1])$. Choose inductively a subsequence $(f_{n_k})$ such that
$$
\norm{f_{n_k}-f}_3^3<2^{-k}.
$$
Then Tonelli's theorem gives
$$
\begin{aligned}
\int_0^1
\sum_{k=1}^{\infty}
\abs{f_{n_k}(x)-f(x)}^3\,dx
&=
\sum_{k=1}^{\infty}
\norm{f_{n_k}-f}_3^3\\
&<
\sum_{k=1}^{\infty}2^{-k}
<\infty.
\end{aligned}
$$
Therefore
$$
\sum_{k=1}^{\infty}
\abs{f_{n_k}(x)-f(x)}^3
<
\infty
$$
for almost every $x$. For each such $x$, the terms of this convergent nonnegative series tend to $0$, so
$$
f_{n_k}(x)\longrightarrow f(x).
$$
Thus a subsequence converges almost everywhere.

:::

:::

::: {.pf-step #s1-3}

Statement (c) is false.


::: pf-proof

Use the same sequence as in step [](#s1-1){.pf-ref}:
$$
f_n=n\mathbf 1_{[0,1/n]}.
$$
For any $\varepsilon>0$ and all $n>\varepsilon$,
$$
\{x:\abs{f_n(x)}>\varepsilon\}
=
[0,1/n],
$$
whose measure is $1/n\to0$. Hence
$$
f_n\longrightarrow0
$$
in measure.

But step [](#s1-1){.pf-ref} gives
$$
\norm{f_n}_3=n^{2/3}\not\to0.
$$
Thus convergence in measure does not imply convergence in $L^3$.

:::

:::

::: {.pf-step #s1-4}

Statement (d) is true.


::: pf-proof

Assume
$$
\norm{f_n-f}_3\longrightarrow0.
$$
Fix $\varepsilon>0$. On the set
$$
E_{n,\varepsilon}
\coloneqq
\{x:\abs{f_n(x)-f(x)}>\varepsilon\},
$$
one has
$$
\abs{f_n-f}^3>\varepsilon^3.
$$
Therefore
$$
\begin{aligned}
\norm{f_n-f}_3^3
&\ge
\int_{E_{n,\varepsilon}}
\abs{f_n-f}^3\,dx\\
&\ge
\varepsilon^3
m(E_{n,\varepsilon}).
\end{aligned}
$$
Hence
$$
m(E_{n,\varepsilon})
\le
\varepsilon^{-3}
\norm{f_n-f}_3^3
\longrightarrow0.
$$
This is convergence in measure.

:::

:::

::: {.pf-step #s1-5}

The answers are
$$
\boxed{
\text{(a) false,\quad
(b) true,\quad
(c) false,\quad
(d) true.}
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish the four assertions respectively.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} records the complete classification.

:::

:::

:::
