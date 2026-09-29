---
schema: qual/card@1
id: P-BKS82-2
kind: problem
title: Every uncountable subset of $\mathbb R^n$ contains a convergent sequence of distinct points with limit in the set
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 2.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the countable-base argument, existence of a nonisolated point in the set, and the recursive choice of distinct terms.
---

::: {.problem}
Let $S\subset\mathbb R^n$ be uncountable. Prove that there is a sequence of distinct points of $S$ converging to a point of $S$.
:::

::: {.solution}
Let $\mathcal B$ be the family of open balls in $\RR^n$ whose centers lie
in $\QQ^n$ and whose radii are positive rational numbers.

::: pf

::: {.pf-step #countable-basis}
The family $\mathcal B$ is a countable basis for the topology of
$\RR^n$.

::: pf-proof
Both $\QQ^n$ and $\QQ_{>0}$ are countable, so $\mathcal B$ is countable.
If $U\subset\RR^n$ is open and $x\in U$, choose $\varepsilon>0$ with
$B(x,\varepsilon)\subset U$. Density of $\QQ^n$ gives
$q\in\QQ^n$ with
$$
\norm{x-q}<\frac{\varepsilon}{4}.
$$
Choose $r\in\QQ_{>0}$ such that
$$
\norm{x-q}<r<\frac{3\varepsilon}{4}.
$$
Then
$$
x\in B(q,r)\subset B(x,\varepsilon)\subset U.
$$
Thus $\mathcal B$ is a basis.
:::

:::

::: {.pf-step #nonisolated-point-exists}
Some point $x\in S$ is not isolated in $S$.

::: pf-proof
Suppose every point of $S$ were isolated. Enumerate the countable basis as
$$
\mathcal B=\{B_1,B_2,\ldots\}.
$$
For each $x\in S$, isolation and step [](#countable-basis){.pf-ref} give at least one basis element
$B_j$ such that
$$
x\in B_j
\qquad\text{and}\qquad
B_j\cap S=\{x\}.
$$
Let $j(x)$ be the least such index. If $j(x)=j(y)$, then the same basis
element has intersection with $S$ equal to both $\{x\}$ and $\{y\}$,
so $x=y$. Hence
$$
x\longmapsto j(x)
$$
is an injection from $S$ into $\NN$, contradicting that $S$ is
uncountable.
:::

:::

::: {.pf-step #every-neighborhood-infinite}
Every neighborhood of the point $x$ from step [](#nonisolated-point-exists){.pf-ref} contains
infinitely many points of $S$ distinct from $x$.

::: pf-proof
Suppose some neighborhood $U$ of $x$ met $S\setminus\{x\}$ in only
finitely many points. Choose $\varepsilon>0$ with
$B(x,\varepsilon)\subset U$. If
$$
B(x,\varepsilon)\cap(S\setminus\{x\})
=
\{y_1,\ldots,y_m\},
$$
then
$$
\delta
\coloneqq
\frac12
\min\bigl(
\varepsilon,
\norm{y_1-x},
\ldots,
\norm{y_m-x}
\bigr)
>0
$$
gives
$$
B(x,\delta)\cap S=\{x\},
$$
contradicting step [](#nonisolated-point-exists){.pf-ref}. If there are no such $y_i$, the ball
$B(x,\varepsilon)$ itself isolates $x$, giving the same contradiction.
:::

:::

::: {.pf-step #distinct-sequence-constructed}
There is a sequence of distinct points
$$
x_k\in S\setminus\{x\}
$$
such that
$$
\norm{x_k-x}<\frac1k
$$
for every $k\ge1$.

::: pf-proof
Choose the points recursively. After distinct
$x_1,\ldots,x_{k-1}$ have been chosen, step [](#every-neighborhood-infinite){.pf-ref} says that
$$
B(x,1/k)\cap(S\setminus\{x\})
$$
is infinite. Removing the finitely many previously chosen points leaves a
nonempty set, so one may choose $x_k$ from it.
:::

:::

::: {.pf-step #sequence-converges}
The sequence from step [](#distinct-sequence-constructed){.pf-ref} consists of distinct points of $S$ and
converges to the point $x\in S$.

::: pf-proof
Distinctness is part of the recursive construction. Moreover,
$$
0\le\norm{x_k-x}<\frac1k\longrightarrow0,
$$
so $x_k\to x$. Since step [](#nonisolated-point-exists){.pf-ref} chose $x\in S$, the limit belongs to
$S$.
:::

:::

::: pf-qed
Step [](#sequence-converges){.pf-ref} is the required sequence and limit.
:::

:::
:::
