---
title: Classes of morphism
order: 3
topics:
- Immersions
- Finite Type Morphisms
- Projective Morphisms
---

# Classes of morphism

## Immersions

[[D-MORIMM]]

A homeomorphism onto a closed subset need not be a closed immersion: the normalization $\AA^1_k\to V(y^2-x^3)$, $t\mapsto(t^2,t^3)$, is a homeomorphism, and $k[t^2,t^3]\to k[t]$ is not surjective.

## Affine, finite, and finite type

[[D-MORAFF]]

[[D-MORFT]]

[[D-MORFIN]]

Finite means finitely generated as a module, while finite type means finitely generated as an algebra; $\AA^1_k \to \Spec k$ separates the two notions.

[[D-MORQF]]

[[FE-MORHYP]]

[[PR-MORFINCHAR]]

## Projective

[[D-MORPROJ]]

The implication chain is
$$
\text{closed immersion} \implies \text{finite} \implies \text{projective} \implies \text{proper} \implies \text{universally closed} ,
$$
together with the fact that finite type sits underneath all of it and is implied by each.
Standard converse counterexamples include $\PP^1_k \to \Spec k$, which is projective but not finite, and the hyperbola projection, which is quasi-finite but not proper.

## Base change

[[D-MORFIB]]

[[PR-MORBC]]

If a property $P$ is stable under base change and $f\colon X\to Y$ has $P$, then every fibre $X_y\to\Spec\kappa(y)$ has $P$.
Closedness is not stable under base change: $\AA^1_k\to\Spec k$ is closed, but its base change $\AA^2_k\to\AA^1_k$, $(x,y)\mapsto x$, sends the closed set $V(xy-1)$ onto $\AA^1_k\setminus\{0\}$.
Properness therefore requires universal closedness.

## Locality of properties of morphisms

[[D-MORLOCAL]]

## Cancellation

[[PR-MORCANCEL]]
