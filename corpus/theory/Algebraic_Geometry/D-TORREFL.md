---
schema: qual/card@1
id: D-TORREFL
kind: definition
title: Reflexive polytopes, Gorenstein Fano toric varieties and the five toric del Pezzos
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Fano Varieties
  - Polytopes
relations:
- kind: uses
  target: D-TORQD
- kind: uses
  target: PR-TORPOS
review: draft
prompts:
- What is a reflexive polytope, and what is its polar dual?
- Classify the toric del Pezzo surfaces.
---

::: {.definition title="Polar dual"}
For $P \subseteq M_\RR$ containing the origin in its interior,
\[
P^\circ = \ts{ u \in N_\RR \st \inp{m}{u} \geq -1 \text{ for all } m \in P } .
\]
:::

::: {.definition title="Reflexive"}
$P$ is \dfn{reflexive} if it is a lattice polytope with facet presentation
\[
P = \ts{ m \in M_\RR \st \inp{m}{u_F} \geq -1 \text{ for every facet } F } ,
\]
that is, every facet lies at lattice distance $1$ from the origin.
Then $P^\circ = \operatorname{Conv}(u_F \st F \text{ a facet of } P)$ is again a lattice polytope, and $(P^\circ)^\circ = P$.
:::

::: {.theorem}
$X_P$ is Gorenstein Fano — $-K_X$ Cartier and ample — exactly when $P$ is reflexive, and then $P_{-K_{X_P}} = P$.
$X_P$ is smooth Fano exactly when $P^\circ$ is a **smooth polytope**: each vertex meets exactly $n = \dim M$ edges, and the primitive vectors along those edges form a lattice basis.
:::

::: {.remark}
In dimension two there are $16$ reflexive polygons up to equivalence, hence $16$ Gorenstein Fano toric surfaces.
Exactly five of them are smooth, giving the toric del Pezzo surfaces:
\[
\PP^2, \quad \PP^1 \times \PP^1, \quad \Bl_1 \PP^2, \quad \Bl_2 \PP^2, \quad \Bl_3 \PP^2 ,
\]
the last three obtained by blowing up the torus-fixed points of $\PP^2$ one at a time.
The list stops at three because a fourth blowup destroys ampleness of $-K$: the fan acquires two adjacent rays whose walls no longer crease.
:::
