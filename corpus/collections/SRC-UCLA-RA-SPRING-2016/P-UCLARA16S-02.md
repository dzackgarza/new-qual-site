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
Let $f\in L^1(\RR)$. Show that the series
$$
\sum_{n=1}^{\infty}\frac1{\sqrt n}f(x-\sqrt n)
$$
converges absolutely for almost all $x\in\RR$.
:::

::: {.solution}

Define
$$
G(x)
\coloneqq
\sum_{n=1}^{\infty}
\frac1{\sqrt n}
\abs{f(x-\sqrt n)}.
$$

::: pf

::: {.pf-step #s1}

For every integer $M$,
$$
\int_M^{M+1}G(x)\,dx
<\infty.
$$


::: pf-proof

::: {.pf-step #s1-1}

Tonelli's theorem gives
$$
\int_M^{M+1}G(x)\,dx
=
\sum_{n=1}^{\infty}
\frac1{\sqrt n}
\int_{M-\sqrt n}^{M+1-\sqrt n}
\abs{f(y)}\,dy.
$$


::: pf-proof

The summands defining $G$ are nonnegative and measurable. Hence Tonelli's theorem allows interchange of the sum and integral:
$$
\begin{aligned}
\int_M^{M+1}G(x)\,dx
&=
\sum_{n=1}^{\infty}
\frac1{\sqrt n}
\int_M^{M+1}\abs{f(x-\sqrt n)}\,dx.
\end{aligned}
$$
The change of variables
$$
y=x-\sqrt n
$$
gives the stated formula.

:::

:::

::: {.pf-step #s1-2}

For each integer $k\ge1$, the integers $n$ satisfying
$$
k\le\sqrt n<k+1
$$
are at most $2k+1$ in number, satisfy
$$
\frac1{\sqrt n}\le\frac1k,
$$
and have
$$
[M-\sqrt n,M+1-\sqrt n]
\subset
[M-k-1,M+1-k].
$$


::: pf-proof

The condition is equivalent to
$$
k^2\le n<(k+1)^2,
$$
which contains exactly
$$
(k+1)^2-k^2=2k+1
$$
integer values of $n$. The weight bound follows from $\sqrt n\ge k$. The interval containment follows from
$$
k\le\sqrt n<k+1.
$$

:::

:::

::: pf-step

The contribution of all indices with
$$
k\le\sqrt n<k+1
$$
to the sum in step [](#s1-1){.pf-ref} is at most
$$
3
\int_{M-k-1}^{M+1-k}\abs{f(y)}\,dy.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the group contains at most $2k+1$ terms, each with coefficient at most $1/k$, and every integration interval is contained in
$$
[M-k-1,M+1-k].
$$
Therefore the group is bounded by
$$
\frac{2k+1}{k}
\int_{M-k-1}^{M+1-k}\abs{f(y)}\,dy.
$$
Since
$$
\frac{2k+1}{k}
\le3
\qquad
(k\ge1),
$$
the claim follows.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\sum_{k=1}^{\infty}
\int_{M-k-1}^{M+1-k}\abs{f(y)}\,dy
\le
2\norm{f}_{L^1}.
$$


::: pf-proof

Split each interval into two unit intervals:
$$
[M-k-1,M+1-k]
=
[M-k-1,M-k]
\cup
[M-k,M+1-k].
$$
As $k$ varies, the intervals in each of the two families have disjoint interiors. Hence
$$
\sum_{k=1}^{\infty}
\int_{M-k-1}^{M-k}\abs{f(y)}\,dy
\le
\norm{f}_1
$$
and
$$
\sum_{k=1}^{\infty}
\int_{M-k}^{M+1-k}\abs{f(y)}\,dy
\le
\norm{f}_1.
$$
Adding the two estimates gives the result.

:::

:::

::: pf-qed

Combining steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref},
$$
\int_M^{M+1}G(x)\,dx
\le
6\norm{f}_1
<\infty.
$$
This proves step [](#s1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s2}

For every integer $M$,
$$
G(x)<\infty
$$
for almost every $x\in[M,M+1]$.


::: pf-proof

The function $G$ is nonnegative and measurable. By step [](#s1){.pf-ref} it is integrable on $[M,M+1]$. A nonnegative integrable function is finite almost everywhere.

:::

:::

::: {.pf-step #s3}

One has
$$
G(x)<\infty
$$
for almost every $x\in\RR$.


::: pf-proof

The real line is the countable union
$$
\RR
=
\bigcup_{M\in\ZZ}[M,M+1].
$$
By step [](#s2){.pf-ref}, the exceptional set in each interval has measure zero. A countable union of null sets is null.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\sum_{n=1}^{\infty}
\frac1{\sqrt n}f(x-\sqrt n)
\text{ converges absolutely for almost every }x\in\RR.
}
$$


::: pf-proof

By definition,
$$
G(x)
=
\sum_{n=1}^{\infty}
\abs{
\frac1{\sqrt n}
f(x-\sqrt n)
}.
$$
Step [](#s3){.pf-ref} says this sum is finite for almost every $x$, which is exactly absolute convergence of the original series.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
