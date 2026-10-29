---
schema: qual/card@1
id: P-UCLAB10S-08
kind: problem
title: Closed and totally bounded subsets of complete metric spaces are compact
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 8. Let $K$ be a closed subset of a complete metric space $(X,d)$.
Assume that for every $\varepsilon>0$, $K$ can be covered by finitely many balls
$$
B_\varepsilon(x)=\{y\in X:d(x,y)<\varepsilon\}.
$$
Prove that $K$ is compact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every Cauchy sequence in $K$ converges to a point of $K$.


::: pf-proof

Let $(x_n)$ be Cauchy in $K$.
Since $K\subseteq X$ and $X$ is complete, there exists $x\in X$ such that
$$
x_n\to x.
$$
Because $K$ is closed and every $x_n\in K$, the limit belongs to $K$.
Thus $K$ is complete.

:::

:::

::: {.pf-step #s1-2}

Every sequence in $K$ has a Cauchy subsequence.


::: pf-proof

Let $(x_n)$ be a sequence in $K$.

Cover $K$ by finitely many balls of radius
$$
\frac12.
$$
At least one such ball contains infinitely many terms of the sequence.
Pass to an infinite subsequence contained in that ball.

Cover $K$ by finitely many balls of radius
$$
\frac1{2^2}.
$$
One of these contains infinitely many terms of the preceding subsequence.
Pass to that infinite subsequence.

Continue inductively.
At stage $j$, obtain an infinite subsequence all of whose terms lie in one ball of radius
$$
2^{-j}.
$$

Choose a diagonal subsequence $(y_j)$ with strictly increasing original indices, where $y_j$ is taken from the stage-$j$ subsequence.
If
$$
m,n\ge j,
$$
then $y_m$ and $y_n$ lie in the same stage-$j$ ball.
Hence
$$
d(y_m,y_n)
<
2^{1-j}.
$$
Given $\varepsilon>0$, choose $j$ so that
$$
2^{1-j}<\varepsilon.
$$
Then all later terms are pairwise within $\varepsilon$.
Thus $(y_j)$ is Cauchy.

:::

:::

::: {.pf-step #s1-3}

Every sequence in $K$ has a convergent subsequence with limit in $K$.


::: pf-proof

By step [](#s1-2){.pf-ref}, every sequence has a Cauchy subsequence.
By step [](#s1-1){.pf-ref}, every Cauchy sequence in $K$ converges to a point of $K$.
Therefore $K$ is sequentially compact.

:::

:::

::: {.pf-step #s1-4}

A sequentially compact metric space is totally bounded.


::: pf-proof

Suppose a metric space $Y$ were sequentially compact but not totally bounded.
Then for some $\varepsilon>0$, no finite collection of $\varepsilon$-balls covers $Y$.
Choose $y_1\in Y$.
Since $B(y_1,\varepsilon)$ does not cover $Y$, choose
$$
y_2\notin B(y_1,\varepsilon).
$$
Inductively, after choosing
$$
y_1,\ldots,y_m,
$$
the finite union
$$
\bigcup_{j=1}^m B(y_j,\varepsilon)
$$
does not cover $Y$, so choose $y_{m+1}$ outside it.
Then
$$
d(y_i,y_j)\ge\varepsilon
$$
for all $i\ne j$.
Hence $(y_j)$ has no Cauchy subsequence and therefore no convergent subsequence, contradicting sequential compactness.
Thus $Y$ is totally bounded.

:::

:::

::: {.pf-step #s1-5}

Every sequentially compact metric space is compact.


::: pf-proof

Let $\mathcal U$ be an open cover of a sequentially compact metric space $Y$.
Suppose no finite subcover exists.

First show that $\mathcal U$ has a Lebesgue number.
If not, then for every positive integer $n$ there exists
$$
y_n\in Y
$$
such that
$$
B(y_n,1/n)
$$
is contained in no member of $\mathcal U$.
Sequential compactness gives a subsequence
$$
y_{n_j}\to y.
$$
Choose
$$
U\in\mathcal U
$$
with
$$
y\in U.
$$
Since $U$ is open, choose $r>0$ with
$$
B(y,r)\subseteq U.
$$
For large $j$,
$$
d(y_{n_j},y)<\frac r2
\qquad\text{and}\qquad
\frac1{n_j}<\frac r2.
$$
Then
$$
B(y_{n_j},1/n_j)
\subseteq
B(y,r)
\subseteq U,
$$
a contradiction.
Thus some $\delta>0$ is a Lebesgue number for the cover.

By step [](#s1-4){.pf-ref}, $Y$ is totally bounded, so finitely many balls of radius $\delta/2$ cover $Y$.
Each such ball has diameter less than $\delta$, hence is contained in some member of $\mathcal U$.
Choosing one member of $\mathcal U$ for each ball gives a finite subcover.
Therefore $Y$ is compact.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{K\text{ is compact}.}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives sequential compactness of $K$, and step [](#s1-5){.pf-ref} gives compactness.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
