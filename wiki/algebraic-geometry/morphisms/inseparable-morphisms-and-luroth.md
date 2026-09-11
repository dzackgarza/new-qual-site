---
title: Inseparable morphisms and Lüroth
order: 6
topics:
- Frobenius
- Purely Inseparable Extensions
- Rational Curves
---

# Inseparable morphisms and Lüroth

Every theorem on the previous page carries the word *separable*, and this page is what happens on the other side of it.
The answer is unusually clean for curves: inseparability is Frobenius and nothing else, so the exceptional case is completely classified rather than merely excluded.

## Frobenius as a morphism over $k$

[[D-IV2FROBTWIST]]

The point that gets dropped is that raising to the $p$-th power is not a morphism of $k$-schemes unless $k = \FF_p$, and the twist is the minimal repair.
After it, Frobenius is a finite morphism of degree $p$ and the field extension it induces is $k(X) \subseteq k(X)^{1/p}$, which is where the degree comes from.

[[PR-IV2INSEP]]

This is the classification: a purely inseparable morphism of curves is a composite of Frobenius maps, so it is an isomorphism of schemes that is not an isomorphism over $k$, and the genus does not move.
Riemann--Hurwitz does not merely fail here, it has nothing to measure, since the map on differentials is zero and $\Omega_{X/Y}$ is a line bundle rather than a torsion sheaf.

## What the classification buys

[[T-IV2LUROTH]]

Lüroth is the payoff, and the proof is two facts placed end to end: a finite morphism of curves cannot decrease the genus, and a genus-$0$ curve over an algebraically closed field is $\PP^1$.
The genus inequality needs both pages — Riemann--Hurwitz across the separable part, the proposition above across the inseparable part — which is why the characteristic-$p$ material is not an appendix to it.

Restated as geometry, Lüroth says unirational implies rational in dimension $1$.
Whether that survives in higher dimension is the Lüroth problem: yes for surfaces in characteristic $0$, no for surfaces in characteristic $p$, and no for threefolds over any field.
The counterexamples and their birational invariants are on the card, and naming one invariant is what separates an answer from a recollection.
