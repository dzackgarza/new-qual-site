---
schema: qual/card@1
id: PR-VA4S3
kind: proposition
title: The Segre embedding, and why $\PP^m \times \PP^n$ is projective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Segre Embedding
  - Projective Varieties
  - Products
relations:
- kind: uses
  target: D-CP2MH
review: draft
prompts:
- Is $\PP^1 \times \PP^1$ a projective variety?
- What equations cut out the Segre image?
- Show that the Segre variety is the categorical product of projective varieties $X \subseteq \PP^n$ and $Y \subseteq \PP^m$.
- What is the graph $\Gamma_f$ of a morphism $f \colon X \to B$ of quasi-projective varieties?
- Give a precise definition of a morphism of projective varieties, in terms of homogeneous coordinates locally.
- 'Describe the image of $[x:y] \mapsto [x^2 : xy : y^2]$, and give equations for the Veronese surface and its ambient $\PP^N$.'
- What is a determinantal variety?
---

::: {.proposition}
The map
\[
\psi: \PP^m \times \PP^n \to \PP^{(m+1)(n+1)-1}, \qquad
([x_i],[y_j]) \mapsto [x_i y_j]
\]
is well defined and injective, and its image is the closed set cut out by the $2 \times 2$ minors
\[
z_{ij} z_{kl} - z_{il} z_{kj} = 0 .
\]
A product of projective varieties is therefore projective.
:::

::: {.remark}
For $m = n = 1$ there is one minor, and the image is the quadric surface
\[
z_{00} z_{11} - z_{01} z_{10} = 0
\]
in $\PP^3$.
The two rulings of that quadric are the images of $\ts{p} \times \PP^1$ and $\PP^1 \times \ts{q}$, and they are what makes it the standard example of a surface whose Picard group is $\ZZ^2$ rather than $\ZZ$.

The minors say the matrix $(z_{ij})$ has rank one, which is the coordinate-free statement: the Segre image is the locus of rank-one tensors in $\PP(V \tensor W)$.
:::
