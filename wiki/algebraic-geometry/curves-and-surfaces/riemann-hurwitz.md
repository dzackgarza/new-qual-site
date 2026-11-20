---
title: Riemann--Hurwitz
order: 11
topics:
- Riemann-Hurwitz
- Ramification
- Branched Covers
---

# Riemann--Hurwitz

Let $f\colon X\to Y$ be a finite separable morphism of smooth projective curves over an algebraically closed field $k$, of degree $n$, with ramification divisor $R=\sum_{p\in X}\length(\Omega_{X/Y})_p\cdot p$.
Then $K_X\sim f^*K_Y+R$ [@Har77, Proposition IV.2.3], and on degrees
$$
2g_X-2=n(2g_Y-2)+\deg R
$$
[@Har77, Corollary IV.2.4].
At a tamely ramified point $\length(\Omega_{X/Y})_p=e_p-1$, and at a wildly ramified point $\length(\Omega_{X/Y})_p\ge e_p$; so $\deg R=\sum_p(e_p-1)$ holds exactly when no point is wildly ramified [@Har77, Proposition IV.2.2 and Corollary IV.2.4, pp. 300--301].

## Ramification

[[D-IV2RAM]]

## The Hurwitz formula

[[T-LKT0U]]

## Genus computations

[[PR-IV2DEGREVEN]]

A degree-$n$ cover of $\PP^1$ has $2g_X-2=-2n+\deg R$, so $2n-2$ points of simple ramification give $g_X=0$, and a degree-two cover of $\PP^1$ with $2g+2$ branch points has $g_X=g$.

## Inseparable maps

[[D-IV2FROBTWIST]]

[[PR-IV2INSEP]]

Separability is a hypothesis of the formula, and it fails for the $k$-linear Frobenius $f\colon Y_p\to Y$: there $f^*\Omega_Y\to\Omega_X$ is the zero map and $\Omega_{X/Y}\cong\Omega_X$ [@Har77, Example IV.2.5.1], which is not a torsion sheaf, so its lengths do not define a ramification divisor and $K_X\sim f^*K_Y+R$ has no analogue.
A finite morphism of curves with purely inseparable function-field extension thus changes no genus [@Har77, Proposition IV.2.5], and Riemann--Hurwitz constrains only the separable part of a general finite morphism [@Har77, Example IV.2.5.4].
