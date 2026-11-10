---
schema: qual/card@1
id: E-MUN-11-4
kind: problem
title: The maximal simply ordered subsets of the plane under $x_0<x_1$ and $y_0\le y_1$
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 4, printed p. 71; the stored
    statement matches, including the three curves and the request to find all maximal
    simply ordered subsets.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.4,
    printed pp. 121-125 (tmp/sources/munkres-solutions-whitman.pdf). His classification is
    the one stated: the graphs of non-decreasing f on an open interval (a,b), unbounded
    above when b is finite and unbounded below when a is finite. The three curve
    verifications and both inclusions of the classification are his, with the case analysis
    compressed here to the three cases his argument turns on.
---

::: {.exercise}

Given two points $(x_0, y_0)$ and $(x_1, y_1)$ of $\RR^2$, define $(x_0, y_0) \prec (x_1, y_1)$ if $x_0 < x_1$ and $y_0 \le y_1$. Show that the curves $y = x^3$ and $y = 2$ are maximal simply ordered subsets of $\RR^2$, and the curve $y = x^2$ is not. Find all maximal simply ordered subsets.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.4, printed pp. 121--125** (`tmp/sources/munkres-solutions-whitman.pdf`); the classification and the verifications below are his.

First $\prec$ is a strict partial order: $x<x$ is never true, and if $x_0<x_1$, $y_0\le y_1$ and $x_1<x_2$, $y_1\le y_2$ then $x_0<x_2$ and $y_0\le y_2$. Two points are comparable exactly when they have distinct $x$-coordinates, the left one with the smaller-or-equal $y$; in particular two points with the same $x$-coordinate are never comparable.

*$y=x^3$.* Points $(u,u^3)$ and $(v,v^3)$ with $u<v$ satisfy $u<v$ and $u^3<v^3$, so the curve is simply ordered. A point $(x,y)$ off the curve is incomparable with $(x,x^3)$, which is on it, since the two share their $x$-coordinate. Hence no proper superset is simply ordered.

*$y=2$.* Points $(u,2)$, $(v,2)$ with $u<v$ satisfy $u<v$ and $2\le2$. A point $(x,y)$ with $y\ne2$ is incomparable with $(x,2)$.

*$y=x^2$.* $(-1,1)$ and $(0,0)$ both lie on the curve, but $-1<0$ while $1>0$, and $0<-1$ is false; so the two are incomparable and the curve is not even simply ordered.

*Classification.* A subset of $\RR^2$ is a maximal simply ordered set exactly when it is
$$
A_f=\{(x,f(x))\mid x\in(a,b)\}
$$
for a non-decreasing $f:(a,b)\to\RR$ on an open interval $(-\infty\le a<b\le\infty)$ which is unbounded above if $b<\infty$ and unbounded below if $a>-\infty$.

*Every $A_f$ is maximal.* It is simply ordered because $f$ is non-decreasing. Let $(x,y)\notin A_f$. If $x\in(a,b)$ then $y\ne f(x)$ and $(x,f(x))\in A_f$ shares the $x$-coordinate with $(x,y)$, so the two are incomparable. If $x\ge b$ (with $b<\infty$) then, $f$ being unbounded above, choose $t\in(a,b)$ with $f(t)>y$; then $t<x$ but $f(t)\le y$ fails, so $t<x$ and $y\le f(t)$ fails, and $x<t$ fails: the two are incomparable. Symmetrically, if $x\le a$ with $a>-\infty$, unboundedness below gives $t\in(a,b)$ with $f(t)<y$, and again $(t,f(t))$ and $(x,y)$ are incomparable.

*Every maximal $B$ is some $A_f$.* Distinct points of $B$ have distinct $x$-coordinates, since equal ones are incomparable, so $B$ is the graph of a function $f$ on its domain $D=\{x:\exists y,\ (x,y)\in B\}$. The domain is an interval: if $x_1<x<x_2$ with $x_i\in D$, then $(x,f(x_1))$ is comparable with every $(t,f(t))\in B$ — for $t\le x_1$ we have $t<x$ and $f(t)\le f(x_1)$, for $x_1\le t<x$ we have $t<x$ and $f(t)\le f(x_1)$ by monotonicity, and for $x<t$ we have $x<t$ and $f(x_1)\le f(t)$ — so by maximality $x\in D$. The function $f$ is non-decreasing because $B$ is simply ordered. If $D$ has a least element $a>-\infty$, then $(a-1,f(a)-1)$ is comparable with every element of $B$, since $a-1<t$ and $f(a)-1\le f(t)$ for all $t\in D$; by maximality it would lie in $B$, contradicting that its first coordinate is outside $D$. So $a=-\infty$ or $D$ has no least element; symmetrically for the right end. Finally, if $b=\sup D<\infty$ and $f$ were bounded above by $M$, then $(b,M+1)$ would be comparable with every element of $B$; and if $a=\inf D>-\infty$ and $f$ were bounded below by $m$, then $(a-1,m-1)$ would be. So $f$ is unbounded above at a finite right end and unbounded below at a finite left end.
:::
