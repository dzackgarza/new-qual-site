---
schema: qual/card@1
id: E-0LZE7
kind: problem
title: The figure eight and the theta space are homotopy equivalent
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
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
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 4, printed p. 366,
    with Example 3 of Section 58 and the homotopy invariance of $\pi_1$. The card describes $f$ and $g$ explicitly and proves $g\circ f\simeq\mathrm{id}_X$ by cancelling the constant loops. For $f\circ g$ it uses that the quotient of the theta space by its central segment, a contractible subcomplex, is a homotopy equivalence, so that $g$ is one and $f$, being a one-sided inverse, is the other; an explicit homotopy exists as well, by sliding each of $f\circ g$'s trips along the central segment, and the card's route is correct on the book's definitions. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published answer has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §58 Exercise 4, his pp. 22-23, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution transcribes the source's description of the
    two maps — the figure eight collapsed onto the vertical bar of the theta, and the bar collapsed
    to the join point — and states what the source gives only in words with its Figure 7, namely
    the two homotopies. Those are supplied here from the book rather than asserted: the figure
    eight and the theta space are both deformation retracts of the doubly punctured plane by
    Examples 2 and 3 on printed p. 362, and composing the inclusion of one space with the
    retraction onto the other gives maps homotopy inverse by §51 Exercise 1 (printed p. 330). So
    the part of the exercise with no written source is the existence of the two homotopies, and
    the card says so. Checked against the book: the exercise on printed p. 367 (the earlier note
    above gave printed p. 366, which is where the exercise list begins; this exercise is on the
    second page of it), the definition of homotopy inverse on printed p. 363, and Examples 2 and 3
    on printed p. 362. Correction to the note of 2026-11-11: that proof rested on the quotient of
    the theta by its central segment being a homotopy equivalence through a contractible
    subcomplex, which is a later chapter's result and was not available in Section 58; the
    argument now on the card uses only Examples 2 and 3.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the description plus the check above, in Lamport form.
---

::: {.exercise}

Let $X$ be the figure eight and let $Y$ be the theta space.
Describe maps $f: X \to Y$ and $g: Y \to X$ that are homotopy inverse to each other.
:::

::: {.solution}
The exercise is §58 Exercise 4, printed p. 367, and it asks for a description of
the two maps. The description is transcribed from Pearse, *Topology (2nd ed.) —
James R. Munkres*, solutions, Cornell 2005, §58 Exercise 4, his pp. 22--23, read
in `tmp/sources/cornell-erin-munkres.md`: the source maps the figure eight into
the theta space by collapsing the region it encloses to the vertical bar of the
theta, and the theta space into the figure eight by collapsing the vertical bar
to the point where the two loops of the figure eight meet. Neither map is
injective, so neither has an inverse, and the source then asserts that the two
composites are homotopic to the identities and describes those homotopies only in
words, with its Figure 7: the composite on the figure eight "scrunchens all the
points inside the dotted line down into the centre point", and the composite on
the theta space "collapses the vertical bar to the centre point of the vertical
bar, and continuously slurps in part of the boundary of the circle to replace the
bar". The source gives no formulas for the two homotopies.

What the source leaves in words is settled here from the book. Both spaces are
deformation retracts of the doubly punctured plane $\RR^2-p-q$: the figure eight
by Example 2 and the theta space by Example 3, both printed p. 362. That gives
maps that are homotopy inverse by three steps of the book's own results, and they
are the description above: a map into the plane followed by a retraction collapses
a region to a graph.

Write $P=\RR^2-p-q$, let $i_X:X\to P$ and $i_Y:Y\to P$ be the inclusions and
$r_X:P\to X$, $r_Y:P\to Y$ the retractions, so that $r_X\circ i_X=
\operatorname{id}_X$, $r_Y\circ i_Y=\operatorname{id}_Y$, and $i_X\circ r_X$ and
$i_Y\circ r_Y$ are each homotopic to $\operatorname{id}_P$ by a homotopy starting
at the identity. Put $f=r_Y\circ i_X:X\to Y$ and $g=r_X\circ i_Y:Y\to X$.

::: pf

::: {.pf-step #gf}
$g\circ f\simeq\operatorname{id}_X$.

::: pf-proof
$g\circ f=r_X\circ i_Y\circ r_Y\circ i_X$. The homotopy
$i_Y\circ r_Y\simeq\operatorname{id}_P$ fixed at its start, composed with $r_X$
on the left and $i_X$ on the right, is a homotopy from
$r_X\circ i_Y\circ r_Y\circ i_X$ to $r_X\circ\operatorname{id}_P\circ i_X=
r_X\circ i_X=\operatorname{id}_X$, by §51 Exercise 1 (printed p. 330).
:::

:::

::: {.pf-step #fg}
$f\circ g\simeq\operatorname{id}_Y$.

::: pf-proof
$f\circ g=r_Y\circ i_X\circ r_X\circ i_Y$, and composing the homotopy
$i_X\circ r_X\simeq\operatorname{id}_P$ with $r_Y$ on the left and $i_Y$ on the
right gives a homotopy to $r_Y\circ i_Y=\operatorname{id}_Y$.
:::

:::

::: {.pf-step}
$\boxed{\text{The figure eight and the theta space are homotopy equivalent}}$,
with $f$ and $g$ as above homotopy inverse to each other.

::: pf-proof
Steps [](#gf){.pf-ref} and [](#fg){.pf-ref} are exactly the two requirements of
the definition on printed p. 363, so $f$ is a homotopy equivalence with homotopy
inverse $g$. The description of the two maps is the source's: $f$ carries the
figure eight into the plane and retracts it onto the theta, which collapses the
region the figure eight encloses onto the vertical bar of the theta, and $g$
carries the theta into the plane and retracts it onto the figure eight, which
collapses the vertical bar to the point where the two loops meet.
:::

:::

:::
:::
