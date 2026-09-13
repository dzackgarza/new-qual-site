---
schema: qual/card@1
id: PR-CRVHYPCI
kind: proposition
title: A hyperelliptic curve is never a complete intersection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hyperelliptic Curves
  - Complete Intersections
  - Canonical Divisor
relations:
- kind: uses
  target: D-CRVHYP
- kind: related-to
  target: FE-CRVLOWG
review: draft
prompts:
- Can a hyperelliptic curve be a complete intersection in $\PP^n$?
- What is the canonical sheaf of a complete intersection curve, and why does that settle the question?
- Which canonical curves are complete intersections?
---

::: {.proposition}
Let $C \subseteq \PP^n$ be a smooth curve of genus $g \geq 2$ which is a complete intersection of hypersurfaces of degrees $d_1,\ldots,d_{n-1}$.
Then $C$ is not hyperelliptic.
:::

::: {.remark}
The reason is that a complete intersection has its canonical class forced to be a multiple of the hyperplane class, and a positive multiple of the hyperplane class is very ample.

Adjunction on the complete intersection gives
\[
\omega_C \cong \OO_C(a), \qquad a = \sum_{i=1}^{n-1} d_i - n - 1 ,
\]
and $\deg \OO_C(1) = \prod d_i =: d > 0$.
So $2g-2 = ad$, and the hypothesis $g \geq 2$ forces $a \geq 1$.

Now $\OO_{\PP^n}(a)$ is very ample for $a \geq 1$, so the linear system it cuts on $C$ separates points and tangent vectors.
That cut system is a subsystem of the complete system $\abs{\OO_C(a)} = \abs{K_C}$, and a linear system containing a very ample subsystem is itself very ample.
Hence $K_C$ is very ample, so the canonical map is an embedding, so $C$ is not hyperelliptic.
(Complete intersections are projectively normal, so in fact the cut system is *all* of $\abs{K_C}$: the canonical embedding of $C$ is the composite of $C \subseteq \PP^n$ with the $a$-uple embedding.
The weaker subsystem statement is already enough for the conclusion.)

The contrapositive is what the exercise asks for: a hyperelliptic curve embeds in projective space in many ways, but never as a complete intersection in any $\PP^n$.
Two checks against curves one can name.
Genus $2$ is entirely hyperelliptic, and such a curve embeds in $\PP^3$ by a divisor of degree $5$; it cannot be a complete intersection there, and indeed the only factorization $5 = d_1 d_2$ is $1 \cdot 5$, which would place the curve in a plane as a quintic of genus $6$.
Genus $4$ runs the other way: the non-hyperelliptic canonical curve is the intersection of a quadric and a cubic in $\PP^3$, with $a = 2+3-3-1 = 1$ and $\omega_C \cong \OO_C(1)$, exactly as the formula predicts for a canonically embedded complete intersection.
:::
