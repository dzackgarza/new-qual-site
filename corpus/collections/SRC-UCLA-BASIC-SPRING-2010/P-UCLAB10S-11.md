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
Suppose
$$
\sum_{n=1}^{\infty}\abs{a_n}<\infty.
$$
Let $\sigma:\NN\to\NN$ be a bijection.
Prove that every rearrangement
$$
\sum_{n=1}^{\infty}a_{\sigma(n)}
$$
converges and has the same sum as $\sum_{n=1}^{\infty}a_n$.
:::

::: {.solution}

Let
$$
S=\sum_{n=1}^{\infty}a_n,
$$
which exists because the series is absolutely convergent.

::: pf

::: {.pf-step #s1-1}

Fix
$$
\varepsilon>0.
$$
There exists
$$
N
$$
such that
$$
\sum_{n>N}\abs{a_n}<\varepsilon.
$$


::: pf-proof

The positive series
$$
\sum_{n=1}^{\infty}\abs{a_n}
$$
converges.
Therefore its tails tend to zero.

:::

:::

::: {.pf-step #s1-2}

Because $\sigma:\NN\to\NN$ is onto, there exists
$$
M
$$
such that
$$
\{1,2,\ldots,N\}
\subseteq
\{\sigma(1),\ldots,\sigma(M)\}.
$$


::: pf-proof

For each
$$
1\le j\le N,
$$
surjectivity gives an index
$$
m_j
$$
with
$$
\sigma(m_j)=j.
$$
Take
$$
M=\max\{m_1,\ldots,m_N\}.
$$

:::

:::

::: {.pf-step #s1-3}

For every
$$
m\ge M,
$$
all terms
$$
a_1,\ldots,a_N
$$
occur among
$$
a_{\sigma(1)},\ldots,a_{\sigma(m)}.
$$


::: pf-proof

This is exactly the containment of index sets from step [](#s1-2){.pf-ref}.
Increasing $m$ beyond $M$ does not remove any previously occurring index.

:::

:::

::: {.pf-step #s1-4}

For
$$
m\ge M,
$$
one has
$$
\abs{
\sum_{j=1}^m a_{\sigma(j)}-S
}
\le
\sum_{n>N}\abs{a_n}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, every index
$$
1,\ldots,N
$$
has already appeared in the rearranged partial sum.
Thus the difference between the rearranged partial sum and the full sum $S$ involves only terms
$$
a_n
$$
with
$$
n>N.
$$

More explicitly, let
$$
E_m
=
\{\sigma(1),\ldots,\sigma(m)\}.
$$
Then
$$
\{1,\ldots,N\}\subseteq E_m,
$$
so
$$
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
$$
Therefore
$$
\abs{
\sum_{j=1}^m a_{\sigma(j)}-S
}
\le
\sum_{\substack{n\notin E_m\\n>N}}\abs{a_n}
\le
\sum_{n>N}\abs{a_n}.
$$

:::

:::

::: {.pf-step #s1-5}

Hence for every
$$
m\ge M,
$$
one has
$$
\abs{
\sum_{j=1}^m a_{\sigma(j)}-S
}
<
\varepsilon.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\sum_{n=1}^{\infty}a_{\sigma(n)}
$$
converges to $S$.


::: pf-proof

Step [](#s1-5){.pf-ref} is precisely the $\varepsilon$-definition of convergence of the rearranged partial sums to $S$.
Thus
$$
\boxed{
\sum_{n=1}^{\infty}a_{\sigma(n)}
=
\sum_{n=1}^{\infty}a_n.
}
$$

:::

:::

::: {.pf-step #s1-7}

In particular, every rearrangement of an absolutely convergent series converges and has the same sum.


::: pf-proof

The bijection $\sigma$ was arbitrary.
Thus step [](#s1-6){.pf-ref} applies to every rearrangement.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
