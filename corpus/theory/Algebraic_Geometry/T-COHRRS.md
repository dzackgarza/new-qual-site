---
schema: qual/card@1
id: T-COHRRS
kind: theorem
title: Riemann--Roch for surfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Surfaces
  - Intersection Theory
relations:
- kind: uses
  target: T-COHSD
- kind: uses
  target: D-COHEULER
review: draft
prompts:
- State Riemann--Roch for a surface.
- How do you show a divisor on a surface is effective?
---

::: {.theorem}
Let $X$ be a smooth projective surface with canonical divisor $K$, and $D$ any divisor.
Then
\[
\chi\qty{\OO_X(D)} = \chi\qty{\OO_X} + \frac{1}{2} D \cdot (D - K) .
\]
:::

::: {.remark}
The curve case is the same statement with $\deg$ in place of the intersection pairing, and the surface case is the first one where the correction term is quadratic rather than linear.
$\chi(\OO_X) = 1 - q + p_g$ is the constant, with $q = h^1(\OO_X)$ the irregularity.

What it is used for is existence, not counting.
Serre duality turns $h^2(D)$ into $h^0(K-D)$, so
\[
h^0(D) \geq \chi(\OO_X) + \tfrac{1}{2} D\cdot(D-K) - h^0(K - D) ,
\]
and once $D$ is positive enough that $K - D$ has no sections, a large right-hand side forces $h^0(D) > 0$ and hence $D$ effective.
That inequality is the standard first move in every surface question about whether a linear system is nonempty.
:::
