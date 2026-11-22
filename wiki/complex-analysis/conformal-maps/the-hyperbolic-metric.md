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
so $d_{\DD}(0,w) = \frac12\log\frac{1+\abs w}{1-\abs w} = \operatorname{artanh}\abs w$ [@SS03, ch. 8, Problem 3(d)].

[[T-DAETF]]

::: {.remark}
The [[complex-analysis/conformal-maps/the-schwarz-lemma#Consequences|Schwarz--Pick inequality]] says that a holomorphic $f\colon\DD\to\DD$ does not increase hyperbolic length, and $d_{\DD}(f(z),f(w))\leq d_{\DD}(z,w)$ for all $z,w\in\DD$ [@SS03, ch. 8, Problem 3(a)--(b)].
:::

## The upper half plane

[[D-HHYP]]

The holomorphic isometries of that metric are exactly the real Möbius transformations [[T-VGDFW|Automorphisms of the upper half-plane]].
The two models are the same metric in different coordinates, and the hyperbolic distance is invariant under every biholomorphism between domains that carries one model to the other.
