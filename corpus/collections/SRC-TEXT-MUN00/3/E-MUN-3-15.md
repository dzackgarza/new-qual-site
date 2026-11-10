---
schema: qual/card@1
id: E-MUN-3-15
kind: problem
title: Which half-open dictionary products have the least upper bound property
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 15, printed p. 29: assuming the
    real line has the least upper bound property, (a) [0,1] and [0,1) have it, (b)
    whether [0,1] x [0,1], [0,1] x [0,1) and [0,1) x [0,1] do in the dictionary order.
    The stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.15,
    printed pp. 36-38 (tmp/sources/munkres-solutions-whitman.pdf). His (a) treats the
    closed and half-open intervals together; his (b) answers yes, yes, no, and the
    counterexample A = {0} x [0,1) with the halving argument is his.
---

::: {.exercise}

Assume that the real line has the least upper bound property.

(a) Show that the sets $[0,1] = \{x \mid 0\le x\le1\}$ and $[0,1) = \{x \mid 0\le x<1\}$ have the least upper bound property.

(b) Does $[0,1]\times[0,1]$ in the dictionary order have the least upper bound property? What about $[0,1]\times[0,1)$? What about $[0,1)\times[0,1]$?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.15, printed pp. 36--38** (`tmp/sources/munkres-solutions-whitman.pdf`); the three answers and all three arguments below are his.

(a) Let $A$ be $[0,1]$ or $[0,1)$, and let $A_0\subset A$ be nonempty and bounded above in $A$ by $b\in A$, so $0\le b\le1$ respectively $0\le b<1$. As a nonempty subset of $\RR$ bounded above, $A_0$ has a least upper bound $c\in\RR$, and $c\le b$ because $b$ is an upper bound. For $x\in A_0$ we have $0\le x\le c\le b$, and $b\le1$ respectively $b<1$; hence $c\in A$. So $c$ is the least upper bound of $A_0$ in $A$.

(b) $[0,1]\times[0,1]$ and $[0,1)\times[0,1]$ have the least upper bound property. Let $X$ be either and let $A\subset X$ be nonempty and bounded above by $x_1\times y_1$. Put
$$
A_x=\{x\mid \text{there is } y \text{ with } x\times y\in A\}\subset[0,1]\ \text{(respectively } [0,1)),
$$
nonempty and bounded above by $x_1$. By (a) it has a least upper bound $a$. If $a\notin A_x$ set $b=0$; if $a\in A_x$, then
$$
A_y=\{y\mid a\times y\in A\}
$$
is nonempty and bounded above by $1$, so by (a) it has a least upper bound $b$. We show that $a\times b$ is the least upper bound of $A$ in the dictionary order.

It is an upper bound: for $x\times y\in A$ we have $x\in A_x$, so $x\le a$; if $x<a$ then $x\times y<a\times b$, and if $x=a$ then $y\in A_y$, so $y\le b$.

It is the least: let $x_0\times y_0<a\times b$. If $x_0<a$ then $x_0$ is not an upper bound of $A_x$, so there is $x\in A_x$ with $x_0<x$, and choosing $y$ with $x\times y\in A$ gives $x_0\times y_0<x\times y\in A$. If $x_0=a$ then $y_0<b$, which forces $b\ne0$ and hence $a\in A_x$; then $y_0$ is not an upper bound of $A_y$, so there is $y\in A_y$ with $y_0<y$, and $a\times y\in A$ lies above $x_0\times y_0$.

$[0,1]\times[0,1)$ does not have the least upper bound property. Take $X=[0,1]\times[0,1)$ and
$$
A=\{0\}\times[0,1).
$$
It is nonempty and bounded above in $X$ by $1\times0$. Let $x_1\times y_1$ be any upper bound of $A$. If $x_1=0$ then $y_1\in[0,1)$, and choosing $y_0$ with $y_1<y_0<1$ gives $0\times y_0\in A$ strictly above $x_1\times y_1$, so $x_1\times y_1$ is not an upper bound; hence $x_1>0$. Then $x_0=x_1/2$ satisfies $0<x_0<x_1$, and $x_0\times0$ is an upper bound of $A$ (every $0\times y$ has first coordinate $0<x_0$), strictly below $x_1\times y_1$. So no upper bound of $A$ is least.
:::
