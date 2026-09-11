---
schema: qual/card@1
id: T-COHFLATCHI
kind: theorem
title: Flatness is constancy of the Hilbert polynomial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Families
  - Hilbert Polynomial
  - Euler Characteristic
relations:
- kind: uses
  target: D-COHEULER
review: draft
prompts:
- What does flatness do to the Hilbert polynomial?
- Give a family that is not flat, and say which invariant jumps.
---

::: {.theorem}
Let $T$ be an integral Noetherian scheme and $\mcf$ a coherent sheaf on $\PP^n_T$.
Then $\mcf$ is flat over $T$ exactly when the Hilbert polynomial of $\restrictionof{\mcf}{\PP^n_t}$ is the same for every $t \in T$.
:::

::: {.remark}
This is the theorem that makes "flat family" mean "family in which the numerical invariants do not jump", and it is the reason the Hilbert scheme is stratified by Hilbert polynomials.

The invariants that do stay constant are exactly the ones read off the Hilbert polynomial: degree, dimension, arithmetic genus, $\chi(\OO)$.
Everything else can degenerate.
Irreducibility, reducedness, the geometric genus, and the Picard number are all lost in flat limits, and a flat family with smooth general fibre can have a singular or non-reduced special fibre.
A conic degenerating to a double line keeps $\chi$ and loses reducedness; that is the standard example to have ready.

The non-example to quote is a blowup, which is not flat because the fibre dimension jumps over the centre.
:::
