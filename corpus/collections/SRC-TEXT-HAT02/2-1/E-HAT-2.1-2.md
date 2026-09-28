---
schema: qual/card@1
id: E-HAT-2.1-2
kind: problem
title: Edge identifications of $\Delta^3$ producing Klein bottle, torus, $S^2$, $\mathbb{RP}^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Collapsed the tetrahedron to the two-face square and read the four side-pairing words, giving the Klein bottle, torus, sphere, and projective plane.
---

::: {.problem}
Show that the $\Delta$-complex obtained from $\Delta^3$ by performing the edge identifications $[\nu_0, \nu_1] \sim [\nu_1, \nu_3]$ and $[\nu_0, \nu_2] \sim [\nu_2, \nu_3]$ deformation retracts onto a Klein bottle.
Find other pairs of identifications of edges that produce $\Delta$-complexes deformation retracting onto a torus, a 2 sphere, and $\mathbb{RP}^2$.
:::

::: {.solution}
Let the vertices of the tetrahedron be
\[
\nu_0,\nu_1,\nu_2,\nu_3.
\]
The union
\[
Q=[\nu_0,\nu_1,\nu_3]\cup[\nu_0,\nu_2,\nu_3]
\]
is a square split by the diagonal $[\nu_0,\nu_3]$, with boundary traversed as
\[
\nu_0\to\nu_1\to\nu_3\to\nu_2\to\nu_0.
\]

<1>1. The tetrahedron deformation retracts onto $Q$ in a way compatible with identifications made only among the four boundary edges of $Q$.
::: {.proof}
The two omitted faces
\[
[\nu_0,\nu_1,\nu_2],
\qquad
[\nu_1,\nu_2,\nu_3]
\]
form an open book on the edge $[\nu_1,\nu_2]$ opposite the diagonal $[\nu_0,\nu_3]$.
Collapse each line segment transverse to $Q$ linearly onto $Q$.
This fixes $Q$ pointwise and gives a deformation retraction.
Since all edge identifications below involve only edges of $Q$, the retraction descends to the corresponding quotients.
:::

<1>2. The identifications in the problem,
\[
[\nu_0,\nu_1]\sim[\nu_1,\nu_3],
\qquad
[\nu_0,\nu_2]\sim[\nu_2,\nu_3],
\]
produce the Klein bottle.
::: {.proof}
Call the first edge class $a$ and the second $b$.
Around the square boundary
\[
\nu_0\to\nu_1\to\nu_3\to\nu_2\to\nu_0
\]
the four directed sides become
\[
a,\ a,\ b^{-1},\ b^{-1}.
\]
Thus the quotient polygon has boundary word
\[
a^2b^{-2}.
\]
After replacing $b$ by $b^{-1}$ this is the standard nonorientable genus-two word
\[
a^2b^2,
\]
which is a Klein-bottle polygon.
By <1>1 the full tetrahedral quotient deformation retracts onto this surface.
:::

<1>3. A torus is obtained by the pairings
\[
[\nu_0,\nu_2]\sim[\nu_1,\nu_3],
\qquad
[\nu_0,\nu_1]\sim[\nu_2,\nu_3],
\]
with the displayed orderings preserved.
::: {.proof}
Let the first edge class be $b$ and the second $a$.
The square boundary word is then
\[
a\,b\,a^{-1}\,b^{-1},
\]
the standard torus polygon.
:::

<1>4. A $2$-sphere is obtained by the pairings
\[
[\nu_0,\nu_2]\sim[\nu_3,\nu_2],
\qquad
[\nu_0,\nu_1]\sim[\nu_3,\nu_1].
\]
::: {.proof}
With suitable labels the square boundary word is
\[
a\,a^{-1}\,b\,b^{-1}.
\]
The two adjacent inverse pairs cancel by folding the corresponding bigons, leaving a $2$-sphere.
Equivalently, this is the usual two-disk decomposition of $S^2$ after the cancellations.
:::

<1>5. A projective plane is obtained by the pairings
\[
[\nu_0,\nu_2]\sim[\nu_3,\nu_1],
\qquad
[\nu_0,\nu_1]\sim[\nu_3,\nu_2].
\]
::: {.proof}
The quotient has two vertex classes, two edge classes, and one $2$-cell.
One edge is a maximal-tree edge joining the two vertices.
Collapse it.
The remaining $1$-cell becomes a loop, and tracing the square boundary shows that the $2$-cell attaches by degree two around this loop.
Thus the quotient has the standard CW structure
\[
e^0\cup_{2}e^1\cup e^2
\]
of $\mathbb{RP}^2$.
:::

<1>6. Hence the requested examples can be chosen exactly as in <1>2--<1>5.
::: {.proof}
Each follows from the square retraction in <1>1 and the corresponding polygon identification.
:::
:::
