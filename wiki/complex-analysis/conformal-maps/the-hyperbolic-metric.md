---
title: The hyperbolic metric
order: 55
topics:
- Hyperbolic Metric
- Hyperbolic Geometry
- Schwarz Lemma
---

# The hyperbolic metric

The unit disc carries a distance in which its own automorphisms are isometries and in which it is complete; every holomorphic self-map of the disc contracts it, which is the Schwarz lemma in invariant form.

[[D-2HXLN]]

## Isometries and the Schwarz lemma

[[D-MFPYG]]

The Blaschke factors are isometries of the hyperbolic metric, and since they move any point to $0$, the hyperbolic distance between two points is computed by pushing one of them to the origin:
$$
d_{\HH}(0,w) = \log\frac{1+\abs w}{1-\abs w},
$$
the length of the diameter from $0$ to $w$ in the metric $\abs{\dz}/(1-\abs z^2)$.

[[T-DAETF]]

::: {.example title="Schwarz--Pick, in the metric"}
For holomorphic $f\colon\DD\to\DD$ the Schwarz lemma applied to $\psi_{f(z)}\circ f\circ\psi_z^{-1}$ gives
$$
\frac{\abs{f'(z)}}{1-\abs{f(z)}^2}\leq\frac{1}{1-\abs z^2}\qquad\text{for all } z\in\DD,
$$
which says that $f$ does not increase hyperbolic length; integrating it along a curve gives $d_{\HH}(f(z),f(w))\leq d_{\HH}(z,w)$.
Equality at one point forces $f$ to be an automorphism of $\DD$.
:::

## The upper half plane

A [[D-FRVBV|Möbius transformation]] carrying $\HH$ onto $\DD$ carries the hyperbolic metric of $\DD$ to
$$
\frac{\abs{\dz}}{\Im z}
$$
on $\HH$, and the isometries of that metric are exactly the real Möbius transformations [[T-VGDFW|Automorphisms of the upper half-plane]].
The two models are the same metric in different coordinates, and the hyperbolic distance is invariant under every biholomorphism between domains that carries one model to the other.
