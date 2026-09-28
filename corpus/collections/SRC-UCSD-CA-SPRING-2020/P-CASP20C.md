---
schema: qual/card@1
id: P-CASP20C
kind: problem
title: "Mobius transformation from a half-disk to a quadrant"
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
  - Conformal Maps
relations: []
review: draft
---

::: {.problem}
For $a \in (-1, 1)$, let $D_a = \{z : |z| < 1, \operatorname{Im} z > a\}$.
For each such $a$, either find a Möbius transformation of $D_a$ onto the quadrant $Q = \{w = re^{i\theta} : r > 0, 0 < \theta < \frac{\pi}{2}\}$, or show that such a transformation cannot exist.
:::

::: {.solution}
The boundary of $D_a$ consists of an arc of the unit circle and a segment of
the horizontal line $\operatorname{Im}z=a$. A Möbius transformation preserves
angles between generalized circles. The two boundary curves of the quadrant
meet orthogonally, so the circle $|z|=1$ and the line
$\operatorname{Im}z=a$ must also meet orthogonally.

At an intersection point $(x,a)$ with $x^2+a^2=1$, the radius vector is
$(x,a)$; the circle tangent is perpendicular to this vector. The tangent is
perpendicular to the horizontal line exactly when it is vertical, equivalently
when $a=0$. Thus no such Möbius map exists unless $a=0$.

For $a=0$, the upper half-disk is mapped to the first quadrant by
\[
\boxed{T(z)=\frac{1+z}{1-z}}.
\]
Indeed, $T$ maps the diameter $(-1,1)$ to the positive real axis and the upper
semicircle to the positive imaginary axis, so it maps the region between them
biholomorphically onto $Q$.
:::
