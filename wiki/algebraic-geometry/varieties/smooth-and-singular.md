---
title: Smooth and singular
order: 4
topics:
- Nonsingularity
- Normal Varieties
- Jacobian Criterion
---

# Smooth and singular

[[D-0SYCY]]

The Jacobian rank condition is computational for a presented variety, while regularity of the local ring is intrinsic and extends to schemes.
Over a perfect field the two criteria agree.

## Smooth hyperplane sections

[[T-BERTINI]]

## Normal crossings

[[D-VARNCROSS]]

## Tangent hyperplanes and the dual variety

[[D-VARDUAL]]

## Normality, the weaker condition

[[D-QJ5M9]]

A normal variety is regular in codimension one, so its singular locus has codimension at least two.
A normal curve is therefore smooth: normalization resolves curve singularities, and the local rings at closed points of a smooth curve are discrete valuation rings.

## Where the singular points are

Finding them is the Jacobian computation: set the partials to zero, intersect with the variety, and use the Euler relation in $\PP^n$:
\[
\sum_i x_i \frac{\partial f}{\partial x_i} = (\deg f) \cdot f
\]
makes the vanishing of the partials imply the vanishing of $f$ whenever $\deg f$ is invertible in $k$.
So for a plane curve in characteristic zero the singular locus is cut out by the partials alone.

## Resolutions

[[D-VARLOGRES]]

[[D-VARCREPANT]]

[[D-SRFADE]]
