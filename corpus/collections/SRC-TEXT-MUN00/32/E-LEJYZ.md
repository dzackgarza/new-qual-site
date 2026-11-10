---
schema: qual/card@1
id: E-LEJYZ
kind: problem
title: Every linear continuum is normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked against Munkres, Topology (2000), Section 32 Exercise 8, printed p. 206, and rewritten;
    no published solution was located, which is recorded with the search in the COMPLAINTS.md entry
    for this batch. Ana Emilia de Orellana's set has no Section 32 Exercise 8, "Doug's World" jumps
    from Problem 32.7 to Section 33, and no other retained set reaches Chapter 4. The parts (a)-(c)
    are the book's printed outline; what was incomplete on the card and is now argued:
    (a) the maximality step that a finite end of a component of X - C lies in C, and the reading of
    a missing end as a ray; (b) the previous version asserted that "there can be at most one such
    bridge component extending to the left and at most one extending to the right" of a neighbourhood
    O of a point x of A with O cap B empty, and now proves it: a bridge component whose chosen point
    lies on one side of the B-end of O contains the whole interval from that chosen point to the
    B-end, so a second such component would meet it; (c) the previous version asserted that along
    [a,b] "the closed sets A and B must be separated by at least one component whose two endpoints
    lie one in A and one in B", and now proves it by the type function on the interval (a,s), where s
    is the first point of B above a, which is locally constant except at the left end of such a
    component. The printed set X - A cup B in part (b) is read as X - (A cup B).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked against the located published solution: dbFin, "Section 32: Problem 8 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-32-normal-spaces/problem-8-solution/ (read
    2026-11-10; kept at tmp/sources/dbfin/section-32-normal-spaces/problem-8-solution.txt), and
    against Munkres, Topology (2000), Section 32 Exercise 8, printed p. 206, Theorem 27.1 and
    Theorem 24.1. Its (a) is complete and agrees with the card: a component of X - C is an interval
    whose ends, if present, lie in C, the smallest upper bound of C lying in C because C is closed.
    Its (c) agrees in substance with the card's type argument: it takes b' the least upper bound of
    B in [a,b] and a' the least upper bound of A in [a,b'], and observes that (a',b') is a bridge
    component of X - (A cup B), so it contains a point of C. Its (b) is not a proof: the point x is
    assumed to have infinitely many points of C near it, "suppose a and b are such points", and the
    conclusion "therefore x is a limit point of B" is asserted about symbols a, b, c that the
    printed text leaves undefined, so the finiteness of the bridge components near a point of A,
    which is the substance of (b), is not established there. The card keeps its proof of (b), and
    this exercise stays in the COMPLAINTS.md entry for part (b).
---

::: {.exercise}

Prove the following.

Theorem.
Every linear continuum $X$ is normal.

