---
title: Weil and Cartier
order: 1
topics:
- Divisors
- Cartier Divisors
- Picard Group
---

# Weil and Cartier

The topic has three parts: define Weil and Cartier divisors, identify when they agree, and compute the resulting class groups or Picard groups.

[[D-5PQ5W]]

[[PR-DIVZEROPOLE]]

A Weil divisor is a subvariety of codimension one; a Cartier divisor is a local equation.
Where the local rings are unique factorization domains a subvariety has a local equation and the two agree, and where they are not, it need not.
On a smooth curve every local ring is a discrete valuation ring, so codimension-one subvarieties and local equations are related by the valuation at each point.

[[PR-Y5S7V]]

[[D-CRVDEGREES]]

[[T-MOVLEM]]

## Computing a Picard group

[[FE-ADOKK]]

The method generalises to every computation in this topic: compare $X$ with something whose Picard group is known, and identify the correction term.
For a singular curve the comparison is with the normalization and the correction is the local unit groups.
For an open subset $U = X \sm Z$ of a smooth variety, the comparison is the excision sequence
\[
\ZZ^{\ts{\text{components of } Z \text{ of codimension } 1}} \to \Cl(X) \to \Cl(U) \to 0 ,
\]
which computes $\Cl(\AA^n) = 0$ from $\Cl(\PP^n) = \ZZ$ and gives the class group of any hypersurface complement immediately.

[[FE-DIVPN]]

[[FE-DIVP1E]]

Together these give model computations of class groups on projective spaces and open subsets, and of $\Pic^0$ on a curve.

## Reduced divisors, multiplicities and pullback

[[D-DIVREDMULT]]
