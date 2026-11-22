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

A morphism $X\to Y$ of schemes is an isomorphism exactly when the induced natural transformation of functors $\Hom(-,X)\to\Hom(-,Y)$ is an isomorphism on every test scheme, by the Yoneda lemma applied to the restricted functor of points on affine schemes ([[PR-SCHFOP]], [[FE-SCHREPFUNCTORS]]).

## Grothendieck topologies

[[D-GROTHTOP]]

[[D-ETFPPF]]

On $\Sch_{/S}$ the étale and fppf pretopologies generate the topologies of [[D-ETFPPF]], and a cover of either is a family $\{U_i\to U\}_{i\in I}$ that is jointly surjective and whose members are étale, respectively flat and locally of finite presentation ([[D-ETFPPF]], [[D-GROTHTOP]]).

## Descent

[[T-FFDESCENT]]

Descent for a cover is the statement that a quasicoherent sheaf on a scheme is the same data on an fppf cover: a descent datum is an isomorphism $\theta\colon C\tensor_{B,p_1}N\to C\tensor_{B,p_2}N$ of $C$-modules satisfying the cocycle identity $p_{23}^*\theta\circ p_{12}^*\theta=p_{13}^*\theta$ after pullback to $B\tensor_AB\tensor_AB$, and for faithfully flat $A\to B$ the descent data on $B$-modules are equivalent to the $A$-modules ([[T-FFDESCENT]], [[D-GROTHTOP]]).

## Torsors

[[D-TORSOR]]
