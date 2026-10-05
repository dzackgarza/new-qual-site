---
schema: qual/card@1
id: P-UCLAB10S-11
kind: problem
title: Absolute convergence is invariant under rearrangement
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
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 11. Suppose
\[
\sum_{n=1}^{\infty}|a_n|<\infty.
\]
Let $\sigma:\mathbb N\to\mathbb N$ be a bijection.
Prove that every rearrangement
\[
\sum_{n=1}^{\infty}a_{\sigma(n)}
\]
converges and has the same sum as $\sum_{n=1}^{\infty}a_n$.
:::

::: {.solution}
Let
\[
S=\sum_{n=1}^{\infty}a_n,
\]
which exists because the series is absolutely convergent.

<1>1. Fix
\[
\varepsilon>0.
\]
There exists
\[
N
\]
such that
\[
\sum_{n>N}|a_n|<\varepsilon.
\]

::: {.proof}
The positive series
\[
\sum_{n=1}^{\infty}|a_n|
\]
converges.
Therefore its tails tend to zero.
:::

<1>2. Because $\sigma:\mathbb N\to\mathbb N$ is onto, there exists
\[
M
\]
such that
\[
\{1,2,\ldots,N\}
\subseteq
\{\sigma(1),\ldots,\sigma(M)\}.
\]

::: {.proof}
For each
\[
1\le j\le N,
\]
surjectivity gives an index
\[
m_j
\]
with
\[
\sigma(m_j)=j.
\]
Take
\[
M=\max\{m_1,\ldots,m_N\}.
\]
:::

<1>3. For every
\[
m\ge M,
\]
all terms
\[
a_1,\ldots,a_N
\]
occur among
\[
a_{\sigma(1)},\ldots,a_{\sigma(m)}.
\]

::: {.proof}
This is exactly the containment of index sets from step <1>2.
Increasing $m$ beyond $M$ does not remove any previously occurring index.
:::

<1>4. For
\[
m\ge M,
\]
one has
\[
\left|
\sum_{j=1}^m a_{\sigma(j)}-S
\right|
\le
\sum_{n>N}|a_n|.
\]

::: {.proof}
By step <1>3, every index
\[
1,\ldots,N
\]
has already appeared in the rearranged partial sum.
Thus the difference between the rearranged partial sum and the full sum $S$ involves only terms
\[
a_n
\]
with
\[
n>N.
\]

More explicitly, let
\[
E_m
=
\{\sigma(1),\ldots,\sigma(m)\}.
\]
Then
\[
\{1,\ldots,N\}\subseteq E_m,
\]
so
\[
\begin{aligned}
\sum_{j=1}^m a_{\sigma(j)}-S
&=
\sum_{n\in E_m}a_n
-
\sum_{n=1}^{\infty}a_n\\
&=
-
\sum_{\substack{n\notin E_m\\n>N}}a_n.
\end{aligned}
\]
Therefore
\[
\left|
\sum_{j=1}^m a_{\sigma(j)}-S
\right|
\le
\sum_{\substack{n\notin E_m\\n>N}}|a_n|
\le
\sum_{n>N}|a_n|.
\]
:::

<1>5. Hence for every
\[
m\ge M,
\]
one has
\[
\left|
\sum_{j=1}^m a_{\sigma(j)}-S
\right|
<
\varepsilon.
\]

::: {.proof}
Combine steps <1>1 and <1>4.
:::

<1>6. Therefore
\[
\sum_{n=1}^{\infty}a_{\sigma(n)}
\]
converges to $S$.

::: {.proof}
Step <1>5 is precisely the $\varepsilon$-definition of convergence of the rearranged partial sums to $S$.
Thus
\[
\boxed{
\sum_{n=1}^{\infty}a_{\sigma(n)}
=
\sum_{n=1}^{\infty}a_n.
}
\]
:::

<1>7. In particular, every rearrangement of an absolutely convergent series converges and has the same sum.

::: {.proof}
The bijection $\sigma$ was arbitrary.
Thus step <1>6 applies to every rearrangement.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
