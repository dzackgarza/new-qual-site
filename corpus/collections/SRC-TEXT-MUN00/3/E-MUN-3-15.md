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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Munkres, *Topology* (2000), §3 Exercise 15, printed p. 29, the three questions matching the printed text. The argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.15, printed pp. 36--38. Checked: the least upper bound $c$ of a subset of $[0,1]$ or $[0,1)$ lies in the interval because $c\le b$ and $c\ge0$; and in the failing case every upper bound admits a strictly smaller one.
---

::: {.exercise}

Assume that the real line has the least upper bound property.

(a) Show that the sets $[0,1] = \{x \mid 0\le x\le1\}$ and $[0,1) = \{x \mid 0\le x<1\}$ have the least upper bound property.

(b) Does $[0,1]\times[0,1]$ in the dictionary order have the least upper bound property? What about $[0,1]\times[0,1)$? What about $[0,1)\times[0,1]$?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.15, printed pp. 36--38** (`tmp/sources/munkres-solutions-whitman.pdf`); the three answers and all three arguments below are his. The statement is Munkres, *Topology* (2000), §3 Exercise 15, printed p. 29.

::: pf

::: {.pf-step #a}
(a) Both $[0,1]$ and $[0,1)$ have the least upper bound property.

::: pf-proof
Let $A_0$ be a nonempty subset of $A=[0,1]$ or $[0,1)$ bounded above in $A$ by $b$, so $0\le b\le1$ or $0\le b<1$. As a nonempty subset of $\RR$ bounded above, $A_0$ has a least upper bound $c\in\RR$, and $c\le b$ because $b$ is an upper bound. For $x\in A_0$ we have $0\le x\le c$, so $c\ge0$, and $c\le b\le1$ respectively $c\le b<1$, so $c\in A$. Hence $c$ is the least upper bound of $A_0$ in $A$.
:::
:::

::: {.pf-step #b-positive}
(b) $[0,1]\times[0,1]$ and $[0,1)\times[0,1]$ in the dictionary order have the least upper bound property.

::: pf-proof
Let $X$ be either and let $A\subset X$ be nonempty and bounded above by $x_1\times y_1$. The set $A_x$ of first coordinates of elements of $A$ is a nonempty subset of $[0,1]$ respectively $[0,1)$, bounded above by $x_1$, so by (a) it has a least upper bound $a$. If $a\notin A_x$ put $b=0$; if $a\in A_x$ then $A_y=\{y\st a\times y\in A\}$ is nonempty and bounded above by $1$, so by (a) it has a least upper bound $b$. Then $a\times b$ is an upper bound of $A$: for $x\times y\in A$ we have $x\in A_x$ so $x\le a$, with $x\times y<a\times b$ if $x<a$ and $y\le b$ if $x=a$. And it is the least: if $x_0\times y_0<a\times b$ and $x_0<a$ then $x_0$ is not an upper bound of $A_x$, so some $x\in A_x$ has $x_0<x$ and $x_0\times y_0<x\times y\in A$; while if $x_0=a$ then $y_0<b$, which forces $b\ne0$ and hence $a\in A_x$, and $y_0$ is not an upper bound of $A_y$, so some $y\in A_y$ has $y_0<y$ and $x_0\times y_0<a\times y\in A$.
:::
:::

::: {.pf-step #b-negative}
(b) $[0,1]\times[0,1)$ in the dictionary order does not have the least upper bound property.

::: pf-proof
Let $X=[0,1]\times[0,1)$ and $A=\{0\}\times[0,1)$, nonempty and bounded above by $1\times0$. Let $x_1\times y_1$ be any upper bound of $A$. If $x_1=0$ then $y_1\in[0,1)$, and choosing $y_0$ with $y_1<y_0<1$ gives $0\times y_0\in A$ strictly above $x_1\times y_1$, so $x_1\times y_1$ is not an upper bound. Hence $x_1>0$. Then $x_0=x_1/2$ satisfies $0<x_0<x_1$, and $x_0\times0$ is an upper bound of $A$ because every $0\times y$ has first coordinate $0<x_0$, and it is strictly below $x_1\times y_1$. So every upper bound of $A$ has a strictly smaller upper bound, and no upper bound is least.
:::
:::

::: {.pf-step}
The answers are: $[0,1]$ and $[0,1)$ yes; $[0,1]\times[0,1]$ yes; $[0,1)\times[0,1]$ yes; $[0,1]\times[0,1)$ no.

::: pf-proof
Step [](#a){.pf-ref} answers (a) and steps [](#b-positive){.pf-ref} and [](#b-negative){.pf-ref} answer the three cases of (b).
:::
:::

:::
:::
