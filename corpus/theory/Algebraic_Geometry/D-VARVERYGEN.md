---
schema: qual/card@1
id: D-VARVERYGEN
kind: definition
title: General and very general hypersurfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hypersurfaces
  - Parameter Spaces
relations: []
review: draft
prompts:
- What is a hypersurface?
- What is a very general hypersurface?
---

::: {.definition title="Hypersurface"}
A \dfn{hypersurface} of degree $d$ in $\PP^n$ is the closed subscheme $V(F)$ of a nonzero homogeneous polynomial $F$ of degree $d$.
Two polynomials define the same hypersurface exactly when they differ by a nonzero scalar, so the hypersurfaces of degree $d$ are the points of
\[
\PP^{N} = \PP H^0(\PP^n, \OO(d)), \qquad N = \binom{n+d}{d} - 1 .
\]
:::

::: {.definition title="General and very general"}
A property holds for a \dfn{general} hypersurface of degree $d$ if it holds for every hypersurface whose point lies outside a proper closed subset of $\PP^N$.
It holds for a \dfn{very general} hypersurface of degree $d$ if it holds for every hypersurface whose point lies outside a countable union of proper closed subsets of $\PP^N$.
:::

::: {.remark}
Over an uncountable algebraically closed field, a countable union of proper closed subsets does not cover $\PP^N$, so a very general hypersurface exists.
Over $\overline{\mathbb{Q}}$ or $\overline{\mathbb{F}}_p$ the countably many hypersurfaces defined over the field can exhaust the parameter space, and "very general" can be vacuous.

Smoothness is a general property: the singular hypersurfaces form the discriminant hypersurface in $\PP^N$.
A property such as $\Pic(X) = \ZZ \cdot \OO_X(1)$ for a surface $X \subseteq \PP^3$ of degree $d \geq 4$ holds only for a very general surface: the Noether--Lefschetz locus where the Picard number jumps is a countable union of proper closed subsets.
:::
