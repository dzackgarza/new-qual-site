---
schema: qual/card@1
id: E-5CC0M
kind: problem
title: The two-fold covering of the figure eight restricted to the axes
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 3, printed p. 375,
    with the definition of an evenly covered neighbourhood and Lemma 60.5's construction. At a point $(n,0)$ with $n\ne0$ of the restricted fibre a small neighbourhood of $E'$ is an interval whose image lies in the circle $A$, so no neighbourhood of the basepoint is evenly covered; at the origin the cross has four branches and the map is not a local homeomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    The printed statement, printed p. 375, writes the restriction of $p$ to $E'$ with the bar of
    restriction, and the stored statement wrote it with a relation bar; the statement now uses the
    restriction macro. No mathematics changed.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §60 Exercise 3, his p. 27, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution is that argument transcribed: the preimage of
    a small neighbourhood of $x_0$ inside $E'$ is one small cross at the origin together with open
    intervals about the nonzero integer points, and no interval maps onto the cross. The source is
    correct and needed no repair; the card makes it exact by choosing the neighbourhood inside the
    disc of radius $1/2$, so that the interval through $(1,0)$ maps into $A$ alone while the
    neighbourhood meets $B$ away from $x_0$. Checked against the book: the exercise on printed
    p. 375, the construction and description of $p$ in the proof of Lemma 60.5 on printed pp.
    373-374, and the definition of a covering map in §53. Not claimed: that the source computes
    the preimage exactly -- it describes it, and the card's computation of the distance $2\abs{\sin\pi t}$ makes the description checkable.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and the
    book's pages named in its own text.
---

::: {.exercise}

Let $p: E \to X$ be the map constructed in the proof of Lemma 60.5. Let $E'$ be the subspace of $E$ that is the union of the $x$-axis and the $y$-axis.
Show that $\restrictionof{p}{E'}$ is not a covering map.
:::

::: {.solution}
The exercise is §60 Exercise 3, printed p. 375, about the covering map
$p:E\to X$ constructed in the proof of Lemma 60.5 (printed pp. 373--374): $X$ is
the union of two circles $A$ and $B$ meeting in the single point $x_0$, and $E$ is
the union of the $x$-axis, the $y$-axis, and a small circle tangent to each
nonzero integer point of either axis, with $p$ wrapping the $x$-axis around $A$,
the $y$-axis around $B$, and each tangent circle homeomorphically onto the other
circle; the integer points of both axes map to $x_0$.

The proof is transcribed from Pearse, *Topology (2nd ed.) — James R. Munkres*,
solutions, Cornell 2005, §60 Exercise 3, his p. 27, read in
`tmp/sources/cornell-erin-munkres.md`. The source's point is that the preimage of
a small neighbourhood of $x_0$ inside $E'$ consists of one small cross at the
origin and of open intervals around the nonzero integer points, and that no
interval is homeomorphic to the cross in the base; the card states the same thing
by choosing the neighbourhood small enough that the interval through $(1,0)$ maps
into the wrong circle.

::: pf

::: {.pf-step #component}
Let $p'=\restrictionof{p}{E'}$ and let $U$ be a neighbourhood of $x_0$ in $X$
contained in the open disc of radius $\tfrac12$ about $x_0$. Then the component
of $p'^{-1}(U)$ containing $(1,0)$ is an interval of the $x$-axis, and its image
under $p'$ is contained in $A$.

::: pf-proof
$p'$ wraps the $x$-axis once around $A$ with $(n,0)\mapsto x_0$ for every integer
$n$, so $p'(t,0)$ is the point of $A$ at distance $2\abs{\sin\pi t}$ from $x_0$.
Because $U$ is contained in the disc of radius $\tfrac12$, a point $(t,0)$ lies
in $p'^{-1}(U)$ exactly when $2\abs{\sin\pi t}<\tfrac12$, that is, when $t$ is within
$\delta$ of an integer for some $\delta\in(0,\tfrac12)$ with $2\sin(\pi\delta)
<\tfrac12$. The points of the $x$-axis in $p'^{-1}(U)$ are therefore the union of
the disjoint open intervals $(n-\delta,n+\delta)\times 0$, and the component
containing $(1,0)$ is $(1-\delta,1+\delta)\times 0$, which lies in the $x$-axis
and does not meet the $y$-axis. Hence its image under $p'$ lies in $A$, since the
$x$-axis is carried into $A$.
:::

:::

::: {.pf-step}
$\boxed{p'\ \text{is not a covering map}}$.

::: pf-proof
Suppose $p'$ were a covering map. Then for the neighbourhood $U$ of $x_0$ in step
[](#component){.pf-ref} — or any smaller one — every component of $p'^{-1}(U)$
would map homeomorphically onto $U$. Let $V$ be the component containing
$(1,0)$; by step [](#component){.pf-ref} its image is contained in $A$, and
$A\cap X$ does not contain any point of $B-\theset{x_0}$. But $U$ is a
neighbourhood of $x_0$ in $X=A\cup B$, so it contains the points of $B$ within
distance $\tfrac12$ of $x_0$, which are points of $B-\theset{x_0}$; these are not
in $A$, so $p'(V)\ne U$. That contradicts the covering condition at the point
$x_0\in U$.
:::

:::

:::
:::
