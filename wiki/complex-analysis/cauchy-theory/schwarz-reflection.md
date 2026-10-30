---
title: Schwarz reflection
order: 70
topics:
- Schwarz Reflection
- Reflection Principle
---

# Schwarz reflection

A holomorphic function on the upper half of a symmetric region that is real on the real axis extends to the whole region by reflection.
The proof glues two holomorphic functions along a segment and applies Morera's theorem.

::: {.remark}
Throughout, $\Omega$ is an open set symmetric about the real axis, so $z\in \Omega \iff \bar{z} \in \Omega$, and $\Omega^+ \coloneqq \Omega\cap\theset{\Im z>0}$, $I\coloneqq\Omega\cap\RR$, and $\Omega^- \coloneqq \Omega\cap\theset{\Im z<0}$.

:::

## The symmetry principle

[[T-5SKNT]]

## The reflection

[[T-Q3GGF]]

::: {.remark}
Composing with Möbius transformations in the domain and the target, the [[T-Q3GGF|reflection principle]] extends a function holomorphic on one side of a line segment or circular arc and continuous up to it, with boundary values on a line or circle, by reflection in the arc and in the target line or circle.

:::

::: {.example title="The real-valued hypothesis is used"}
The constant function $f(z) = i$ on $\Omega^+$ is continuous up to $I$ but not real valued there.
Its reflection is $\overline{f(\bar z)} = -i$ on $\Omega^-$, and the glued function is discontinuous on $I$.

:::
