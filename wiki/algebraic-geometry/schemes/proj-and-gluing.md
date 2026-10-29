---
title: Proj and gluing
order: 3
topics:
- Proj
- Gluing
- Projective Space
---

# Proj and gluing

Every scheme is glued from affine open subschemes along open subschemes of their pairwise intersections.

## Gluing

[[D-SCHGLUE]]

The geometry depends on the chosen overlap isomorphism.
Two copies of $\AA^1$ along $\AA^1 \sm \theset{0}$ give $\PP^1$ when the overlap isomorphism is $x\mapsto1/x$ and the non-separated line with a doubled origin when it is the identity.

[[FE-SCHLINE]]

## Proj

[[D-SCHPROJ]]

$\Proj S$ is covered by the affine opens $D_+(f)=\Spec S_{(f)}$ for homogeneous $f$ of positive degree, glued along $D_+(fg)$.
For $S=k[x_0,\ldots,x_n]$, the charts $D_+(x_i)$ with transition functions $x_j/x_i$ give $\PP^n_k$.
A homogeneous ideal $I\subseteq S$ gives the closed subscheme $\Proj(S/I)\subseteq\Proj S$.

[[T-SCHPRJC]]

For a ring $A$, $\PP^n_A=\PP^n_\ZZ\times_{\Spec\ZZ}\Spec A$, and $\OO_{\PP^n_A}(d)$ is the pullback of $\OO_{\PP^n_\ZZ}(d)$.
Since $\PP^n_\ZZ\to\Spec\ZZ$ is proper and properness is stable under [[algebraic-geometry/schemes/fibre-products-and-base-change|base change]], $\PP^n_A\to\Spec A$ is proper.

## Quotients by group actions

[[D-GITQUOT]]

## Relative Spec and relative Proj

[[D-SCHRELSPECPROJ]]

## Blowing up and blowing down

[[D-SCHBLOWUP]]
