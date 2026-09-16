---
schema: qual/card@1
id: P-AGH528STABLEBUNDLE
kind: problem
title: Stability of rank two bundles and classification of the unstable indecomposables
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
---

::: {.problem}
A locally free sheaf $\mathcal{E}$ on a curve $C$ is said to be **stable** if for every quotient locally free sheaf
\[
\mathcal{E} \rightarrow \mathcal{F} \rightarrow 0, \qquad \mathcal{F} \neq \mathcal{E}, \mathcal{F} \neq 0
,\]
we have
\[
(\operatorname{deg} \mathcal{F}) / \operatorname{rank} \mathcal{F}>(\operatorname{deg} \mathcal{E}) / \operatorname{rank} \mathcal{E}
.\]
Replacing $>$ by $\geqslant$ defines **semistable**.

a. A decomposable $\mathcal{E}$ is never stable.

b. If $\mathcal{E}$ has rank 2 and is normalized, then $\mathcal{E}$ is stable (respectively, semistable) if and only if $\deg \mathcal{E}>0$ (respectively, $\geqslant 0$).

c. Show that the indecomposable locally free sheaves $\mathcal{E}$ of rank 2 that are not semistable are classified, up to isomorphism, by giving
    (1) an integer $0<e \leqslant 2 g-2$,
    (2) an element $\mathcal{L} \in \Pic C$ of degree $-e$, and
    (3) a nonzero $\xi \in H^1\left(\mathcal{L}\dual\right)$, determined up to a nonzero scalar multiple.
:::
