---
title: The Riemann sphere
order: 58
topics:
- Riemann Sphere
- Extended Complex Plane
- Möbius Transformations
---

# The Riemann sphere

The plane plus one point at infinity is a compact surface on which every [[D-7DFVJ|meromorphic function]] becomes a [[D-E7A5W|holomorphic]] map to the sphere, and on which the [[D-FRVBV|Möbius transformations]] act as its biholomorphisms.

[[D-3QTVR]]

Stereographic projection from the north pole carries the plane onto the sphere of unit diameter minus that pole, sending the circle $\abs z = R$ to a circle of latitude and the disc $\abs z<R$ to the cap below it [@SS03, ch. 3, the Riemann sphere (pp. 88--89)]; a sequence with $\abs{z_n}\to\infty$ is exactly a sequence leaving every such cap, which is what makes $\infty$ a limit point.

## Maps of the sphere

[[T-UBWL2]]

[[D-FRVBV]]

A Möbius transformation permutes the generalized circles — the circles and the lines of $\CC$, a line being a circle through $\infty$ — and acts transitively on the triples of distinct points of $\CP^1$.

[[PR-74KHY]]

::: {.example title="The point at infinity in a coordinate"}
The map $z\mapsto1/z$ interchanges $0$ and $\infty$, and in the coordinate $w = 1/z$ near $\infty$ it reads $w\mapsto w$: the pole of $1/z$ at $0$ is the behaviour at $\infty$ of $z$ itself.
A polynomial of degree $n\geq1$ has a pole of order $n$ at $\infty$, since $p(1/w)$ has a pole of order $n$ at $w=0$ ([[D-BPBSQ|singularities at infinity]]).
:::

## Distance on the sphere

::: {.fact title="Chordal distance"}
The chordal distance between two points of $\CP^1$, measured in the stereographic model on the sphere of radius $1$, is
$$
d(z,w) = \frac{2\abs{z-w}}{\sqrt{1+\abs z^2}\sqrt{1+\abs w^2}}, \qquad d(z,\infty) = \frac{2}{\sqrt{1+\abs z^2}},
$$
so that $d(0,\infty) = 2$ is the diameter; on the sphere of diameter $1$ of [[D-3QTVR]] every distance is halved.
Either way this makes $\CP^1$ a compact metric space, and the metric gives the topology above.
It is the quantity that makes $\CP^1$ the natural target of the rational functions: a rational function extends to a continuous map $\CP^1\to\CP^1$, and because $\infty$ is at a finite distance from every point, a sequence of meromorphic functions that tends to $\infty$ uniformly is convergent in this metric like any other sequence of maps into a compact space.
:::
