---
schema: qual/card@1
id: P-UCLARA16S-02
kind: problem
title: Almost everywhere convergence of $\sum n^{-1/2}f(x-\sqrt n)$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1(\mathbb R)$. Show that the series
\[
\sum_{n=1}^{\infty}\frac1{\sqrt n}f(x-\sqrt n)
\]
converges absolutely for almost all $x\in\mathbb R$.
:::

Define
\[
G(x)
\coloneqq
\sum_{n=1}^{\infty}
\frac1{\sqrt n}
|f(x-\sqrt n)|.
\]

::: pf

::: pf-step

For every integer $M$,
\[
\int_M^{M+1}G(x)\,dx
<\infty.
\]


::: pf-proof

::: pf-step

Tonelli's theorem gives
\[
\int_M^{M+1}G(x)\,dx
=
\sum_{n=1}^{\infty}
\frac1{\sqrt n}
\int_{M-\sqrt n}^{M+1-\sqrt n}
|f(y)|\,dy.
\]


::: pf-proof

The summands defining $G$ are nonnegative and measurable. Hence Tonelli's theorem allows interchange of the sum and integral:
\[
\begin{aligned}
\int_M^{M+1}G(x)\,dx
&=
\sum_{n=1}^{\infty}
\frac1{\sqrt n}
\int_M^{M+1}|f(x-\sqrt n)|\,dx.
\end{aligned}
\]
The change of variables
\[
y=x-\sqrt n
\]
gives the stated formula.

:::

:::

::: pf-step

For each integer $k\ge1$, the integers $n$ satisfying
\[
k\le\sqrt n<k+1
\]
are at most $2k+1$ in number, satisfy
\[
\frac1{\sqrt n}\le\frac1k,
\]
and have
\[
[M-\sqrt n,M+1-\sqrt n]
\subset
[M-k-1,M+1-k].
\]


::: pf-proof

The condition is equivalent to
\[
k^2\le n<(k+1)^2,
\]
which contains exactly
\[
(k+1)^2-k^2=2k+1
\]
integer values of $n$. The weight bound follows from $\sqrt n\ge k$. The interval containment follows from
\[
k\le\sqrt n<k+1.
\]

:::

:::

::: pf-step

The contribution of all indices with
\[
k\le\sqrt n<k+1
\]
to the sum in step <2>1 is at most
\[
3
\int_{M-k-1}^{M+1-k}|f(y)|\,dy.
\]


::: pf-proof

By step <2>2, the group contains at most $2k+1$ terms, each with coefficient at most $1/k$, and every integration interval is contained in
\[
[M-k-1,M+1-k].
\]
Therefore the group is bounded by
\[
\frac{2k+1}{k}
\int_{M-k-1}^{M+1-k}|f(y)|\,dy.
\]
Since
\[
\frac{2k+1}{k}
\le3
\qquad
(k\ge1),
\]
the claim follows.

:::

:::

::: pf-step

One has
\[
\sum_{k=1}^{\infty}
\int_{M-k-1}^{M+1-k}|f(y)|\,dy
\le
2\|f\|_{L^1}.
\]


::: pf-proof

Split each interval into two unit intervals:
\[
[M-k-1,M+1-k]
=
[M-k-1,M-k]
\cup
[M-k,M+1-k].
\]
As $k$ varies, the intervals in each of the two families have disjoint interiors. Hence
\[
\sum_{k=1}^{\infty}
\int_{M-k-1}^{M-k}|f(y)|\,dy
\le
\|f\|_1
\]
and
\[
\sum_{k=1}^{\infty}
\int_{M-k}^{M+1-k}|f(y)|\,dy
\le
\|f\|_1.
\]
Adding the two estimates gives the result.

:::

:::

::: pf-qed

Combining steps <2>1 through <2>4,
\[
\int_M^{M+1}G(x)\,dx
\le
6\|f\|_1
<\infty.
\]
This proves step <1>1.

:::

:::

:::

::: pf-step

For every integer $M$,
\[
G(x)<\infty
\]
for almost every $x\in[M,M+1]$.


::: pf-proof

The function $G$ is nonnegative and measurable. By step <1>1 it is integrable on $[M,M+1]$. A nonnegative integrable function is finite almost everywhere.

:::

:::

::: pf-step

One has
\[
G(x)<\infty
\]
for almost every $x\in\mathbb R$.


::: pf-proof

The real line is the countable union
\[
\mathbb R
=
\bigcup_{M\in\mathbb Z}[M,M+1].
\]
By step <1>2, the exceptional set in each interval has measure zero. A countable union of null sets is null.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum_{n=1}^{\infty}
\frac1{\sqrt n}f(x-\sqrt n)
\text{ converges absolutely for almost every }x\in\mathbb R.
}
\]


::: pf-proof

By definition,
\[
G(x)
=
\sum_{n=1}^{\infty}
\left|
\frac1{\sqrt n}
f(x-\sqrt n)
\right|.
\]
Step <1>3 says this sum is finite for almost every $x$, which is exactly absolute convergence of the original series.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
