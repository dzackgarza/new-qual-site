---
schema: qual/card@1
id: T-CRVEMBP3
kind: theorem
title: Every curve embeds in $\PP^3$ and projects to a nodal plane curve
slogan: 'Project until secants fill the room: every smooth projective curve embeds in $\PP^3$, and a general further projection gives only nodes.'
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
---

::: {.theorem}
Let $C$ be a smooth projective curve over an algebraically closed field $k$.
Then $C$ admits a closed immersion into $\PP^3_k$.
If $\operatorname{char}k=0$, a general projection of such an embedding from a point of $\PP^3\sm C$ is birational onto a plane curve whose only singularities are ordinary nodes.
:::

::: {.proposition title="The projection criterion"}
Let $C \subseteq \PP^N_k$ be a smooth projective curve and let $O \notin C$; write $\varphi_O$ for projection away from $O$.
Then $\varphi_O$ is a closed immersion exactly when $O$ lies on no secant line through two distinct points of $C$ and on no embedded tangent line to $C$.
The secant variety has dimension at most $3$ and the tangent variety at most $2$, so for $N \geq 4$ such a point $O$ exists.
In characteristic zero, a general center $O\in\PP^3\sm C$ meets only finitely many secants, lies on no tangent or trisecant, and makes the two projected tangent directions distinct at every identified pair. Hence the plane image has only ordinary nodes.
:::

::: {.remark}
Choose a very ample divisor of sufficiently large degree, for example one of degree at least $2g+1$ by [[PR-CRVDEGBD]], to embed $C$ in some projective space. Since secants sweep a subset of dimension at most $3$ and tangents one of dimension at most $2$, successive projections from points outside those loci preserve the embedding until the ambient space is $\PP^3$.

The consequence for genus is the nodal formula: if a plane curve of degree $d$ has $r$ nodes and nothing worse, its normalization has genus
$$
g = \binom{d-1}{2} - r .
$$
Thus a nodal plane model of degree $d$ records the genus by its node count. Over characteristic zero, the Severi variety of irreducible degree-$d$ plane curves with exactly $r$ nodes and no other singularities is nonempty for $0\leq r\leq\binom{d-1}{2}$ and is irreducible of dimension
$$
\frac{d(d+3)}2-r.
$$
:::
