---
schema: qual/card@1
id: P-AMD-RKY5I5U7
kind: problem
title: Octagon pasting homeomorphic to $\mathbb{R}^2/\mathbb{Z}^2$
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Surfaces
  - Homeomorphisms
relations: []
review: draft
---

::: {.problem}
Show that octagon pasting is homeomorphic to the $T = \mathbb{R}^2 / \mathbb{Z}^2$.
:::

::: {.solution}
<1>1. The retained statement is under-specified: no octagon edge-pairing is given.
::: {.proof}
The original archived `Justin's Problems.pdf` contains exactly the sentence in this card and no accompanying octagon diagram; the legacy rendered solutions page likewise has an empty solution entry and no image reference. An octagon by itself does not determine a quotient space: the equivalence relation on its boundary is essential data.
:::

<1>2. Different edge-pairings of an octagon give non-homeomorphic spaces, so the missing data cannot be reconstructed from the word “octagon”.
::: {.proof}
For example, pairing the four pairs of opposite sides of a regular octagon by translations gives the standard closed orientable surface of genus $2$, whose first homology is $\mathbb Z^4$, so it is not a torus. On the other hand, subdivide each side of the standard square fundamental polygon for the torus into two segments; after a small deformation the resulting fundamental polygon is an octagon, and the induced pairings give a torus. Thus at least two inequivalent “octagon pastings” exist.
:::

<1>3. For the intended torus-type octagon pasting—namely, any octagon obtained by subdividing/deforming the square fundamental polygon while retaining the top-bottom and left-right translation identifications—the quotient is homeomorphic to
$$\boxed{\mathbb R^2/\mathbb Z^2.}$$
::: {.proof}
Let $Q=[0,1]^2$ with $(0,y)\sim(1,y)$ and $(x,0)\sim(x,1)$. Subdividing boundary edges and applying a homeomorphism from $Q$ onto an octagonal disc does not change the quotient relation: conjugating the square identifications by that homeomorphism gives the octagon pasting. Therefore the octagon quotient is homeomorphic to
$$Q/\sim\;\cong\mathbb R^2/\mathbb Z^2,$$
the latter homeomorphism being induced by $(x,y)\mapsto[(x,y)]$ modulo integer translations.
:::

<1>4. Hence a rigorous proof of the unconditional printed sentence is impossible until the missing edge-pairing diagram or equivalent boundary-identification data is restored.
::: {.proof}
By <1>2, the conclusion depends on that omitted datum. Step <1>3 proves the result once the intended torus-type pairing is specified.
:::
:::
