---
schema: qual/card@1
id: P-AGH3411LERAYACYCLIC
kind: problem
title: Cech cohomology agrees with derived functor cohomology on acyclic covers
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Acyclic Covers
  - Sheaf Cohomology
relations: []
review: draft
---

::: {.problem}
This exercise shows that Čech cohomology will agree with the usual cohomology whenever the sheaf has no cohomology on any of the open sets.
More precisely, let $X$ be a topological space, $\mcf$ a sheaf of abelian groups, and $\mathfrak{U}=(U_i)$ an open cover.
Assume for any finite intersection $V=U_{i_0} \intersect \cdots \intersect U_{i_p}$ of open sets of the covering, and for any $k>0$, that $H^k(V, \ro{\mcf}{V})=0$.
Then prove that for all $p \geq 0$, the natural maps
\[
\check{H}^p(\mathfrak{U}, \mcf) \to H^p(X, \mcf)
\]
of (4.4) are isomorphisms.
Show also that one can recover (4.5) as a corollary of this more general result.
:::
