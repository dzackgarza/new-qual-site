---
schema: qual/card@1
id: P-UCLAB13S-03
kind: problem
title: Sequential compactness, completeness, and total boundedness
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Prove that a metric space is sequentially compact if and only if it is complete and totally bounded.

A metric space is totally bounded when for every $\varepsilon>0$ it can be covered by finitely many balls of radius $\varepsilon$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose first that $X$ is sequentially compact.
Then $X$ is complete.


::: pf-proof

Let $(x_n)$ be a Cauchy sequence in $X$.
Sequential compactness gives a convergent subsequence
$$
x_{n_k}\to x
$$
for some $x\in X$.

Fix $\varepsilon>0$.
Choose $N$ such that
$$
d(x_m,x_n)<\frac{\varepsilon}{2}
$$
for all $m,n\ge N$.
Also choose $k$ so large that
$$
n_k\ge N
$$
and
$$
d(x_{n_k},x)<\frac{\varepsilon}{2}.
$$
Then for every $n\ge N$,
$$
\begin{aligned}
d(x_n,x)
&\le
d(x_n,x_{n_k})
+
d(x_{n_k},x)\\
&<
\varepsilon.
\end{aligned}
$$
Thus
$$
x_n\to x.
$$
Hence every Cauchy sequence converges, so $X$ is complete.

:::

:::

::: {.pf-step #s1-2}

If $X$ is sequentially compact, then $X$ is totally bounded.


::: pf-proof

Suppose not.
Then there exists
$$
\varepsilon>0
$$
such that no finite union of $\varepsilon$-balls covers $X$.

Choose
$$
x_1\in X.
$$
Since
$$
B(x_1,\varepsilon)
$$
does not cover $X$, choose
$$
x_2\notin B(x_1,\varepsilon).
$$
Inductively, after choosing
$$
x_1,\ldots,x_n,
$$
the finite union
$$
\bigcup_{j=1}^nB(x_j,\varepsilon)
$$
does not cover $X$, so choose
$$
x_{n+1}
$$
outside it.

Then
$$
d(x_i,x_j)\ge\varepsilon
$$
whenever
$$
i\ne j.
$$
Hence no subsequence can be Cauchy, and therefore no subsequence can converge.
This contradicts sequential compactness.
Thus $X$ is totally bounded.

:::

:::

::: {.pf-step #s1-3}

Now suppose conversely that $X$ is complete and totally bounded.
Let
$$
(x_n)
$$
be any sequence in $X$.
Then $(x_n)$ has a Cauchy subsequence.


::: pf-proof

Cover $X$ by finitely many balls of radius
$$
\frac12.
$$
At least one such ball contains infinitely many terms of the sequence.
Pass to an infinite subsequence contained in that ball.

Next cover $X$ by finitely many balls of radius
$$
\frac1{2^2}.
$$
One of these contains infinitely many terms of the preceding subsequence.
Pass again to an infinite subsequence.

Continue inductively.
At stage $k$, obtain an infinite subsequence all of whose terms lie in a ball of radius
$$
2^{-k}.
$$

Choose a diagonal subsequence
$$
(y_k)
$$
with strictly increasing original indices, where $y_k$ is chosen from the stage-$k$ subsequence.
If
$$
m,n\ge k,
$$
then both $y_m$ and $y_n$ belong to the same stage-$k$ ball, so
$$
d(y_m,y_n)
<
2^{1-k}.
$$
Given $\varepsilon>0$, choose $k$ so large that
$$
2^{1-k}<\varepsilon.
$$
Then
$$
d(y_m,y_n)<\varepsilon
$$
for all $m,n\ge k$.
Thus $(y_k)$ is Cauchy.

:::

:::

::: {.pf-step #s1-4}

The Cauchy subsequence from step [](#s1-3){.pf-ref} converges in $X$.


::: pf-proof

The space $X$ is complete by hypothesis.
Therefore every Cauchy sequence in $X$, including the subsequence $(y_k)$, converges to a point of $X$.

:::

:::

::: {.pf-step #s1-5}

Hence $X$ is sequentially compact.


::: pf-proof

The original sequence $(x_n)$ was arbitrary.
Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} show that every sequence has a convergent subsequence.
This is the definition of sequential compactness.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
X\text{ is sequentially compact}
\iff
X\text{ is complete and totally bounded}.
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove the forward implication, and steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} prove the converse.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required equivalence.

:::

:::

:::
