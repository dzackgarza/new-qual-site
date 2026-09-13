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

The genus-one case is the one asked about, and the answer is that the Abel--Jacobi map is an isomorphism $E \to \Jac(E)$ — an elliptic curve is its own Jacobian, and its group law is Abel's theorem written for three points.

That construction uses periods and integration, so it exists only over $\CC$.

[[T-CRVJACFUN]]

The functorial construction is the one that survives in characteristic $p$ and in families, and asking for it is the standard way to push past the analytic answer.
The definition to be able to write down is $\Pic^0(X/T) = \Pic^0(X \times T)/p^*\Pic(T)$; the quotient is what makes the functor representable, since a bundle pulled back from the base twists nothing on any fibre.

Smooth of dimension $g$ comes from dual numbers — the tangent space at the origin is $H^1(X, \OO_X)$ — plus the observation that a group scheme is homogeneous, so smoothness at one point is smoothness everywhere.
Properness is the valuative criterion, and it works because $X \times \operatorname{Spec} R$ is regular, so divisors extend.

The map from $\Sym^n X$ is the computational handle: surjective once $n \geq g$ by Riemann--Roch, with fibres the complete linear systems, which recovers $\dim \Jac(X) = g$ a second time.
