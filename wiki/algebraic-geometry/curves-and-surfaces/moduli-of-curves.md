---
title: Moduli of curves
order: 6
topics:
- Moduli
- Automorphisms
- Curves
---

# Moduli of curves

The coarse moduli space in genus $0$ is a point, while in genus $1$ the $j$-invariant identifies the coarse moduli space with $\AA^1$.
For $g\ge2$, the coarse moduli space $M_g$ is an irreducible quasi-projective variety of dimension $3g-3$.

[[D-CRVMOD]]

A fine moduli space represents the functor of families of smooth curves of genus $g$; a coarse moduli space receives a natural transformation from that functor that is universal among maps to schemes and bijective on geometric points.
Let $C$ have an automorphism $\sigma$ of order $2$, with $\operatorname{char}k\neq2$.
The quotient of $C\times\Gm$ by $(x,t)\mapsto(\sigma x,-t)$, mapped to $\Gm$ by $t\mapsto t^2$, is a family whose fibres are all isomorphic to $C$ but which is not isomorphic to $C\times\Gm$; a fine moduli space would classify it by a constant map and force it to be trivial.

For genus $1$, [[algebraic-geometry/curves-and-surfaces/elliptic-curves|elliptic curves]] gives the coarse moduli space $\AA^1$ with coordinate $j$ and the nontrivial family $ty^2=x^3-x$ with constant fibres.

## The dimension count

[[T-CRVMG]]

Deformation theory gives $h^1(C,T_C)=h^0(C,\omega_C^{\otimes2})=3g-3$.
In genus $2$, six branch points on $\PP^1$ modulo $\PGL_2$ give $6-3=3$.
In genus $3$, smooth plane quartics, an open subset of $\PP^{14}$, modulo $\PGL_3$ give $14-8=6$.

## Automorphism groups

[[PR-CRVAUT]]

Finiteness of $\Aut C$ makes each $\PGL_3$-orbit of smooth plane quartics $8$-dimensional, which the count $14-8=6$ uses; nontriviality of $\Aut C$ on the hyperelliptic locus is what keeps any genus from having a fine moduli space.

## Smoothness and properness of the moduli stacks

[[T-MGSMOOTH]]

## Stable maps

[[D-STABLEMAP]]
