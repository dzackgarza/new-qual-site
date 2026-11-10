---
schema: qual/card@1
id: E-E5ZWY
kind: problem
title: Every order topology is regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked against Munkres, Topology (2000), Section 31 Exercise 3, printed p. 199, and rewritten.
    The located sets both fall short here, which is why the proof is the card's own and the search
    is recorded in the COMPLAINTS.md entry for this batch: Ana Emilia de Orellana, printed p. 32,
    argues only for a point x lying between two other points (her "there exists (a,b) containing x
    with (a,b) cap A empty" fails when x is the least or the greatest element, where the basis
    element about x is a half-open interval), and "Doug's World", printed p. 4, contains an
    undefined set W and undefined symbols a and b and likewise assumes both sides exist. The card
    now separates the four positions of x in the order, uses convexity of a basis element for
    [u,v] <= B, and applies Lemma 31.1(a). The previous version said "choose an interior cut
    strictly between that endpoint and x when such a point exists" without saying what happens when
    it does not.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution now that it is available: Jesper Michael Moller,
    "Solutions to exercises in Munkres", file S31.pdf, Exercise 31.3, page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S31.pdf, Internet Archive snapshot 20191101081351 of
    web.math.ku.dk/~moller/e02/3gt/opg/S31.pdf), and checked against Munkres, Topology (2000),
    Section 31 Exercise 3, printed p. 199, and Lemma 31.1(a). Moller proves the same four-case
    statement by the criterion of Lemma 31.1(b): with U = (a,b) and A = (a,x), B = (x,b) he treats
    u in A with v in B, then A = B = empty (when {x} = (a,b) is open and closed), then A empty with
    v in B, then u in A with B empty. The card's proof is that argument with the cases named by the
    position of x in the order; the least-element case here splits into Moller's two cases (2) and
    (3) according as a point lies between x and b. Moller's case (1) is printed with the chain
    "x in (u,v) subset (u,v) subset [u,v] subset (a,b)", in which the middle inclusion should be the
    closure of (u,v) inside [u,v]; the card writes the closure inclusion. This supersedes the
    previous note, which recorded that no complete published proof had been found.
---

::: {.exercise}

Show that every order topology is regular.
:::

::: {.solution}
In an ordered set $X$ with the order topology the rays $(-\infty, y)$ and $(x, \infty)$ are open, and for $x < y$ they are disjoint neighbourhoods of $x$ and $y$; hence $X$ is Hausdorff and one-point sets are closed. By Lemma 31.1(a) it is enough to show that each point has arbitrarily small neighbourhoods whose closures lie inside a prescribed neighbourhood.

::: pf

::: pf-step
For $x \in X$ and an open neighbourhood $U$ of $x$ there is an open neighbourhood $V$ of $x$ with $\overline{V} \subset U$.

::: pf-proof
If $X = \{x\}$ take $V = X = U$. Otherwise let $B$ be a basis element with $x \in B \subset U$. A basis element of the order topology is convex, and we distinguish the position of $x$ in the order.

If $X$ has a point below $x$ and a point above $x$, then $B$ contains points $u < x < v$, and convexity gives $[u, v] \subset B \subset U$; then $V = (u, v)$ is open, contains $x$, and $\overline{V} \subset [u, v] \subset U$.

If $x$ is the least element of $X$, then $X$ has a point above $x$ and $B$ contains an interval $[x, b)$ with $b > x$. If there is a point $v$ with $x < v < b$, then $V = [x, v)$ is open, contains $x$, and $\overline{V} \subset [x, v] \subset [x, b) \subset U$; if there is none, then $[x, b) = \{x\}$ is an open neighbourhood of $x$ with $\overline{\{x\}} = \{x\} \subset U$.

If $x$ is the greatest element of $X$, the preceding paragraph applies to the reverse order: $B$ contains an interval $(b, x]$, and with $b < v < x$ the set $V = (v, x]$ is open, contains $x$, and $\overline{V} \subset [v, x] \subset (b, x] \subset U$.

Every point of a nonempty ordered set is its least element, its greatest element, or has points on both sides, so one of these cases applies.
:::

:::

::: pf-step
$X$ is regular.

::: pf-proof
One-point sets are closed in $X$, and the preceding step is the criterion of Lemma 31.1(a).
:::

:::

:::
:::