(a) Let $C$ be a nonempty closed subset of $X$.
If $U$ is a component of $X - C$, show that $U$ is a set of the form $(c, c')$ or $(c, \infty)$ or $(-\infty, c)$, where $c, c' \in C$.

(b) Let $A$ and $B$ be closed disjoint subsets of $X$.
For each component $W$ of $X - A \cup B$ that is an open interval with one end point in $A$ and the other in $B$, choose a point $c_W$ of $W$.
Show that the set $C$ of the points $c_W$ is closed.

(c) Show that if $V$ is a component of $X - C$, then $V$ does not intersect both $A$ and $B$.
:::

::: {.solution}
Throughout, $X$ is a linear continuum: it has the least upper bound property and contains a point strictly between any two of its points. Hence $X$ is connected and locally connected (its intervals are connected), closed intervals in $X$ are compact (Theorem 27.1), and every connected subspace of $X$ is an interval. We read the printed set $X - A\cup B$ in part (b) as $X-(A\cup B)$, the only reading under which the exercise makes sense; the components in question are components of the complement of the two closed sets.

::: pf

::: pf-step
(a) If $C$ is a nonempty closed subset of $X$ and $U$ is a component of $X-C$, then $U$ is $(c,c')$, or $\{x : x < c\}$, or $\{x : x > c\}$, with $c,c'\in C$.

::: pf-proof
A component of $X-C$ is connected, hence an interval, and it is open because $X-C$ is open and $X$ is locally connected. So $U$ is an interval with no largest and no smallest element inside it. If $U$ has a right end $c$ in $X$, then $c\notin X-C$, since otherwise a small interval about $c$ would lie in $X-C$ and together with $U$ form a larger connected subset of $X-C$; thus $c\in C$, and similarly for the left end. A missing end is written as the ray $\{x : x < c\}$ or $\{x : x > c\}$.
:::

:::

::: pf-step
(b) With $A$ and $B$ disjoint closed subsets of $X$, the set $C_0$ of the chosen points $c_W$ is closed.

::: pf-proof
We show that each $x\in X-C_0$ has a neighbourhood meeting $C_0$ in no point.

If $x\notin A\cup B$, let $W$ be the component of $X-(A\cup B)$ containing $x$; it is open, and it contains at most the one chosen point $c_W$, so an interval about $x$ inside $W$ avoiding $c_W$ avoids $C_0$.

Let $x\in A$. Since $B$ is closed and $x\notin B$, choose a convex neighbourhood $O$ of $x$ with $O\cap B=\varnothing$, written $(p,q)$ when $x$ has points of $O$ on both sides. Let $W=(u,v)$ be a component of $X-(A\cup B)$ whose chosen point $c_W$ lies in $O$; its ends lie in $A\cup B$, one in $A$ and one in $B$, and its $B$-end is not in $O$. If the $B$-end is $v>q$, then by convexity $(c_W,v)\subset W$, so $W$ contains every point of $O$ above $c_W$, and no second component whose chosen point lies above $c_W$ in $O$ can exist. If the $B$-end is $u<p$, then symmetrically $(u,c_W)\subset W$ contains every point of $O$ below $c_W$, and no second component whose chosen point lies below $c_W$ in $O$ can exist. Hence $O$ contains at most two points of $C_0$, and a smaller convex neighbourhood of $x$ inside $O$ avoids both. The case $x\in B$ is symmetric, with the roles of $A$ and $B$ exchanged.
:::

:::

::: pf-step
(c) If $V$ is a component of $X-C_0$, then $V$ does not meet both $A$ and $B$.

::: pf-proof
Suppose $a\in A\cap V$ and $b\in B\cap V$ with $a<b$. Since $V$ is an interval, $[a,b]\subset V$.

Let $s=\min(B\cap[a,b])$, which exists and lies in $B$ because $B$ is closed. Since $B$ is closed and $a\notin B$, $s\neq a$, so $B\cap[a,s)=\varnothing$. Nor is $(a,s)$ contained in $A$: otherwise $s\in\bar A=A$, contradicting $A\cap B=\varnothing$ and $s\in B$. So there is $t\in(a,s)$ outside $A\cup B$, and the component $W=(p,q)$ of $X-(A\cup B)$ containing $t$ has $p\ge a$ and $q\le s$, since $p<a$ would put $a\in W$ and $q>s$ would put $s\in W$.

Every point of $(a,s)$ is now either in $A$ or in a component of $X-(A\cup B)$ whose ends lie in $A\cup\{s\}$: by the same argument its left end is $\ge a$ and its right end is $\le s$, and $B\cap[a,s)=\varnothing$. Call such a point of type $A$ if it lies in $A$ or in a component whose right end lies in $A$, and of type $B$ if it lies in a component whose right end is $s$. Type is constant on each component and on a neighbourhood of each of its points, except at a point of $A$ that is the left end of a component whose right end is $s$; such a component is a component of $X-(A\cup B)$ with one end in $A$ and the other in $B$, that is, one of the components counted in the construction of $C_0$.

Points of $(a,s)$ just above $a$ are either of type $A$ or lie in a component whose left end is $a$ and whose right end is $s$. In the second case that component is one of those counted, and its chosen point lies in $(a,s)\subset(a,b)\subset V$, contradicting $V\cap C_0=\varnothing$. So type is $A$ near $a$. Type is $B$ near $s$: since $A$ is closed and $s\notin A$, a neighbourhood of $s$ meets $A$ in no point below $s$, and its points lie in a component with right end $s$, as $B\cap[a,s)=\varnothing$.

Since $(a,s)$ is connected and type is locally constant away from the left ends of the counted components, type cannot take both values $A$ and $B$ unless one of those components has its left end $y\in[a,s)$ and its right end $s$. That component's chosen point then lies in $(y,s)\subset(a,b)\subset V$, again contradicting $V\cap C_0=\varnothing$. In either case $V$ meets $A$ and $B$ in no pair of points.
:::

:::

::: pf-step
Every linear continuum is normal.

::: pf-proof
Let $A$ and $B$ be disjoint closed subsets of $X$; if one of them is empty, it and the other are separated by $\varnothing$ and $X$. Otherwise form the closed set $C_0$ of part (b). The components of the open set $X-C_0$ are open, being components of an open set in a locally connected space. Let $U$ be the union of the components meeting $A$ and $V$ the union of those meeting $B$. Each of $A$ and $B$ lies in its union, both are open, and they are disjoint by part (c). One-point sets of $X$ are closed, since $\{x\}$ has the open complement $\{y : y<x\}\cup\{y : y>x\}$. Hence $X$ is normal.
:::

:::

:::
:::
