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
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 4, printed p. 158, with the
    definition of linear continuum and the order topology of §14; the stored statement is
    the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.4, PDF p. 4. A nonempty bounded set without a
    least upper bound gives a separation of X into the union of the open rays below its
    members and the union of the open rays above its upper bounds, and a gap between two
    points gives a separation into two open rays. (tmp/sources/munkres-solutions-positron-
    ch3.pdf).
---

::: {.exercise}

Let $X$ be an ordered set in the order topology.
Show that if $X$ is connected, then $X$ is a linear continuum.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.4, PDF p. 4** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the two steps are theirs.

Let $X$ be an ordered set, with more than one element, in the order topology, and suppose $X$ connected.

*$X$ has the least upper bound property.* Let $A$ be a nonempty subset bounded above, and let $B$ be the set of its upper bounds, which is nonempty. Suppose $A$ has no least upper bound, that is, $B$ has no smallest element. Put
$$
C=\bigcup_{a\in A}(-\infty,a),\qquad D=\bigcup_{b\in B}(b,+\infty),
$$
unions of open rays, hence open in $X$. They are disjoint: if $x\in C\cap D$ then $x<a$ for some $a\in A$ and $x>b$ for some $b\in B$, so $b<x<a$ with $b$ an upper bound of $A$ — impossible. They cover $X$: if $x\in B$ then, $B$ having no smallest element, there is $b\in B$ with $b<x$, so $x\in(b,+\infty)\subset D$; if $x\notin B$ then $x$ is not an upper bound of $A$, so $x<a$ for some $a\in A$ and $x\in C$. Finally $C$ and $D$ are nonempty: $D\ne\varnothing$ because $B\ne\varnothing$, and $C\ne\varnothing$ because $A\ne\varnothing$ and $A$ has an upper bound. So $C,D$ separate $X$, contradiction. Hence $A$ has a least upper bound.

*$X$ is densely ordered.* If $x<y$ with no element between them, then $(-\infty,y)$ and $(x,+\infty)$ are disjoint nonempty open sets whose union is $X$, a separation.

So $X$ is a linear continuum.
:::
