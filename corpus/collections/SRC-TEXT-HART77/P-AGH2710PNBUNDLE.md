---
schema: qual/card@1
id: P-AGH2710PNBUNDLE
kind: problem
title: Projective n-space bundles over a scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Bundles
  - Locally Free Sheaves
  - Descent
relations: []
review: draft
---

::: {.problem}
Let $X$ be a noetherian scheme.

a. By analogy with the definition of a vector bundle (Ex. 5.18), define the notion of a **projective $n\dash$space bundle** over $X$: a scheme $P$ with a morphism $\pi: P \to X$ such that $P$ is locally isomorphic to $U \times \PP^n$ for $U \subseteq X$ open, and the transition automorphisms on $\Spec A \times \PP^n$ are given by $A\dash$linear automorphisms of the homogeneous coordinate ring $A[x_0, \ldots, x_n]$, e.g. $x'_i = \sum_j a_{ij} x_j$ with $a_{ij} \in A$.

b. If $\mce$ is a locally free sheaf of rank $n+1$ on $X$, then $\PP(\mce)$ is a $\PP^n\dash$bundle over $X$.

c. Assume that $X$ is regular, and show that every $\PP^n\dash$bundle $P$ over $X$ is isomorphic to $\PP(\mce)$ for some locally free sheaf $\mce$ on $X$.
*Hint:* let $U \subseteq X$ be an open set with $\pi\inv(U) \cong U \times \PP^n$, and let $\mcl_0$ be the invertible sheaf $\OO(1)$ on $U \times \PP^n$.
Show that $\mcl_0$ extends to an invertible sheaf $\mcl$ on $P$, then show that $\pi_* \mcl = \mce$ is a locally free sheaf on $X$ and that $P \cong \PP(\mce)$.
Can you weaken the hypothesis that $X$ is regular?

d. Conclude, in the case $X$ regular, that there is a bijection between $\PP^n\dash$bundles over $X$ and equivalence classes of locally free sheaves $\mce$ of rank $n+1$ under the relation $\mce \sim \mce'$ if and only if $\mce' \cong \mce \tensor \mcm$ for some invertible sheaf $\mcm$ on $X$.
:::
