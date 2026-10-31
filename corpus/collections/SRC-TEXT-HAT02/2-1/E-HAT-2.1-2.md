---
schema: qual/card@1
id: E-HAT-2.1-2
kind: problem
title: Edge identifications of $\Delta^3$ producing Klein bottle, torus, $S^2$, $\RP^2$
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
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The card wrote the vertices of the simplex as the Greek letter, `\nu_0`,
    where Hatcher writes them `v_0`; the vertex symbol is restored throughout.
    Found by comparing the statement with the printed exercise.
---

::: {.problem}
Show that the $\Delta$-complex obtained from $\Delta^3$ by performing the order-preserving edge identifications $[v_0, v_1] \sim [v_1, v_3]$ and $[v_0, v_2] \sim [v_2, v_3]$ deformation retracts onto a Klein bottle.
Find other pairs of identifications of edges that produce $\Delta$-complexes deformation retracting onto a torus, a 2 sphere, and $\RP^2$.
:::

::: {.solution}
Let the vertices of the tetrahedron be
$$
v_0,v_1,v_2,v_3.
$$
The union
$$
Q=[v_0,v_1,v_3]\cup[v_0,v_2,v_3]
$$
is a square split by the diagonal $[v_0,v_3]$, with boundary traversed as
$$
v_0\to v_1\to v_3\to v_2\to v_0.
$$

::: pf

::: {.pf-step #s1}

The tetrahedron deformation retracts onto $Q$ in a way compatible with identifications made only among the four boundary edges of $Q$.

::: pf-proof

The two omitted faces
$$
[v_0,v_1,v_2],
\qquad
[v_1,v_2,v_3]
$$
form an open book on the edge $[v_1,v_2]$ opposite the diagonal $[v_0,v_3]$.
Collapse each line segment transverse to $Q$ linearly onto $Q$.
This fixes $Q$ pointwise and gives a deformation retraction.
Since all edge identifications below involve only edges of $Q$, the retraction descends to the corresponding quotients.

:::

:::

::: {.pf-step #s2}

The identifications in the problem,
$$
[v_0,v_1]\sim[v_1,v_3],
\qquad
[v_0,v_2]\sim[v_2,v_3],
$$
produce the Klein bottle.

::: pf-proof

Call the first edge class $a$ and the second $b$.
Around the square boundary
$$
v_0\to v_1\to v_3\to v_2\to v_0
$$
the four directed sides become
$$
a,\ a,\ b^{-1},\ b^{-1}.
$$
Thus the quotient polygon has boundary word
$$
a^2b^{-2}.
$$
After replacing $b$ by $b^{-1}$ this is the standard nonorientable genus-two word
$$
a^2b^2,
$$
which is a Klein-bottle polygon.
By step [](#s1){.pf-ref} the full tetrahedral quotient deformation retracts onto this surface.

:::

:::

::: {.pf-step #s3}

A torus is obtained by the pairings
$$
[v_0,v_2]\sim[v_1,v_3],
\qquad
[v_0,v_1]\sim[v_2,v_3],
$$
with the displayed orderings preserved.

::: pf-proof

Let the first edge class be $b$ and the second $a$.
The square boundary word is then
$$
a\,b\,a^{-1}\,b^{-1},
$$
the standard torus polygon.

:::

:::

::: {.pf-step #s4}

A $2$-sphere is obtained by the pairings
$$
[v_0,v_2]\sim[v_3,v_2],
\qquad
[v_0,v_1]\sim[v_3,v_1].
$$

::: pf-proof

With suitable labels the square boundary word is
$$
a\,a^{-1}\,b\,b^{-1}.
$$
The two adjacent inverse pairs cancel by folding the corresponding bigons, leaving a $2$-sphere.
Equivalently, this is the usual two-disk decomposition of $S^2$ after the cancellations.

:::

:::

::: {.pf-step #s5}

A projective plane is obtained by the pairings
$$
[v_0,v_2]\sim[v_3,v_1],
\qquad
[v_0,v_1]\sim[v_3,v_2].
$$

::: pf-proof

The quotient has two vertex classes, two edge classes, and one $2$-cell.
One edge is a maximal-tree edge joining the two vertices.
Collapse it.
The remaining $1$-cell becomes a loop, and tracing the square boundary shows that the $2$-cell attaches by degree two around this loop.
Thus the quotient has the standard CW structure
$$
e^0\cup_{2}e^1\cup e^2
$$
of $\RP^2$.

:::

:::

::: pf-step

Hence the requested examples can be chosen exactly as in steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

::: pf-proof

Each follows from the square retraction in step [](#s1){.pf-ref} and the corresponding polygon identification.

:::

:::

:::

:::
