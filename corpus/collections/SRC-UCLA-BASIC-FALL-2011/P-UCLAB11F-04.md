---
schema: qual/card@1
id: P-UCLAB11F-04
kind: problem
title: Limits obtainable by rearranging two alternating series
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 4. If the terms of a series $\sum a_n$ are rearranged, the limiting value can sometimes change.
Find all resulting limiting values of each of the following series, and prove your assertions:
\[
\sum_{n=1}^{\infty}\frac{(-1)^n}{n},
\qquad
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}.
\]
:::

::: {.solution}
For the first series, write
\[
p_k=\frac1{2k}
\qquad\text{and}\qquad
q_k=-\frac1{2k-1}.
\]

<1>1. The positive subseries of the first series diverges to $+\infty$, and its negative subseries diverges to $-\infty$.

::: {.proof}
One has
\[
\sum_{k=1}^{\infty}p_k
=
\frac12\sum_{k=1}^{\infty}\frac1k
=+\infty.
\]
Also
\[
-q_k=\frac1{2k-1}\ge\frac1{2k},
\]
so
\[
\sum_{k=1}^{\infty}(-q_k)=+\infty.
\]
Hence
\[
\sum_{k=1}^{\infty}q_k=-\infty.
\]
:::

<1>2. Fix any target
\[
L\in\mathbb R.
\]
There is a rearrangement of the first series constructed by repeatedly taking unused positive terms until the partial sum first exceeds $L$, then unused negative terms until it first falls below $L$.

::: {.proof}
Step <1>1 guarantees that every positive block and every negative block terminates after finitely many terms. Within each sign, use terms in their original order. Thus no term is repeated.

Every positive block contains at least one new positive term and every negative block contains at least one new negative term, so after infinitely many blocks every $p_k$ and every $q_k$ has appeared. Hence the construction is a genuine rearrangement.
:::

<1>3. The rearrangement in step <1>2 converges to $L$.

::: {.proof}
At the end of a positive block, if the last term added is $p_k$, then
\[
0<S-L\le p_k.
\]
At the end of a negative block, if the last term added is $q_k$, then
\[
0<L-S\le -q_k.
\]
As the blocks proceed, the indices of the newly used terms tend to infinity, and
\[
p_k\to0,
\qquad
q_k\to0.
\]
Therefore the successive overshoots and undershoots tend to zero.

Given $\varepsilon>0$, eventually every new positive and negative term has absolute value less than $\varepsilon$. From then on, positive-block endpoints lie in
\[
(L,L+\varepsilon),
\]
negative-block endpoints lie in
\[
(L-\varepsilon,L),
\]
and all intermediate partial sums lie between the adjacent endpoints. Hence every sufficiently late partial sum lies in
\[
(L-\varepsilon,L+\varepsilon).
\]
Thus the rearranged series converges to $L$.
:::

<1>4. The set of finite limiting values obtainable by rearranging
\[
\sum_{n=1}^{\infty}\frac{(-1)^n}{n}
\]
is
\[
\boxed{\mathbb R}.
\]

::: {.proof}
Step <1>3 constructs, for every prescribed $L\in\mathbb R$, a rearrangement converging to $L$. Conversely, every finite limiting value of a rearrangement is by definition a real number.
:::

<1>5. The second series
\[
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}
\]
is absolutely convergent.

::: {.proof}
Its absolute-value series is
\[
\sum_{n=1}^{\infty}\frac1{n^2},
\]
which converges.
:::

<1>6. Every rearrangement of an absolutely convergent series has the same sum as the original series.

::: {.proof}
Let
\[
\sum_{n=1}^{\infty}a_n
\]
be absolutely convergent with sum $S$, and let $\sigma:\mathbb N\to\mathbb N$ be a bijection.
Fix $\varepsilon>0$. Choose $N$ such that
\[
\sum_{n>N}|a_n|<\varepsilon.
\]
Since $\sigma$ is onto, there is $M$ such that
\[
\{1,\ldots,N\}
\subseteq
\{\sigma(1),\ldots,\sigma(M)\}.
\]
For every $m\ge M$, the difference between
\[
\sum_{j=1}^m a_{\sigma(j)}
\]
and $S$ consists only of terms $a_n$ with $n>N$, some included and some omitted. Therefore its absolute value is bounded by
\[
\sum_{n>N}|a_n|<\varepsilon.
\]
Hence the rearranged partial sums converge to $S$.
:::

<1>7. Every rearrangement of the second series has the single limiting value
\[
\boxed{
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}
=
-\frac{\pi^2}{12}
}.
\]

::: {.proof}
By steps <1>5--<1>6, every rearrangement has the original sum.
Using the standard Basel sum
\[
\sum_{n=1}^{\infty}\frac1{n^2}
=
\frac{\pi^2}{6},
\]
split it into even and odd parts:
\[
\sum_{k=1}^{\infty}\frac1{(2k)^2}
=
\frac14\cdot\frac{\pi^2}{6}
=
\frac{\pi^2}{24}.
\]
Thus
\[
\sum_{k=1}^{\infty}\frac1{(2k-1)^2}
=
\frac{\pi^2}{6}-\frac{\pi^2}{24}
=
\frac{\pi^2}{8}.
\]
Therefore
\[
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}
=
\frac{\pi^2}{24}-\frac{\pi^2}{8}
=
-\frac{\pi^2}{12}.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 gives all finite rearrangement limits of the first series, and step <1>7 gives the unique rearrangement limit of the second.
:::
:::
