---
schema: qual/card@1
id: P-UCLAB09S-04
kind: problem
title: Compactness, completeness, connectedness, and total boundedness
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Let $(X,d)$ be an arbitrary metric space.

(a) Define compactness of $X$ using open covers.

(b) Define completeness of $X$.

(c) Define connectedness of $X$.

(d) Is $\QQ$, with its usual metric, connected?
Justify your answer.

(e) Suppose $X$ is complete.
Prove that $X$ is compact if and only if, for every $r>0$, $X$ can be covered by finitely many balls of radius $r$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The metric space $X$ is *compact* if every open cover of $X$ has a finite subcover.


::: pf-proof

This is the open-cover definition of compactness.

:::

:::

::: {.pf-step #s1-2}

The metric space $X$ is *complete* if every Cauchy sequence in $X$ converges to a point of $X$.


::: pf-proof

This is the definition of completeness.

:::

:::

::: {.pf-step #s1-3}

The metric space $X$ is *connected* if it cannot be written as
\[
X=U\cup V
\]
where $U,V$ are disjoint nonempty subsets that are open in $X$.


::: pf-proof

This is the definition of connectedness.
Equivalently, the only subsets of $X$ that are both open and closed are
\[
\varnothing
\quad\text{and}\quad
X.
\]

:::

:::

::: {.pf-step #s1-4}

The space $\QQ$ with its usual metric is not connected.


::: pf-proof

Choose an irrational number, for example
\[
\alpha=\sqrt2.
\]
Define
\[
U=\{q\in\QQ:q<\alpha\}
\]
and
\[
V=\{q\in\QQ:q>\alpha\}.
\]
Both sets are nonempty, disjoint, and their union is all of $\QQ$ because
\[
\alpha\notin\QQ.
\]

Moreover,
\[
U
=
\QQ\cap(-\infty,\alpha)
\]
and
\[
V
=
\QQ\cap(\alpha,\infty),
\]
so both are open in the subspace topology on $\QQ$.
Thus
\[
\QQ=U\cup V
\]
is a separation.
Hence
\[
\boxed{\QQ\text{ is disconnected}.}
\]

:::

:::

::: {.pf-step #s1-5}

If $X$ is compact, then for every $r>0$, finitely many open balls of radius $r$ cover $X$.


::: pf-proof

Fix
\[
r>0.
\]
The family
\[
\{B(x,r):x\in X\}
\]
is an open cover of $X$.
Compactness gives points
\[
x_1,\ldots,x_N\in X
\]
such that
\[
X
=
B(x_1,r)
\cup\cdots\cup
B(x_N,r).
\]

:::

:::

::: {.pf-step #s1-6}

Conversely, suppose that for every $r>0$, $X$ can be covered by finitely many balls of radius $r$.
Then every sequence in $X$ has a Cauchy subsequence.


::: pf-proof

Let
\[
(x_n)
\]
be a sequence in $X$.

Cover $X$ by finitely many balls of radius
\[
\frac12.
\]
At least one of these balls contains infinitely many terms of the sequence.
Choose an infinite subsequence all of whose terms lie in that ball.

Cover $X$ by finitely many balls of radius
\[
\frac1{2^2}.
\]
One of these balls contains infinitely many terms of the subsequence just chosen.
Pass to that infinite subsequence.

Continue inductively.
After stage $k$, obtain an infinite subsequence all of whose terms lie in a ball of radius
\[
2^{-k}.
\]

Choose the diagonal subsequence
\[
y_k,
\]
where $y_k$ is chosen from the stage-$k$ subsequence with increasing original index.
If
\[
m,n\ge k,
\]
then both $y_m$ and $y_n$ lie in the same stage-$k$ ball of radius $2^{-k}$.
Therefore
\[
d(y_m,y_n)
<
2^{1-k}.
\]
Given $\varepsilon>0$, choose $k$ with
\[
2^{1-k}<\varepsilon.
\]
Then
\[
d(y_m,y_n)<\varepsilon
\]
for all $m,n\ge k$.
Thus $(y_k)$ is Cauchy.

:::

:::

::: {.pf-step #s1-7}

If $X$ is complete and satisfies the finite-ball-cover property, then every sequence in $X$ has a convergent subsequence.


::: pf-proof

By step [](#s1-6){.pf-ref}, every sequence has a Cauchy subsequence.
Completeness implies that this Cauchy subsequence converges to a point of $X$.
Thus $X$ is sequentially compact.

:::

:::

::: {.pf-step #s1-8}

In a metric space, sequential compactness implies compactness.


::: pf-proof

First, sequential compactness implies total boundedness.
Indeed, if for some $\varepsilon>0$ no finite collection of $\varepsilon$-balls covered $X$, one could inductively choose
\[
x_1,x_2,\ldots
\]
so that
\[
d(x_i,x_j)\ge\varepsilon
\]
for all $i\ne j$.
Such a sequence has no Cauchy, hence no convergent, subsequence, contradicting sequential compactness.

Now let
\[
\mathcal U
\]
be an open cover of $X$.
Suppose no positive number is a Lebesgue number for this cover.
Then for each $n$ there is
\[
x_n\in X
\]
such that
\[
B(x_n,1/n)
\]
is contained in no member of $\mathcal U$.
Sequential compactness gives a subsequence
\[
x_{n_j}\to x.
\]
Choose
\[
U\in\mathcal U
\]
with
\[
x\in U.
\]
Since $U$ is open, choose $\rho>0$ with
\[
B(x,\rho)\subseteq U.
\]
For sufficiently large $j$,
\[
d(x_{n_j},x)<\frac{\rho}{2}
\qquad\text{and}\qquad
\frac1{n_j}<\frac{\rho}{2}.
\]
Then
\[
B(x_{n_j},1/n_j)
\subseteq
B(x,\rho)
\subseteq U,
\]
contradicting the choice of $x_{n_j}$.
Hence the cover has some Lebesgue number $\delta>0$.

By total boundedness, finitely many balls of radius
\[
\delta/2
\]
cover $X$.
Each such ball has diameter less than $\delta$, so by the Lebesgue-number property it lies inside some member of $\mathcal U$.
Choosing one such member for each ball gives a finite subcover of $\mathcal U$.
Thus $X$ is compact.

:::

:::

::: {.pf-step #s1-9}

If $X$ is complete, then
\[
\boxed{
X\text{ is compact}
\iff
\text{for every }r>0,\ X\text{ is covered by finitely many }r\text{-balls}.
}
\]


::: pf-proof

The forward implication is step [](#s1-5){.pf-ref}.
For the reverse implication, steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} give sequential compactness, and step [](#s1-8){.pf-ref} turns sequential compactness into compactness.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the requested definitions, step [](#s1-4){.pf-ref} answers part (d), and step [](#s1-9){.pf-ref} proves part (e).

:::

:::

:::
