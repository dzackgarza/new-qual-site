---
schema: qual/card@1
id: P-AGH457AUTOMORPHISMSGENUSTHREE
kind: problem
title: Automorphisms of genus $3$ curves and the Klein quartic with $168$ automorphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Canonical Divisor
  - Embeddings
relations: []
review: draft
---

::: {.problem}
a. Any automorphism of a curve of genus 3 is induced by an automorphism of $\PP^2$ via the canonical embedding.

b. \* Assume $\characteristic k \neq 3$. If $X$ is the curve given by
$$
x^3 y+y^3 z+z^3 x=0
$$
the group $\Aut X$ is the simple group of order 168, whose order is the maximum $84(g-1)$ allowed by (Ex. 2.5). See Burnside ($\S$ 232) or Klein.

c. \* Most curves of genus 3 have no automorphisms except the identity.

    Hint: For each $n$, count the dimension of the family of curves with an automorphism $T$ of order $n$. For example, if $n=2$, then for suitable choice of coordinates, $T$ can be written as $x \mapsto -x$, $y \mapsto y$, $z \mapsto z$. Then there is an 8-dimensional family of curves fixed by $T$; changing coordinates there is a 4-dimensional family of such $T$, so the curves having an automorphism of degree 2 form a family of dimension 12 inside the 14-dimensional family of all plane curves of degree 4.

    More generally it is true (at least over $\CC$) that for any $g \geq 3$, a "sufficiently general" curve of genus $g$ has no automorphisms except the identity; see Baily.
:::
