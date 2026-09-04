---
schema: qual/card@1
id: P-3TQB5
kind: problem
title: Nested closed versus open sets in a compact space
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 2 of the official UGA Spring 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the finite-intersection-property proof uses compactness alone, and checked the decreasing relative-open intervals in [0,1] give an empty intersection.
---

::: {.problem}
In each part of this problem $X$ is a compact topological space.
Give a proof or a counterexample for each statement.

a. If $\{F_n\}_{n=1}^\infty$ is a sequence of nonempty closed subsets of $X$ such that $F_{n+1}\subset F_n$ for all $n$, then
\[
\bigcap_{n=1}^\infty F_n\ne\emptyset.
\]

b. If $\{O_n\}_{n=1}^\infty$ is a sequence of nonempty open subsets of $X$ such that $O_{n+1}\subset O_n$ for all $n$, then
\[
\bigcap_{n=1}^\infty O_n\ne\emptyset.
\]
:::

::: {.solution}
<1>1. Part (a) is true.
::: {.proof}
Suppose, toward a contradiction, that
\[
\bigcap_{n=1}^\infty F_n=\emptyset.
\]
Then
\[
X=\bigcup_{n=1}^\infty (X\setminus F_n).
\]
Each $X\setminus F_n$ is open because $F_n$ is closed, so these complements form an open cover of the compact space $X$.
Hence finitely many of them cover $X$: for some indices $n_1,\dots,n_r$,
\[
X=\bigcup_{j=1}^r(X\setminus F_{n_j}).
\]
Taking complements gives
\[
\bigcap_{j=1}^r F_{n_j}=\emptyset.
\]
Let $N=\max\{n_1,\dots,n_r\}$.
Because the sets are nested decreasingly,
\[
\bigcap_{j=1}^rF_{n_j}=F_N.
\]
But $F_N$ is nonempty by hypothesis, a contradiction.
Therefore
\[
\boxed{\bigcap_{n=1}^\infty F_n\ne\emptyset}.
\]
:::

<1>2. Part (b) is false.
::: {.proof}
Take
\[
X=[0,1]
\]
with its usual topology and, for $n\ge1$, let
\[
O_n=(0,1/n).
\]
Each $O_n$ is open in the subspace $[0,1]$, each is nonempty, and
\[
O_{n+1}\subset O_n.
\]
However, if $x$ belonged to every $O_n$, then $x>0$ and
\[
x<\frac1n
\]
for every $n$.
Choosing $n>1/x$ gives $1/n<x$, a contradiction.
Thus
\[
\boxed{\bigcap_{n=1}^\infty O_n=\emptyset}.
\]
So compactness does not imply the asserted conclusion for decreasing nonempty open sets.
:::
:::
