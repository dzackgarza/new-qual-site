---
title: Smooth, unramified, and étale
order: 4
topics:
- Smooth Morphisms
- Étale Morphisms
- Jacobian Criterion
---

# Smooth, unramified, and étale

Three conditions on a morphism that all say "the fibres are as nice as the base allows", differing in the relative dimension they permit.
The organising statement is that étale is smooth of relative dimension $0$, and that unramified is the half of étale that flatness is missing from.

## Unramified and étale

[[D-MORUNR]]

[[D-MORETALE]]

The differentials give the working criterion in both cases: unramified is $\Omega_{X/Y} = 0$, and étale is that together with flatness.
For a map of curves the condition is that every ramification index is $1$, which is the same $e_p$ that Riemann--Hurwitz counts, so this is not a separate theory from [[algebraic-geometry/curves-and-surfaces/index|curves]].

## Ramification, measured

[[D-IV2RAM]]

Ramified is the negation of unramified, and it is measured rather than merely observed: $e_p$ counts how far the pulled-back uniformizer is from being one, and the length of $(\Omega_{X/Y})_p$ turns that count into the divisor Riemann--Hurwitz adds up.
The two agree only when $e_p$ is invertible in $k$; in the wild case the length is strictly larger than $e_p-1$.

[[PR-IV2DEGREVEN]]

The parity statement gives an immediate consistency check on any branching count.

## Étale covers

[[D-IV2ETCOV]]

Finite étale is the algebraic covering space, and the projective line has only the trivial ones, by the same Riemann--Hurwitz with the ramification term set to zero.
In characteristic $p$ the affine line has nontrivial Artin--Schreier covers, while $\PP^1$ has no nontrivial finite étale covers.

## Smoothness

[[D-MORSM]]

[[T-MORSMREG]]

Smooth is a property of a morphism, regular is a property of a local ring, and they agree over a perfect field and not otherwise.
The failure over imperfect fields comes from inseparability; $\Spec \FF_p(t)[x]/(x^p-t)$ is regular but not smooth.

[[PR-MORJAC]]

The Jacobian criterion must be applied on the variety itself: a rank drop is relevant only at points satisfying the defining equations.

## Where smoothness fails

[[FE-MORFROB]]

[[T-MORGEN]]

Frobenius is nowhere smooth and shows why generic smoothness needs characteristic zero.
Generic *flatness* has no characteristic-zero hypothesis.

## Normal and regular morphisms

[[D-MORNORMREG]]

## Henselian rings

[[D-HENSEL]]
