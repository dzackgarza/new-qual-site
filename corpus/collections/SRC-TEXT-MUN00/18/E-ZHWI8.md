---
schema: qual/card@1
id: E-ZHWI8
kind: problem
title: The set where f is at most g is closed
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Order Topology
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $Y$ be an ordered set in the order topology.
Let $f, g: X \to Y$ be continuous.

(a) Show that the set $\ts{x \mid f(x) \leq g(x)}$ is closed in $X$.

(b) Let $h: X \to Y$ be the function

$$
h(x) = \min\ts{f(x), g(x)}.
$$

Show that $h$ is continuous.
[Hint: Use the pasting lemma.]
:::

::: {.solution}
(a) Let
\[
C=\{x\in X:f(x)\le g(x)\}.
\]
We show its complement is open. Suppose $f(x)>g(x)$. If there is $y\in Y$ with
\[
g(x)<y<f(x),
\]
then continuity gives the open neighborhood
\[
f^{-1}((y,\infty))\cap g^{-1}(( -\infty,y))
\]
of $x$, and every point in it satisfies $f>g$.

If there is no point strictly between $g(x)$ and $f(x)$, then $g(x)$ and $f(x)$ are consecutive in the order. The rays
\[
(g(x),\infty),\qquad (-\infty,f(x))
\]
are disjoint open neighborhoods of $f(x)$ and $g(x)$ respectively. Their inverse images again give a neighborhood of $x$ on which $f>g$. Thus $\{f>g\}$ is open and $C$ is closed.

(b) Put
\[
C=\{f\le g\},\qquad D=\{g\le f\}.
\]
By part (a), $C$ and $D$ are closed and $C\cup D=X$. On $C$, $h=f$; on $D$, $h=g$. These two definitions agree on $C\cap D=\{f=g\}$. Since the restrictions are continuous, the pasting lemma gives that $h$ is continuous.
:::
