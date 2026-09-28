---
title: Smooth, unramified, and étale
order: 4
topics:
- Smooth Morphisms
- Étale Morphisms
- Jacobian Criterion
---

# Smooth, unramified, and étale

A morphism locally of finite presentation is étale exactly when it is smooth of relative dimension $0$, and exactly when it is flat and unramified.

## Unramified and étale

[[D-MORUNR]]

[[D-MORETALE]]

A morphism locally of finite type is unramified exactly when $\Omega_{X/Y}=0$, and étale exactly when it is also flat.
A finite morphism of smooth curves over an algebraically closed field is unramified at $p$ exactly when $e_p=1$; these are the ramification indices in [[algebraic-geometry/curves-and-surfaces/genus|Riemann--Hurwitz]].

## Ramification index and ramification divisor

[[D-IV2RAM]]

For a uniformizer $t$ at $f(p)$, $e_p=v_p(f^*t)$, and the ramification divisor is $R=\sum_p\operatorname{length}(\Omega_{X/Y})_p\cdot p$.
The length equals $e_p-1$ exactly when $e_p$ is invertible in $k$; in the wild case it is strictly larger than $e_p-1$.

[[PR-IV2DEGREVEN]]

For a degree-two cover of $\PP^1$ by a curve of genus $g$, in characteristic $\neq2$, every ramification point has $e_p=2$, and parity with Riemann--Hurwitz gives $2g+2$ branch points.

## Étale covers

[[D-IV2ETCOV]]

A connected finite étale cover $X\to\PP^1$ of degree $n$ has $2g_X-2=-2n$ by Riemann--Hurwitz, so $n=1$: $\PP^1$ has no nontrivial connected finite étale covers.
In characteristic $p$ the affine line has the nontrivial connected finite étale Artin--Schreier covers $y^p-y=x$.

## Smoothness

[[D-MORSM]]

[[T-MORSMREG]]

A scheme $X$ locally of finite type over a field $k$ is smooth over $k$ exactly when $X_{\bar k}$ is regular; for $k$ perfect this holds exactly when $X$ is regular.
Over the imperfect field $\FF_p(t)$, $\Spec\FF_p(t)[x]/(x^p-t)$ is regular, being a field, and is not smooth, since $\FF_p(t^{1/p})\otimes_{\FF_p(t)}\overline{\FF_p(t)}$ is not reduced.

[[PR-MORJAC]]

## Where smoothness fails

[[FE-MORFROB]]

[[T-MORGEN]]

The Frobenius $F\colon\PP^n_k\to\PP^n_k$ in characteristic $p$ is a dominant morphism of smooth varieties that is smooth at no point, so generic smoothness fails in characteristic $p$.
$F$ is finite and flat, and generic flatness holds in every characteristic.

## Normal and regular morphisms

[[D-MORNORMREG]]

## Henselian rings

[[D-HENSEL]]
