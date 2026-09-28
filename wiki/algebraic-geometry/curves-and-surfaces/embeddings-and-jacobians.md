---
title: Embeddings and Jacobians
order: 2
topics:
- Very Ample Divisors
- Canonical Divisor
- Jacobians
---

# Embeddings and Jacobians

[[T-D8TUX]]

In the criterion, $p\neq q$ is separation of points and $p=q$ is separation of tangent vectors at $p$.
Every $D$ with $\deg D\ge2g+1$ is very ample; the canonical divisor, of degree $2g-2$, is very ample exactly when $g\ge3$ and $C$ is not hyperelliptic.

If $g\ge2$, $\pi\colon C\to\PP^1$ has degree two, and $p+q$ is a fibre, then $K\sim(g-1)(p+q)$ and $\ell(K-p-q)=g-1=\ell(K)-1$, so $\abs{K}$ does not separate $p$ and $q$, and the canonical map factors through $\pi$.

## The Jacobian

[[T-U5QSY]]

By Abel's theorem and Jacobi inversion, the Abel--Jacobi map induces an isomorphism of groups $\Pic^0(X)\cong\Jac(X)=H^0(X,\Omega^1)^\vee/H_1(X,\ZZ)$, a $g$-dimensional complex torus that is an abelian variety.

In genus one, $p\mapsto[p-p_0]$ is an isomorphism $E\to\Jac(E)$, and it carries the group law of $(E,p_0)$ to addition in $\Jac(E)$.

The period construction is analytic and applies to curves over $\CC$.

[[T-CRVJACFUN]]

The functorial construction applies over any field and in families.
In $\Pic^0(X/T)=\Pic^0(X\times T)/p^*\Pic(T)$, the quotient identifies two families that differ by a line bundle pulled back from $T$; such families have isomorphic restrictions to every fibre $X_t$.

The tangent space at the origin, computed from $T=\Spec k[\varepsilon]/(\varepsilon^2)$, is $H^1(X,\OO_X)$, of dimension $g=\dim\Jac(X)$, so $\Jac(X)$ is smooth at the origin; translations act transitively on its points, so it is smooth everywhere.
Properness follows from the valuative criterion: for a discrete valuation ring $R$, $X\times\Spec R$ is regular, so a line bundle on the generic fibre extends by taking the closure of a divisor.

The map $\Sym^nX\to\Pic^n(X)$, $D\mapsto\OO_X(D)$, has fibre $\abs{L}\cong\PP^{\ell(L)-1}$ over $L$.
For $n\ge g$ it is surjective by Riemann--Roch, and for $n=g$ its general fibre is a point, so $\dim\Jac(X)=g$.
