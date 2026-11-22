---
title: Inseparable morphisms and Lüroth
order: 6
topics:
- Frobenius
- Purely Inseparable Extensions
- Rational Curves
---

# Inseparable morphisms and Lüroth

Over an algebraically closed field $k$ of characteristic $p>0$, a finite morphism $X\to Y$ of curves whose function-field extension is purely inseparable is a composition of $k$-linear Frobenius morphisms, $X$ and $Y$ are isomorphic as abstract schemes, and $g(X)=g(Y)$ [@Har77, Proposition IV.2.5]; every finite morphism of curves factors into a separable morphism followed by such a purely inseparable one [@Har77, Example IV.2.5.4].

## Frobenius as a morphism over $k$

[[D-IV2FROBTWIST]]

The absolute Frobenius is a morphism of $k$-schemes only when $a^p=a$ for every $a\in k$; the Frobenius twist modifies the structure morphism of the source so that the relative Frobenius is $k$-linear.
The $k$-linear Frobenius of a curve is finite of degree $p$ and induces $k(X)\subseteq k(X)^{1/p}$, an extension of degree $p$ because $k(X)$ has transcendence degree $1$ over the perfect field $k$.

[[PR-IV2INSEP]]

Over a perfect field a purely inseparable morphism of curves is a homeomorphism whose function-field extension is purely inseparable, and the genus is unchanged [@Har77, Proposition IV.2.5].
For the $k$-linear Frobenius $F\colon X\to X'$, the map $F^*\Omega_{X'}\to\Omega_X$ is zero, so $\Omega_{X/X'}\cong\Omega_X$ is a line bundle, and the Riemann--Hurwitz formula $2g-2=p(2g-2)$ fails for $g\neq1$ [@Har77, Example IV.2.5.1].

## Lüroth's theorem

[[T-IV2LUROTH]]

Lüroth's theorem is that a finitely generated subfield of $k(t)$ of transcendence degree one is of the form $k(u)$, so a curve dominated by $\PP^1$ is rational [@Har77, Example IV.2.5.5]; it uses that a finite morphism of smooth projective curves satisfies $g(X)\ge g(Y)$ [@Har77, Example IV.2.5.4].

Restated as geometry, Lüroth says unirational implies rational in dimension $1$.
In higher dimension this is the Lüroth problem: unirational implies rational for surfaces over an algebraically closed field of characteristic $0$, and fails for surfaces in characteristic $p$ (Zariski surfaces) and for threefolds over $\CC$ (cubic threefolds, by the intermediate Jacobian).
