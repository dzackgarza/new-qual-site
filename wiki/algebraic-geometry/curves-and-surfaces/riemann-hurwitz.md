---
title: Riemann--Hurwitz
order: 11
topics:
- Riemann-Hurwitz
- Ramification
- Branched Covers
---

# Riemann--Hurwitz

A finite separable morphism of smooth curves is a covering map away from finitely many points, and Riemann–Hurwitz is the bookkeeping of what happens at those points.
The statement is that the pullback of the canonical class falls short of the canonical class of the source by exactly the ramification divisor, and taking degrees turns it into a formula for the genus of a cover in terms of the genus of the base, the degree, and the ramification.
That formula is how almost every genus in this chapter is computed, and its failure in characteristic $p$ is where wild ramification enters.

## Ramification

[[D-IV2RAM]]

The ramification index $e_p$ is the order of vanishing at $p$ of a pulled-back uniformizer, so it measures how many sheets the map collapses locally, and $e_p=1$ at all points is the unramified case — a covering map.
For a finite separable morphism only finitely many points are ramified, since separability makes $\Omega_{X/Y}$ a torsion sheaf supported on the points where the map is not locally an isomorphism; inseparable maps are ramified everywhere, which is the whole reason the separability hypothesis is in the theorem.

## The Hurwitz formula

[[T-LKT0U]]

The proof is worth keeping in mind because it is the model for every other computation of a canonical class: the relative cotangent sequence
$$
\inverseof{f}\Omega_Y\longrightarrow\Omega_X\longrightarrow\Omega_{X/Y}\longrightarrow0
$$
is short exact for a nonconstant separable map, the left map is injective exactly because of separability, and $\Omega_{X/Y}$ is a torsion sheaf whose length at $p$ is the contribution of $p$ to $\deg R$.
So $K_X=f^*K_Y+R$ as divisor classes, and the displayed formula is its degree.

## What the formula computes

[[PR-IV2DEGREVEN]]

A cover of $\PP^1$ of degree $n$ has $2g_X-2=-2n+\deg R$, so the genus is read off the ramification: a degree-$n$ map with $2n-2$ points of simple ramification has $g_X=0$ and is the standard rational cover, and a degree-two cover with $2g+2$ branch points has $g_X=g$ — the hyperelliptic family ([[D-CRVHYP]]).
That the degree of the ramification divisor is even is not obvious from the definition and is immediate from the formula, which is the reason it is stated as a proposition: it is a parity constraint on which ramification data can occur.

## Wild ramification

In characteristic $p$ an index can be divisible by $p$, and then $\length(\Omega_{X/Y})_p$ exceeds $e_p-1$: the contribution of $p$ to $R$ is the different exponent
$$
d_p=e_p-1+\text{(a correction divisible by }p\text{)},
$$
so the tame formula $\deg R=\sum(e_p-1)$ is an underestimate and the Hurwitz formula still holds with the different.
The smallest example is already instructive: the Artin–Schreier cover $y^p-y=x$ is a degree-$p$ map $\PP^1\to\PP^1$ ramified only over $\infty$, where the different exponent is $2p-2$ rather than the $p-1$ the tame count would give, and the source is still rational — the true count $2p-2$ is what makes $2g-2=-2p+(2p-2)=-2$ come out, while the tame count would give no genus at all ([@Har77, Section IV.2]).
Separability cannot be dropped either, and the failure is total: the Frobenius $\PP^1\to\PP^1$ is a homeomorphism with $e_p=p$ everywhere, kills every differential, and the formula has no meaning for it.

## Inseparable and purely inseparable maps

[[PR-IV2INSEP]]

[[D-IV2FROBTWIST]]

In dimension one the inseparable maps are not a small pathology but a described family: a purely inseparable morphism of smooth curves is a relative Frobenius, so every inseparable cover is obtained from a separable one by composing with a Frobenius twist of the source.
That is what makes the separable hypothesis of Riemann–Hurwitz harmless in practice: an inseparable map of curves is a composition of maps of degree $p^k$ whose structure is known, and the interesting geometry happens in the separable part ([[FE-MORFROB]]).

## Where the formula is used

Riemann–Hurwitz is the tool that computes a genus from a description of a curve as a cover: the plane curve of degree $d$ with its projection to $\PP^1$, the hyperelliptic curve with its degree-two map, and the modular curve of a subgroup are all handled the same way ([[algebraic-geometry/curves-and-surfaces/genus|genus]]).
It is also the constraint that rules out maps: a curve with a large automorphism group has to ramify, and the bound $\cardinality{\Aut C}\le 84(g-1)$ for $g\ge2$ is exactly that constraint pushed to its limit ([[PR-CRVAUT]]).
