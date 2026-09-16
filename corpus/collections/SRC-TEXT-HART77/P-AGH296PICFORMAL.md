---
schema: qual/card@1
id: P-AGH296PICFORMAL
kind: problem
title: The Picard group of a noetherian formal scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Picard Groups
  - Mittag-Leffler Condition
relations: []
review: draft
---

::: {.problem}
Let $\mathfrak{X}$ be a noetherian formal scheme, let $\mci$ be an ideal of definition, and for each $n$ let $Y_n$ be the scheme $(\mathfrak{X}, \OO_\mathfrak{X}/\mci^n)$.
Assume that the inverse system of groups $(\Gamma(Y_n, \OO_{Y_n}))$ satisfies the Mittag-Leffler condition.
Then prove that $\Pic \mathfrak{X} = \inverselim_n \Pic Y_n$.
As in the case of a scheme, we define $\Pic \mathfrak{X}$ to be the group of locally free $\OO_\mathfrak{X}\dash$modules of rank $1$ under $\tensor$.
Proceed in the following steps.

a. Use the fact that $\ker(\Gamma(Y_{n+1}, \OO_{Y_{n+1}}) \to \Gamma(Y_n, \OO_{Y_n}))$ is a nilpotent ideal to show that the inverse system $(\Gamma(Y_n, \OO_{Y_n}^*))$ of units in the respective rings also satisfies (ML).

b. Let $\mcf$ be a coherent sheaf of $\OO_\mathfrak{X}\dash$modules, and assume that for each $n$ there is some isomorphism $\varphi_n: \mcf/\mci^n \mcf \cong \OO_{Y_n}$.
Then show that there is an isomorphism $\mcf \cong \OO_\mathfrak{X}$.
Be careful, because the $\varphi_n$ may not be compatible with the maps in the two inverse systems $(\mcf/\mci^n \mcf)$ and $(\OO_{Y_n})$.
Conclude that the natural map $\Pic \mathfrak{X} \to \inverselim_n \Pic Y_n$ is injective.

c. Given an invertible sheaf $\mcl_n$ on $Y_n$ for each $n$, and given isomorphisms $\mcl_{n+1} \tensor \OO_{Y_n} \cong \mcl_n$, construct maps $\mcl_{n'} \to \mcl_n$ for each $n' \geq n$ so as to make an inverse system, and show that $\mcl = \inverselim_n \mcl_n$ is a coherent sheaf on $\mathfrak{X}$.
Then show that $\mcl$ is locally free of rank $1$, and thus conclude that the map $\Pic \mathfrak{X} \to \inverselim_n \Pic Y_n$ is surjective.
Be careful here, because even though each $\mcl_n$ is locally free of rank $1$, the open sets needed to make them free might get smaller and smaller with $n$.

d. Show that the hypothesis that $(\Gamma(Y_n, \OO_{Y_n}))$ satisfies (ML) holds if either $\mathfrak{X}$ is affine, or each $Y_n$ is projective over a field $k$.
See (III, Ex. 11.5--11.7) for further examples and applications.
:::
