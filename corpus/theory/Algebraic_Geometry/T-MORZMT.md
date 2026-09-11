---
schema: qual/card@1
id: T-MORZMT
kind: theorem
title: Zariski's main theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski's Main Theorem
  - Quasi-finite Morphisms
  - Normality
relations:
- kind: uses
  target: D-MORQF
- kind: uses
  target: PR-MORFINCHAR
review: draft
prompts:
- State Zariski's main theorem.
- What does Zariski's main theorem say about birational morphisms to a normal variety?
---

::: {.theorem title="Grothendieck's form"}
A separated quasi-finite morphism $f : X \to Y$ of Noetherian schemes factors as
\[
X \injects \overline{X} \to Y
\]
with the first an open immersion and the second finite.
:::

::: {.theorem title="Zariski's form"}
Let $f : X \to Y$ be a birational projective morphism of Noetherian integral schemes with $Y$ **normal**.
Then $f_* \OO_X = \OO_Y$ and every fibre of $f$ is connected.
In particular a birational projective morphism to a normal $Y$ that is quasi-finite is an isomorphism.
:::

::: {.remark}
The first form is the structural statement: quasi-finite is finite minus a compactification, which is exactly what the hyperbola projection showed, and the theorem says that gap is the only one.
Read alongside "finite equals proper plus quasi-finite", it says a quasi-finite morphism fails to be finite only by missing points of a finite one.

The second form is the one used in birational geometry, and normality is where all the weight sits.
Without it the theorem fails: the normalisation of a nodal cubic is a birational projective quasi-finite morphism that is not an isomorphism, and the two preimages of the node are exactly the disconnected fibre that normality would forbid.
So the theorem is the precise sense in which a normal variety cannot be improved by a birational morphism without contracting something positive-dimensional.
:::
