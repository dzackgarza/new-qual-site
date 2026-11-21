---
title: Functors and topologies
order: 1
topics:
- Functors Of Points
- Grothendieck Topologies
- Descent
---

# Functors and topologies

A scheme is studied through the functor it represents on test schemes, and once the objects are functors the topology can be changed: covers need not be open immersions, and the sheaf condition is stated for a Grothendieck topology rather than for a topological space [@Vak25, §6.2].

## Functors of points

[[FE-SCHREPFUNCTORS]]

[[D-OPENSUBFUNCTOR]]

A morphism $X\to Y$ of schemes is an isomorphism exactly when the induced natural transformation of functors $\mathrm{Hom}(-,X)\to\mathrm{Hom}(-,Y)$ is an isomorphism on every test scheme, by the Yoneda lemma applied to the restricted functor of points on affine schemes ([[PR-SCHFOP]], [[FE-SCHREPFUNCTORS]]).

## Grothendieck topologies

[[D-GROTHTOP]]

[[D-ETFPPF]]

A Grothendieck topology on a category specifies, for each object, the families of morphisms that count as covers, subject to the axioms that isomorphisms are covers and that covers pull back and compose; the fppf topology is the one whose covers are jointly surjective flat families of finite presentation ([[D-GROTHTOP]], [[D-ETFPPF]]).

## Descent

[[T-FFDESCENT]]

A sheaf for a Grothendieck topology is a functor whose sections satisfy the gluing axiom for every cover of that topology, so descent is the statement that a quasicoherent sheaf on a scheme is the same data on any fppf cover, together with the gluing isomorphism on the fibre products of the cover ([[T-FFDESCENT]], [[D-GROTHTOP]]).

## Torsors

[[D-TORSOR]]
