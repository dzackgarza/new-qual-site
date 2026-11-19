---
schema: qual/card@1
id: E-HAT-3.3-1
kind: problem
title: Nonorientable 1-manifolds without Hausdorff
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: two copies of $\RR$ glued along their punctured lines by a homeomorphism
    that is increasing on one component of the overlap and decreasing on the other, so no choice of
    direction on the two charts is consistent; the two origins are distinct but inseparable, which
    is what the failure of the Hausdorff condition buys.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 1, printed p. 257. The collection's provenance is the book, and no retained solution set covers this exercise; the argument is the card's own. Checked: each copy of $\RR$ is an open chart; the two origins are not separated by disjoint neighbourhoods, so the Hausdorff condition genuinely fails; the transition is increasing on the positive component and equal to $t\mapsto1/t$, which is decreasing, on the negative one; and no choice of chart orientations can be consistent on both components, which is nonorientability.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Notation repair after the corpus check reported an undefined control word. The closing
    sentence of the chart step wrote `\R`, which neither vocabularies/macros.json nor the
    MathJax command set the site loads defines, so the page could not render it; the card writes
    `\RR` everywhere else, including three lines above, and now does here too. Mathematics
    unchanged.
---

::: {.problem}
Show that there exist nonorientable 1-dimensional manifolds if the Hausdorff condition is dropped from the definition of a manifold.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 1, printed p. 257. The point of the construction is the pair of origins: they are distinct, so the quotient is not Hausdorff, while the glued lines make it a connected 1-dimensional manifold with an orientation-reversing transition.

::: pf

::: {.pf-step #construction}
Let $\RR_+$ and $\RR_-$ be two copies of $\RR$, and let $X$ be the quotient of their disjoint union that identifies $t\in\RR_+\setminus\{0\}$ with $t\in\RR_-\setminus\{0\}$ for $t>0$ and with $1/t\in\RR_-\setminus\{0\}$ for $t<0$, leaving the two origins unglued.

::: pf-proof
The identification is a homeomorphism between the punctured lines, so the quotient is well defined; the two copies of $0$ are distinct points of $X$.
:::
:::

::: {.pf-step #manifold}
$X$ is a 1-dimensional manifold, with each copy of $\RR$ as a chart.

::: pf-proof
The image of $\RR_+$ in $X$ is the whole of $X$ minus the single point $0_-$, and likewise for $\RR_-$; each is open, and the map from $\RR$ to its image is a bijection onto an open set that is a homeomorphism for the quotient topology. So every point of $X$ lies in a chart homeomorphic to an open subset of $\RR$.
:::
:::

::: {.pf-step #hausdorff}
$X$ is not Hausdorff.

::: pf-proof
The two origins $0_+$ and $0_-$ are distinct. Every neighbourhood of $0_+$ contains the images of all sufficiently small positive $t$, and the same holds for $0_-$, because the positive parts of the two lines are identified; so no two disjoint open sets contain the two origins.
:::
:::

::: {.pf-step #connected}
$X$ is connected.

::: pf-proof
The image of each copy of $\RR$ is connected and meets the image of the other in the nonempty set of points represented by positive $t$, so the union of the two images, which is $X$, is connected.
:::
:::

::: {.pf-step #transition}
The transition between the two charts is $t\mapsto t$ on the positive component of the overlap and $t\mapsto 1/t$ on the negative component.

::: pf-proof
On the positive part the identification is the identity of $\RR$; on the negative part it is $t\mapsto1/t$, whose derivative $-1/t^2$ is negative, so it reverses the order while the identity preserves it.
:::
:::

::: {.pf-step #nonorientable}
$X$ is nonorientable.

::: pf-proof
An orientation of the connected manifold $X$ restricts to a choice of one of the two directions on each of the two charts, and these choices must be carried to each other by every chart transition. On the positive component of the overlap the identity requires the two choices to agree, while on the negative component the decreasing map $t\mapsto1/t$ requires them to disagree. No pair of choices satisfies both, so $X$ admits no orientation.
:::
:::

::: {.pf-step #conclusion}
There is a nonorientable 1-dimensional manifold that is not Hausdorff.

::: pf-proof
Steps [](#manifold){.pf-ref}, [](#hausdorff){.pf-ref} and [](#nonorientable){.pf-ref} give the three properties of $X$.
:::
:::

:::
:::
