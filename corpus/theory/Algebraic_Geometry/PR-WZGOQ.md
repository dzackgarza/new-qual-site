---
schema: qual/card@1
id: PR-WZGOQ
kind: proposition
title: Hypersurface complements are affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Hypersurfaces
  - Veronese Embedding
relations:
- kind: uses
  target: D-BIVAU
review: draft
prompts:
- Is the complement of a hypersurface in $\AA^n$ affine?
- Is the complement of a hypersurface in $\PP^n$ affine?
---

::: {.proposition}
Let $f$ be nonconstant.
Then $\AA^n \sm V(f)$ is affine, with coordinate ring $k[x_1,\ldots,x_n]_f$.
So is $\PP^n \sm V(f)$ for $f$ homogeneous of degree $d$.
:::

::: {.remark}
Affine case: $D_f$ is isomorphic to the closed subvariety $V(1 - y f) \subseteq \AA^{n+1}$, the graph of $1/f$.
The extra coordinate $y$ is the inverse that was missing, which is the same trick that reduces the strong Nullstellensatz to the weak one.

Projective case, in two steps.
For a hyperplane, $\PP^n \sm V(x_i)$ is the standard chart $\AA^n$.
For $\deg f = d$, the $d$-uple Veronese $\PP^n \injects \PP^N$ carries $V(f)$ into a hyperplane section, so the complement becomes a closed subvariety of $\PP^N$ minus a hyperplane, hence a closed subvariety of $\AA^N$.

The second case is worth rehearsing, because a projective variety minus a nonempty closed set being affine is the first thing that makes "affine" and "projective" feel like properties of a variety rather than of a presentation.
:::
