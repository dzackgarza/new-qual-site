---
schema: qual/card@1
id: T-CRVCAST
kind: theorem
title: Castelnuovo's bound for space curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Space Curves
  - Genus
  - Quadric Surface
relations:
- kind: uses
  target: FE-CRVQUAD
review: draft
prompts:
- How large can the genus of a curve of degree $d$ in $\PP^3$ be?
- State Castelnuovo's bound.
---

::: {.theorem}
Let $C \subseteq \PP^3$ be a smooth curve of degree $d$ and genus $g$ not contained in a plane.
Then $d \geq 3$ and
\[
g \leq
\begin{cases}
\tfrac{1}{4}d^2 - d + 1 , & d \text{ even} , \\[2pt]
\tfrac{1}{4}(d^2-1) - d + 1 , & d \text{ odd} .
\end{cases}
\]
The bound is attained for every $d \geq 3$, and a curve attaining it lies on a quadric surface.
:::

::: {.remark}
The bound and its equality case are one statement: the extremal curves are the balanced curves on a quadric.
Type $(a,a)$ on a smooth quadric has $d = 2a$ and $g = (a-1)^2 = \tfrac{1}{4}d^2 - d + 1$, and type $(a,a+1)$ has $d = 2a+1$ and $g = a^2 - a$, which is the odd formula.
So the honest way to remember Castelnuovo is to remember the quadric and balance the bidegree.

The contrast with plane curves is the point of the question.
A plane curve of degree $d$ has $g = \binom{d-1}{2} \approx \tfrac{1}{2}d^2$, roughly twice Castelnuovo's bound: spreading a curve out into $\PP^3$ costs genus, and the hypothesis that $C$ is not planar is what makes the smaller bound apply.
:::
