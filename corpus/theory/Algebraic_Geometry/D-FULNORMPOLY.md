---
schema: qual/card@1
id: D-FULNORMPOLY
kind: definition
title: Normal polytopes and very ample dilations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Polytopes
  - Ample Divisors
relations:
- kind: uses
  target: PR-TORPOS
- kind: uses
  target: D-TORPOLY
review: draft
prompts:
- What is a normal lattice polytope, and how does it relate to very ampleness?
- How large must k be before kP is guaranteed normal?
---

::: {.definition title="Normal"}
A lattice polytope $P \subseteq M_\RR$ is \dfn{normal} if
$$
(kP \intersect M) + (\ell P \intersect M) = (k+\ell)P \intersect M \quad \text{for all } k, \ell \geq 1 ,
$$
equivalently $k \cdot (P \intersect M) = (kP) \intersect M$ for all $k \geq 1$, equivalently $(P \intersect M) \times \ts{1}$ generates the semigroup $C(P) \intersect (M \times \ZZ)$, where $C(P) \da \Cone(P \times \ts{1})$.
:::

::: {.proposition title="Normality and dilation"}
1. Normal implies very ample.

2. If $P$ is full-dimensional with $\dim P \geq 2$, then $kP$ is normal for every $k \geq \dim P - 1$.
:::

::: {.remark title="Consequences for very ampleness"}
For a full-dimensional lattice polytope $P$ of dimension $d\ge2$, the proposition gives that $kP$ is normal, hence very ample, for every $k\ge d-1$.
For $d=2$ this holds for $k=1$: every lattice polygon is normal, so every ample divisor on a complete toric surface is very ample.
For $d=3$, $kP$ is normal for every $k\ge2$, so a lattice polytope of dimension three that is not very ample can occur only at $k=1$.

The toric variety $X_P$ is $\Proj$ of the semigroup ring $\CC[C(P)\intersect(M\times\ZZ)]$, graded by the last coordinate.
So $P$ is normal if and only if this ring is generated in degree $1$, that is, if and only if the embedding of $X_P$ by the characters in $P\intersect M$ is projectively normal.
:::
