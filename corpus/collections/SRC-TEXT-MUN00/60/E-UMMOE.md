---
schema: qual/card@1
id: E-UMMOE
kind: problem
title: A two-fold covering detecting nonabelian fundamental group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 5, printed p. 375,
    with Lemma 60.5 and the homotopy lifting criterion, Lemma 54.3. The lifts of $f*g$ and $g*f$ from the same point end at distinct vertices of the covering shown in Figure 60.3, so the loops are not path homotopic and the two classes do not commute. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    The published proof of this exercise is Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §60 Exercise 5, his pp. 27-28, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md, and its argument is transcribed on the card: two loops,
    their lifts from one point, different endpoints, Theorem 54.3. Its covering space, and the
    book's Figure 60.3, are pictures: the source names the edges $A_0,A_1,B_0,B_1$ and their
    degrees and then reads the liftings off Figure 8 without stating which vertices the edges join,
    and the book's exercise states only the degrees. The card records that the two endpoints are
    therefore not in the text, and that no incidence with four edges over three points makes the
    map a covering at the vertices, so the picture cannot be reconstructed from the text; the
    argument is carried out instead with the covering of Lemma 60.5, whose construction the book
    gives in words on printed pp. 373-374, and the conclusion proved is Lemma 60.5, that the
    figure-eight group is not abelian. Checked against the book: the exercise on printed p. 375,
    Lemma 60.5 and its proof on printed pp. 373-374, Lemma 54.1 on printed p. 342 and Theorem 54.3
    on printed p. 344. Not claimed: that the book proves $p$ is a covering map for the Lemma 60.5
    space -- it leaves that to the reader, and the card says so.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as above, in Lamport form, with the sourced argument, the part with
    no transcribable source, and the book's pages named in its own text.
---

::: {.exercise}

Consider the covering map indicated in Figure 60.3 of the text.
Here, $p$ wraps $A_1$ around $A$ twice and wraps $B_1$ around $B$ twice; $p$ maps $A_0$ and $B_0$ homeomorphically onto $A$ and $B$, respectively.
Use this covering space to show that the fundamental group of the figure eight is not abelian.
:::

::: {.solution}
The exercise is §60 Exercise 5, printed p. 375, and the answer is that the
fundamental group of the figure eight is not abelian. The argument is the one
Pearse gives, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005,
§60 Exercise 5, his pp. 27--28, read in
`tmp/sources/cornell-erin-munkres.md`: exhibit a covering of the figure eight,
lift the loops $f*g$ and $g*f$ from the same point, and find that the two lifts
end at different points, so by Theorem 54.3 (printed p. 344) the loops are not
path homotopic.

The covering space the exercise names cannot be used for that as the text stands.
The book's exercise states only the degrees of its four edges — $p$ wraps $A_1$
around $A$ twice, $B_1$ around $B$ twice, and maps $A_0$ and $B_0$
homeomorphically — and its Figure 60.3 is a picture; Pearse's text names the same
four edges and reads the two liftings off its own Figure 8, without stating which
vertices the edges join. Which points of the cover the two lifts end at is
therefore not in either text, and a graph with three points over $x_0$ and four
edges has no consistent incidence that makes its covering map a covering at the
vertices, so the picture cannot be reconstructed from the text either. So this
part of the exercise has no transcribable published proof, and the card carries
out the same argument with the covering of Lemma 60.5, whose construction the book
states in words on printed pp. 373--374; the conclusion is Lemma 60.5 itself,
that the figure-eight group is not abelian.

Take $X=A\cup B$ the union of two circles in $\RR^2$ meeting in the single point
$x_0$, and let $E$ be the subspace of the plane consisting of the $x$-axis, the
$y$-axis, and one small circle tangent to the $x$-axis at each nonzero integer
point and one small circle tangent to the $y$-axis at each nonzero integer point.
Let $p:E\to X$ wrap the $x$-axis around $A$ and the $y$-axis around $B$, carrying
each integer point of either axis to $x_0$, carry each circle tangent to the
$x$-axis homeomorphically onto $B$, and carry each circle tangent to the
$y$-axis homeomorphically onto $A$; the book's proof of Lemma 60.5 asserts, and
asks the reader to check, that $p$ is a covering map.

::: pf

::: {.pf-step #loops}
$f=p\circ\tilde f$ and $g=p\circ\tilde g$ are loops in $X$ at $x_0$ going once
around $A$ and once around $B$, where $\tilde f(s)=(s,0)$ and $\tilde g(s)=(0,s)$
for $s\in I$.

::: pf-proof
$\tilde f$ runs along the $x$-axis from the origin to $(1,0)$, and $p$ wraps the
$x$-axis once around $A$ carrying both endpoints to $x_0$; so $f$ is a loop at
$x_0$ going once around $A$. Likewise $\tilde g$ runs along the $y$-axis from the
origin to $(0,1)$, which $p$ wraps once around $B$.
:::

:::

::: {.pf-step #lifts}
The lift of $f*g$ beginning at the origin ends at $(1,0)$, and the lift of $g*f$
beginning at the origin ends at $(0,1)$.

::: pf-proof
Consider the path in $E$ that runs along the $x$-axis from the origin to $(1,0)$
and then once around the circle $C_1$ tangent to the $x$-axis at $(1,0)$. It is
continuous, it begins at the origin, and it projects under $p$ to $f$ followed by
a loop based at $x_0$ traversing $B$ once, because $p$ carries $C_1$
homeomorphically onto $B$ and carries the tangency point to $x_0$; that composite
is $f*g$. Since the lift of a path from a given point is unique (Lemma 54.1,
printed p. 342), this is the lift of $f*g$ from the origin, and it ends at
$(1,0)$, which lies in $p^{-1}(x_0)$.

Likewise the path along the $y$-axis from the origin to $(0,1)$ followed by once
around the circle tangent there projects to $g*f$, since that circle maps
homeomorphically onto $A$; so the lift of $g*f$ ends at $(0,1)$.
:::

:::

::: {.pf-step}
$\boxed{\pi_1(X,x_0)\ \text{is not abelian}}$.

::: pf-proof
The points $(1,0)$ and $(0,1)$ are distinct, so the lifts of $f*g$ and of $g*f$
starting at the origin do not end at the same point. By Theorem 54.3 (printed
p. 344) two paths from $x_0$ to $x_0$ that are path homotopic have lifts from a
given point ending at the same point; hence $f*g$ and $g*f$ are not path
homotopic, that is, $[f]*[g]\ne[g]*[f]$ in $\pi_1(X,x_0)$, and the group is not
abelian. That is Lemma 60.5, printed p. 373.
:::

:::

:::
:::
