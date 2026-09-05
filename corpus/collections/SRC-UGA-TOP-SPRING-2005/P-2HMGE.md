---
schema: qual/card@1
id: P-2HMGE
kind: problem
title: A connected normal space with more than one point is uncountable
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Spring 2005 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used Urysohn's lemma to map two distinct points to 0 and 1; connectedness
    forces the image to be all of [0,1], hence the domain is uncountable.
---

::: {.problem}
Show that a connected, normal topological space with more than a single point is uncountable.
:::

::: {.solution}
<1>1. Choose distinct points $x_0,x_1\in X$. There is a continuous map
\[
f:X\longrightarrow[0,1]
\]
such that $f(x_0)=0$ and $f(x_1)=1$.
::: {.proof}
Under the standard convention used here, a normal space is $T_1$, so the singletons
\[
\{x_0\},\qquad \{x_1\}
\]
are disjoint closed subsets of $X$.
Urysohn's lemma therefore gives a continuous map $f:X\to[0,1]$ with
\[
f(x_0)=0,
\qquad
f(x_1)=1.
\]
:::

<1>2. One has
\[
f(X)=[0,1].
\]
::: {.proof}
The continuous image of a connected space is connected, so $f(X)$ is a connected subset of $[0,1]$ containing both $0$ and $1$.

Let $t\in(0,1)$.
If $t\notin f(X)$, then
\[
f(X)\cap(-\infty,t)
\qquad\text{and}\qquad
f(X)\cap(t,\infty)
\]
are disjoint nonempty relatively open subsets whose union is $f(X)$: the first contains $0$, and the second contains $1$.
This contradicts connectedness of $f(X)$.
Hence every $t\in(0,1)$ belongs to $f(X)$, and the endpoints already belong to $f(X)$ by <1>1.
Thus $f(X)=[0,1]$.
:::

<1>3. The space $X$ is uncountable.
::: {.proof}
If $X$ were countable, then its image $f(X)$ under any function would be countable.
But <1>2 gives
\[
f(X)=[0,1],
\]
and the interval $[0,1]$ is uncountable by Cantor's diagonal argument.
This contradiction proves that $X$ is uncountable.
:::
:::
