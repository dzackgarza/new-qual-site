---
schema: qual/card@1
id: P-AGH287INFEXT
kind: problem
title: Infinitesimal extensions of a scheme by a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Deformation Theory
  - Coherent Sheaves
  - Nilpotent Ideals
relations: []
review: draft
---

::: {.problem}
As an application of the infinitesimal lifting property, consider the following general problem.
Let $X$ be a scheme of finite type over $k$, and let $\mcf$ be a coherent sheaf on $X$.
We seek to classify schemes $X'$ over $k$ which have a sheaf of ideals $\mci$ such that $\mci^2 = 0$ and $(X', \OO_{X'}/\mci) \cong (X, \OO_X)$, and such that $\mci$ with its resulting structure of $\OO_X\dash$module is isomorphic to the given sheaf $\mcf$.
Such a pair $X', \mci$ is called an **infinitesimal extension of the scheme $X$ by the sheaf $\mcf$**.

One such extension, the trivial one, is obtained as follows.
Take $\OO_{X'} = \OO_X \oplus \mcf$ as sheaves of abelian groups, and define multiplication by
\[
(a \oplus f) \cdot (a' \oplus f') = aa' \oplus (af' + a'f)
.\]
Then the topological space $X$ with the sheaf of rings $\OO_{X'}$ is an infinitesimal extension of $X$ by $\mcf$.

The general problem of classifying extensions of $X$ by $\mcf$ can be quite complicated.
So for now, just prove the following special case: if $X$ is affine and nonsingular, then any extension of $X$ by a coherent sheaf $\mcf$ is isomorphic to the trivial one.
See (III, Ex. 4.10) for another case.
:::
