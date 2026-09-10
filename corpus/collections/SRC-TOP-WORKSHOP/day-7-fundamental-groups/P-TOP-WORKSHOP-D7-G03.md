---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G03
kind: problem
title: A quotient identifying points of a torus and a sphere
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(June ’05) Find a cell structure for the quotient space obtained by identifying two distinct points $a,b$ in a $2$-torus to a third point $c$ in a $2$-sphere, and compute a presentation for the fundamental group of this space.
:::

::: {.solution}
Let \(T=T^2\). Subdivide \(T\) so that \(a\) and \(b\) are vertices and choose an edge path from \(a\) to \(b\). After identifying \(a\sim b\), that path becomes one additional loop. Collapsing a maximal tree in the resulting \(1\)-skeleton gives a CW model with one \(0\)-cell, three \(1\)-cells \(x,y,t\), and one torus \(2\)-cell attached by the commutator word
\[
[x,y]=xyx^{-1}y^{-1}.
\]

The sphere meets the torus quotient only at the common point \(c\). Give \(S^2\) its CW structure with one \(0\)-cell and one \(2\)-cell attached by the constant map. Thus the whole quotient has a CW model with one \(0\)-cell; \(1\)-cells \(x,y,t\); a \(2\)-cell attached by \([x,y]\); and a further \(2\)-cell attached trivially (the sphere).

The trivial sphere attaching map adds no relation to \(\pi_1\). Therefore
\[
\pi_1(X)\cong\langle x,y,t\mid [x,y]=1\rangle
\cong \mathbb Z^2*\mathbb Z.
\]
:::
