---
schema: qual/card@1
id: P-AGH346SQUAREZEROPIC
kind: problem
title: Picard groups under a square-zero thickening
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Picard Group
  - Infinitesimal Extensions
relations: []
review: draft
---

::: problem
Let $(X, \mco_X)$ be a ringed space, let $\mci$ be a sheaf of ideals with $\mci^2=0$, and let $X_0$ be the ringed space $(X, \mco_X/\mci)$.
Show that there is an exact sequence of sheaves of abelian groups on $X$,
\[
0 \to \mci \to \mco_X^* \to \mco_{X_0}^* \to 0,
\]
where $\mco_X^*$ (respectively, $\mco_{X_0}^*$) denotes the sheaf of (multiplicative) groups of units in the sheaf of rings $\mco_X$ (respectively, $\mco_{X_0}$), the map $\mci \to \mco_X^*$ is defined by $a \mapsto 1+a$, and $\mci$ has its usual (additive) group structure.
Conclude there is an exact sequence of abelian groups
\[
\cdots \to H^1(X, \mci) \to \Pic X \to \Pic X_0 \to H^2(X, \mci) \to \cdots.
\]
:::
