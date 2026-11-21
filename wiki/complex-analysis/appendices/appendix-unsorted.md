---
order: 91
title: The Gamma function and conic sections
topics:
- Gamma Function
- Conic Sections
---

# The Gamma function and conic sections

## The Gamma function

[[D-Q3MYK]]

The integral $\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\dt$ converges for $\Re z>0$, and the integration by parts that gives $\Gamma(z+1) = z\Gamma(z)$ is what continues it: $\Gamma(n+1) = n!$ for $n\geq0$, and $\Gamma$ has simple poles at $0,-1,-2,\ldots$ with no others.

[[PR-NLV6Q]]

[[PR-FBQ6F]]

The poles, residues, product expansion, and reflection formula of $\Gamma$ are on [[complex-analysis/appendices/special-functions#The Gamma function|Special functions]], and its relation to the Beta function is on [[complex-analysis/appendices/special-functions#The Beta function|the Beta function]].

## Conic sections

A conic is the zero set of a quadratic $Q(x,y) = ax^2+bxy+cy^2+dx+ey+f$; for a nondegenerate real conic with at least one real point, the discriminant $b^2-4ac$ decides its type — negative for an ellipse, zero for a parabola, positive for a hyperbola — and completing the square brings it to a standard form.

::: {.fact title="Conics in polar form"}
With the focus at the origin and the directrix the line $x = d$, the conic with eccentricity $e\geq0$ is
$$
r = \frac{ed}{1+e\cos\theta},
$$
an ellipse for $0<e<1$, a parabola for $e = 1$, and a hyperbola for $e>1$; the equation is the polar form of the focus--directrix definition, the ratio of the distance to the focus to the distance to the directrix being $e$.
The standard forms, their classification by the discriminant, and completing the square are on [[complex-analysis/basics/precalculus|Precalculus preliminaries]].
:::

[[E-6H7HD]]
