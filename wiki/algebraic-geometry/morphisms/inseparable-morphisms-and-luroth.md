---
title: Inseparable morphisms and Lüroth
order: 6
topics:
- Frobenius
- Purely Inseparable Extensions
- Rational Curves
---

# Inseparable morphisms and Lüroth

Over an algebraically closed field $k$ of characteristic $p>0$, a finite morphism $X\to Y$ of smooth projective curves factors as a purely inseparable morphism $X\to X'$ followed by a separable morphism $X'\to Y$, and every purely inseparable morphism of curves is a composite of $k$-linear Frobenius morphisms.

## Frobenius as a morphism over $k$

[[D-IV2FROBTWIST]]

The absolute Frobenius is a morphism of $k$-schemes only when $a^p=a$ for every $a\in k$; the Frobenius twist modifies the structure morphism of the source so that the relative Frobenius is $k$-linear.
The $k$-linear Frobenius of a curve is finite of degree $p$ and induces $k(X)\subseteq k(X)^{1/p}$, an extension of degree $p$ because $k(X)$ has transcendence degree $1$ over the perfect field $k$.

[[PR-IV2INSEP]]

The source and target of a purely inseparable morphism of curves are isomorphic as schemes, not over $k$, so they have the same genus.
For the $k$-linear Frobenius $F\colon X\to X'$, the map $F^*\Omega_{X'}\to\Omega_X$ is zero, so $\Omega_{X/X'}\cong\Omega_X$ is a line bundle, and the Riemann--Hurwitz formula $2g-2=p(2g-2)$ fails for $g\neq1$.

## Lüroth's theorem

[[T-IV2LUROTH]]

In the proof, a finite morphism $X\to Y$ of smooth projective curves satisfies $g(X)\ge g(Y)$: Riemann--Hurwitz gives the inequality across the separable part, and [[PR-IV2INSEP]] gives equality across the purely inseparable part.
A genus-$0$ curve over an algebraically closed field is $\PP^1$.

Restated as geometry, Lüroth says unirational implies rational in dimension $1$.
In higher dimension this is the Lüroth problem: unirational implies rational for surfaces over an algebraically closed field of characteristic $0$, and fails for surfaces in characteristic $p$ (Zariski surfaces) and for threefolds over $\CC$ (cubic threefolds, by the intermediate Jacobian).
