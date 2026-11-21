---
schema: qual/card@1
id: L-ZXBBI
kind: lemma
title: A nonconstant holomorphic map from a compact Riemann surface is surjective
slogan: 'A nonconstant holomorphic map from a compact Riemann surface is onto a compact target, with finite fibres and finite branching.'
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Surfaces
  - Holomorphic Functions
  - Compactness
relations: []
review: draft
---

::: {.lemma}
Let $X$ and $Y$ be connected Riemann surfaces with $X$ compact, and let $f\colon X\to Y$ be a nonconstant holomorphic map.
Then

- $f$ is surjective,

- $Y$ is compact,

- $\inverseof{f}(q)$ is finite for every $q\in Y$, and

- the ramification locus of $f$ in $X$ and the branch locus $f(\text{ramification locus})$ in $Y$ are finite.

Surjectivity is the statement, in the proper-maps paragraph of §2 of C. McMullen, *Advanced Complex Analysis*, that a holomorphic map from a compact Riemann surface is proper and a nonconstant proper map is surjective; the same paragraph gives the degree as the constant number of preimages with multiplicity. The compactness of $Y$ and the finiteness of the fibres are compactness of the image and discreteness of a fibre in the compact $X$, and the ramification and branch loci are finite because each is the image of a finite union of finite fibres.
:::

::: {.proof}
By the open mapping theorem, $f(X)$ is open in $Y$; as the continuous image of a compact space in a Hausdorff space it is also compact, hence closed.
Since $Y$ is connected and $X\neq\emptyset$, $f(X)=Y$, so $f$ is surjective and $Y=f(X)$ is compact.
For $q\in Y$, the fibre $\inverseof{f}(q)$ is closed in $X$, and it is discrete because a nonconstant holomorphic map on a connected Riemann surface has isolated preimages of each point; a closed discrete subset of a compact space is finite.
In a local coordinate the ramification points are the zeros of the derivative of a nonconstant holomorphic function, so the ramification locus is closed and discrete in $X$, hence finite, and its image, the branch locus, is finite.
:::
