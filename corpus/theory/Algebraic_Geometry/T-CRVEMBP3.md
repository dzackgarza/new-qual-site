---
schema: qual/card@1
id: T-CRVEMBP3
kind: theorem
title: Every curve embeds in $\PP^3$ and projects to a nodal plane curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projection
  - Curves
  - Singularities
relations:
- kind: uses
  target: PR-CRVDEGBD
- kind: uses
  target: D-G1AEH
review: draft
prompts:
- Can every curve be embedded in projective space, and in which one?
- Is every curve birational to a plane curve, and how singular can it be?
- What is the classification of curves in $\PP^n$?
---

::: {.theorem}
Every smooth projective curve embeds in $\PP^3$, and is birational to a plane curve with at worst nodes.
:::

::: {.proposition title="The projection criterion"}
Let $C \subseteq \PP^N$ and $O \notin C$, and let $\varphi$ be projection away from $O$.
Then $\varphi$ is a closed immersion exactly when $O$ lies on no secant and no tangent line of $C$.
The secant variety has dimension at most $3$ and the tangent variety at most $2$, so for $N \geq 4$ such a point $O$ exists.
For $N=3$, $\varphi$ is birational onto a nodal image exactly when $O$ lies on only finitely many secants, on no tangent, on no multisecant, and on no secant whose two tangent lines are coplanar.
:::

::: {.remark}
The dimension count is the whole argument and is the thing to say out loud: secants sweep at most a threefold, tangents at most a surface, and $\PP^N$ has room to avoid both as soon as $N \geq 4$.
Projection then drops the ambient dimension one step at a time until it stops at $\PP^3$, where the secant variety fills the space and further projection must lose injectivity.

The consequence for genus is the nodal formula: if a plane curve of degree $d$ has $r$ nodes and nothing worse, its normalization has genus
\[
g = \binom{d-1}{2} - r .
\]
So classifying all curves reduces to studying the family of plane curves of degree $d$ with $r$ nodes, which is nonempty exactly for $0 \leq r \leq \binom{d-1}{2}$ and, by Severi and Harris, irreducible of dimension $\tfrac{1}{2}d(d+3) - r$.
The two extremes are Bertini at $r=0$ and, at the top, the rational curve obtained by projecting the degree-$d$ rational normal curve in $\PP^d$ down to the plane.
:::
