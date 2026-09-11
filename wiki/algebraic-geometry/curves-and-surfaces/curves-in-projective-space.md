---
title: Curves in projective space
order: 5
topics:
- Space Curves
- Projection
- Quadric Surface
---

# Curves in projective space

A curve is abstract until a divisor puts it somewhere.
The questions here are which divisors do that, where the curve lands, and what pairs of degree and genus are possible.

[[PR-CRVDEGBD]]

The three thresholds are one Riemann--Roch computation repeated, and the thing to be able to say is which of them are sharp.
None of the sufficient conditions is necessary, and the canonical divisor on a plane quartic is the counterexample to keep.

[[T-CRVEMBP3]]

Every curve fits in $\PP^3$, and the argument is a dimension count: secants sweep a threefold, tangents a surface, so a general centre of projection misses both until the ambient space runs out of room.
Projecting once more into the plane costs injectivity, and nodes are the cheapest way to pay.

[[D-CRVPLSING]]

Being able to name what is worse than a node is what makes the previous sentence a claim rather than a slogan.
The examiner's question is usually why a given plane model cannot have come from a general projection, and the answer is that its singularity is a codimension-one coincidence.

## Curves on a quadric

[[FE-CRVQUAD]]

This is the example family to reach for whenever a curve of prescribed genus is needed, since type $(g+1,2)$ produces one for every $g$.
It also identifies most of the named space curves: the twisted cubic is type $(1,2)$, the elliptic quartic is $(2,2)$, and the canonical genus-$4$ sextic is $(3,3)$.

## What is possible

[[T-CRVCAST]]

Castelnuovo's bound and its equality case are the same statement read twice, because the extremal curves are the balanced curves on a quadric.
Comparing it with $\binom{d-1}{2}$ for plane curves gives the slogan: spreading a curve out into $\PP^3$ costs about half its genus.

[[FE-CRVDEGS]]

Organising the low-degree list by whether $\OO_C(1)$ is special is what makes it memorable, rather than a table.
