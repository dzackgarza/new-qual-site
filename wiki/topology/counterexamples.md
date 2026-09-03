---
title: Counterexamples
order: 9
topics:
- Counterexamples
---

# Counterexamples

Filed by the statement each one refutes.

## Point-set

**Compact implies closed** -- false without Hausdorff.
In the line with two origins, a compact set need not be closed; in a Hausdorff space it always is.

**Closed and bounded implies compact** -- false outside $\RR^n$: the unit ball of an infinite-dimensional normed space is closed, bounded, and not compact.

**Continuous image of a closed set is closed** -- false: projection $\RR^2\to\RR$ sends the hyperbola $xy=1$ onto $\RR\sm\ts0$.
Continuous images preserve compactness and connectedness, not closedness.

**A quotient of a Hausdorff space is Hausdorff** -- false: the line with two origins is a quotient of two copies of $\RR$.

**Connected implies path connected** -- false: the topologist's sine curve.
It is also the standard example of connected but not locally connected.

**Countable products of nice spaces stay nice** -- false in the box topology, true in the product topology.
$\RR^\omega$ is connected in the product topology and not in the box topology; connectedness of arbitrary products is a theorem for the product topology, not the box topology.

**A metric space is complete** -- not a topological property: $(0,1)$ and $\RR$ are homeomorphic and only one is complete.

## Fundamental group and covering spaces

**$\pi_1$ determines the space** -- false: $S^2$ and $\RP^2$ are distinguished by $\pi_1$, but $S^1\vee S^2$ and $S^1$ have the same $\pi_1$ and different homology.

**A simply connected space is contractible** -- false: $S^2$.

**Every space has a universal cover** -- false without semi-local simple connectedness: the Hawaiian earring.

**A subgroup of $\pi_1$ gives a covering space** -- true for nice spaces, and that correspondence is the classification; it fails exactly where the universal cover does.

## Homology

**Homology determines the space** -- false: the Poincaré homology sphere has the homology of $S^3$ and is not $S^3$; more simply, $S^1\vee S^2$ and $\RP^3$ are distinguished only by finer invariants.

**$H_*$ determines $\pi_1$** -- false, since $H_1$ sees only the abelianization: any perfect group has $H_1 = 0$.

**A map inducing isomorphisms on homology is a homotopy equivalence** -- true for simply connected CW complexes, false in general.

**Homology commutes with infinite products** -- false; it commutes with direct limits and with wedges.

## Manifolds

**A closed manifold has $H_n = \ZZ$** -- only if orientable.
The Klein bottle has $H_2 = 0$, which is exactly how it is told apart from the torus.

**Every manifold is triangulable** -- true in dimensions at most three, false in general.

**Homotopy equivalent manifolds are homeomorphic** -- false: homotopy type does not determine homeomorphism type.
