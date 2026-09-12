---
schema: qual/card@1
id: E-ZY1RB
kind: problem
title: Connected ordered sets are linear continua
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Connectedness
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

Let $X$ be an ordered set in the order topology.
Show that if $X$ is connected, then $X$ is a linear continuum.
:::

::: {.solution}
Let $X$ be connected in its order topology.

First, the order must be dense. If $x<y$ and no point lies strictly between them, then
\[
(-\infty,y)\qquad\text{and}\qquad(x,\infty)
\]
are disjoint nonempty open sets whose union is $X$, a separation. Thus for every $x<y$ there is $z$ with $x<z<y$.

Now let $A\subseteq X$ be nonempty and bounded above, and let $B$ be the set of upper bounds of $A$. If $B$ had no least element, then both $B$ and $X-B$ would be nonempty open sets. Indeed, if $b\in B$, choose a smaller upper bound $b'<b$; then $(b',\infty)$ is a neighborhood of $b$ contained in $B$. If $x\notin B$, choose $a\in A$ with $x<a$; then $(-\infty,a)$ is a neighborhood of $x$ contained in $X-B$. These two sets would separate $X$, contradiction.

Therefore $B$ has a least element, which is exactly $\sup A$. Hence $X$ has the least-upper-bound property and a dense order, so it is a linear continuum.
:::
