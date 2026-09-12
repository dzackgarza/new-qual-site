---
title: Cohomology of projective schemes
order: 4
topics:
- Coherent Sheaves
- Vanishing Theorems
- Euler Characteristic
---

# Cohomology of projective schemes

Properness is what makes cohomology finite, and twisting is what makes it vanish.

[[T-COHFIN]]

[[T-COHSVAN]]

The two are proved together.
Finiteness is the statement that lets one write $h^i$ at all; Serre vanishing is the statement that lets one ignore everything except $h^0$ after a large enough twist.
The threshold in "$n \gg 0$" depends on the sheaf, and no single $n$ works for every coherent sheaf at once: shifting the sheaf by a negative twist delays the vanishing beyond any fixed bound.

## The invariant that does not jump

[[D-COHEULER]]

[[T-COHFLATCHI]]

Individual cohomology dimensions are unstable and their alternating sum is not.
The Hilbert polynomial as a graded-ring construction lives in [[algebraic-geometry/varieties/dimension-and-degree|dimension and degree]]; the content here is that it equals $\chi(\mcf(n))$, and that this identification is what makes flatness and constancy of numerical invariants the same condition.

Flatness, from [[algebraic-geometry/morphisms/finite-and-flat|finite and flat]], is then not a technical hypothesis but a definition of "family" chosen so that the Euler characteristic is constant.
