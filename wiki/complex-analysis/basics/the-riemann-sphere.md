---
title: The Riemann sphere
order: 58
topics:
- Riemann Sphere
- Extended Complex Plane
- Möbius Transformations
---

# The Riemann sphere

This page writes $\CC$ for the plane, $\CP^1$ for the sphere and $\infty$ for the point at infinity, all as in the transcluded definition.

[[D-3QTVR]]

Stereographic projection from the north pole carries the plane onto the sphere of unit diameter minus that pole. In the coordinates $(X,Y,Z)$ of $\RR^3$ with $\CC$ as the $(X,Y)$-plane, the projection sends, for each $R>0$, the circle $\abs z = R$ to the circle of constant $Z = R^2/(R^2+1)$ and the disc $\abs z<R$ to the cap below it, by the formulas of [@SS03, ch. 3, §3]; it is conformal and carries circles to circles (C. McMullen, *Advanced Complex Analysis*, Theorem 2.12). A sequence with $\abs{z_n}\to\infty$ is exactly a sequence leaving every such cap, which is what makes $\infty$ a limit point.

## Maps of the sphere

[[T-UBWL2]]

[[D-FRVBV]]

[[T-QGL7C]]

[[PR-74KHY]]

::: {.example title="The point at infinity in a coordinate"}
The map $z\mapsto1/z$ interchanges $0$ and $\infty$, and in the coordinate $w = 1/z$ near $\infty$ it reads $w\mapsto w$: the pole of $1/z$ at $0$ is the behaviour at $\infty$ of $z$ itself.
A polynomial of degree $n\geq1$ has a pole of order $n$ at $\infty$, since $p(1/w)$ has a pole of order $n$ at $w=0$ ([[D-BPBSQ|singularities at infinity]]).
:::

## Distance on the sphere

[[D-CHRD2]]

::: {.remark}
The extension of a meromorphic function to $\CP^1$ that the sphere is used for is [[T-UBWL2]], and the distances are those of [[D-CHRD2]].
:::
