---
schema: qual/card@1
id: E-UMMOE
kind: problem
title: A three-sheeted covering of the figure eight detecting two noncommuting loops
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
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Rewritten to use the covering space the exercise names. The previous solution argued that no
    incidence of four edges over three points makes $p$ a covering at the vertices, and so replaced
    the exercise's covering by the one of Lemma 60.5; the first of those claims is false. Three
    points over $x_0$ and the four edges $A_0,A_1,B_0,B_1$ do admit an incidence, the one drawn in
    Figure 60.3: $A_1$ passes through $e_0$ and $e_2$, $B_1$ through $e_0$ and $e_1$, $A_0$ is
    attached to $B_1$ at $e_1$ and $B_0$ to $A_1$ at $e_2$; each of the three points then has four
    ends, two over $A$ and two over $B$, because the attached circles contribute both their ends at
    the single vertex where they hang. With that incidence $p$ is a three-sheeted covering, the
    lift of the $A$-loop from $e_0$ ends at $e_2$, the lift of the $B$-loop from $e_0$ ends at
    $e_1$, and the products' lifts inherit those endpoints, which is Pearse's argument as written.
    The title changed from "two-fold" to "three-sheeted", the cover having three points over $x_0$;
    the Lemma 60.5 route is now only mentioned as the second proof it is. Checked against the book:
    the exercise and Figure 60.3 on printed p. 375, Lemma 60.5 and the description of its covering
    on printed pp. 373-374, Lemma 54.1 on printed p. 342 and Theorem 54.3 on printed p. 344.
    Correction to the source-checked note of 2026-11-14 above: the claim there that the incidence
    cannot be reconstructed is withdrawn, and the degrees of the edges together with the drawn
    incidence do determine the covering; not claimed: that either text writes the incidence in
    words -- the book's exercise states the degrees only, and Pearse reads the lifts off its own
    figure.
---

::: {.exercise}

Consider the covering map indicated in Figure 60.3 of the text.
Here, $p$ wraps $A_1$ around $A$ twice and wraps $B_1$ around $B$ twice; $p$ maps $A_0$ and $B_0$ homeomorphically onto $A$ and $B$, respectively.
Use this covering space to show that the fundamental group of the figure eight is not abelian.
:::

::: {.solution}
The exercise is §60 Exercise 5, and the answer is that the
fundamental group of the figure eight is not abelian. The proof is transcribed
from Pearse, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005,
§60 Exercise 5, his, read in
`tmp/sources/cornell-erin-munkres.md`: take two loops, lift them from one point of
the covering space the exercise names, and find that the two lifts of the two
products end at different points, so by Theorem 54.3  the products
are not path homotopic.

*The covering space.* Let $X=A\cup B$ be the figure eight, two circles meeting in
the single point $x_0$. The covering space of Figure 60.3 has
three points over $x_0$, written $e_0,e_1,e_2$, and four circles: the circle $A_1$
passes through $e_0$ and $e_2$, the circle $B_1$ passes through $e_0$ and $e_1$,
the circle $A_0$ is attached to $B_1$ at $e_1$, and the circle $B_0$ is attached
to $A_1$ at $e_2$. The map $p$ wraps each of the two arcs of $A_1$ once around
$A$, wraps each of the two arcs of $B_1$ once around $B$, and maps $A_0$
homeomorphically onto $A$ and $B_0$ homeomorphically onto $B$.

The exercise states only the degrees of its four edges, which points of the cover
they join being what its figure shows; the incidence above is the one drawn there,
and it is consistent. At $e_0$ the four ends are the two arcs of $A_1$ and the
two arcs of $B_1$; at $e_1$ they are the two arcs of $B_1$ together with the two
ends of the circle $A_0$ attached there; at $e_2$ they are the two arcs of $A_1$
together with the two ends of $B_0$. At each of the three points the four ends
map one-to-one onto the four half-arcs of $A$ and $B$ at $x_0$, so a small
neighbourhood of each is carried homeomorphically onto a neighbourhood of $x_0$,
and over a point of $A-\theset{x_0}$ and of $B-\theset{x_0}$ there are three
points of the cover. So $p$ is a covering map with three sheets. The two attached
circles each have both their ends at the one vertex they hang from, and that is
what the count requires: the named circles form a graph with six edges — $A_1$ and
$B_1$ each cut by its two vertices into two arcs, and $A_0$, $B_0$ being loops —
so twelve edge-ends in all, four at each of the three points.

::: pf

::: {.pf-step #lifts}
The lift of $f$ from $e_0$ ends at $e_2$ and the lift of $g$ from $e_0$ ends at
$e_1$, where $f$ and $g$ are the loops at $x_0$ going once around $A$ and once
around $B$. Hence the lift of $f*g$ from $e_0$ ends at $e_2$ and the lift of $g*f$
from $e_0$ ends at $e_1$.

::: pf-proof
Away from $x_0$ the loop $f$ lies in $A-\theset{x_0}$, and the points of the
cover over $A-\theset{x_0}$ are the interiors of the two arcs of $A_1$ and the
interior of the circle $A_0$. The ends at $e_0$ that lie over $A$ are therefore
the two arcs of $A_1$, the circle $A_0$ being attached at $e_1$. So a lift of $f$
from $e_0$ starts along one of those arcs and, $p$ being injective on the arc,
runs along it until $f$ returns to $x_0$, that is, to its other endpoint $e_2$.
Such a lift exists and is unique from the given point (Lemma 54.1), so the lift of $f$ from $e_0$ ends at $e_2$.

For the product $f*g$ the lift continues from $e_2$ with the lift of $g$. At
$e_2$ the ends over $B$ are the two ends of the circle $B_0$, since $B_1$ does
not pass through $e_2$; so the lift of $g$ from $e_2$ runs once around $B_0$ and
returns to $e_2$. Hence the lift of $f*g$ from $e_0$ ends at $e_2$.

The same argument with $A$ and $B$ exchanged and $e_1$ in place of $e_2$ gives
that the lift of $g$ from $e_0$ runs along an arc of $B_1$ to $e_1$, and that the
lift of $f$ from $e_1$ runs once around $A_0$ and returns to $e_1$; so the lift
of $g*f$ from $e_0$ ends at $e_1$.
:::

:::

::: {.pf-step}
$\boxed{\pi_1(X,x_0)\ \text{is not abelian}}$.

::: pf-proof
The points $e_1$ and $e_2$ are distinct. If $f*g$ and $g*f$ were path homotopic,
their lifts from the same point $e_0$ would end at the same point of the cover
(Theorem 54.3); by step [](#lifts){.pf-ref} those endpoints are
$e_1$ and $e_2$. Hence $[f]*[g]\ne[g]*[f]$ in $\pi_1(X,x_0)$, that is, the
fundamental group of the figure eight is not abelian. The covering gives another
proof of Lemma 60.5 , whose own covering the book describes in
words on printed pp. 373--374 and leaves to the reader to check.
:::

:::

:::
:::
