---
title: Vanishing and duality
order: 2
topics:
- Serre Criterion
- Serre Duality
- Riemann-Roch
---

# Vanishing and duality

Two theorems, each asked as "state and prove" and then probed on its hypotheses.

[[T-5IOUR]]

The proof is short enough to give in full, and the probes attach to its two steps.
Noetherianness supplies coherent ideals and finite subcovers, and both can be replaced: the criterion survives for quasicompact quasi-separated schemes with quasicoherent ideals.
Quasicompactness cannot be dropped, and the witness is an infinite disjoint union of affines — all higher cohomology vanishes, the scheme is not affine.

Knowing which hypothesis is load-bearing is the entire content of the follow-ups, so it is worth rehearsing the proof until the two uses are visible.

## Duality, and the theorem it makes computable

[[T-COHSD]]

Duality is a statement in any dimension and gets asked in the dimension the examiner picks, so it is worth stating with $\omega_X$ and the perfect pairing first and specialising afterwards.
Smoothness is what identifies the dualizing sheaf with the top forms; properness is what makes the target $H^n(X,\omega_X) \cong k$ exist at all.

[[T-MWDVL]]

Riemann--Roch is stated best in its Euler-characteristic form: $\chi(\OO(D)) = \deg D + 1 - g$ is linear in $D$, and duality is what turns the unknown $h^1$ into a second $h^0$ that can be counted.

The two specialisations are asked directly.
At $D = 0$ it says the global differentials on a curve of genus $g$ form a $g$-dimensional space.
At $D = K$ it gives $\deg K = 2g-2$, the input to Riemann--Hurwitz in [[algebraic-geometry/curves-and-surfaces/index|curves and surfaces]].

## One dimension up

[[T-COHRRS]]

The surface statement is the same theorem with the intersection pairing in place of the degree, and it is used for a different purpose: not to count sections but to force them to exist.
Duality converts $h^2$ into $h^0(K-D)$, and the resulting inequality is the first move in any question about whether a divisor on a surface is effective.

## Finiteness and vanishing for ample twists

[[T-CARTSERRE]]

[[T-KODVAN]]

[[T-GAGA]]

## Topology of hyperplane sections

[[T-LEFHYP]]

[[T-HARDLEF]]

## Affineness and nilpotents

[[T-AFFRED]]
