---
title: Vanishing and duality
order: 2
topics:
- Serre Criterion
- Serre Duality
- Riemann-Roch
---

# Vanishing and duality

Two theorems whose hypotheses control both the statements and their proofs.

[[T-5IOUR]]

The proof separates into two uses of its hypotheses.
Noetherianness supplies coherent ideals and finite subcovers, and both can be replaced: the criterion survives for quasicompact quasi-separated schemes with quasicoherent ideals.
Quasicompactness cannot be dropped, and the witness is an infinite disjoint union of affines — all higher cohomology vanishes, the scheme is not affine.

The two uses of the hypotheses are independent, so weakening either one must be checked at the step where it enters.

## Duality, and the theorem it makes computable

[[T-COHSD]]

In any dimension, duality is naturally stated using $\omega_X$ and the perfect pairing, with lower-dimensional forms obtained by specialization.
Smoothness is what identifies the dualizing sheaf with the top forms; properness is what makes the target $H^n(X,\omega_X) \cong k$ exist at all.

[[T-MWDVL]]

The Euler-characteristic form $\chi(\OO(D)) = \deg D + 1 - g$ is linear in $D$, and duality turns the unknown $h^1$ into a second $h^0$ that can be counted.

Two specializations are used repeatedly.
At $D = 0$ it says the global differentials on a curve of genus $g$ form a $g$-dimensional space.
At $D = K$ it gives $\deg K = 2g-2$, the input to Riemann--Hurwitz in [[algebraic-geometry/curves-and-surfaces/index|curves and surfaces]].

## One dimension up

[[T-COHRRS]]

The surface statement is the same theorem with the intersection pairing in place of the degree, and it is used for a different purpose: not to count sections but to force them to exist.
Duality converts $h^2$ into $h^0(K-D)$, and the resulting inequality gives a standard criterion for forcing a divisor on a surface to be effective.

## Finiteness and vanishing for ample twists

[[T-CARTSERRE]]

[[T-KODVAN]]

[[T-GAGA]]

## Topology of hyperplane sections

[[T-LEFHYP]]

[[T-HARDLEF]]
