---
schema: qual/card@1
id: P-UCLAB02S-01
kind: problem
title: Connectedness of the closed unit interval
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
Prove that the closed interval $[0,1]$ is connected.
:::

::: pf

::: pf-step

Suppose, for contradiction, that
\[
[0,1]=U\cup V
\]
where $U$ and $V$ are disjoint nonempty subsets that are open in the subspace topology on $[0,1]$.


::: pf-proof

This is exactly the negation of connectedness.

:::

:::

::: pf-step

Choose
\[
u\in U
\qquad\text{and}\qquad
v\in V.
\]
After interchanging $U$ and $V$ if necessary, assume
\[
u<v.
\]


::: pf-proof

Both sets are nonempty.
Their chosen points are distinct because $U\cap V=\varnothing$.
Thus one of them is smaller than the other.

:::

:::

::: pf-step

Define
\[
S=U\cap[u,v].
\]
Then $S$ is nonempty and bounded above.


::: pf-proof

The point $u$ belongs to $S$, so $S\ne\varnothing$.
Also
\[
S\subseteq[u,v],
\]
so $v$ is an upper bound.

:::

:::

::: pf-step

Let
\[
c=\sup S.
\]
Then
\[
u\le c\le v.
\]


::: pf-proof

The least-upper-bound property applies by step <1>3.
Since $u\in S$, one has $c\ge u$.
Since $v$ is an upper bound for $S$, one has $c\le v$.

:::

:::

::: pf-step

The point $c$ cannot belong to $U$.


::: pf-proof

Suppose
\[
c\in U.
\]
Because $U$ is open in $[0,1]$, there exists $\varepsilon>0$ such that
\[
(c-\varepsilon,c+\varepsilon)\cap[0,1]
\subseteq U.
\]

Since $v\in V$ and $U\cap V=\varnothing$, one has
\[
c\ne v.
\]
Thus $c<v$.
Choose
\[
t\in(c,\min\{c+\varepsilon,v\}).
\]
Then
\[
t\in U\cap[u,v]=S,
\]
but
\[
t>c,
\]
contradicting that $c$ is an upper bound for $S$.

:::

:::

::: pf-step

The point $c$ cannot belong to $V$.


::: pf-proof

Suppose
\[
c\in V.
\]
Because $V$ is open in $[0,1]$, there exists $\varepsilon>0$ such that
\[
(c-\varepsilon,c+\varepsilon)\cap[0,1]
\subseteq V.
\]

Since
\[
u\in U
\]
and $U\cap V=\varnothing$, one has
\[
c\ne u.
\]
Thus $c>u$.

By the defining property of the supremum, for every
\[
\delta>0
\]
there exists
\[
s\in S
\]
such that
\[
c-\delta<s\le c.
\]
Take
\[
0<\delta<\min\{\varepsilon,c-u\}.
\]
Then there exists
\[
s\in S
\]
with
\[
c-\delta<s\le c.
\]
Hence
\[
s\in(c-\varepsilon,c+\varepsilon)\cap[0,1]
\subseteq V.
\]
But
\[
s\in S\subseteq U,
\]
contradicting
\[
U\cap V=\varnothing.
\]

:::

:::

::: pf-step

The assumed separation is impossible.


::: pf-proof

By step <1>4,
\[
c\in[0,1].
\]
Since
\[
[0,1]=U\cup V,
\]
the point $c$ must belong to either $U$ or $V$.
Steps <1>5 and <1>6 rule out both possibilities.

:::

:::

::: pf-step

Therefore
\[
\boxed{[0,1]\text{ is connected}.}
\]


::: pf-proof

The assumption that $[0,1]$ admits a separation leads to the contradiction in step <1>7.

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
