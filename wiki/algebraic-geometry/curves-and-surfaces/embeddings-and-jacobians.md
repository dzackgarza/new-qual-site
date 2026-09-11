---
title: Embeddings and Jacobians
order: 2
topics:
- Very Ample Divisors
- Canonical Divisor
- Jacobians
---

# Embeddings and Jacobians

Having a genus, the next questions are what the curve can be embedded as and what its line bundles form.

[[T-D8TUX]]

The numerical criterion is the thing to remember, because it converts "is this an embedding" into two applications of Riemann--Roch: a linear system embeds exactly when removing any two points drops the dimension by two, which is separating points and tangent vectors written arithmetically.
Degree at least $2g+1$ is the crude sufficient condition, and the canonical system is the interesting borderline case.

Hyperelliptic curves are the exception in every statement here, and they are the exception for one reason: a degree-two map to $\PP^1$ is a pencil that cannot be made to separate the two points of a fibre.

## The Jacobian

[[T-U5QSY]]

Abel's theorem and Jacobi inversion together identify $\Pic^0$ with a $g$-dimensional abelian variety, which is the sense in which the Jacobian is significant: the classification of degree-zero line bundles stops being a list and becomes a variety.

The genus-one case is the one asked about, and the answer is that the Abel--Jacobi map is an isomorphism $E \to \operatorname{Jac}(E)$ — an elliptic curve is its own Jacobian, and its group law is Abel's theorem written for three points.
