---
schema: qual/card@1
id: P-AGXMISCGENUSZEROCONIC
kind: problem
title: Every genus zero smooth projective curve over $\CC$ is a plane conic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann--Roch
  - Rational Curves
  - Conics
relations: []
review: draft
---

::: {.problem}
Is every smooth projective curve of genus 0 defined over the field of complex numbers isomorphic to a conic in the projective plane?
Give an explanation for your answer.
:::

::: {.solution}
Sketch: yes.
Apply the Riemann--Roch theorem, which guarantees the existence of a nonconstant meromorphic function with a simple pole at exactly one point.
Argue that this meromorphic function identifies the curve with $\PP^1$, and using that fact, embed the curve as a conic in the plane in any convenient way.
For example, if $t_0, t_1$ are projective coordinates on $\PP^1$, let $z_0=t_0^2$, $z_1=t_0 t_1$, $z_2=t_1^2$ be the map to $\PP^2$.
The conic is then $z_0 z_2=z_1^2$.

Alternatively, one can consider the complete linear system attached to the anticanonical divisor.
:::
