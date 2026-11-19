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

The Blaschke factors are isometries of the hyperbolic metric, and since they move any point to $0$, the hyperbolic distance between two points is computed by pushing one of them to the origin.
For $w = s\in[0,1)$ the shortest curve from $0$ to $s$ is the segment, and its length in the metric $\abs{\dz}/(1-\abs z^2)$ is
$$
\int_0^s\frac{\dr}{1-r^2} = \operatorname{artanh}s = \frac12\log\frac{1+s}{1-s},
$$
so $d_{\DD}(0,w) = \frac12\log\frac{1+\abs w}{1-\abs w} = \operatorname{artanh}\abs w$ [@SS03, ch. 8, Problem 3(d) (p. 256)].

[[T-DAETF]]

::: {.example title="Schwarz--Pick, in the metric"}
For holomorphic $f\colon\DD\to\DD$ the Schwarz lemma applied to $\psi_{f(z)}\circ f\circ\psi_z^{-1}$ gives
$$
\frac{\abs{f'(z)}}{1-\abs{f(z)}^2}\leq\frac{1}{1-\abs z^2}\qquad\text{for all } z\in\DD,
$$
which says that $f$ does not increase hyperbolic length; integrating it along a curve gives $d_{\DD}(f(z),f(w))\leq d_{\DD}(z,w)$ [@SS03, ch. 8, Problem 3(a)--(b) (p. 256)].
Equality at one point forces $f$ to be an automorphism of $\DD$.
:::

## The upper half plane

A [[D-FRVBV|Möbius transformation]] carrying $\HH$ onto $\DD$ carries the hyperbolic metric of $\DD$ to
$$
\frac{\abs{\dz}}{2\Im z}
$$
on $\HH$: for the Cayley transform $\Psi(z) = (z-i)/(z+i)$ one has $\abs{\Psi'(z)} = 2/\abs{z+i}^2$ and $1-\abs{\Psi(z)}^2 = 4\Im z/\abs{z+i}^2$, so $\abs{\Psi'\,dz}/(1-\abs{\Psi}^2) = \abs{\dz}/(2\Im z)$.
The holomorphic isometries of that metric are exactly the real Möbius transformations [[T-VGDFW|Automorphisms of the upper half-plane]].
The two models are the same metric in different coordinates, and the hyperbolic distance is invariant under every biholomorphism between domains that carries one model to the other.
