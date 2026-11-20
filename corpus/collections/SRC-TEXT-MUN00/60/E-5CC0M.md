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
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The first step was replaced. It had computed the points of the $x$-axis in $p'^{-1}(U)$ from the
    formula $2\abs{\sin\pi t}$ for the distance of $p'(t,0)$ from $x_0$, which presumes a choice of
    $A$ as the unit circle wrapped uniformly, a choice the book's construction of $p$ does not make;
    and its "exactly when" holds only for $U$ whose intersection with $A$ is all of the disc's,
    whereas a smaller evenly covered $U$ gives smaller intervals. The card now argues without
    coordinates: at $y=(1,0)$ the space $E'$ is locally an interval of the $x$-axis, which $p$
    carries into $A$, while every neighbourhood of $x_0$ in $X$ contains points of
    $B-\theset{x_0}$. So if $p'$ were a covering, the sheet $V$ at $y$ — homeomorphic to a connected
    evenly covered $U$ — would contain a point $z$ mapping to $B-\theset{x_0}$, hence on the $y$-axis
    by the first step, hence, $V$ being connected and meeting both axes away from the origin, would
    contain the origin; and then $p'$ would take the distinct points $y$ and the origin to $x_0$,
    contradicting injectivity on the sheet. Checked against the book: the exercise on printed
    p. 375, the construction of $p$ in the proof of Lemma 60.5 on printed pp. 373-374, and the
    definition of a covering map in §53. Correction to the note of 2026-11-14 above: the card no
    longer computes $2\abs{\sin\pi t}$, so the clause there about that computation describes text
    that is no longer on the card; the statement repair recorded there stands.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    The attribution is corrected, from a second reader's report on this card. The
    solution opened with "The proof is transcribed from Pearse", and that had stopped
    being true when the argument was replaced: Pearse's proof of §60 Exercise 3 is
    made at the basepoint x_0, by describing the preimage inside E' of a small cross
    in X and remarking that an interval and a cross are not homeomorphic, while the
    argument on the card works at y = (1,0), never computes that preimage, and uses
    instead that p carries the x-axis into A, that every neighbourhood of x_0 meets
    B minus x_0, and that a sheet is connected and carries p' homeomorphically. The
    preamble now says which two sentences are the source's -- the description of the
    preimage and the observation that no map of a cross onto an interval is injective
    -- and says that the argument below is the card's own. The argument itself was
    re-read and is unchanged: the sheet V through y is connected and homeomorphic to
    U, it meets the x-axis at y and the y-axis at a point over b, so it contains the
    origin, where p' takes the same value x_0 as at y. Checked against the book: the
    exercise on printed p. 375 and the construction of p in the proof of Lemma 60.5
    on printed pp. 373-374. Not claimed: that the source computes the preimage
    exactly, which the note of 2026-11-14 already recorded.
---

::: {.exercise}

Let $p: E \to X$ be the map constructed in the proof of Lemma 60.5. Let $E'$ be the subspace of $E$ that is the union of the $x$-axis and the $y$-axis.
Show that $\restrictionof{p}{E'}$ is not a covering map.
:::

::: {.solution}
The exercise is §60 Exercise 3, about the covering map
$p:E\to X$ constructed in the proof of Lemma 60.5: $X$ is
the union of two circles $A$ and $B$ meeting in the single point $x_0$, and $E$ is
the union of the $x$-axis, the $y$-axis, and a small circle tangent to each
nonzero integer point of either axis, with $p$ wrapping the $x$-axis around $A$,
the $y$-axis around $B$, and each tangent circle homeomorphically onto the other
circle; the integer points of both axes map to $x_0$.

Pearse, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005, §60
Exercise 3, his p. 27, read in `tmp/sources/cornell-erin-munkres.md`, is the source
of two things here. One is the description of the preimage, inside $E'$, of a small
neighbourhood of $x_0$: a small cross at the origin together with an open interval
about each nonzero integer point. The other is the observation that settles the
exercise at the basepoint, that such an interval and the cross in $X$ are not
homeomorphic, because no map of a cross onto an interval is injective.

The argument below is the card's own and does not follow the source's: it finds the
failure at the point $y=(1,0)$, where $E'$ is locally an interval of the $x$-axis,
and it never computes that preimage. What it uses is that $p$ carries the $x$-axis
into $A$, that every neighbourhood of $x_0$ in $X$ contains points of
$B-\theset{x_0}$, and that a sheet is connected and mapped homeomorphically.

::: pf

::: {.pf-step #local}
Near $y=(1,0)$ the space $E'$ is an interval of the $x$-axis, and $p$ carries it
into $A$; while every neighbourhood of $x_0$ in $X$ contains points of
$B-\theset{x_0}$.

::: pf-proof
The point $y=(1,0)$ lies on the $x$-axis and not on the $y$-axis, which is at
distance $1$ from it, so the disc of radius $\tfrac12$ about $y$ meets $E'$ in an
interval of the $x$-axis. The whole $x$-axis is carried by $p$ into $A$, by the
construction of $p$; so every neighbourhood of $y$ in $E'$ contains points, other
than $y$ itself, whose images lie in $A$.

On the other side, $B$ is a circle through $x_0$ and has no isolated points, so
for any neighbourhood $U$ of $x_0$ in $X$ the set $U\cap B$ is a neighbourhood of
$x_0$ in $B$ and contains points of $B-\theset{x_0}$. Those points lie in no
subset of $A$, since $A\cap B=\theset{x_0}$.
:::

:::

::: {.pf-step}
$\boxed{p'=\restrictionof{p}{E'}\ \text{is not a covering map}}$.

::: pf-proof
Suppose it were. Then $x_0$ has an evenly covered neighbourhood, and we may take
it of the form $U=D\cap X$ for an open disc $D$ about $x_0$ so small that $D\cap X$
lies in an evenly covered set: such a $U$ is evenly covered, a neighbourhood
contained in an evenly covered set being evenly covered by restriction of the
sheets, and it is connected, being the union of an arc of $A$ through $x_0$ and an
arc of $B$ through $x_0$. The point $y$ lies in a sheet $V$ of $p'^{-1}(U)$, that
is, a neighbourhood of $y$ in $E'$ that $p'$ maps homeomorphically onto $U$; so
$V$ is homeomorphic to $U$ and hence connected. Choose
$b\in U\cap(B-\theset{x_0})$, which is nonempty by step [](#local){.pf-ref}, and
then $z\in V$ with $p'(z)=b$.

The point $z$ is not on the $x$-axis, since $p$ carries the $x$-axis into $A$ and
$b\notin A$; so $z$ lies on the $y$-axis. Thus $V$ meets the $x$-axis at
$y\ne(0,0)$ and meets the $y$-axis at $z$. A subset of $E'$ meeting both axes
outside the origin contains the origin: without it, its intersections with the two
axes would be two disjoint nonempty sets, each open and closed in the subset, so
the subset would be disconnected. Hence $(0,0)\in V$. But
$p'(0,0)=x_0=p'(1,0)=p'(y)$ with $(0,0)\ne y$, so $p'$ is not injective on $V$,
contradicting that it maps $V$ homeomorphically onto $U$.
:::

:::

:::
:::
