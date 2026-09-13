---
schema: qual/card@1
id: P-AGH344REFINEMENTH1
kind: problem
title: Cech cohomology in the limit over coverings computes $H^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Refinements
  - Sheaf Cohomology
relations: []
review: draft
---

::: problem
On an arbitrary topological space $X$ with an arbitrary abelian sheaf $\mcf$, Čech cohomology may not give the same result as the derived functor cohomology.
But here we show that for $H^1$, there is an isomorphism if one takes the limit over all coverings.

a. Let $\mathfrak{U}=(U_i)_{i \in I}$ be an open covering of the topological space $X$.
A refinement of $\mathfrak{U}$ is a covering $\mathfrak{V}=(V_j)_{j \in J}$, together with a map $\lambda: J \to I$ of the index sets, such that for each $j \in J$, $V_j \subseteq U_{\lambda(j)}$.
If $\mathfrak{V}$ is a refinement of $\mathfrak{U}$, show that there is a natural induced map on Čech cohomology, for any abelian sheaf $\mcf$, and for each $i$,
\[
\lambda^i: \check{H}^i(\mathfrak{U}, \mcf) \to \check{H}^i(\mathfrak{V}, \mcf).
\]
The coverings of $X$ form a partially ordered set under refinement, so we can consider the Čech cohomology in the limit
\[
\colim_{\mathfrak{U}} \check{H}^i(\mathfrak{U}, \mcf).
\]

b. For any abelian sheaf $\mcf$ on $X$, show that the natural maps (4.4) for each covering
\[
\check{H}^i(\mathfrak{U}, \mcf) \to H^i(X, \mcf)
\]
are compatible with the refinement maps above.

c. Now prove the following theorem.
Let $X$ be a topological space, $\mcf$ a sheaf of abelian groups.
Then the natural map
\[
\colim_{\mathfrak{U}} \check{H}^1(\mathfrak{U}, \mcf) \to H^1(X, \mcf)
\]
is an isomorphism.

Hint: Embed $\mcf$ in a flasque sheaf $\mcg$, and let $\mcr=\mcg/\mcf$, so that we have an exact sequence $0 \to \mcf \to \mcg \to \mcr \to 0$.
Define a complex $D^\bullet(\mathfrak{U})$ by
\[
0 \to C^\bullet(\mathfrak{U}, \mcf) \to C^\bullet(\mathfrak{U}, \mcg) \to D^\bullet(\mathfrak{U}) \to 0.
\]
Then use the exact cohomology sequence of this sequence of complexes, and the natural map of complexes $D^\bullet(\mathfrak{U}) \to C^\bullet(\mathfrak{U}, \mcr)$, and see what happens under refinement.
:::
