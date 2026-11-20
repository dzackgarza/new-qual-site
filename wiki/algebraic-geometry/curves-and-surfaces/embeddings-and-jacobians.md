---
title: Embeddings and Jacobians
order: 9
topics:
- Jacobian
- Abel-Jacobi
- Canonical Embedding
---

# Embeddings and Jacobians

Two constructions attach a projective space or an abelian variety to a smooth projective curve: a very ample class gives a closed embedding into $\PP^N$ ([[T-DIVMAPPN]]), and the degree-zero part of the Picard group gives the Jacobian, an abelian variety of dimension $g$ whose tangent space at the identity is $H^1(C,\OO_C)$ ([[T-CRVJACFUN]], [[D-MODPIC]]).

[[T-D8TUX]]

## The Jacobian

[[T-U5QSY]]

[[T-CRVJACFUN]]

For a smooth projective curve $C$ of genus $g$ the functor of degree-zero line bundles is represented by a smooth proper group scheme $\Jac(C)$ of dimension $g$, so $\Pic^0(C)$ is the group of points of $\Jac(C)$ ([[T-U5QSY]], [[T-CRVJACFUN]], [[D-MODPIC]]).
A point $P_0\in C(k)$ gives the morphism $C\to\Jac(C)$, $P\mapsto\OO_C(P-P_0)$, which is an embedding for $g\ge1$ ([[T-U5QSY]]); the theta divisor on $\Jac(C)$ is the principal polarization ([[D-DIVPOLAR]]).

## Abel--Jacobi

The Abel--Jacobi map sends a degree-zero divisor $\sum_i(p_i-q_i)$ to the functional $\omega\mapsto\sum_i\int_{q_i}^{p_i}\omega$ on $H^0(C,\Omega_C^1)$ ([[T-U5QSY]]).
Abel's theorem says that a degree-zero divisor is principal exactly when its image is zero, and Jacobi inversion says that the map is surjective; together they identify $\Pic^0(C)$ with $\Jac(C)(\CC)$ ([[T-U5QSY]]).
In genus $1$ the map $P\mapsto\OO_C(P-P_0)$ is an isomorphism $C\to\Jac(C)$ ([[T-U5QSY]], [[T-CRVJACFUN]]).
