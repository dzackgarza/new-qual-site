---
title: Fibre products and base change
order: 4
topics:
- Fibre Products
- Base Change
- Functor Of Points
---

# Fibre products and base change

The fibre product is the one construction that carries the weight of the theory: intersections, fibres, field extensions and products are all the same operation with different labels.

[[D-SCHFPR]]

The affine case is the whole computation, and the gluing is bookkeeping.
Say the tensor product first, then note that the underlying set of a fibre product is not the fibre product of the underlying sets — this is the standard follow-up and the place where a set-theoretic instinct goes wrong.

## Fibres

[[PR-SCHFIB]]

The fibre is the reason for the construction.
A morphism is a family of schemes parametrised by the target, and the scheme-theoretic fibre is what keeps that family from losing information at the bad points: multiplicity at a branch point and a residue field extension at a point that only splits after enlarging the field.

## Base change

[[D-SCHBC]]

Base change is the single operation behind three different questions, and naming which one is in play is most of an answer.
"Geometrically integral" is base change to every field extension; "the fibre over $y$" is base change to $\Spec \kappa(y)$; "spread out over a smaller base" is base change along a map of bases.
The list of adjectives stable under base change is long and the exceptions are few, so the examiner will ask for an exception rather than the list.

## The functor of points

[[PR-SCHFOP]]

The universal property in the definition of the fibre product is a statement about $\Hom(T, -)$ for all $T$, which is to say it is a statement about the functor of points.
Reading it that way turns the two standard computations — maps out of a field and maps out of the dual numbers — into the statement that points and tangent vectors are both things a scheme is probed by, and it is the language in which moduli problems are posed.
