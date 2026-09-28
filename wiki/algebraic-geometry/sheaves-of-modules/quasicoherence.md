---
title: Quasicoherence and twisting
order: 1
topics:
- Quasicoherent Sheaves
- Line Bundles
- Twisting Sheaves
---

# Quasicoherence and twisting

A sheaf of modules is useful exactly when it is locally a module, and the bank asks this twice: once about differentials, once about the sheaves on projective space that everything is built from.

[[D-QNTZY]]

The question "is this sheaf quasicoherent" is answered by exhibiting a local presentation, never by producing a global module.
That is the form to reach for, because a presentation exists in cases where the module is unavailable.

## The twists

[[D-CB9XS]]

[[FE-SHFPONE]]

$\OO(1)$ is where the grading on the homogeneous coordinate ring becomes geometry: its sections are the linear forms, its $d$-th power has the degree-$d$ forms, and the Hilbert polynomial of [[algebraic-geometry/varieties/dimension-and-degree|dimension and degree]] is the function $d \mapsto h^0(X, \OO_X(d))$ for $d \gg 0$.

Every coherent sheaf on projective space is a quotient of a sum of twists.
The consequence to carry is that any cohomological statement about coherent sheaves can be proved by descending induction from the twists, which is how the computation of $H^*(\PP^n, \OO(d))$ becomes the computation of everything.
