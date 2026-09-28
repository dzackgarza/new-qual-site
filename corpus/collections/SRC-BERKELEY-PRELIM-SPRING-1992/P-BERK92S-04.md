---
schema: qual/card@1
id: P-BERK92S-04
kind: problem
title: Every infinite closed subset of $\mathbb R^n$ is the closure of a countable set
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Show that every infinite closed subset of $\mathbb R^n$ is the closure of a countable set.
:::

::: {.solution}
Let $F\subseteq\RR^n$ be closed. Let $\mathcal B$ be the family of
open balls with centers in $\QQ^n$ and positive rational radii.

<1>1. There is a countable set $D\subseteq F$ meeting every member of
$\mathcal B$ that meets $F$.

::: {.proof}
The family $\mathcal B$ is countable. For each $B\in\mathcal B$ with
$B\cap F\ne\varnothing$, choose one point
$$
x_B\in B\cap F,
$$
and set
$$
D\coloneqq
\{x_B:B\in\mathcal B,\ B\cap F\ne\varnothing\}.
$$
Thus $D$ is countable and contained in $F$.
:::

<1>2. $F\subseteq\overline D$.

::: {.proof}
Fix $x\in F$ and an open neighborhood $U$ of $x$. Rational balls form
a base for the Euclidean topology, so there is $B\in\mathcal B$ with
$$
x\in B\subseteq U.
$$
Since $x\in B\cap F$, step <1>1 provides
$x_B\in D\cap B\subseteq D\cap U$. Thus every neighborhood of $x$
meets $D$, so $x\in\overline D$.
:::

<1>3. $\overline D=F$.

::: {.proof}
Step <1>2 gives $F\subseteq\overline D$. Conversely, $D\subseteq F$
by step <1>1, and $F$ is closed, so $\overline D\subseteq F$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 expresses the given closed set as the closure of the
countable set $D$.
:::
:::
