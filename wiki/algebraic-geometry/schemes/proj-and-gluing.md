---
title: Proj and gluing
order: 3
topics:
- Proj
- Gluing
- Projective Space
---

# Proj and gluing

Affine schemes are all the local information there is, so every scheme that is not affine arrives by gluing, and $\Proj$ is the one gluing done often enough to deserve a name.

## Gluing

[[D-SCHGLUE]]

The construction is not deep and the examiner knows it, so the value is in what you glue.
Two copies of $\AA^1$ along $\AA^1 \sm \ts{0}$ give either $\PP^1$ or a pathology, according to which isomorphism you use on the overlap.

[[FE-SCHLINE]]

## Proj

[[D-SCHPROJ]]

$\Proj$ is the gluing in the previous section done uniformly: the charts are the loci $D_+(f)$ where a homogeneous $f$ is invertible, and the transition maps are the ratios.
What makes it worth a separate construction is that the charts and the gluing are both read off a single graded ring, so a graded ideal produces a closed subscheme of $\Proj S$ without any further work — this is how projective varieties become schemes.

[[T-SCHPRJC]]

The reason to define $\PP^n$ over $\ZZ$ and base change, rather than glue afresh over each base, is that the properties of $\PP^n\slice S$ that matter — properness, the computation of $\OO(d)$ and its cohomology — are stable under base change, so they are proved once.
Base change is the subject of [[algebraic-geometry/schemes/fibre-products-and-base-change|the next page]].
