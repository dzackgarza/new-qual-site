---
title: Dimension
order: 7
topics:
- Dimension
- Krull Dimension
- Codimension
---

# Dimension

Dimension is the one numerical invariant of a scheme that is decided by the underlying topological space alone, and on an affine scheme it is a ring-theoretic invariant: chains of irreducible closed subsets are chains of prime ideals with the order reversed.
This page states both descriptions, records the theorems that make the invariant computable — the principal ideal theorem, the additivity of dimension along a closed subset, the coincidence with transcendence degree — and keeps the two ways dimension is used apart: as the bound in the vanishing theorems, and as the exponent in fibre-dimension statements.

## Dimension and codimension

[[D-SCHDIM]]

The definition sees no nilpotents: $\dim X=\dim X^\red$, so a fat point has dimension zero however long its coordinate ring is.
Codimension is the local invariant, and the equality $\codim_X Z=\dim\OO_{X,\zeta}$ at the generic point $\zeta$ of $Z$ is what turns statements about chains of subvarieties into statements about local rings.

## Krull dimension

[[D-5LJUX]]

For a finitely generated domain $B$ over a field, $\krulldim B=\trdeg_k\Frac B$, so the dimension of a variety is the number of independent parameters and nothing more complicated.
The same comparison is what makes dimension computable on a scheme: $\dim\Spec A=\krulldim A$ for every ring, whether or not it is noetherian, and the local rings of an irreducible closed subset of codimension one are exactly the one-dimensional ones.

## Codimension one

[[PR-VARHT]]

Krull's principal ideal theorem is the reason codimension-one subvarieties are hypersurfaces wherever the ambient scheme is factorial: in a unique factorization domain every height-one prime is principal, so every irreducible closed subset of codimension one in affine space is cut out by one equation.
It cuts the other way too: the criterion that a noetherian domain is a unique factorization domain exactly when every height-one prime is principal makes the class group of the previous chapter a codimension-one measurement ([[algebraic-geometry/divisors/class-group-and-picard-group|the class group and the Picard group]]).

## Dimension and cohomology

[[T-COHGROTH]]

The bound is topological and holds for every sheaf of abelian groups on a noetherian space, which is why it appears before any hypothesis of quasicoherence is available.
It is attained: $H^n(\PP^n,\OO(-n-1))\neq0$ ([[T-IJW1K]]), so the vanishing theorem cannot be improved and the dimension of a projective scheme is genuinely its cohomological length.

## Dimension in families

For a morphism $f\colon X\to Y$ the dimension of a fibre is an upper semicontinuous function of the point of $Y$, so $\dim X-\dim Y$ is a bound and not an equality, and the failure of equality is what the fibre dimension theorem measures ([[T-MORFIBDIM]]).
The hypothesis that restores it is a dimension count plus Cohen--Macaulayness: for a morphism locally of finite type from a Cohen--Macaulay scheme to a regular one, the equality $\dim\OO_{X,x}=\dim\OO_{Y,y}+\dim\OO_{X_y,x}$ at every point forces flatness ([[T-MORMIRACLE]]).

## Dimension as a hypothesis

Two appearances of the number in this chapter are worth separating.
Dimension bounds cohomology from above, which is a statement about a single scheme and needs no family; and dimension constrains fibres, which is a statement about all fibres at once and needs flatness to be useful.
[[algebraic-geometry/varieties/dimension-and-degree|Dimension and degree]] is the projective case of the same invariant, where the Hilbert polynomial refines the dimension by one more number, its degree.
