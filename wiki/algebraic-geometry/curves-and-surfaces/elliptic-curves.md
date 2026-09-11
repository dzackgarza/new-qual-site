---
title: Elliptic curves
order: 4
topics:
- Elliptic Curves
- j-Invariant
- Group Schemes
---

# Elliptic curves

Genus $1$ is the only genus where the classification is finished, and the reason is that the curve is its own Jacobian.

[[PR-CRVGRP]]

The group law is not extra structure laid on top of the curve.
It is linear equivalence, transported along a Riemann--Roch bijection, and the chord-and-tangent construction is that equivalence written in the coordinates of the plane cubic model.

Asked whether an elliptic curve is a group scheme, the answer is yes and the proof is that addition and inversion are morphisms, which is what makes $[n]$ a finite morphism with computable kernel.

## Classification

[[T-CRVJINV]]

The construction chains together the tools from the rest of the chapter: $\abs{2p_0}$ gives the degree-two map, Riemann--Hurwitz counts four branch points, a Möbius transformation normalizes three of them, and $j$ is the symmetric function killing the residual $S_3$-ambiguity.

The word *coarse* carries weight.
Points of $\AA^1$ are isomorphism classes, but there are nontrivial families with all fibres isomorphic, so no fine moduli space exists — the automorphisms $\pm 1$ present on every elliptic curve are what obstruct it.
